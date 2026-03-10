"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
11. Вложенные циклы в матричных задачах

381. Все элементы с наибольшим значением в данной целочисленной квадратной матрице порядка 10 заменить нулями.
"""


import random

def get_matrix():
    """Выбор способа ввода целочисленной матрицы 10x10."""
    print("=== Задача 381: Замена нулями всех максимальных элементов ===")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод")
    print("2 — Случайная генерация")
    print("3 — Готовые примеры")

    choice = input("Ваш выбор (1/2/3): ").strip()
    while choice not in ('1', '2', '3'):
        choice = input("Выберите 1, 2 или 3: ").strip()

    n = 10  # порядок матрицы

    if choice == '1':
        try:
            print(f"Введите матрицу {n}x{n} построчно (целые числа):")
            matrix = []
            for i in range(n):
                row = list(map(int, input(f"Строка {i+1}: ").split()))
                if len(row) != n:
                    print(f"Ошибка: в строке должно быть {n} чисел.")
                    return None
                matrix.append(row)
            return matrix
        except ValueError:
            print("Ошибка ввода. Введите целые числа.")
            return None

    elif choice == '2':
        matrix = [[random.randint(-10, 10) for _ in range(n)] for _ in range(n)]
        print("\nСгенерирована матрица 10x10:")
        for row in matrix:
            print(" ".join(f"{x:4d}" for x in row))
        return matrix

    else:
        examples = [
            [[i*j for j in range(1,11)] for i in range(1,11)],
            [[random.randint(1,20) for _ in range(10)] for _ in range(10)],
            [[1,2,3,4,5,6,7,8,9,10] for _ in range(10)],
            [[0]*10 for _ in range(10)]  # все нули
        ]
        print("\nГотовые примеры:")
        for idx, ex in enumerate(examples, 1):
            print(f"{idx}: Первая строка: {ex[0][:5]}...")
        try:
            num = int(input("Выберите номер примера: "))
            if 1 <= num <= len(examples):
                return examples[num-1]
            else:
                print("Неверный номер!")
                return None
        except ValueError:
            print("Ошибка ввода.")
            return None

def main():
    matrix = get_matrix()
    if matrix is None:
        return

    print("\nИсходная матрица:")
    for row in matrix:
        print(" ".join(f"{x:4d}" for x in row))

    # Находим максимальное значение
    max_val = max(max(row) for row in matrix)

    if max_val == 0:
        print("\nМаксимальный элемент = 0, матрица остаётся без изменений.")
    else:
        print(f"\nМаксимальный элемент = {max_val}")

    # Заменяем все вхождения max_val на 0
    modified = [row[:] for row in matrix]  # копия
    for i in range(10):
        for j in range(10):
            if modified[i][j] == max_val:
                modified[i][j] = 0

    print("\nМатрица после замены:")
    for row in modified:
        print(" ".join(f"{x:4d}" for x in row))

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
