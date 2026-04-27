"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
11. Вложенные циклы в матричных задачах

400. Дана действительная квадратная матрица порядка n. Получить x1 * xn + x2 * xn-1 + ... + xn * x1, где xk - наибольшее значение элементов k-й строки данной матрицы.
"""


import random

def get_matrix():
    """
    Выбор способа ввода действительной квадратной матрицы порядка n.
    Возвращает (n, matrix).
    """
    print("Задача 400: Сумма произведений максимумов строк")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод")
    print("2 — Случайная числа")
    print("3 — Готовые примеры")

    while True:
        choice = input("Ваш выбор (1/2/3): ").strip()
        if choice in ('1', '2', '3'):
            break
        print("Ошибка: выберите 1, 2 или 3.")

    if choice == '1':
        while True:
            try:
                n = int(input("Введите порядок матрицы n (> 0):"))
                if n <= 0:
                    print("Порядок должен быть положительным.")
                    continue
                print(f"Введите матрицу {n}x{n} построчно (действительные числа через пробел):")
                matrix = []
                for i in range(n):
                    row = list(map(float, input(f"Строка {i+1}: ").split()))
                    if len(row) != n:
                        print(f"Ошибка: строке должен быть {n} чисел.")
                        break
                    matrix.append(row)
                else:
                    return n, matrix
                print("Попробуйте ввести матрицу заново.")
            except ValueError:
                print("Ошибка ввода. Ожидает числа.")

    elif choice == '2':
        n = random.randint(3, 6)
        matrix = [[round(random.uniform(-5, 5), 2) for _ in range(n)] for _ in range(n)]
        print(f"\nСлучайная матрица порядка {n}:")
        for row in matrix:
            print(" ".join(f"{x:8.2f}" for x in row))
        return n, matrix
    
    else:
        # Готовые примеры
        examples = [
            (3, [
                [1.0, 2.0, 3.0],
                [4.0, 5.0, 6.0],
                [7.0, 8.0, 9.0]
            ]),
            (4, [
                [1.5, -2.3, 4.0, 0.0],
                [3.1, 2.0, -1.0, 5.5],
                [0.0, 1.0, 2.0, 3.0],
                [7.0, 0.5, -3.0, 2.2]
            ]),
            (3, [
                [-1.0, -2.0, -3.0],
                [0.0, 0.0, 0.0],
                [5.0, 5.0, 5.0]
            ]),
            (2, [
                [2.5, 3.5],
                [0.0, -1.0]
            ]),
            (5, [
                [1.0, 2.0, 3.0, 4.0, 5.0],
                [2.0, 3.0, 4.0, 5.0, 1.0],
                [3.0, 4.0, 5.0, 1.0, 2.0],
                [4.0, 5.0, 1.0, 2.0, 3.0],
                [5.0, 1.0, 2.0, 3.0, 4.0]
            ])
        ]
        print("\nГотовые примеры:")
        for idx, (n_val, mat) in enumerate(examples, 1):
            print(f"{idx}: порядок {n_val}")
            for row in mat:
                print("  ", " ".join(f"{x:6.2f}" for x in row))
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
    n, matrix = get_matrix()

    # Находим максимумы строк
    max_vals = [max(row) for row in matrix]

    # Вычисляем сумму x_k * x_{n+1-k}
    total = sum(max_vals[k] * max_vals[n - 1 - k] for k in range(n))

    # Вывод результатов
    print("\n" + "=" * 60)
    print("РЕЗУЛЬТАТЫ")
    print("=" * 60)
    print(f"Матрица порядка {n}:")
    for i, row in enumerate(matrix):
        print(f"Строка {i+1:2d}:", " ".join(f"{x:8.2f}" for x in row))

    print("\nМаксимальные элементы строк (x_k):")
    for k, val in enumerate(max_vals, 1):
        print(f"  x_{k} = {val:.2f}")

    print("\nВычисление суммы:")
    terms = []
    for k in range(n):
        term = max_vals[k] * max_vals[n - 1 - k]
        terms.append(f"x_{k+1} * x_{n-k} = {max_vals[k]:.2f} * {max_vals[n-1-k]:.2f} = {term:.4f}")
        # Чтобы не загромождать вывод при большом n, покажем первые и последние слагаемые
        if n <= 6:
            for t in terms:
                print(f"  {t}")
        else:
            for t in terms[:3]:
                print(f"  {t}")
            print(" ...")
            for t in terms[-3:]:
                print(f"  {t}")
            
        print(f"\nИтоговая сумма: {total:.4f}")
        print("=" * 60)

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
