"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
10. Вложенные циклы

355. Даны натуральные числа x1, y1,...,xn,yn. Построить на экране точки с координатами xi,yi * (i = 1,...,n) и соединить пары наиболее удаленных друг от друга.
"""


import random
import math
import tkinter as tk

def get_points():
    """Выбор способа ввода точек."""
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
            print(f"Введите {2*n} целых чисел (x1 y1 x2 y2 ... x{n} y{n}) через пробел:")
            line = input().strip()
            tokens = line.split()
            if len(tokens) != 2*n:
                print(f"Ожидалось {2*n} чисел, получено {len(tokens)}.")
                return None
            nums = [int(t) for t in tokens]
            if any(v < 1 for v in nums):
                print("Все числа должны быть натуральными (>=1).")
                return None
            points = [(nums[i], nums[i+1]) for i in range(0, 2*n, 2)]
            return points
        except ValueError:
            print("Ошибка ввода.")
            return None

    elif choice == '2':
        n = random.randint(3, 10)
        points = [(random.randint(1, 30), random.randint(1, 30)) for _ in range(n)]
        print(f"Сгенерировано {n} точек:")
        for i, (x, y) in enumerate(points, 1):
            print(f"({x}, {y})", end=" ")
        print()
        return points

    else:  # choice == '3'
        examples = [
            [(1,1), (2,2), (3,3), (4,4), (5,5)],  # n=5
            [(1,10), (2,9), (3,8), (4,7), (5,6), (6,5), (7,4)],  # n=7
            [(1,1), (10,10), (1,10), (10,1)],  # n=4, максимальное расстояние между (1,1) и (10,10) или (1,10)-(10,1)
            [(5,5), (5,6), (6,5), (6,6)],  # n=4, все расстояния равны 1
            [(2,3), (4,5), (6,7), (8,9), (10,11), (12,13)]  # n=6
        ]
        print("Готовые примеры наборов точек:")
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

def max_distance_pairs(points):
    """Возвращает список пар индексов (i,j) с максимальным расстоянием."""
    n = len(points)
    max_dist = -1
    pairs = []
    for i in range(n):
        for j in range(i+1, n):
            dx = points[i][0] - points[j][0]
            dy = points[i][1] - points[j][1]
            dist = dx*dx + dy*dy  # квадрат расстояния
            if dist > max_dist:
                max_dist = dist
                pairs = [(i, j)]
            elif dist == max_dist:
                pairs.append((i, j))
    return pairs, math.sqrt(max_dist)

class GraphApp:
    def __init__(self, points):
        self.points = points
        self.n = len(points)
        self.root = tk.Tk()
        self.root.title("Наиболее удалённые точки")

        # Кнопка для повторного поиска (не обязательна, но можно)
        frame = tk.Frame(self.root)
        frame.pack(side=tk.TOP, fill=tk.X)
        btn = tk.Button(frame, text="Найти пары с макс. расстоянием", command=self.find_and_draw)
        btn.pack(pady=5)

        self.canvas = tk.Canvas(self.root, width=600, height=600, bg='white')
        self.canvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        self.compute_transform()
        self.find_and_draw()
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

    def find_and_draw(self):
        self.canvas.delete("all")
        pairs, max_dist = max_distance_pairs(self.points)

        # Рисуем все линии пар с максимальным расстоянием
        for i, j in pairs:
            x1, y1 = self.transform(self.points[i][0], self.points[i][1])
            x2, y2 = self.transform(self.points[j][0], self.points[j][1])
            self.canvas.create_line(x1, y1, x2, y2, fill='red', width=2)

        # Рисуем точки
        r = 5
        for idx, (x, y) in enumerate(self.points):
            cx, cy = self.transform(x, y)
            self.canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill='blue', outline='black')
            self.canvas.create_text(cx, cy-10, text=str(idx+1), font=('Arial', 10))

        # Отображаем информацию
        info = f"Максимальное расстояние: {max_dist:.2f} (квадрат {max_dist**2:.0f}), найдено {len(pairs)} пар"
        self.canvas.create_text(10, 10, anchor='nw', text=info, font=('Arial', 12), fill='black')

def main():
    points = get_points()
    if points is None:
        return
    print("\nИсходные точки:")
    for i, (x, y) in enumerate(points, 1):
        print(f"{i}: ({x}, {y})")
    GraphApp(points)

if __name__ == "__main__":
    main()
