"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
11. Вложенные циклы в матричных задачах

401. Дана действительная квадратная матрица порядка n, натуральные числа i, j (1 <= i <= n, 1 <= j <= n). Из матрицы удалить i-строку и j-столбец.
"""


import random

def get_matrix_and_indices():
    """
    Выбор способа ввода квадратной матрицы порядка n и индексов i, j.
    Возвращает (n, matrix, i, j).
    """
    print("=== Задача 401: Удаление i-й строки и j-го столбца ===")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод")
    print("2 — Случайная числа")
    print("3 — Готовые примеры")

    while True:
        choice = input("Ваш выбор (1/2/3): ").strip()
        if choice in ('1', '2', '3'):
            break
        print("Ошибка: выберите 1, 2 или 3.")

    if choice == '1':
        while True:
            try:
                n = int(input("Введите порядок матрицы n (> 1, чтобы можно было удалить): "))
                if n <= 1:
                    print("Порядок должен быть больше 1.")
                    continue
                print(f"Введите матрицу {n}×{n} построчно (действительные числа через пробел):")
                matrix = []
                for k in range(n):
                    row = list(map(float, input(f"Строка {k+1}: ").split()))
                    if len(row) != n:
                        print(f"Ошибка: в строке должно быть {n} чисел.")
                        break
                    matrix.append(row)
                else:
                    # Ввод индексов
                    i = int(input(f"Введите номер строки для удаления (1..{n}): "))
                    j = int(input(f"Введите номер столбца для удаления (1..{n}): "))
                    if 1 <= i <= n and 1 <= j <= n:
                        return n, matrix, i, j
                    else:
                        print(f"Индексы должны быть в диапазоне 1..{n}.")
                        continue
                print("Попробуйте ввести матрицу заново.")
            except ValueError:
                print("Ошибка ввода. Ожидаются числа.")

    elif choice == '2':
        n = random.randint(3, 6)
        matrix = [[round(random.uniform(-5, 5), 2) for _ in range(n)] for _ in range(n)]
        i = random.randint(1, n)
        j = random.randint(1, n)
        print(f"\nСгенерированы: n = {n}, i = {i}, j = {j}")
        print("Матрица:")
        for row in matrix:
            print(" ".join(f"{x:8.2f}" for x in row))
        return n, matrix, i, j

    else:
        # Готовые примеры
        examples = [
            (3, [
                [1.0, 2.0, 3.0],
                [4.0, 5.0, 6.0],
                [7.0, 8.0, 9.0]
            ], 2, 2),
            (4, [
                [1.1, 2.2, 3.3, 4.4],
                [5.5, 6.6, 7.7, 8.8],
                [9.9, 10.0, 11.1, 12.2],
                [13.3, 14.4, 15.5, 16.6]
            ], 1, 4),
            (3, [
                [0.0, 0.0, 0.0],
                [1.0, -1.0, 2.0],
                [2.0, -2.0, 3.0]
            ], 3, 1),
            (2, [
                [10.0, 20.0],
                [30.0, 40.0]
            ], 1, 2)
        ]
        print("\nГотовые примеры:")
        for idx, (n_val, mat, i_val, j_val) in enumerate(examples, 1):
            print(f"{idx}: n = {n_val}, удалить строку {i_val}, столбец {j_val}")
            for row in mat:
                print("   ", " ".join(f"{x:6.2f}" for x in row))
            print()
        while True:
            try:
                num = int(input("Выберите номер примера: "))
                if 1 <= num <= len(examples):
                    n, matrix, i, j = examples[num-1]
                    return n, matrix, i, j
                else:
                    print(f"Номер должен быть от 1 до {len(examples)}.")
            except ValueError:
                print("Ошибка ввода. Введите целое число.")

def remove_row_and_column(matrix, i, j):
    """Удаляет i-ю строку и j-й столбец из матрицы. Индексы с 1."""
    new_matrix = []
    for r, row in enumerate(matrix):
        if r == i - 1:   # пропускаем i-ю строку
            continue
        new_row = [elem for c, elem in enumerate(row) if c != j - 1]
        new_matrix.append(new_row)
    return new_matrix

def main():
    data = get_matrix_and_indices()
    if data is None:
        return
    n, matrix, i, j = data

    new_matrix = remove_row_and_column(matrix, i, j)

    # Вывод результатов
    print("\n" + "=" * 60)
    print("РЕЗУЛЬТАТЫ")
    print("=" * 60)
    print(f"Исходная матрица порядка {n}:")
    for idx, row in enumerate(matrix):
        print(f"Строка {idx+1:2d}:", " ".join(f"{x:8.2f}" for x in row))

    print(f"\nУдаляем строку {i} и столбец {j}.")
    print(f"\nМатрица после удаления (порядок {n-1}):")
    if new_matrix:
        for idx, row in enumerate(new_matrix):
            print(f"Строка {idx+1:2d}:", " ".join(f"{x:8.2f}" for x in row))
    else:
        print("(пустая матрица)")

    print("="*60)

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
