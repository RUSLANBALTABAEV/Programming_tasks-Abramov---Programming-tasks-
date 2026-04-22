"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
11. Вложенные циклы в матричных задачах

392. Дана целочисленная квадратная матрица порядка 8. Найти наименьшее из значений элементов столбца, который обладает наибольшей суммой модулей элементов. Если таких столбцов несколько, то взять первый из них.
"""


import random

def get_matrix(n=8):
    """Выбор способа ввода целочисленной матрицы порядка n (по умолчанию 8)."""
    print(f"Задача 392. Наименьший элемент в столбце с наибольшей суммой модулей")
    print(f"Матрица порядка {n}")
    print("Выберите способ ввода:")
    print("1 - Ручной ввод")
    print("2 - Случайные числа")
    print("3 - Готовые примеры")

    while True:
        choice = input("Ваш выбор (1/2/3): ").strip()
        if choice in ('1', '2', '3'):
            break
        print("Ошибка: выберите 1, 2, или 3.")

    if choice == '1':
        while True:
            try:
                print(f"Введите матрицу {n}x{n} построчно (целые числа через пробел):")
                matrix = []
                for i in range(n):
                    row = list(map(int, input(f"Строка {i+1}: ").split()))
                    if len(row) != n:
                        print(f"Ошибка: в строке должно быть {n} чисел.")
                        break
                    matrix.append(row)
                else:
                    return matrix
                print("Попробуйте ввести матрицу занова.")
            except ValueError:
                print("Ошибка: введите только целые числа.")

    elif choice == '2':
        matrix = [[random.randint(-20, 20) for _ in range(n)] for _ in range(n)]
        print("\nСгенерированная матрица с помощью модуля random:")
        for row in matrix:
            print(" ".join(f"{x:5d}" for x in row))
        return matrix
    
    else:
        # Готовый примеры матриц 8x8
        examples = [
            ([[1, -2, 3, -4, 5, -6, 7, -8],
              [2, 3, 4, 5, 6, 7, 8, 9],
              [-1, -2, -3, -4, -5, -6, -7, -8],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [10, -10, 10, -10, 10, 10, -10, 10, -10],
              [1, 1, 1, 1, 1, 1, 1, 1],
              [5, -5, 5, -5, 5, -5, 5, -5],
              [9, 8, 7, 6, 5, 4, 3, 2]]),
            ([[-5, 2, 0, -3, 1, 4, -2, 3],
              [6, -7, 8, -9, 10, -11, 12, -13],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [1, 2, 3, 4, 5, 6, 7, 8],
              [-1, -2, -3, -4, -5, -6, -7, -8],
              [15, -14, 13, -12, 11, -10, 9, -8],
              [2, 2, 2, 2, 2, 2, 2, 2],
              [7, 6, 5, 4, 3, 2, 1, 0]]),
            ([[1, 2, 3, 4, 5, 6, 7, 8],
              [8, 7, 6, 5, 4, 3, 2, 1],
              [0, -1, -2, -3, -4, -5, -6, -7],
              [10, 10, 10, 10, 10, 10, 10, 10],
              [-10, -10, -10, -10, -10, -10, -10, -10],
              [5, 5, 5, 5, 5, 5, 5, 5],
              [-5, -5, -5, -5, -5, -5, -5, -5],
              [2, -2, 2, -2, 2, -2, 2, -2]])
        ]
        print("\nГотовые примеры матрицы 8x8):")
        for idx, mat in enumerate(examples, 1):
            print(f"{idx}:")
            for row in mat:
                print("  ", " ".join(f"{x:4d}" for x in row))
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

def main():
    n = 8 # Порядок матрицы
    matrix = get_matrix(n)
    if matrix is None:
        return
    
    # Вычисляем сумму модулей по столбцам
    sums = [0] * n
    for j in range(n):
        col_sum = sum(abs(matrix[i][j]) for i in range(n))
        sums[j] = col_sum

    # Находим столбец с максимальной суммой модулей (первый при равенстве)
    max_sum = max(sums)
    max_col_index = sums.index(max_sum)

    # Находим наименьший элемент в этом столбце
    min_in_col = min(matrix[i][max_col_index] for i in range(n))

    # Вывод результатов
    print("\n" + "=" * 70)
    print("РЕЗУЛЬТАТЫ")
    print("Исходная матрица:")
    for i, row in enumerate(matrix):
        print(f"Строка {i+1:2d}:", " ".join(f"{x:5d}" for x in row))

    print("\nСуммы модулей по столбцам:")
    for j in range(n):
        print(f"Столбец {j+1:2d}: {sums[j]:4d}")

    print(f"\nМаксимальная сумма модулей: {max_sum}")
    print(f"Номер столбца с максимальной суммой модулей: {max_col_index + 1} (индекс {max_col_index})")

    print("=" * 70)

if __name__ == "__main__":
    main()
    input("\nнажмите Enter, чтобы завершить программу.")
