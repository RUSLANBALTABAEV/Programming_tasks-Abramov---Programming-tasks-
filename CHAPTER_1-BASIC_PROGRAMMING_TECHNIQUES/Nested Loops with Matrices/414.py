"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
11. Вложенные циклы в матричных задачах

414. Даны натуральные числа x1, y1, ..., xn, yn. Числа xi, yi рассматриваются как координаты i-й точки (i = 1, …, n). Обозначим через rij расстояние от i-й точки до j-й. Получить на экране заданные точки и соединить отрезком i-ю точку с j-й в том случае, если выполняется по крайней мере одно условие: 
а) rij имеет наибольшее значение из ri1, ri2, ..., rin;
б) rji имеет наибольшее значение из rj1, rj2, ..., rjn.
"""


import math
import random


def calculate_distance(x1, y1, x2, y2):
    """Вычисление расстояния между двумя точками."""
    return math.hypot(x2 - x1, y2 - y1)


def get_points():
    """Получение списка точек выбранным способом."""
    print("Задача 414: Соединение точек с наиболее удалёнными")
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
                n = int(input("Введите количество точек (≥ 2): "))
                if n < 2:
                    print("Нужно не менее 2 точек.")
                    continue
                points = []
                for i in range(n):
                    while True:
                        try:
                            x, y = map(float, input(f"Точка {i+1} (x y): ").split())
                            break
                        except ValueError:
                            print("Ошибка. Введите два числа через пробел.")
                    points.append((x, y))
                return points
            except ValueError:
                print("Ошибка ввода. Ожидается целое число.")

    elif choice == '2':
        while True:
            try:
                n = int(input("Введите количество точек (≥ 2): "))
                if n < 2:
                    print("Нужно не менее 2 точек.")
                    continue
                points = [(random.randint(0, 20), random.randint(0, 20)) for _ in range(n)]
                print("Сгенерированы точки:", points)
                return points
            except ValueError:
                print("Ошибка ввода. Введите целое число.")

    else:
        examples = [
            ([(0,0), (10,0), (10,10), (0,10)], "Вершины квадрата"),
            ([(0,0), (5,5), (10,0)], "Равнобедренный треугольник"),
            ([(0,0), (3,4), (6,0), (3,2)], "Смешанный набор"),
            ([(1,1), (1,1), (2,2)], "Две совпадающие точки")
        ]
        print("\nГотовые примеры:")
        for idx, (pts, desc) in enumerate(examples, 1):
            print(f"{idx}: {desc} – {pts}")
        while True:
            try:
                num = int(input("Выберите номер примера: "))
                if 1 <= num <= len(examples):
                    return examples[num-1][0]
                else:
                    print(f"Номер должен быть от 1 до {len(examples)}.")
            except ValueError:
                print("Ошибка ввода. Введите целое число.")


def main():
    points = get_points()
    n = len(points)

    if n < 2:
        print("Недостаточно точек для соединения (требуется хотя бы 2).")
        return

    # 1. Матрица расстояний (вычисляем только для i < j)
    dist_matrix = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            d = calculate_distance(*points[i], *points[j])
            dist_matrix[i][j] = d
            dist_matrix[j][i] = d

    # 2. Поиск рёбер
    edges = set()
    all_zero = True
    for i in range(n):
        max_dist = max(dist_matrix[i])
        if max_dist > 0:
            all_zero = False
        farthest = [j for j, d in enumerate(dist_matrix[i]) if d == max_dist and i != j]
        for j in farthest:
            edges.add(tuple(sorted((i, j))))

    # 3. Вывод результатов
    print("\n" + "=" * 40)
    print("РЕЗУЛЬТАТЫ")
    print("=" * 40)
    print("1. Координаты точек:")
    for i, (x, y) in enumerate(points):
        print(f"   Точка {i+1}: ({x}, {y})")

    if all_zero:
        print("\n2. Все точки совпадают — соединений нет.")
    elif edges:
        print(f"\n2. Соединить отрезком следующие пары точек (всего {len(edges)}):")
        for i, j in sorted(edges):
            p1, p2 = points[i], points[j]
            d = dist_matrix[i][j]
            print(f"   Точка {i+1} {p1} <--> Точка {j+1} {p2}  (Расстояние: {d:.2f})")
    else:
        print("\n2. Нет пар, удовлетворяющих условию.")

    # ASCII-схема для наглядности (при n ≤ 10)
    if n <= 10:
        print("\n3. Схематичное отображение связей (сетка 10×10):")
        xs = [p[0] for p in points]
        ys = [p[1] for p in points]
        min_x, max_x = min(xs), max(xs)
        min_y, max_y = min(ys), max(ys)
        width = max_x - min_x if max_x != min_x else 1
        height = max_y - min_y if max_y != min_y else 1

        rows, cols = 10, 10
        grid = [[' ' for _ in range(cols)] for _ in range(rows)]

        for i, (x, y) in enumerate(points):
            c = int(((x - min_x) / width) * (cols - 1))
            r = int(((max_y - y) / height) * (rows - 1))
            c = max(0, min(c, cols - 1))
            r = max(0, min(r, rows - 1))
            if grid[r][c] != ' ':
                grid[r][c] = '*'
            else:
                grid[r][c] = str(i + 1)

        for row in grid:
            print(''.join(row))
        print("(Цифры — номера точек, '*' — наложение нескольких точек)")
    else:
        print("\n(Схематичный вывод пропущен из-за большого числа точек)")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
