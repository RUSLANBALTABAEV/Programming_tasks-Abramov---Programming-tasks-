"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
11. Вложенные циклы в матричных задачах

386. В данной действительной матрице размера 6*9 поменять местами строку, содержащую элемент с наибольшим значением, со строкой, содержащей элемент с наименьшим значением. Предполагается, что эти элементы единственны.
"""


import random

def get_matrix():
    """Выбор способа ввода матрицы 6×9."""
    print("=== Задача 386: Обмен строк с макс. и мин. элементами ===")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод")
    print("2 — Случайная генерация")
    print("3 — Готовые примеры")

    choice = input("Ваш выбор (1/2/3): ").strip()
    while choice not in ('1', '2', '3'):
        choice = input("Выберите 1, 2 или 3: ").strip()

    n_rows, n_cols = 6, 9

    if choice == '1':
        try:
            print(f"Введите матрицу {n_rows}x{n_cols} построчно (действительные числа):")
            matrix = []
            for i in range(n_rows):
                row = list(map(float, input(f"Строка {i+1}: ").split()))
                if len(row) != n_cols:
                    print(f"Ошибка: в строке должно быть {n_cols} чисел, получено {len(row)}.")
                    return None
                matrix.append(row)
            return matrix
        except ValueError:
            print("Ошибка ввода. Введите действительные числа.")
            return None

    elif choice == '2':
        matrix = [[random.uniform(-100, 100) for _ in range(n_cols)] for _ in range(n_rows)]
        print("\nСгенерирована матрица 6x9:")
        for row in matrix:
            print(" ".join(f"{x:8.4f}" for x in row))
        return matrix

    else:
        # Готовые примеры
        examples = [
            # Пример 1: числа от 1 до 54 по строкам
            [[i*9 + j + 1 for j in range(9)] for i in range(6)],
            # Пример 2: смесь положительных и отрицательных
            [[ (i+1)*(j+1) * (-1)**(i+j) for j in range(9)] for i in range(6)],
            # Пример 3: все нули, кроме одного минимума и максимума
            [[0]*9 for _ in range(6)],
            # Пример 4: равномерно возрастающие
            [[ (i+1)*0.5 + j for j in range(9)] for i in range(6)],
            # Пример 5: случайный, но фиксированный (зададим явно)
            [
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [9, 8, 7, 6, 5, 4, 3, 2, 1],
                [1, 3, 5, 7, 9, 8, 6, 4, 2],
                [2, 4, 6, 8, 1, 3, 5, 7, 9],
                [0, -1, -2, -3, -4, -5, -6, -7, -8],
                [10, 11, 12, 13, 14, 15, 16, 17, 18]
            ]
        ]
        # Модифицируем пример 3, чтобы был один минимум и максимум
        examples[2][0][0] = -100   # min
        examples[2][5][8] = 100    # max
        print("\nГотовые примеры:")
        for idx, ex in enumerate(examples, 1):
            print(f"{idx}: Первая строка: {ex[0][:4]}...")
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
        print(" ".join(f"{x:8.4f}" for x in row))

    # Поиск индексов строк с минимальным и максимальным элементами
    min_val = float('inf')
    max_val = float('-inf')
    min_row = max_row = -1

    for i, row in enumerate(matrix):
        for val in row:
            if val < min_val:
                min_val = val
                min_row = i
            if val > max_val:
                max_val = val
                max_row = i

    # Проверка на единственность (просто предупредим)
    count_min = sum(1 for row in matrix for val in row if val == min_val)
    count_max = sum(1 for row in matrix for val in row if val == max_val)
    if count_min > 1:
        print(f"\nПредупреждение: найдено {count_min} элементов с минимальным значением {min_val:.4f}. Используется первый (строка {min_row+1}).")
    if count_max > 1:
        print(f"Предупреждение: найдено {count_max} элементов с максимальным значением {max_val:.4f}. Используется первый (строка {max_row+1}).")

    if min_row == max_row:
        print("\nМинимальный и максимальный элементы находятся в одной строке. Обмен не имеет смысла.")
        return

    print(f"\nМинимальный элемент {min_val:.4f} находится в строке {min_row+1}")
    print(f"Максимальный элемент {max_val:.4f} находится в строке {max_row+1}")

    # Обмен строками
    matrix[min_row], matrix[max_row] = matrix[max_row], matrix[min_row]

    print("\nМатрица после обмена:")
    for row in matrix:
        print(" ".join(f"{x:8.4f}" for x in row))

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
