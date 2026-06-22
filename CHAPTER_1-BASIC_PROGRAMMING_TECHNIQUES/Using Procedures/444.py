"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
12. Использование процедур 

В задачах этого параграфа будем для краткости говорить просто о процедурах, подразумевая, что решающий задачи сам выберет подходящее средство программирования – подпрограмму, функцию и 
т. д. Этот выбор должен быть сделан с учётом как характера задач, так и особенностей используемого языка программирования.

444. Даны натуральное число n, действительные числа x1, y1, x2, y2, ..., xn, yn. Найти площадь n–угольника, вершины которого при некотором последовательном обходе имеют координаты (x1, y1), (x2, y2), …, (xn, yn). (Определить процедуру вычисления площади треугольника по координатам его вершин.)
"""


import math
import random


def triangle_area(x1, y1, x2, y2, x3, y3):
    """
    Вычисляет площадь треугольника по координатам трёх вершин.
    S = 0.5 * |(x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)|
    """
    return 0.5 * abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1))


def get_polygon():
    """Выбор способа ввода числа вершин и их координат."""
    print("Задача 444: Площадь n-угольника")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод")
    print("2 — Случайная генерация")
    print("3 — Готовые примеры")

    while True:
        choice = input("Ваш выбор (1/2/3): ").strip()
        if choice in ('1', '2', '3'):
            break
        print("Ошибка: выберите 1, 2 или 3.")

    if choice == '1':
        while True:
            try:
                n = int(input("Введите количество вершин n (>=3): "))
                if n < 3:
                    print("Многоугольник должен иметь минимум 3 вершины.")
                    continue
                print(f"Введите {2 * n} чисел (x1 y1 x2 y2 ... xn yn) через пробел:")
                data = list(map(float, input().split()))
                if len(data) != 2 * n:
                    print(f"Ожидалось {2 * n} чисел.")
                    continue
                vertices = [(data[i], data[i + 1]) for i in range(0, 2 * n, 2)]
                return vertices
            except ValueError:
                print("Ошибка ввода.")

    elif choice == '2':
        n = random.randint(3, 7)
        # Генерируем случайные точки и сортируем их по полярному углу вокруг центра,
        # чтобы получить простой многоугольник без самопересечений.
        pts = [(round(random.uniform(-10, 10), 2), round(random.uniform(-10, 10), 2)) for _ in range(n)]
        cx = sum(p[0] for p in pts) / n
        cy = sum(p[1] for p in pts) / n
        pts.sort(key = lambda p: math.atan2(p[1] - cy, p[0] - cx))
        print(f"Сгенерирован {n} - угольник: {pts}")
        return pts

    else:  # готовые примеры
        examples = [
            [(0, 0), (4, 0), (4, 3)],                     # прямоугольный треугольник, S =6
            [(0, 0), (2, 0), (2, 2), (0, 2)],               # квадрат 2 x 2, S = 4
            [(1, 1), (4, 2), (3, 5), (-1, 4)],              # четырёхугольник, S ≈...
            [(0, 0), (3, 0), (3, 1), (1, 1), (1, 2), (0, 2)]  # сложный 6-угольник, S =...
        ]
        print("Готовые примеры:")
        for idx, verts in enumerate(examples, 1):
            print(f"{idx}: {verts}")
        while True:
            try:
                num = int(input("Выберите номер примера: "))
                if 1 <= num <= len(examples):
                    return examples[num-1]
                else:
                    print(f"Номер от 1 до {len(examples)}.")
            except ValueError:
                print("Введите целое число.")


def main():
    vertices = get_polygon()
    n = len(vertices)

    total_area = 0.0
    # Разбиваем многоугольник на треугольники с общей вершиной в первой точке
    for i in range(1, n - 1):
        x1, y1 = vertices[0]
        x2, y2 = vertices[i]
        x3, y3 = vertices[i + 1]
        total_area += triangle_area(x1, y1, x2, y2, x3, y3)

    print(f"\nКоординаты вершин: {vertices}")
    print(f"Площадь {n} - угольника: {total_area:.6f}")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
