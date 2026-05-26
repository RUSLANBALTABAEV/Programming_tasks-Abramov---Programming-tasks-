"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
11. Вложенные циклы в матричных задачах

421. Дана символьная матрица размера 13×18. Найти: 
а) номер первой по порядку строки, содержащий наибольшее число цифр;
б) номер первого по порядку столбца, содержащего наименьшее число пробелов на пересечении со строками, номера которых чётны; 
в) номер последней по порядку строки, содержащей наибольшее количество букв ш, щ;
г) номер последнего по порядку столбца, в котором содержится наибольшее количество попарно различных символов.
"""


import random

ROWS = 13
COLS = 18


def ensure_length(row_str, length=COLS):
    """Дополняет строку пробелами или обрезает до нужной длины."""
    if len(row_str) < length:
        return row_str.ljust(length)
    else:
        return row_str[:length]


def get_matrix():
    """Выбор способа ввода символьной матрицы 13×18."""
    print("Задача 421: Анализ символьной матрицы 13×18")
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
            print(f"Введите {ROWS} строк по {COLS} символов:")
            matrix = []
            for i in range(ROWS):
                row_str = input(f"Строка {i+1}: ").rstrip('\n')
                row_str = ensure_length(row_str)
                matrix.append(list(row_str))
            return matrix

    elif choice == '2':
        chars = (
            [chr(random.randint(65, 90)) for _ in range(5)] +
            [chr(random.randint(97, 122)) for _ in range(5)] +
            [chr(random.randint(48, 57)) for _ in range(5)] +
            [' ', ' ', ' ', 'ш', 'щ', '.', ',', '!', '?', '-']
        )
        matrix = [[random.choice(chars) for _ in range(COLS)] for _ in range(ROWS)]
        print("\nСгенерирована матрица 13×18:")
        for row in matrix:
            print("".join(row))
        return matrix

    else:
        # Готовые примеры (каждая строка ровно 18 символов)
        example1 = [
            "Hello World! 2024 ",   # дополнено пробелом до 18
            "Python 3.12 rule  ",   # дополнено пробелами
            "шщшщшщ шщ шщ шщ  ",
            "123456789012345678",
            "ABCDEFGHIJKLMNOPQR",
            "abcdefghijklmnopqr",
            "aaaa bbbb cccc dddd",
            "ш щ ш щ ш щ ш щ ш щ",
            "001122334455667788",
            "unique symbols here",
            "another line 12345",
            "шшшшшшшшшшшшшшшшшш",
            "finish 9999 8888 77"
        ]

        example2 = [
            "                  ",
            "                  ",
            "                  ",
            "ш щ ш щ ш щ ш щ ш щ",
            "шщшщшщшщшщшщшщшщшщ",
            "abcdefg 1234567890",
            "ABCDEFG 1234567890",
            "#### #### #### ###",
            ",,,, ,,,, ,,,, ,,,,",
            "111111111111111111",
            "222222222222222222",
            "шшшшшшшшшшшшшшшшшш",
            "abcdefghijklmnopqr"
        ]

        # Гарантируем, что все строки длиной 18
        examples = [
            [list(ensure_length(s)) for s in example1],
            [list(ensure_length(s)) for s in example2]
        ]
        print("\nГотовые примеры:")
        for idx, mat in enumerate(examples, 1):
            print(f"{idx}:")
            for row in mat:
                print("".join(row))
            print()
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
    matrix = get_matrix()

    print("\nИсходная матрица 13×18:")
    for row in matrix:
        print("".join(row))

    # а) Первая строка с наибольшим числом цифр
    max_digits = -1
    first_row_digits = -1
    for i in range(ROWS):
        digit_count = sum(1 for ch in matrix[i] if '0' <= ch <= '9')
        if digit_count > max_digits:
            max_digits = digit_count
            first_row_digits = i + 1

    # б) Первый столбец с наименьшим числом пробелов на чётных строках
    min_spaces = float('inf')
    first_col_spaces = -1
    for j in range(COLS):
        spaces_count = 0
        for i in range(1, ROWS, 2):   # строки 2,4,…,12 (индексы 1,3,…,11)
            if matrix[i][j] == ' ':
                spaces_count += 1
        if spaces_count < min_spaces:
            min_spaces = spaces_count
            first_col_spaces = j + 1

    # в) Последняя строка с наибольшим количеством 'ш' или 'щ'
    max_sh = -1
    last_row_sh = -1
    for i in range(ROWS):
        sh_count = sum(1 for ch in matrix[i] if ch in ('ш', 'щ'))
        if sh_count >= max_sh:
            max_sh = sh_count
            last_row_sh = i + 1

    # г) Последний столбец с наибольшим числом уникальных символов
    max_unique = -1
    last_col_unique = -1
    for j in range(COLS):
        unique = set(matrix[i][j] for i in range(ROWS))
        unique_count = len(unique)
        if unique_count >= max_unique:
            max_unique = unique_count
            last_col_unique = j + 1

    print("\n" + "=" * 40)
    print("РЕЗУЛЬТАТЫ")
    print("=" * 40)
    print(f"а) Номер первой строки с наибольшим числом цифр: {first_row_digits} (цифр: {max_digits})")
    print(f"б) Номер первого столбца с наименьшим числом пробелов на чётных строках: {first_col_spaces} (пробелов: {min_spaces})")
    print(f"в) Номер последней строки с наибольшим количеством 'ш'/'щ': {last_row_sh} (букв: {max_sh})")
    print(f"г) Номер последнего столбца с наибольшим количеством различных символов: {last_col_unique} (различных: {max_unique})")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
