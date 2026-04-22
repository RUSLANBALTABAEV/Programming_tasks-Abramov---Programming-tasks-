"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
11. Вложенные циклы в матричных задачах

393. Даны натуральное число n, целочисленная квадратная матрица порядка n. Получить b1,...,bn, где bi - это 
а) наименьшее из значений элементов, находящихся в начале i-й строки матрицы до элемента, принадлежащего главной диагонали, включительно;
б) значение первого по порядку положительного элемента i-й строки (если элементов нет, то принять bi = 1);
в) сумма элементов, расположенных за первым отрицательным элементом в i-й строке (если все элементы строки неотрицательны, то принять bi = 100);
г) сумма элементов, предшествующих последнему отрицательному элементу i-й строки (если все элементы строки неотрицательны, то принять bi = -1).
"""

import random

def get_matrix():
    """Выбор способа ввода квадратный матрицы порядка n."""
    print("Задача 393. Вычисление вектора b по заданному условию.")
    print("Выберите способ ввода:")
    print("1 - Ручной ввод")
    print("2 - Случайная числа")
    print("3 - Готовые примеры")

    while True:
        choice = input("Ваш выбор (1/2/3): ").strip()
        if choice in ('1', '2', '3'):
            break
        print("Ошибка: выберите 1, 2, или 3.")

    if choice == '1':
        while True:
            try:
                n = int(input("Введите порядок матрицы n (>0): "))
                if n <= 0:
                    print("Порядок должен быть положительным.")
                    continue
                print(f"Введите матрицу {n}x{n} построчно (целые числа через пробел):")
                matrix = []
                for i in range(n):
                    row = list(map(int, input(f"Строка {i+1}: ").split()))
                    if len(row) != n:
                        print(f"Ошибка: в строке должно быть {n} чисел.")
                        break
                    matrix.append(row)
                else:
                    return n, matrix
            except ValueError:
                print("Ошибка ввода. Введите целые числа.")

    elif choice == '2':
        n = random.randint(3, 6)
        matrix = [[random.randint(-10, 10) for _ in range(n)] for _ in range(n)]
        print(f"\nСгенерированная матрица порядка {n} с помощью модуля random:")
        for row in matrix:
            print(" ".join(f"{x:5d}" for x in row))
        return n, matrix
    
    else:
        examples = [
            (3, [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]),
            (4, [[2, -1, 0, 3], [-5, 4, 2, -3], [1, 2, 3, 4], [0, -2, 5, -1]]),
            (3, [[5, 6, 7], [1, -1, 1], [-2, -3, -4]]),
            (4, [[-1, -2, -3, -4], [5, 6, 7, 8], [9, 10, -11, 12], [13, -14, 15, -16]]),
            (3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
            ]
        print("\nГотовые примеры:")
        for idx, (n_val, mat) in enumerate(examples, 1):
            print(f"{idx}: порядок {n_val}")
            for row in mat:
                print("  ", " ".join(f"{x:4d}" for x in row))
            print()
        while True:
            try:
                num = int(input("Выберите номер примера: "))
                if 1 <= num <= len(examples):
                    n, matrix = examples[num - 1]
                    return n, matrix
                else:
                    print(f"Номер должен быть от 1 до {len(examples)}.")
            except ValueError:
                print("Ошибка ввода. Введите целое число.")

def choose_variant():
    """Выбор варианта вычисления b_i: (а, б, в, г)."""
    print("\nВыберите вариант вычисления b_i:")
    print("а) наименьший элемент от начала строки до главной диагонали включительно")
    print("б) первый положительный элемент (или 1, если нет)")
    print("в) сумма элементов за первым отрицательным (или 100, если нет отрицательных)")
    print("г) сумма элементов перед последним отрицательным (или -1, если нет отрицательных)")

    while True:
        var = input("Ваш выбор (а/б/в/г): ").strip().lower()
        if var in ('а', 'a', 'б', 'b', 'в', 'v', 'г', 'g'):
            # нормализуем
            if var in ('а', 'a'): return 'a'
            if var in ('б', 'b'): return 'b'
            if var in ('в', 'v'): return 'v'
            if var in ('г', 'g'): return 'd'
        print("Ошибка: введите а, б, в или г.")

def compute_b(matrix, n, variant):
    """Вычисляет вектор b согласно выбранному варианту."""
    b = []
    for i in range(n):
        row = matrix[i]
        if variant == 'a':
            # Элементы от j=0 до j=1 включительно (главная диагональ)
            sub = row[:i+1]
            b.append(min(sub))
        elif variant == 'b':
            pos = next((x for x in row if x > 0), None)
            b.append(pos if pos is not None else 1)
        elif variant == 'c':
            # Первый отрицательный элемент
             first_neg_idx = -1
             for idx, val in enumerate(row):
                 if val < 0:
                     first_neg_idx = idx
                     break
                 if first_neg_idx == -1:
                        b.append(100)
                 else:
                     # сумма элементов за ним (индексы > first_neg_idx)
                     s = sum(row[first_neg_idx + 1:])
                     b.append(s)
        elif variant == 'd':
            # Последний отрицательный элемент
            last_neg_idx  = -1
            for idx in range(n-1, -1, -1):
                if row[idx] < 0:
                    last_neg_idx = idx
                    break
            if last_neg_idx == -1:
                b.append(-1)
            else:
                # сумма элементов перед ним (индексы < last_neg_idx)
                s = sum(row[:last_neg_idx])
                b.append(s)
    return b

def main():
    data = get_matrix()
    if data is None:
        return
    n, matrix = data

    variant = choose_variant()
    b = compute_b(matrix, n, variant)

    # Вывод результатов
    print("\n" + "="*60)
    print("РЕЗУЛЬТАТЫ")
    print("="*60)
    print(f"Матрица порядка {n}:")
    for i, row in enumerate(matrix):
        print(f"Строка {i+1:2d}:", " ".join(f"{x:5d}" for x in row))

    variant_names = {'a': 'а', 'b': 'б', 'c': 'в', 'd': 'г'}
    print(f"\nВариант: {variant_names[variant]}")
    print("Вектор b:")
    for i, val in enumerate(b):
        print(f"  b_{i+1} = {val}")
    print("=" * 60)

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
