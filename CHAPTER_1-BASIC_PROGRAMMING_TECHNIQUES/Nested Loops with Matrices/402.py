"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
11. Вложенные циклы в матричных задачах

402. Даны натуральное число n >= 2, действительная квадратная матрица порядка n. Построить последовательность b1, ..., bn из нулей и единиц, в которой bi = 1 тогда и только тогда, когда 
а) элементы i-строки матрицы образуют возрастающую последовательность;
б) элементы i-строки матрицы образуют возрастающую убывающую или убывающую последовательность.
"""


import random

def get_matrix():
    """Выбор способа ввода действительной квадратной матрицы порядка n (n ≥ 2)."""
    print("Задача 402: Бинарный вектор по монотонности строк")
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
                n = int(input("Введите порядок матрицы n (>= 2): "))
                if n < 2:
                    print("Порядок должен быть >= 2.")
                    continue
                print(f"Введите матрицу {n}x{n} построчно (действителые числа через пробел):")
                matrix = []
                for i in range(n):
                    row = list(map(float, input(f"Строка {i+1}: ").split()))
                    if len(row) != n:
                        print(f"Ошибка: в строке должно быть {n} чисел.")
                        break
                    matrix.append(row)
                else:
                    return n, matrix
                print("Попробуйте ввести матрицу заново.")
            except ValueError:
                print("Ошибка ввода. Ожидает числа.")

    elif choice == '2':
        n = random.randint(3, 5)
        matrix = [[round(random.uniform(-5, 5), 2) for _ in range(n)] for _ in range(n)]
        print(f"\nСгенерирована матрица порядка {n}:")
        for row in matrix:
            print(" ".join(f"{x:8.2f}" for x in row))
        return n, matrix
    
    else:
        examples = [
            (3, [[1.0, 2.0, 3.0], [3.0, 2.0, 1.0], [1.0, 0.0, 2.0]]),   # строго возраст, строго убыв, не монот
            (4, [[0.1, 0.2, 0.3, 0.4], [5.5, 5.0, 4.5, 4.0], [7.7, 7.7, 7.7, 7.7], [9.0, 8.0, 10.0, 11.0]]),
            (2, [[-1.0, 2.0], [2.0, -1.0]]),
            (3, [[1.0, 2.0, 2.0], [2.0, 2.0, 1.0], [1.0, 3.0, 2.0]])
        ]
        print("\nГотовые примеры:")
        for idx, (n_val, mat) in enumerate(examples, 1):
            print(f"{idx}: порядок {n_val}")
            for row in mat:
                print("  ", " ".join(f"{x:6.2f}" for x in row))
            print()
        while True:
            try:
                num = int(input("Выберите номер примера: "))
                if 1 <= num <= len(examples):
                    return examples[num - 1]
                else:
                    print(f"Номер должен быть от 1 до {len(examples)}.")
            except ValueError:
                print("Ошибка ввода. Введите целое число.")

def is_strictly_increasing(row):
    """Проверяет строгое возрастание элементов."""
    return all(row[i] < row[i + 1] for i in range(len(row) - 1))

def is_strictly_monotonic(row):
    """Проверяет строгую монотонность (возрастание или убывание)."""
    return is_strictly_increasing(row) or all(row[i] > row[i + 1] for i in range(len(row) - 1))

def choose_variant():
    """Выбор условия (а или б)."""
    print("\nВыберите условие для b_i = 1:")
    print("а) элементы строки образуют возрастающую последовательность")
    print("б) элементы строки образуют возрастающую или убывающую последовательность")
    while True:
        var = input("Ваш выбор (а/б): ").strip().lower()
        if var in ('а', 'a'): return 'a'
        if var in ('б', 'b'): return 'b'
        print("Ошибка: введите 'а' или 'б'.")

def main():
    n, matrix = get_matrix()
    variant = choose_variant()

    if variant == 'a':
        check_func = is_strictly_increasing
    else:
        check_func = is_strictly_monotonic

    b = [1 if check_func(row) else 0 for row in matrix]

    # Вывод
    print("\n" + "=" * 60)
    print("РЕЗУЛЬТАТЫ")
    print("=" * 60)
    print(f"Матрица порядка {n}:")
    for i, row in enumerate(matrix):
        print(f"Строка {i+1:2d}:", " ".join(f"{x:8.2f}" for x in row))

    print(f"\nВектор b (условие: {variant}):")
    for i, val in enumerate(b):
        print(f"  b_{i+1} = {val}")
    print("=" * 60)

if __name__ == "__main__":
    main()
    input("\Нажмите Enter, чтобы завершить программу.")
