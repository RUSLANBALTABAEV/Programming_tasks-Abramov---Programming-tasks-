"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
11. Вложенные циклы в матричных задачах

384. Дана действительная матрица размера m*n. Найти сумму наибольших значений элементов ее строк.
"""


import random

def get_matrix():
    """Выбор способа ввода размеров и элементов матрицы."""
    print("=== Задача 384: Сумма наибольших значений элементов строк ===")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод")
    print("2 — Случайная генерация")
    print("3 — Готовые примеры")

    choice = input("Ваш выбор (1/2/3): ").strip()
    while choice not in ('1', '2', '3'):
        choice = input("Выберите 1, 2 или 3: ").strip()

    if choice == '1':
        try:
            m = int(input("Введите количество строк m (>0): "))
            n = int(input("Введите количество столбцов n (>0): "))
            if m <= 0 or n <= 0:
                print("Размеры должны быть положительными.")
                return None
            print("Введите матрицу построчно (действительные числа):")
            matrix = []
            for i in range(m):
                row = list(map(float, input(f"Строка {i+1}: ").split()))
                if len(row) != n:
                    print(f"Ошибка: в строке должно быть {n} чисел, получено {len(row)}.")
                    return None
                matrix.append(row)
            return m, n, matrix
        except ValueError:
            print("Ошибка ввода.")
            return None

    elif choice == '2':
        m = random.randint(2, 6)
        n = random.randint(2, 7)
        matrix = [[random.uniform(-10, 10) for _ in range(n)] for _ in range(m)]
        print(f"\nСгенерирована матрица {m}×{n}:")
        for row in matrix:
            print(" ".join(f"{x:8.4f}" for x in row))
        return m, n, matrix

    else:
        examples = [
            (2, 3, [[1, 2, 3], [4, 5, 6]]),
            (3, 2, [[-1.5, 2.3], [3.1, -4.2], [5.7, -6.8]]),
            (2, 4, [[0, 0, 0, 0], [1, -1, 2, -2]]),
            (3, 3, [[1, 1, 1], [2, 2, 2], [3, 3, 3]]),
            (4, 1, [[10], [20], [30], [40]])  # вектор-столбец
        ]
        print("\nГотовые примеры (m, n, матрица):")
        for idx, (m_val, n_val, mat) in enumerate(examples, 1):
            print(f"{idx}: {m_val}×{n_val}, первый элемент {mat[0][0]}")
        try:
            num = int(input("Выберите номер примера: "))
            if 1 <= num <= len(examples):
                m, n, matrix = examples[num-1]
                return m, n, matrix
            else:
                print("Неверный номер!")
                return None
        except ValueError:
            print("Ошибка ввода.")
            return None

def main():
    data = get_matrix()
    if data is None:
        return
    m, n, matrix = data

    # Вычисление суммы максимумов по строкам
    total = 0.0
    for i in range(m):
        row_max = max(matrix[i])  # находим максимум в строке
        total += row_max
        print(f"Максимум в строке {i+1}: {row_max:.6f}")

    print("\n" + "="*50)
    print("РЕЗУЛЬТАТ")
    print("="*50)
    print(f"Сумма наибольших значений элементов строк: {total:.6f}")
    print("="*50)

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
