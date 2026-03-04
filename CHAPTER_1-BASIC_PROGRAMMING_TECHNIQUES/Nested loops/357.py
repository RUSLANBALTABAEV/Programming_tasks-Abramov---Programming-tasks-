"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
10. Вложенные циклы

357. Даны натуральные числа x1, y1, r1,....,xn, yn, rn, которые задают последовательность окружностей так, что xi, yi - координаты центра, а ri - радуис i-й окружности (i = 1, ..., n). Получить на экране окружности , которые имеют общие точки с некоторыми другими окружностями последовательности.
"""


import random
import math
import tkinter as tk

def get_circles():
    """Выбор способа ввода окружностей (x, y, r)."""
    print("Выберите способ ввода:")
    print("1 - Ручной ввод")
    print("2 - Случайная генерация")
    print("3 - Готовый пример")
    choice = input("Ваш выбор (1/2/3): ").strip()
    while choice not in ('1', '2', '3'):
        choice = input("Некорректно. Выберите 1, 2 или 3: ")

    if choice == '1':
        try:
            n = int(input("Введите количество окружностей n (>0): "))
            if n <= 0:
                print("n должно быть положительным.")
                return None
            print(f"Введите {3*n} натуральных чисел (x1 y1 r1 ... x{n} y{n} r{n}) через пробел:")
            line = input().strip()
            tokens = line.split()
            if len(tokens) != 3*n:
                print(f"Ожидалось {3*n} чисел, получено {len(tokens)}.")
                return None
            nums = [int(t) for t in tokens]
            if any(v < 1 for v in nums):
                print("Все числа должны быть натуральными (>=1).")
                return None
            circles = []
            for i in range(0, 3*n, 3):
                x, y, r = nums[i], nums[i+1], nums[i+2]
                circles.append((x, y, r))
            return circles
        except ValueError:
            print("Ошибка ввода.")
            return None

    elif choice == '2':
        n = random.randint(3, 8)
        circles = []
        for _ in range(n):
            x = random.randint(10, 300)
            y = random.randint(10, 300)
            r = random.randint(5, 50)
            circles.append((x, y, r))
        print(f"Сгенерировано {n} окружностей (x, y, r):")
        for i, (x, y, r) in enumerate(circles, 1):
            print(f"{i}: центр ({x}, {y}), радиус {r}")
        return circles

    else:  # choice == '3'
        examples = [
            # несколько примеров
            [(100,100,30), (150,120,25), (200,200,40), (50,50,20), (180,180,15)],
            [(50,50,30), (120,60,30), (80,120,30), (200,200,50), (250,250,30), (150,150,20)],
            [(100,100,20), (120,100,20), (140,100,20), (160,100,20), (180,100,20)], # цепочка касающихся
            [(200,200,50), (200,200,30), (300,300,40), (100,100,10)], # вложенные
            [(50,50,10), (80,80,10), (110,110,10), (140,140,10)] # отдельные
        ]
        print("Готовые примеры наборов окружностей:")
        for idx, ex in enumerate(examples, 1):
            print(f"{idx}: {ex[:3]}... (всего {len(ex)} окружностей)")
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

def find_intersecting_circles(circles):
    """Возвращает список булевых значений, указывающих, имеет ли окружность общие точки с какой-либо другой."""
    n = len(circles)
    has_intersection = [False] * n
    for i in range(n):
        x1, y1, r1 = circles[i]
        for j in range(i+1, n):
            x2, y2, r2 = circles[j]
            dx = x1 - x2
            dy = y1 - y2
            d2 = dx*dx + dy*dy
            # Условие пересечения: |r1 - r2| <= d <= r1 + r2
            if (r1 - r2)**2 <= d2 <= (r1 + r2)**2:
                has_intersection[i] = True
                has_intersection[j] = True
    return has_intersection

class CircleApp:
    def __init__(self, circles):
        self.circles = circles
        self.n = len(circles)
        self.has_intersection = find_intersecting_circles(circles)

        self.root = tk.Tk()
        self.root.title("Окружности, имеющие общие точки")

        # Информационная панель
        frame = tk.Frame(self.root)
        frame.pack(side=tk.TOP, fill=tk.X)
        count = sum(self.has_intersection)
        info = f"Всего окружностей: {self.n}, из них с общими точками: {count}"
        tk.Label(frame, text=info).pack(pady=5)

        self.canvas = tk.Canvas(self.root, width=600, height=600, bg='white')
        self.canvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        self.compute_transform()
        self.draw()
        self.root.mainloop()

    def compute_transform(self):
        # Определяем область с учетом радиусов
        xs = [c[0] for c in self.circles]
        ys = [c[1] for c in self.circles]
        rs = [c[2] for c in self.circles]
        min_x = min(xs) - max(rs)
        max_x = max(xs) + max(rs)
        min_y = min(ys) - max(rs)
        max_y = max(ys) + max(rs)

        # Добавим отступ 10%
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
        # Рисуем все окружности
        for idx, (x, y, r) in enumerate(self.circles):
            cx, cy = self.transform(x, y)
            r_scaled = r * self.scale
            if self.has_intersection[idx]:
                # Красная сплошная
                self.canvas.create_oval(cx - r_scaled, cy - r_scaled,
                                        cx + r_scaled, cy + r_scaled,
                                        outline='red', width=2)
            else:
                # Серая пунктирная
                self.canvas.create_oval(cx - r_scaled, cy - r_scaled,
                                        cx + r_scaled, cy + r_scaled,
                                        outline='gray', width=1, dash=(4, 2))
            # Подпись номера окружности
            self.canvas.create_text(cx, cy, text=str(idx+1), font=('Arial', 8), fill='black')

def main():
    circles = get_circles()
    if circles is None:
        return
    print("\nИсходные окружности (x, y, r):")
    for i, (x, y, r) in enumerate(circles, 1):
        print(f"{i}: центр ({x}, {y}), радиус {r}")
    CircleApp(circles)

if __name__ == "__main__":
    main()
