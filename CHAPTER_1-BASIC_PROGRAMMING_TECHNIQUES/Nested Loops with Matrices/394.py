"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
11. Вложенные циклы в матричных задачах

394. Дана целочисленная квадратная матрица порядка n. Найти номера строк:
а) все элементы которых – нули;
б) элементы в каждой из которых одинаковы;
в) все элементы которых четны;
г) элементы каждой из которых образуют монотонную последовательность (монотонно убывающую или монотонно возрастающую);
д) элементы которых образуют симметричные последовательности (палиндромы).
"""


import random

def get_matrix():
    """Выбор способа ввода квадратной матрицы порядка n."""
    print("Задача 394: Поиск строк с заданными свойствами")
    print("Выберите способ ввода:")
    print("1 - Ручной ввод")
    print("2 - Случайные числы")
    print("3 - Готовые примеры")

    while True:
        choice = input("Ваш выбор (1/2/3): ").strip()
        if choice in ('1', '2', '3'):
            break
        print("Ошибка: выберите 1, 2 или 3.")

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
                print("Попробуйте ввести матрицу заново.")
            except ValueError:
                print("Ошибка ввода. Ожидаются целые числа.")

    elif choice == '2':
        n = random.randint(3, 6)
        matrix = [[random.randint(-5, 5) for _ in range(n)] for _ in range(n)]
        print(f"\nСгенерированная матрица порядка {n} с помощью модуля random: случайных чисел от -5 до 5")
        for row in matrix:
            print(" ".join(f"{x:4d}" for x in row))
        return n, matrix
    
    else:
        examples = [
            (3, [[0, 0, 0], [1, 1, 1], [2, 4, 6]]),
            (4, [[0, 0, 0, 0], [3, 3, 3, 3], [1, 2, 3, 4], [5, 4, 3, 2]]),
            (3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            (4, [[2, 2, 2, 2], [0, 0, 0, 0], [1, 3, 5, 7], [1, 2, 1, 2]]),
            (5, [[1, 2, 3, 2, 1], [5, 5, 5, 5, 5], [0, 0, 0, 0, 0], [1, 3, 2, 4, 5], [2, 4, 6, 8, 10]])
            ]
        print("\nГотовые примеры:")
        for idx, (n_val, mat) in enumerate(examples, 1):
            print(f"{idx}: порядок {n_val}")
            for row in mat:
                print("  ", " ".join(f"{x:3d}" for x in row))
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

def all_zeros(row):
    """Проверяет, все ли элементы строки равны нулю."""
    return all(x == 0 for x in row)

def all_equal(row):
    """Проверяет, все ли элементы строки одинаковы."""
    return len(set(row)) == 1

def all_even(row):
    """Проверяет, все ли элементы строки чётные."""
    return all(x % 2 == 0 for x in row)

def is_monotonic(row):
    """Проверяет, образует ли строка монотонную (неубывающую или невозрастающую) последовательность."""
    if len(row) <= 1:
        return True
    # Проверка на неубывание
    nod_decreasing = all(row[i] <= row[i+1] for i in range(len(row) - 1))
    # Проверка на невозрастание
    nod_increasing = all(row[i] >= row[i+1] for i in range(len(row) - 1))

def is_palindrome(row):
    """Проверяет, является ли строка палиндромом."""
    return row == row[::-1]

def main():
    data = get_matrix()
    if data is None:
        return
    n, matrix = data

    # Списки номеров строк (индексация с 1)
    rows_zeros = []
    rows_equal = []
    rows_even = []
    rows_monotonic = []
    rows_palindrome = []

    for i, row in enumerate(matrix):
        if all_zeros(row):
            rows_zeros.append(i+1)
        if all_equal(row):
            rows_equal.append(i+1)
        if all_even(row):
            rows_even.append(i+1)
        if is_monotonic(row):
            rows_monotonic.append(i+1)
        if is_palindrome(row):
            rows_palindrome.append(i+1)

    # Вывод результатов
    print("\n" + "=" * 60)
    print("РЕЗУЛЬТАТЫ")
    print("=" * 60)
    print(f"Матрица порядка {n}:")
    for i, row in enumerate(matrix):
        print(f"Строка {i+1:2d}:", " ".join(f"{x:4d}" for x in row))

    def print_rows(title, lst):
        if lst:
            print(f"{title}: {lst}")
        else:
            print(f"{title}: нет таких строк")
        
        print("\nНомера строк, удовлетворяющих условиям:")
        print_rows("а) все элементы - нули", rows_zeros)
        print_rows("б) все элементы одинаковы", rows_equal)
        print_rows("в) все элементы чётные", rows_even)
        print_rows("г) монотонная последовательность (неубывающая или невозрастающая)", rows_monotonic)
        print_rows("д) симметричная последовательность (палиндром)", rows_palindrome)

        print("=" * 60)

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
