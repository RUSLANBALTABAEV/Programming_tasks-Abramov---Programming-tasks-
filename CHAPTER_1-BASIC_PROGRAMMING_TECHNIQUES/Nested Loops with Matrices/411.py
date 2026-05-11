"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
11. Вложенные циклы в матричных задачах

411. Будем называть соседями элемента с индексами i, j некоторой матрицы такие элементы этой матрицы, соответствующие индексы которых отличаются от i и j не более чем на единицу. Для данной целочисленной матрицы [aij] i = 1, ..., n; j=1, ..., m найти матрицу из нулей и единиц [bij] = i = 1, ..., n; j = 1, ..., m, элемент которой bij равен единице, когда 
а) все соседи aij меньше самого aij;
б) все соседи aij и само aij равны нулю;
в) среди соседей aij есть не менее двух совпадающих с aij.
"""


import random

def get_matrix():
    """Выбор способа ввода целочисленной матрицы размера n x m."""
    print("Задача 411: Построение бинарной матрицы по соседям")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод")
    print("2 — Случайные числа")
    print("3 — Готовые примеры")

    while True:
        choice = input("Ваш выбор (1/2/3): ").strip()
        if choice in ('1', '2', '3'):
            break
        print("Ошибка: выберите 1, 2 или 3.")

    if choice == '1':
        while True:
            try:
                n = int(input("Введите количество строк n ( > 0): "))
                m = int(input("Введите количество столбцов m ( > 0): "))
                if n <= 0 or m <= 0:
                    print("Размеры должны быть положительными.")
                    continue
                print(f"Введите матрицу {n}x{m} построчно (целые числа через пробел):")
                matrix = []
                for i in range(n):
                    row = list(map(int, input(f"Строка {i + 1}: ").split()))
                    if len(row) != m:
                        print(f"Ошибка: в строке должно быть {m} чисел.")
                        break
                    matrix.append(row)
                else:
                    return n, m, matrix
                print("Попробуйте ввести матрицу заново.")
            except ValueError:
                print("Ошибка ввода. Ожидаются целые числа.")

    elif choice == '2':
        n = random.randint(3, 6)
        m = random.randint(3, 6)
        matrix = [[random.randint(-2, 3) for _ in range(m)] for _ in range(n)]
        print(f"\nСгенерирована матрица {n}x{m}:")
        for row in matrix:
            print(" ".join(f"{x:4d}" for x in row))
        return n, m, matrix

    else:
        # Готовые примеры
        examples = [
            (4, 4, [
                [5, 1, 2, 0],
                [1, 5, 0, 0],
                [3, 0, 0, 0],
                [0, 0, 0, 0]
            ]),
            (3, 3, [
                [1, 2, 3],
                [2, 2, 2],
                [3, 2, 1]
            ]),
            (3, 4, [
                [0, 0, 0, 1],
                [0, 0, 0, 0],
                [1, 0, 0, 0]
            ]),
            (1, 1, [[0]]),
            (2, 2, [
                [1, 1],
                [1, 1]
            ])
        ]
        print("\nГотовые примеры:")
        for idx, (n_val, m_val, mat) in enumerate(examples, 1):
            print(f"{idx}: {n_val}x{m_val}")
            for row in mat:
                print("   ", " ".join(f"{x:3d}" for x in row))
        while True:
            try:
                num = int(input("Выберите номер примера: "))
                if 1 <= num <= len(examples):
                    return examples[num-1]
                else:
                    print(f"Номер должен быть от 1 до {len(examples)}.")
            except ValueError:
                print("Ошибка ввода. Введите целое число.")

def choose_variant():
    """Выбор варианта условия."""
    print("\nВыберите условие для b_{ij} = 1:")
    print("а) все соседи a_{ij} меньше самого a_{ij}")
    print("б) все соседи a_{ij} и само a_{ij} равны нулю")
    print("в) среди соседей a_{ij} есть не менее двух совпадающих с a_{ij}")
    while True:
        var = input("Ваш выбор (а/б/в или a/b/v): ").strip().lower()
        mapping = {'а': 'a', 'a': 'a', 'б': 'b', 'b': 'b', 'в': 'c', 'v': 'c', 'c': 'c'}
        if var in mapping:
            return mapping[var]
        print("Некорректный ввод. Попробуйте ещё раз.")

def get_neighbors(matrix, i, j, n, m):
    """Возвращает список значений существующих соседей элемента (i, j)."""
    neighbors = []
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            if di == 0 and dj == 0:
                continue
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m:
                neighbors.append(matrix[ni][nj])
    return neighbors

def compute_binary_matrix(n, m, matrix, variant):
    """Формирует бинарную матрицу по выбранному варианту."""
    result = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            val = matrix[i][j]
            neighbors = get_neighbors(matrix, i, j, n, m)
            if variant == 'a':   # все соседи меньше самого элемента
                if not neighbors:  # нет соседей (матрица 1x1) – условие считается истинным
                    result[i][j] = 1
                elif all(nb < val for nb in neighbors):
                    result[i][j] = 1
            elif variant == 'b': # элемент и все соседи равны нулю
                if val == 0 and (not neighbors or all(nb == 0 for nb in neighbors)):
                    result[i][j] = 1
            elif variant == 'c': # среди соседей не менее двух равных val
                count = sum(1 for nb in neighbors if nb == val)
                if count >= 2:
                    result[i][j] = 1
    return result

def main():
    n, m, matrix = get_matrix()
    variant = choose_variant()
    binary = compute_binary_matrix(n, m, matrix, variant)

    variant_names = {
        'a': "все соседи меньше самого элемента",
        'b': "элемент и все соседи равны нулю",
        'c': "не менее двух соседей совпадают с элементом"
    }

    print("\n" + "=" * 60)
    print("РЕЗУЛЬТАТЫ")
    print("=" * 60)
    print(f"Исходная матрица {n}x{m}:")
    for row in matrix:
        print(" ".join(f"{x:4d}" for x in row))

    print(f"\nУсловие: {variant_names[variant]}")
    print("Бинарная матрица:")
    for row in binary:
        print(" ".join(f"{x:4d}" for x in row))
    print("=" * 60)

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
