"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
11. Вложенные циклы в матричных задачах

420. Дано натуральное n, символьная квадратная матрица порядка n. Получить последовательность b1, …, bn из нулей и единиц, в которой bi = 1 тогда и только тогда, когда в i-строке число символов * не меньше числа пробелов. 
"""


import random


def get_matrix():
    """Выбор способа ввода символьной квадратной матрицы порядка n."""
    print("Задача 420: Подсчёт звёздочек и пробелов в строках")
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
                n = int(input("Введите порядок матрицы n (> 0): "))
                if n <= 0:
                    print("Порядок должен быть положительным.")
                    continue
                print(f"Введите {n} строк по {n} символов (без пробелов между символами):")
                matrix = []
                for i in range(n):
                    row_str = input(f"Строка {i+1}: ").rstrip('\n')
                    # При ручном вводе будем принимать строку длиной n (если меньше — добавим пробелы, если больше — обрежем)
                    if len(row_str) < n:
                        row_str = row_str.ljust(n)
                    elif len(row_str) > n:
                        row_str = row_str[:n]
                    matrix.append(list(row_str))
                return n, matrix
            except ValueError:
                print("Ошибка ввода. Ожидается целое число для n.")

    elif choice == '2':
        n = random.randint(3, 8)
        # Генерируем случайные строки из символов: '*', ' ', и ещё что-то для разнообразия
        symbols = ['*', ' ', 'A', 'B', 'C', '.', '-', '+']
        matrix = []
        for _ in range(n):
            row = [random.choice(symbols) for _ in range(n)]
            matrix.append(row)
        print(f"\nСгенерирована матрица порядка {n}:")
        for row in matrix:
            print("".join(row))
        return n, matrix

    else:
        # Готовые примеры
        examples = [
            (4, [['*', '*', ' ', '*'],
                 [' ', ' ', '*', ' '],
                 ['*', '*', '*', '*'],
                 [' ', ' ', ' ', ' ']]),
            (3, [['*', ' ', ' '],
                 [' ', '*', ' '],
                 ['*', '*', '*']]),
            (5, [['*', ' ', '*', ' ', '*'],
                 [' ', ' ', ' ', ' ', ' '],
                 ['*', '*', ' ', ' ', ' '],
                 ['*', '*', '*', '*', '*'],
                 [' ', '*', ' ', '*', ' ']])
        ]
        print("\nГотовые примеры:")
        for idx, (n_val, mat) in enumerate(examples, 1):
            print(f"{idx}: порядок {n_val}")
            for row in mat:
                print("".join(row))
        while True:
            try:
                num = int(input("Выберите номер примера: "))
                if 1 <= num <= len(examples):
                    return examples[num-1]
                else:
                    print(f"Номер должен быть от 1 до {len(examples)}.")
            except ValueError:
                print("Ошибка ввода. Введите целое число.")


def main():
    n, matrix = get_matrix()

    # Вывод исходной матрицы
    print("\nИсходная матрица:")
    for row in matrix:
        print("".join(row))

    # Формирование последовательности b
    b = []
    for i in range(n):
        stars = row.count('*') if (row := matrix[i]) else 0
        spaces = row.count(' ')
        b.append(1 if stars >= spaces else 0)

    print("\nПоследовательность b:")
    for i, val in enumerate(b):
        print(f"  b_{i+1} = {val}")

    print("\n(1 – звёздочек не меньше пробелов, 0 – иначе)")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
