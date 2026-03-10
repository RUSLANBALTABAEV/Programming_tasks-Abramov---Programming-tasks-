"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
11. Вложенные циклы в матричных задачах

383. Дана действительная матрица размера 18*n. Найти значение наибольшего по модулю элемента матрицы, а также индексы какого-нибудь элемента с найденным значением модуля.
"""


import random

def get_matrix():
    """Выбор способа ввода матрицы 18×n."""
    print("=== Задача 383: Наибольший по модулю элемент матрицы 18×n ===")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод")
    print("2 — Случайная генерация")
    print("3 — Готовые примеры")

    choice = input("Ваш выбор (1/2/3): ").strip()
    while choice not in ('1', '2', '3'):
        choice = input("Выберите 1, 2 или 3: ").strip()

    n_rows = 18

    if choice == '1':
        try:
            n = int(input("Введите количество столбцов n (>0): "))
            if n <= 0:
                print("n должно быть положительным.")
                return None
            print(f"Введите матрицу {n_rows}×{n} построчно (действительные числа):")
            matrix = []
            for i in range(n_rows):
                row = list(map(float, input(f"Строка {i+1}: ").split()))
                if len(row) != n:
                    print(f"Ошибка: в строке должно быть {n} чисел, получено {len(row)}.")
                    return None
                matrix.append(row)
            return matrix
        except ValueError:
            print("Ошибка ввода.")
            return None

    elif choice == '2':
        n = random.randint(1, 10)
        matrix = [[random.uniform(-100, 100) for _ in range(n)] for _ in range(n_rows)]
        print(f"\nСгенерирована матрица {n_rows}×{n}:")
        for i, row in enumerate(matrix):
            print(f"Строка {i+1}: " + " ".join(f"{x:8.4f}" for x in row))
        return matrix

    else:
        examples = [
            # Несколько примеров с разными n
            ([[i*j for j in range(1,4)] for i in range(1,19)], 3),  # n=3
            ([[random.randint(-10,10) for _ in range(5)] for _ in range(18)], 5),  # n=5
            ([[1.5, -2.3, 4.7] for _ in range(18)], 3),  # n=3, все строки одинаковы
            ([[0]*2 for _ in range(18)], 2),  # n=2, все нули
            ([[(-1)**i * i*j for j in range(1,4)] for i in range(1,19)], 3)  # знакопеременные
        ]
        # Для определённости зафиксируем конкретные матрицы
        # В примерах укажем только матрицы, а n определим из длины строки
        print("\nГотовые примеры:")
        for idx, (mat, n_val) in enumerate(examples, 1):
            print(f"{idx}: {n_val} столбцов, первая строка: {mat[0][:5]}")
        try:
            num = int(input("Выберите номер примера: "))
            if 1 <= num <= len(examples):
                matrix, _ = examples[num-1]
                return matrix
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

    n_rows = len(matrix)
    n_cols = len(matrix[0]) if n_rows > 0 else 0

    # Поиск максимального по модулю элемента
    max_abs = -1.0
    max_i = max_j = -1
    for i in range(n_rows):
        for j in range(n_cols):
            val = abs(matrix[i][j])
            if val > max_abs:
                max_abs = val
                max_i, max_j = i, j

    print("\n" + "="*60)
    print("РЕЗУЛЬТАТ")
    print("="*60)
    if max_abs >= 0:
        print(f"Наибольший по модулю элемент: {matrix[max_i][max_j]:.6f} (модуль {max_abs:.6f})")
        print(f"Индексы: строка {max_i+1}, столбец {max_j+1}")
    else:
        print("Матрица пуста?")
    print("="*60)

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
