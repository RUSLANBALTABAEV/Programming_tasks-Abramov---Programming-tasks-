"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
10. Вложенные циклы

354. Даны натуральные числа. x1,y1,...,x10,y10. Посторить на экране точки с координатами xi,yi * (i = 1,..., n) и соединить отрезками прямых:
а) каждую из n точек со всеми остальными n-1 точками;
б) точки с номерами одной четности;
в) точки с номерами разной четности.
"""


import random
import tkinter as tk

def get_points():
    """Выбор способа ввода 10 точек (x, y)."""
    print("Выберите способ ввода 10 точек (x_i, y_i):")
    print("1 - Ручной ввод")
    print("2 - Случайная генерация")
    print("3 - Готовый пример")
    choice = input("Ваш выбор (1/2/3): ").strip()
    while choice not in ('1', '2', '3'):
        choice = input("Некорректно. Выберите 1, 2 или 3: ")

    if choice == '1':
        try:
            print("Введите 20 целых чисел (x1 y1 x2 y2 ... x10 y10) через пробел:")
            line = input().strip()
            tokens = line.split()
            if len(tokens) != 20:
                print("Ожидалось 20 чисел.")
                return None
            nums = [int(t) for t in tokens]
            if any(v < 1 for v in nums):
                print("Все числа должны быть натуральными (>=1).")
                return None
            points = [(nums[i], nums[i+1]) for i in range(0, 20, 2)]
            return points
        except ValueError:
            print("Ошибка ввода.")
            return None

    elif choice == '2':
        points = [(random.randint(1, 30), random.randint(1, 30)) for _ in range(10)]
        print("Сгенерированы точки:")
        for i, (x, y) in enumerate(points, 1):
            print(f"({x}, {y})", end=" ")
        print()
        return points

    else:
        examples = [
            [(1,1), (2,2), (3,3), (4,4), (5,5), (6,6), (7,7), (8,8), (9,9), (10,10)],
            [(1,2), (2,3), (3,4), (4,5), (5,6), (6,7), (7,8), (8,9), (9,10), (10,11)],
            [(5,5), (6,6), (7,7), (8,8), (9,9), (10,10), (11,11), (12,12), (13,13), (14,14)],
            [(2,3), (4,5), (6,7), (8,9), (10,11), (1,1), (2,2), (3,3), (4,4), (5,5)],
            [(1,10), (2,9), (3,8), (4,7), (5,6), (6,5), (7,4), (8,3), (9,2), (10,1)]
        ]
        print("Готовые примеры:")
        for idx, ex in enumerate(examples, 1):
            print(f"{idx}: {ex[:3]}...")
        try:
            idx = int(input("Выберите номер: "))
            if 1 <= idx <= len(examples):
                return examples[idx-1]
            else:
                print("Неверный номер.")
                return None
        except ValueError:
            print("Ошибка ввода.")
            return None

class GraphApp:
    def __init__(self, points):
        self.points = points  # список кортежей (x, y)
        self.n = len(points)
        self.mode = 'all'  # 'all', 'same', 'diff'
        self.root = tk.Tk()
        self.root.title("Соединение точек")

        # Верхняя панель с кнопками
        frame = tk.Frame(self.root)
        frame.pack(side=tk.TOP, fill=tk.X)

        btn_all = tk.Button(frame, text="Все со всеми", command=lambda: self.set_mode('all'))
        btn_all.pack(side=tk.LEFT, padx=5, pady=5)

        btn_same = tk.Button(frame, text="Одинаковая чётность", command=lambda: self.set_mode('same'))
        btn_same.pack(side=tk.LEFT, padx=5, pady=5)

        btn_diff = tk.Button(frame, text="Разная чётность", command=lambda: self.set_mode('diff'))
        btn_diff.pack(side=tk.LEFT, padx=5, pady=5)

        # Холст для рисования
        self.canvas = tk.Canvas(self.root, width=600, height=600, bg='white')
        self.canvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        # Вычисляем масштаб и сдвиг
        self.compute_transform()

        # Первоначальная отрисовка
        self.redraw()

        self.root.mainloop()

    def compute_transform(self):
        """Определяем коэффициенты для преобразования координат точек в координаты холста."""
        xs = [p[0] for p in self.points]
        ys = [p[1] for p in self.points]
        min_x, max_x = min(xs), max(xs)
        min_y, max_y = min(ys), max(ys)

        # Добавим отступы 10% с каждой стороны
        dx = max(1, (max_x - min_x) * 0.1)
        dy = max(1, (max_y - min_y) * 0.1)
        view_min_x = min_x - dx
        view_max_x = max_x + dx
        view_min_y = min_y - dy
        view_max_y = max_y + dy

        # Размер холста
        canvas_width = self.canvas.winfo_reqwidth()
        canvas_height = self.canvas.winfo_reqheight()
        # Если холст ещё не создан, используем 600
        if canvas_width < 10:
            canvas_width = 600
            canvas_height = 600

        # Масштаб
        self.scale_x = canvas_width / (view_max_x - view_min_x)
        self.scale_y = canvas_height / (view_max_y - view_min_y)
        # Используем одинаковый масштаб для сохранения пропорций
        self.scale = min(self.scale_x, self.scale_y)

        # Сдвиг
        self.offset_x = -view_min_x * self.scale + (canvas_width - (view_max_x - view_min_x) * self.scale) / 2
        self.offset_y = -view_min_y * self.scale + (canvas_height - (view_max_y - view_min_y) * self.scale) / 2

    def transform(self, x, y):
        """Преобразует координаты точки в координаты на холсте."""
        cx = x * self.scale + self.offset_x
        cy = y * self.scale + self.offset_y
        return cx, cy

    def set_mode(self, mode):
        self.mode = mode
        self.redraw()

    def redraw(self):
        self.canvas.delete("all")
        # Рисуем линии
        for i in range(self.n):
            for j in range(i+1, self.n):
                draw = False
                if self.mode == 'all':
                    draw = True
                elif self.mode == 'same':
                    if (i+1) % 2 == (j+1) % 2:  # номера с 1
                        draw = True
                else:  # diff
                    if (i+1) % 2 != (j+1) % 2:
                        draw = True
                if draw:
                    x1, y1 = self.transform(self.points[i][0], self.points[i][1])
                    x2, y2 = self.transform(self.points[j][0], self.points[j][1])
                    self.canvas.create_line(x1, y1, x2, y2, fill='blue', width=1)

        # Рисуем точки
        r = 5
        for i, (x, y) in enumerate(self.points):
            cx, cy = self.transform(x, y)
            self.canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill='red', outline='black')
            self.canvas.create_text(cx, cy-10, text=str(i+1), font=('Arial', 10))

def main():
    points = get_points()
    if points is None:
        return
    print("\nИсходные точки (с номерами 1..10):")
    for i, (x, y) in enumerate(points, 1):
        print(f"{i}: ({x}, {y})")
    GraphApp(points)

if __name__ == "__main__":
    main()
