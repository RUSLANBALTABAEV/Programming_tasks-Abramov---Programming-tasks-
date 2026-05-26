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

def main():
    print("Задача 422: Выравнивание строк по ширине (justify)")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод")
    print("2 — Случайная генерация")
    print("3 — Готовые примеры")

    choice = input("Ваш выбор (1/2/3): ").strip()
    while choice not in ('1', '2', '3'):
        choice = input("Ошибка: выберите 1, 2 или 3: ").strip()

    if choice == '1':
        n = int(input("Введите количество строк n: "))
        m = int(input("Введите количество столбцов m: "))
        print(f"Введите {n} строк по {m} символов:")
        matrix = []
        for i in range(n):
            row = input(f"Строка {i+1}: ")
            if len(row) != m:
                if len(row) < m:
                    row = row.ljust(m)
                else:
                    row = row[:m]
            matrix.append(list(row))
    elif choice == '2':
        n = random.randint(3, 6)
        m = random.randint(12, 25)
        letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        matrix = []
        for _ in range(n):
            while True:
                num_words = random.randint(2, 5)
                words = [''.join(random.choice(letters) for _ in range(random.randint(2, 6))) for _ in range(num_words)]
                gaps = [random.randint(1, 4) for _ in range(num_words-1)]
                row = words[0]
                for gap, w in zip(gaps, words[1:]):
                    row += ' ' * gap + w
                if len(row) <= m:
                    row = row.ljust(m)
                else:
                    row = row[:m]
                if ' ' in row.rstrip():  # есть пробел внутри
                    break
            matrix.append(list(row))
        print(f"\nСгенерирована матрица {n}×{m}:")
        for row in matrix:
            print(''.join(row))
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
        print("Готовые примеры:")
        for idx, (n_val, m_val, rows) in enumerate(examples, 1):
            print(f"{idx}: {n_val}×{m_val}")
            for row in rows:
                print(row)
        num = int(input("Выберите номер примера: "))
        n, m, rows = examples[num-1]
        matrix = [list(row) for row in rows]

    # Обработка строк (выравнивание)
    result = []
    for i in range(n):
        text = ''.join(matrix[i])
        words = text.split()
        if not words:
            result.append(matrix[i])
            continue
        if len(words) == 1:
            new_row = list(words[0]) + [' '] * (m - len(words[0]))
            result.append(new_row[:m])
            continue

        total_letters = sum(len(w) for w in words)
        total_spaces = m - total_letters
        gaps = len(words) - 1

        base = total_spaces // gaps
        extra = total_spaces % gaps  # первые extra промежутков получат +1 пробел

        new_row = []
        for j in range(gaps):
            new_row.extend(list(words[j]))
            spaces = base + (1 if j < extra else 0)
            new_row.extend([' '] * spaces)
        new_row.extend(list(words[-1]))
        result.append(new_row[:m])

    print("\nРезультат (выровненная матрица):")
    for row in result:
        print(''.join(row))

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
