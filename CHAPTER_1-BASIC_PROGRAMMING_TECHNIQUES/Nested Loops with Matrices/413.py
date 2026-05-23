"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
11. Вложенные циклы в матричных задачах

413. Таблица футбольного чемпионата задана квадратной матрицей порядка n, в которой все элементы, принадлежащие главной диагонали, равны нулю, а каждый элемент, не принадлежащий главной диагонали, равен 2, 1 или 0 (числу очков, набранных в игре: 2 — выигрыш, 1 — ничья, 0 — проигрыш). 
а) Найти число команд, имеющих больше побед, чем поражений.
б) Определить номера команд, прошедших чемпионат без поражений.
в) Выяснить, имеется ли хотя бы одна команда, выигравшая более половины игр.
"""


import random

def get_matrix():
    """Получение квадратной матрицы порядка n, описывающей результаты чемпионата."""
    print("Задача 413: Анализ футбольного чемпионата")
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
                n = int(input("Введите количество команд n (> 0): "))
                if n <= 0:
                    print("Число команд должно быть положительным.")
                    continue
                print("Введите матрицу результатов построчно (0, 1 или 2, на диагонали 0):")
                matrix = []
                for i in range(n):
                    row = list(map(int, input(f"Строка {i+1}: ").split()))
                    if len(row) != n:
                        print(f"Ошибка: в строке должно быть {n} чисел.")
                        break
                    # Проверка корректности значений
                    valid = all(x in (0, 1, 2) for x in row)
                    if not valid:
                        print("Значения должны быть 0, 1 или 2.")
                        break
                    if row[i] != 0:
                        print("Диагональный элемент должен быть равен 0.")
                        break
                    matrix.append(row)
                else:
                    return n, matrix
                print("Попробуйте ввести матрицу заново.")
            except ValueError:
                print("Ошибка ввода. Ожидаются целые числа.")

    elif choice == '2':
        n = random.randint(4, 8)
        matrix = []
        for i in range(n):
            row = []
            for j in range(n):
                if i == j:
                    row.append(0)
                else:
                    row.append(random.choice([0, 1, 2]))
            matrix.append(row)
        print(f"\nСгенерирована матрица {n}×{n}:")
        for row in matrix:
            print(" ".join(f"{x:2d}" for x in row))
        return n, matrix

    else:
        examples = [
            (4, [
                [0, 2, 1, 0],
                [0, 0, 2, 2],
                [1, 0, 0, 2],
                [2, 0, 0, 0]
            ]),
            (3, [
                [0, 2, 2],
                [0, 0, 2],
                [0, 0, 0]
            ]),
            (5, [
                [0, 2, 1, 2, 2],
                [0, 0, 2, 0, 1],
                [1, 0, 0, 2, 1],
                [0, 2, 0, 0, 2],
                [0, 1, 1, 0, 0]
            ])
        ]
        print("\nГотовые примеры:")
        for idx, (n_val, mat) in enumerate(examples, 1):
            print(f"{idx}: {n_val} команд")
            for row in mat:
                print("  ", " ".join(f"{x:2d}" for x in row))
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

    wins = [0] * n
    losses = [0] * n

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if matrix[i][j] == 2:
                wins[i] += 1
            elif matrix[i][j] == 0:
                losses[i] += 1

    # а) Число команд с победами > поражений
    count_a = sum(1 for i in range(n) if wins[i] > losses[i])
    print(f"\nа) Число команд, имеющих больше побед, чем поражений: {count_a}")

    # б) Команды без поражений
    undefeated = [i+1 for i in range(n) if losses[i] == 0]
    if undefeated:
        print("б) Номера команд, прошедших чемпионат без поражений:", undefeated)
    else:
        print("б) Команд без поражений нет.")

    # в) Есть ли команда, выигравшая более половины игр
    half_games = (n - 1) / 2
    exists = any(wins[i] > half_games for i in range(n))
    if exists:
        print("в) Да, есть хотя бы одна команда, выигравшая более половины игр.")
    else:
        print("в) Нет, ни одна команда не выиграла более половины игр.")

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
