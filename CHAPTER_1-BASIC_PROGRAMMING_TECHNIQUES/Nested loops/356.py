"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
10. Вложенные циклы

356. Даны натуральные числа x1, y1, c1,...,xn, yn, cn. Каждые три числа xi, yi, ci задают координаты точки и ее цвет (i = 1, ..., n). Из точек одного цвета получить на экране:
а) первую;
б) последнюю.
"""


import random
import tkinter as tk

def get_data():
    """Выбор способа ввода данных: n и троек (x, y, c)."""
    print("Выберите способ ввода:")
    print("1 - Ручной ввод")
    print("2 - Случайная генерация")
    print("3 - Готовый пример")
    choice = input("Ваш выбор (1/2/3): ").strip()
    while choice not in ('1', '2', '3'):
        choice = input("Некорректно. Выберите 1, 2 или 3: ")

    if choice == '1':
        try:
            n = int(input("Введите количество точек n (>0): "))
            if n <= 0:
                print("n должно быть положительным.")
                return None
            print(f"Введите {3*n} натуральных чисел (x1 y1 c1 ... x{n} y{n} c{n}) через пробел:")
            line = input().strip()
            tokens = line.split()
            if len(tokens) != 3*n:
                print(f"Ожидалось {3*n} чисел, получено {len(tokens)}.")
                return None
            nums = [int(t) for t in tokens]
            if any(v < 1 for v in nums):
                print("Все числа должны быть натуральными (>=1).")
                return None
            # Разбиваем на тройки
            points = []
            for i in range(0, 3*n, 3):
                x, y, c = nums[i], nums[i+1], nums[i+2]
                points.append((x, y, c))
            return points
        except ValueError:
            print("Ошибка ввода.")
            return None

    elif choice == '2':
        n = random.randint(3, 10)
        points = []
        for _ in range(n):
            x = random.randint(1, 30)
            y = random.randint(1, 30)
            c = random.randint(1, 5)  # цвета от 1 до 5
            points.append((x, y, c))
        print(f"Сгенерировано {n} точек (x, y, c):")
        for i, (x, y, c) in enumerate(points, 1):
            print(f"{i}: ({x}, {y}, цвет {c})")
        return points

    else:  # choice == '3'
        examples = [
            [(1,1,1), (2,2,1), (3,3,2), (4,4,2), (5,5,3)],  # n=5
            [(1,10,1), (2,9,2), (3,8,1), (4,7,2), (5,6,3), (6,5,3)],  # n=6
            [(5,5,1), (5,6,1), (6,5,2), (6,6,2), (7,7,1), (8,8,2)],  # n=6
            [(2,3,1), (4,5,1), (6,7,2), (8,9,2), (10,11,3), (12,13,3), (14,15,4)],  # n=7
            [(1,1,1), (1,1,2), (2,2,1), (2,2,2), (3,3,3)]  # n=5, повтор координат
        ]
        print("Готовые примеры наборов точек (x,y,c):")
        for idx, ex in enumerate(examples, 1):
            print(f"{idx}: {ex[:3]}... (всего {len(ex)} точек)")
        try:
            idx = int(input("Выберите номер примера: "))
            if 1 <= idx <= len(examples):
                return examples[idx-1]
            else:
                print("Неверный номер.")
                return None
        except ValueError:
            print("Ошибка ввода.")
            return None

def find_first_last(points):
    """Для каждого цвета возвращает словарь: цвет -> (first_index, last_index) (индексы с 0)."""
    first = {}
    last = {}
    for i, (x, y, c) in enumerate(points):
        if c not in first:
            first[c] = i
        last[c] = i
    # Объединяем
    result = {}
    for c in first:
        result[c] = (first[c], last[c])
    return result

class FirstLastApp:
    def __init__(self, points):
        self.points = points  # список (x, y, c)
        self.n = len(points)
        self.first_last = find_first_last(points)

        self.root = tk.Tk()
        self.root.title("Первая и последняя точки каждого цвета")

        # Информационная панель
        frame = tk.Frame(self.root)
        frame.pack(side=tk.TOP, fill=tk.X)
        info = f"Всего точек: {self.n}, уникальных цветов: {len(self.first_last)}"
        tk.Label(frame, text=info).pack(pady=5)

        self.canvas = tk.Canvas(self.root, width=600, height=600, bg='white')
        self.canvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        self.compute_transform()
        self.draw()
        self.root.mainloop()

    def compute_transform(self):
        xs = [p[0] for p in self.points]
        ys = [p[1] for p in self.points]
        min_x, max_x = min(xs), max(xs)
        min_y, max_y = min(ys), max(ys)

        dx = max(1, (max_x - min_x) * 0.1)
        dy = max(1, (max_y - min_y) * 0.1)
        view_min_x = min_x - dx
        view_max_x = max_x + dx
        view_min_y = min_y - dy
        view_max_y = max_y + dy

        canvas_width = self.canvas.winfo_reqwidth()
        canvas_height = self.canvas.winfo_reqheight()
        if canvas_width < 10:
            canvas_width = 600
            canvas_height = 600

        self.scale_x = canvas_width / (view_max_x - view_min_x)
        self.scale_y = canvas_height / (view_max_y - view_min_y)
        self.scale = min(self.scale_x, self.scale_y)
        self.offset_x = -view_min_x * self.scale + (canvas_width - (view_max_x - view_min_x) * self.scale) / 2
        self.offset_y = -view_min_y * self.scale + (canvas_height - (view_max_y - view_min_y) * self.scale) / 2

    def transform(self, x, y):
        cx = x * self.scale + self.offset_x
        cy = y * self.scale + self.offset_y
        return cx, cy

    def draw(self):
        self.canvas.delete("all")
        # Сначала нарисуем все точки серым (фон), чтобы показать контекст
        r = 3
        for idx, (x, y, c) in enumerate(self.points):
            cx, cy = self.transform(x, y)
            self.canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill='lightgray', outline='gray')

        # Теперь выделим первые и последние
        r_big = 8
        for color, (first_idx, last_idx) in self.first_last.items():
            # Первая точка
            x, y, _ = self.points[first_idx]
            cx, cy = self.transform(x, y)
            self.canvas.create_oval(cx-r_big, cy-r_big, cx+r_big, cy+r_big, outline='green', width=3)
            self.canvas.create_text(cx, cy-15, text=f"c{color} first", font=('Arial', 8), fill='green')

            # Последняя точка (если отличается)
            if first_idx != last_idx:
                x, y, _ = self.points[last_idx]
                cx, cy = self.transform(x, y)
                self.canvas.create_oval(cx-r_big, cy-r_big, cx+r_big, cy+r_big, outline='red', width=3)
                self.canvas.create_text(cx, cy-15, text=f"c{color} last", font=('Arial', 8), fill='red')
            else:
                # Если одна, пометим как first/last
                self.canvas.create_text(cx, cy+15, text="first/last", font=('Arial', 8), fill='purple')

        # Подпишем все точки с цветом? Можно добавить подписи
        for idx, (x, y, c) in enumerate(self.points):
            cx, cy = self.transform(x, y)
            self.canvas.create_text(cx+10, cy-10, text=f"{idx+1}({c})", font=('Arial', 6), fill='black')

def main():
    points = get_data()
    if points is None:
        return
    print("\nИсходные точки (x, y, цвет):")
    for i, (x, y, c) in enumerate(points, 1):
        print(f"{i}: ({x}, {y}, цвет {c})")
    FirstLastApp(points)

if __name__ == "__main__":
    main()
