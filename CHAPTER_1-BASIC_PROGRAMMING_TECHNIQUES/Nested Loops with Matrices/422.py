"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
11. Вложенные циклы в матричных задачах

422. При перепечатке текста на пишущей машинке часто получается так, что в конце строки остаётся несколько неиспользованных позиций. Число неиспользованных позиций меняется от строки к строке, и поэтому правый край отпечатанного текста получается неровным. Типографский набор даёт ровный правый край, в частности, за счёт увеличения промежутков между словами,
встречающимися в строке. 
Предполагается задача выбора подходящих промежутков. Дана
символьная матрица n×m, в каждой из строк которой имеется по
крайней мере один пробел, за которым следует отличный от пробела
символ (т. е. имеется по крайней мере одна группа пробелов внутри
строки). За счёт изменения групп пробелов внутри строк надо добиться
того, чтобы в конце каждой из строк пробелы отсутствовали.
Количества пробелов в разных группах, располагающихся внутри
одной и той же строки, должны различаться не более чем на единицу.
"""


import random

# ------------------------------------------------------------
# 1. Функции ввода матрицы
# ------------------------------------------------------------
def get_matrix():
    """Выбор способа ввода символьной матрицы n×m."""
    print("Задача 422: Выравнивание строк по ширине (justify)")
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
                n = int(input("Введите количество строк n: "))
                m = int(input("Введите количество столбцов m: "))
                if n <= 0 or m <= 0:
                    print("Размеры должны быть положительными.")
                    continue
                print(f"Введите {n} строк по {m} символов каждая:")
                matrix = []
                for i in range(n):
                    row_str = input(f"Строка {i+1}: ").rstrip('\n')
                    if len(row_str) != m:
                        # дополняем или обрезаем до m (с предупреждением)
                        if len(row_str) < m:
                            row_str = row_str.ljust(m)
                        else:
                            row_str = row_str[:m]
                    matrix.append(list(row_str))
                return n, m, matrix
            except ValueError:
                print("Ошибка ввода. Ожидаются целые числа.")

    elif choice == '2':
        # Случайная генерация: обязательно не менее двух слов в каждой строке
        n = random.randint(3, 6)
        m = random.randint(12, 25)
        letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        matrix = []
        for _ in range(n):
            # создаём строку, в которой не менее двух слов и есть внутренние пробелы
            while True:
                num_words = random.randint(2, 5)
                words = []
                for _ in range(num_words):
                    wlen = random.randint(2, 6)
                    word = ''.join(random.choice(letters) for _ in range(wlen))
                    words.append(word)
                # пробелы между словами (пока неравномерно)
                gaps = [random.randint(1, 4) for _ in range(num_words-1)]
                row = words[0]
                for gap, w in zip(gaps, words[1:]):
                    row += ' ' * gap + w
                # добавляем случайное число концевых пробелов, чтобы общая длина была m
                if len(row) < m:
                    row += ' ' * (m - len(row))
                elif len(row) > m:
                    # обрежем до m (потеряется часть последнего слова или пробелы – не страшно)
                    row = row[:m]
                # Проверим, что внутри есть пробел и он не в конце
                if ' ' in row and row[-1] != ' ':  # чтобы было чётко видно выравнивание
                    # но условие лишь требует наличие пробела в середине,
                    # а для наглядности сделаем так, что пробелы в конце есть
                    if ' ' in row.rstrip():
                        break
            matrix.append(list(row))
        print(f"\nСгенерирована матрица {n}×{m}:")
        for row in matrix:
            print(''.join(row))
        return n, m, matrix

    else:  # готовые примеры
        examples = [
            (3, 20,
             ["Hello  world  2024 ",
              "Python   is  great",
              "Justify    this  !"]),
            (4, 25,
             ["a   b  c   d        ",
              "one   two three    ",
              "The  quick  brown fox",
              "   too   many   spaces"])
        ]
        print("\nГотовые примеры:")
        for idx, (n_val, m_val, rows) in enumerate(examples, 1):
            print(f"{idx}: {n_val}×{m_val}")
            for row in rows:
                print(row)
        while True:
            try:
                num = int(input("Выберите номер примера: "))
                if 1 <= num <= len(examples):
                    n, m, rows = examples[num-1]
                    matrix = [list(row) for row in rows]
                    return n, m, matrix
                else:
                    print(f"Номер должен быть от 1 до {len(examples)}.")
            except ValueError:
                print("Ошибка ввода. Введите целое число.")

# ------------------------------------------------------------
# 2. Выравнивание строки
# ------------------------------------------------------------
def justify_row(row, m):
    """
    Принимает список символов строки длиной m.
    Возвращает новый список символов той же длины,
    в котором пробелы равномерно распределены между словами,
    а концевых пробелов нет (последний символ не пробел).
    """
    # Извлекаем слова и позиции пробелов
    # Сначала разбиваем на слова по пробелам (игнорируя ведущие и концевые пробелы)
    text = ''.join(row)
    words = text.split()  # разбивает по любым пробелам, удаляет пустоты
    num_words = len(words)
    if num_words == 0:
        # нет слов – оставляем строку как есть (вряд ли случится по условию)
        return row
    if num_words == 1:
        # по условию такого быть не должно, но на всякий случай
        # размещаем слово в начале, остальное – пробелы (будет нарушение, но выход)
        new_row = list(words[0]) + [' '] * (m - len(words[0]))
        return new_row[:m]

    # Общая длина всех слов
    total_letters = sum(len(w) for w in words)
    total_spaces_to_distribute = m - total_letters
    gaps = num_words - 1

    # Базовая длина промежутка
    base = total_spaces_to_distribute // gaps
    extra = total_spaces_to_distribute % gaps  # первые 'extra' промежутков получат +1 пробел

    # Собираем строку
    result = []
    for i in range(gaps):
        result.extend(list(words[i]))
        spaces_here = base + (1 if i < extra else 0)
        result.extend([' '] * spaces_here)
    result.extend(list(words[-1]))

    # Длина должна стать m; если нет (из-за округлений), корректируем
    if len(result) < m:
        # добавляем недостающие пробелы в последний промежуток? 
        # Лучше в конец, но это даст концевые пробелы. 
        # По логике должно быть точное равенство, т.к. total_spaces = m - total_letters.
        # Разве что total_spaces_to_distribute < 0? Это невозможно при корректных данных.
        pass
    elif len(result) > m:
        result = result[:m]

    return result

# ------------------------------------------------------------
# 3. Основная программа
# ------------------------------------------------------------
def main():
    n, m, matrix = get_matrix()

    print("\nИсходная матрица:")
    for row in matrix:
        print(''.join(row))

    # Обрабатываем каждую строку
    result_matrix = []
    for row in matrix:
        new_row = justify_row(row, m)
        result_matrix.append(new_row)

    print("\nВыровненная матрица (правый край ровный):")
    for row in result_matrix:
        print(''.join(row))

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
