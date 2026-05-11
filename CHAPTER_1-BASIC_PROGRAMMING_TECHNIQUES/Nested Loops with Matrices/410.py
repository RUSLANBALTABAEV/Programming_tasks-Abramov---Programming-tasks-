"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
11. Вложенные циклы в матричных задачах

410. Дана целочисленная матрица [aij]i,j = 1, ..., n. Получить b1, …, bn, где bi - это 
а) nEj=1 * a ^ 2 ij;            б) nEj=1 * (-1) ^ i + j;
в) nPj=1 * aij;                 г) nEj=1 * abs(aij);
д) Pj * aij для всех таких j, что 1 < aij <= n;
е) max(a) 1 <= j <= n * min(aij) 1 <= j <= n.
"""


import random
import math

def get_matrix():
    """Выбор способа ввода целочисленной квадратной матрицы порядка n."""
    print("Задача 410: Вычисление b_i для каждого i")
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
                n = int(input("Введите порядок матрицы n ( > 0): "))
                if n <= 0:
                    print("Порядок должен быть положительным.")
                    continue
                print(f"Введите матрицу {n}×{n} построчно (целые числа через пробел):")
                matrix = []
                for i in range(n):
                    row = list(map(int, input(f"Строка {i+1}: ").split()))
                    if len(row) != n:
                        print(f"Ошибка: в строке должно быть {n} чисел.")
                        break
                    matrix.append(row)
                else:
                    return n, matrix
                print("Попробуйте ввести матрицу заново.")
            except ValueError:
                print("Ошибка ввода. Ожидаются целые числа.")

    elif choice == '2':
        n = random.randint(3, 6)
        matrix = [[random.randint(-4, 7) for _ in range(n)] for _ in range(n)]
        print(f"\nСгенерирована матрица порядка {n}:")
        for row in matrix:
            print(" ".join(f"{x:4d}" for x in row))
        return n, matrix

    else:
        # Готовые примеры
        examples = [
            (3, [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ]),
            (4, [
                [2, -3, 0, 5],
                [1, 2, 2, 4],
                [-1, 3, -2, 1],
                [0, 4, 6, 3]
            ]),
            (3, [
                [0, 0, 0],
                [1, 2, 3],
                [-2, -1, 4]
            ]),
            (5, [
                [1, 2, 3, 4, 5],
                [0, 1, 0, 0, 0],
                [2, 3, 5, 7, 11],
                [1, 1, 1, 1, 1],
                [4, 0, 6, 0, 2]
            ])
        ]
        print("\nГотовые примеры:")
        for idx, (n_val, mat) in enumerate(examples, 1):
            print(f"{idx}: n = {n_val}")
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
    """Выбор одного из шести вариантов (a–е)."""
    print("\nВарианты вычисления b_i:")
    print("a) сумма квадратов элементов i-й строки")
    print("б) сумма (-1) ^ (i + j) * a_ij по j")
    print("в) произведение элементов i-й строки")
    print("г) сумма |a_ji| по j (модули элементов i-го столбца)")
    print("д) произведение a_ji для j, где 1 < a_ji ≤ n")
    print("е) (max в строке i) * (min в столбце i)")
    while True:
        var = input("Ваш выбор (а/б/в/г/д/е или a/b/v/g/d/e): ").strip().lower()
        mapping = {
            'а': 'a', 'a': 'a',
            'б': 'b', 'b': 'b',
            'в': 'v', 'v': 'v',
            'г': 'g', 'g': 'g',
            'д': 'd', 'd': 'd',
            'е': 'e', 'e': 'e'
        }
        if var in mapping:
            return mapping[var]
        print("Некорректный ввод. Попробуйте ещё раз.")

def compute_b(n, matrix, variant):
    """Возвращает список b_1..b_n для выбранного варианта."""
    b = []
    for i in range(n):  # i = 0..n-1 соответствует строке i+1
        if variant == 'a':   # сумма квадратов в строке
            s = sum(matrix[i][j] ** 2 for j in range(n))
            b.append(s)
        elif variant == 'b': # сумма (-1)^(i+j+2) * a_ij (т.к. индексы 1-based)
            s = sum(((-1) ** ((i + 1) + (j + 1))) * matrix[i][j] for j in range(n))
            # эквивалентно (-1) ** (i + j) с учётом +2 -> тот же знак
            b.append(s)
        elif variant == 'v': # произведение строки
            prod = 1
            for j in range(n):
                prod *= matrix[i][j]
            b.append(prod)
        elif variant == 'g': # сумма модулей элементов в столбце i
            s = sum(abs(matrix[j][i]) for j in range(n))
            b.append(s)
        elif variant == 'd': # произведение по столбцу i элементов со значением 1 < a_ji <= n
            prod = 1
            found = False
            for j in range(n):
                val = matrix[j][i]
                if 1 < val <= n:
                    prod *= val
                    found = True
            b.append(prod if found else 1)  # пустое произведение = 1
        elif variant == 'e': # max в строке i * min в столбце i
            max_row = max(matrix[i])
            min_col = min(matrix[j][i] for j in range(n))
            b.append(max_row * min_col)
    return b

def main():
    n, matrix = get_matrix()
    variant = choose_variant()
    b = compute_b(n, matrix, variant)

    variant_names = {
        'a': "Сумма квадратов строки",
        'b': "Сумма (-1) ^ (i + j) * a_ij",
        'v': "Произведение строки",
        'g': "Сумма |a_ji| по столбцу i",
        'd': "Произведение a_ji при 1 < a_ji ≤ n",
        'e': "(max строки) * (min столбца)"
    }

    print("\n" + "=" * 60)
    print("РЕЗУЛЬТАТЫ")
    print("=" * 60)
    print(f"Матрица порядка {n}:")
    for idx, row in enumerate(matrix):
        print(f"Строка {idx+1:2d}:", " ".join(f"{x:4d}" for x in row))

    print(f"\nВариант: {variant_names[variant]}")
    for i, val in enumerate(b):
        print(f"  b_{i+1} = {val}")
    print("="*60)

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
