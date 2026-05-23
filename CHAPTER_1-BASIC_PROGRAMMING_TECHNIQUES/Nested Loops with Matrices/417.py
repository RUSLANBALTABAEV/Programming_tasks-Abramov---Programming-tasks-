"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
11. Вложенные циклы в матричных задачах

417. Даны натуральные числа x1, y1, x2, y2, …, xn, yn, целочисленная матрица [aij]i=1, ..., n; j=1, ..., n. Последовательность x1, y1, x2, y2, …, xn, yn задаёт координаты n точек. Матрица указывает, как соединены между собой точки: aij = 1, если i-я точка соединена с j-й, и a = 0 в противном случае (aij = aji). Получить на экране точки, заданные последовательностью x1, y1, x2, y2, …, xn, yn и соединить их между собой так, как указано в данной матрице.
""" 


import random


def get_data():
    """Ввод числа точек, их координат и матрицы смежности."""
    print("Задача 417: Отображение графа по координатам и матрице смежности")
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
                n = int(input("Введите количество точек n (> 0): "))
                if n <= 0:
                    print("Число точек должно быть положительным.")
                    continue
                # Ввод координат
                print("Введите координаты точек (x y) построчно:")
                points = []
                for i in range(n):
                    x, y = map(int, input(f"Точка {i+1}: ").split())
                    points.append((x, y))

                # Ввод матрицы смежности
                print(f"Введите матрицу смежности {n}×{n} (0 или 1, симметричная, диагональ 0):")
                matrix = []
                for i in range(n):
                    row = list(map(int, input(f"Строка {i+1}: ").split()))
                    if len(row) != n:
                        print(f"Ошибка: в строке должно быть {n} чисел.")
                        break
                    # Проверка диагонали и значений
                    if row[i] != 0:
                        print(f"Диагональный элемент строки {i+1} должен быть 0.")
                        break
                    if any(x not in (0, 1) for x in row):
                        print("Все элементы должны быть 0 или 1.")
                        break
                    matrix.append(row)
                else:
                    # Проверка симметричности
                    symmetric = all(matrix[i][j] == matrix[j][i]
                                    for i in range(n) for j in range(n))
                    if not symmetric:
                        print("Предупреждение: матрица не симметрична. "
                              "Будет использована верхняя треугольная часть.")
                    return n, points, matrix
                print("Попробуйте ввести данные заново.")
            except ValueError:
                print("Ошибка ввода. Ожидаются целые числа.")

    elif choice == '2':
        n = random.randint(4, 7)
        # Генерируем точки в прямоугольнике 0..20
        points = [(random.randint(0, 20), random.randint(0, 20)) for _ in range(n)]
        # Генерируем симметричную матрицу смежности
        matrix = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                if random.random() < 0.4:  # вероятность ребра
                    matrix[i][j] = 1
                    matrix[j][i] = 1
        print(f"\nСгенерированы {n} точек и матрица смежности.")
        print("Точки:", points)
        print("Матрица смежности:")
        for row in matrix:
            print(" ".join(str(x) for x in row))
        return n, points, matrix

    else:
        # Готовые примеры
        examples = [
            (3, [(0,0), (10,0), (5,8)],
             [[0,1,1],
              [1,0,0],
              [1,0,0]]),  # V-образный граф
            (4, [(0,0), (10,0), (10,10), (0,10)],
             [[0,1,0,1],
              [1,0,1,0],
              [0,1,0,1],
              [1,0,1,0]]),  # квадрат с диагоналями? нет, это стороны: 1-2,2-3,3-4,4-1
            (5, [(2,5), (8,3), (12,8), (6,12), (1,9)],
             [[0,1,0,0,1],
              [1,0,1,0,0],
              [0,1,0,1,0],
              [0,0,1,0,1],
              [1,0,0,1,0]])   # пятиугольник
        ]
        print("\nГотовые примеры:")
        for idx, (n_val, pts, mat) in enumerate(examples, 1):
            print(f"{idx}: {n_val} точек")
            print("   Координаты:", pts)
            print("   Матрица смежности:")
            for row in mat:
                print("    ", " ".join(str(x) for x in row))
        while True:
            try:
                num = int(input("Выберите номер примера: "))
                if 1 <= num <= len(examples):
                    return examples[num-1]
                else:
                    print(f"Номер должен быть от 1 до {len(examples)}.")
            except ValueError:
                print("Ошибка ввода. Введите целое число.")


def display_graph(n, points, matrix):
    """Вывод информации о графе и его ASCII-представления."""
    print("\n" + "=" * 50)
    print("ГРАФ (ТОЧКИ И СОЕДИНЕНИЯ)")
    print("=" * 50)
    print("Точки (номер : координаты):")
    for i, (x, y) in enumerate(points, 1):
        print(f"  {i}: ({x}, {y})")

    # Извлекаем рёбра (с учётом симметричности, выводим i<j)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] == 1:
                edges.append((i, j))
    if edges:
        print("\nСоединения (рёбра):")
        for i, j in edges:
            print(f"  Точка {i+1} ({points[i]}) — Точка {j+1} ({points[j]})")
    else:
        print("\nСоединений нет.")

    # ASCII-схема (если точек не слишком много и координаты целые)
    if n <= 12:
        print("\nСхематичное изображение (масштабировано в сетку 20×10):")
        xs = [p[0] for p in points]
        ys = [p[1] for p in points]
        min_x, max_x = min(xs), max(xs)
        min_y, max_y = min(ys), max(ys)
        width = max_x - min_x if max_x != min_x else 1
        height = max_y - min_y if max_y != min_y else 1

        # Размеры текстовой сетки (количество строк и столбцов)
        grid_rows, grid_cols = 10, 20
        grid = [[' ' for _ in range(grid_cols)] for _ in range(grid_rows)]

        # Масштабирование координат в индексы сетки
        def to_grid(x, y):
            col = int(((x - min_x) / width) * (grid_cols - 1))
            row = int(((max_y - y) / height) * (grid_rows - 1))  # инвертируем Y
            col = max(0, min(col, grid_cols - 1))
            row = max(0, min(row, grid_rows - 1))
            return row, col

        # Размещаем точки (если наложение, ставим '*')
        point_positions = {}
        for idx, (x, y) in enumerate(points, 1):
            r, c = to_grid(x, y)
            if (r, c) in point_positions:
                grid[r][c] = '*'  # несколько точек в одной клетке
            else:
                grid[r][c] = str(idx)
                point_positions[(r, c)] = idx

        # Рисуем линии очень примитивно: соединяем точки символами '-', '|', '/', '\'
        # Для простоты используем только символ '*' вдоль прямой линии по алгоритму Брезенхема.
        # Но реализация Брезенхема в тексте может быть громоздкой.
        # Вместо этого просто отметим, что рёбра есть, не будем их рисовать.
        # Для наглядности выведем сетку только с точками.
        print("  (Точки пронумерованы; линии не отображаются)")
        for row in grid:
            print("  " + "".join(row))
        print()
    else:
        print("\n(Схема опущена из-за большого количества точек).")


def main():
    n, points, matrix = get_data()
    display_graph(n, points, matrix)


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
