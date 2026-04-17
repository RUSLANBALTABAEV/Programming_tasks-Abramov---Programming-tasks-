"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
11. Вложенные циклы в матричных задачах

390. Дана действительная матрица размера n*m. Получить последовательность b1,...,bn, где bk - это 
а) наибольшее из значений элементов k-й строки;
б) сумма наибольшего и наименьшего из значений элементов k-й строки;
в) число отрицательных элементов в k-й строке;
г) произведение квадратов тех элементов k-й строки, модули которых принадлежать отрезку [1,1.5].
"""


import random

def get_matrix():
    """Выбор способа ввода матрицы n×m с повторным запросом при ошибках."""
    print("=== Задача 390: Характеристики строк матрицы ===")
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
                n = int(input("Введите количество строк n (>0): "))
                m = int(input("Введите количество столбцов m (>0): "))
                if n <= 0 or m <= 0:
                    print("Размеры должны быть положительными.")
                    continue
                print("Введите матрицу построчно (действительные числа):")
                matrix = []
                for i in range(n):
                    row = list(map(float, input(f"Строка {i+1}: ").split()))
                    if len(row) != m:
                        print(f"Ошибка: в строке должно быть {m} чисел.")
                        break
                    matrix.append(row)
                else:
                    return n, m, matrix
                print("Попробуйте ввести матрицу заново.")
            except ValueError:
                print("Ошибка ввода. Ожидаются числа.")

    elif choice == '2':
        n = random.randint(2, 6)
        m = random.randint(2, 7)
        matrix = [[random.uniform(-2, 2) for _ in range(m)] for _ in range(n)]
        print(f"\nСгенерирована матрица {n}×{m}:")
        for row in matrix:
            print(" ".join(f"{x:8.4f}" for x in row))
        return n, m, matrix

    else:
        examples = [
            (3, 3, [[1.2, -0.5, 1.6], [0.8, 1.1, -1.3], [1.4, 1.7, 0.9]]),
            (2, 4, [[1.3, 1.6, -2.0, 0.7], [0.5, 1.2, 1.8, -1.1]]),
            (3, 2, [[1.1, 1.4], [0.9, 1.2], [1.5, 1.3]]),
            (2, 3, [[-1, 0, 1], [2, -2, 3]]),
            (3, 3, [[1.5, 2.0, 1.2], [0.8, 1.5, 1.5], [1.1, 1.3, 1.4]])
        ]
        print("\nГотовые примеры:")
        for idx, (n_val, m_val, mat) in enumerate(examples, 1):
            print(f"{idx}: {n_val}×{m_val}")
            for row in mat:
                print("   ", " ".join(f"{x:6.2f}" for x in row))
        while True:
            try:
                num = int(input("Выберите номер примера: "))
                if 1 <= num <= len(examples):
                    n, m, matrix = examples[num-1]
                    return n, m, matrix
                else:
                    print(f"Номер должен быть от 1 до {len(examples)}.")
            except ValueError:
                print("Ошибка ввода. Введите целое число.")

def main():
    data = get_matrix()
    if data is None:
        return
    n, m, matrix = data

    max_vals = []
    sum_min_max = []
    neg_count = []
    prod_squares = []

    for row in matrix:
        max_val = max(row)
        min_val = min(row)
        max_vals.append(max_val)
        sum_min_max.append(max_val + min_val)
        neg_count.append(sum(1 for x in row if x < 0))

        prod = 1.0
        found = False
        for x in row:
            if 1.0 <= abs(x) <= 1.5:
                prod *= x * x
                found = True
        prod_squares.append(prod if found else 0.0)

    print("\n" + "="*60)
    print("РЕЗУЛЬТАТЫ")
    print("="*60)
    for i in range(n):
        print(f"Строка {i+1}:")
        print(f"  а) наибольшее значение: {max_vals[i]:.6f}")
        print(f"  б) сумма наибольшего и наименьшего: {sum_min_max[i]:.6f}")
        print(f"  в) количество отрицательных элементов: {neg_count[i]}")
        print(f"  г) произведение квадратов элементов с |x|∈[1,1.5]: {prod_squares[i]:.6f}")
        print("-" * 40)
    print("="*60)

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
