"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
11. Вложенные циклы в матричных задачах

407. Даны натуральные числа n и m, действительное число r, действительная матрица размера n x m. Получить значение b1 * r ^ n - 1 + b2 * r ^ n - 2 + ... + bn, где bk - первый по порядку положительный элемент в k-й строке матрицы (k = 1, ..., n); если в k-строке нет положительных элементов, то bk = 0.5.
"""


import random

def get_params_and_matrix():
    """Выбор способа ввода n, m, r и матрицы n×m."""
    print("Задача 407: Сумма b_k * r^(n-k)")
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
                n = int(input("Введите количество строк n (> 0): "))
                m = int(input("Введите количество столбцов m (> 0): "))
                if n <= 0 or m <= 0:
                    print("Размеры должны быть положительными.")
                    continue
                r = float(input("Введите число r: "))
                print(f"Введите матрицу {n}x{m} построчно (действительные числа через пробел):")
                matrix = []
                for i in range(n):
                    row = list(map(float, input(f"Строка {i + 1}: ").split()))
                    if len(row) != m:
                        print(f"Ошибка: в строке должен быть {m} чисел.")
                        break
                    matrix.append(row)
                else:
                    return n, m, r, matrix
                print("Попробуйте ввести матрицу заново.")
            except ValueError:
                print("Ошибка ввода. Ожидаются числа.")
            
    elif choice == '2':
        n = random.randint(2, 5)
        m = random.randint(3, 6)
        r = round(random.uniform(0.5, 3.0), 2)
        matrix = [[round(random.uniform(-5, 5), 2) for _ in range(m)] for _ in range(n)]
        for row in matrix:
            print(" ".join(f"{x:7.2f}" for x in row))
        return n, m, r, matrix
    
    else:
        # Готовые примеры (n, m, r, matrix)
        examples = [
            (3, 4, 2.0, [
                [0.0, 1.5, -2.0, 3.0],
                [-1.0, -2.0, 4.0, 0.0],
                [0.0, 0.0, 0.0, -1.0]
            ]),
            (2, 3, 1.5, [
                [2.0, -1.0, 0.5],
                [-3.0, -4.0, -5.0]
            ]),
            (4, 2, 0.5, [
                [1.0, 2.0],
                [-1.0, 3.0],
                [0.0, 0.0],
                [2.5, -0.1]
            ])
        ]
        print("\nГотовые примеры:")
        for idx, (n_val, m_val, r_val, mat) in enumerate(examples, 1):
            print(f"{idx}: n = {n_val}, m = {m_val}, r = {r_val}")
            for row in mat:
                print("  ", " ".join(f"{x:6.2f}" for x in row))

        while True:
            try:
                num = int(input("Выберите номер примера: "))
                if 1 <= num <= len(examples):
                    return examples[num - 1]
                else:
                    print(f"Номер должен быть от 1 до {len(examples)}.")
            except ValueError:
                print("Ошибка ввода. Введите целое число.")


def compute_sum(n, r, matrix):
    """Вычисляет сумму b_1*r^(n-1) + ... + b_n."""
    b = []
    for i in range(n):
        # первый положительный элемент в строке
        found = False
        for val in matrix[i]:
            if val > 0:
                b.append(val)
                found = True
                break
        if not found:
            b.append(0.5)

    total = 0.0
    for k in range(n):
        exponent = n - 1 - k
        term = b[k] * (r ** exponent)
        total += term
        # Для вывода
        print(f"  b_{k + 1} = {b[k]:.2f}, r^{exponent} = {r**exponent:.4f}, слагаемое = {term:.4f}")

        return total, b
    

def main():
    data = get_params_and_matrix()
    if data is None:
        return
    n, m, r, matrix = data

    print("\n" + "=" * 60)
    print("РЕЗУЛЬТАТЫ")
    print("=" * 60)
    print(f"n = {n}, m = {m}, r = {r}")
    print("Матрица:")
    for i, row in enumerate(matrix):
        print(f"Строка {i+1:2d}:", " ".join(f"{x:7.2f}" for x in row))

    print("\nПостроение b_k и вычисление суммы:")
    total, b = compute_sum(n, r, matrix)

    print(f"\nИтоговая сумма = {total:.4f}")
    print("=" * 60)

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
