"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
11. Вложенные циклы в матричных задачах

395. Даны натуральное число n, действительное число x, действительная матрица размера nx2n. Получить последовательность b1,...,bn из нулей и единиц, где bi = 1, если элементы i-й строки матрицы не превосходят x, и bi = 0 в противном случае.
"""


import random

def get_params_and_matrix():
    """Выбор способа ввода n, x и матрицы размера n × 2n."""
    print("=== Задача 395: Бинарный вектор по условию ≤ x ===")
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
                n = int(input("Введите натуральное число n (>0): "))
                if n <= 0:
                    print("n должно быть положительным.")
                    continue
                x = float(input("Введите действительное число x: "))
                m = 2 * n
                print(f"Введите матрицу {n}×{m} построчно (действительные числа через пробел):")
                matrix = []
                for i in range(n):
                    row = list(map(float, input(f"Строка {i+1}: ").split()))
                    if len(row) != m:
                        print(f"Ошибка: в строке должно быть {m} чисел.")
                        break
                    matrix.append(row)
                else:
                    return n, x, matrix
                print("Попробуйте ввести матрицу заново.")
            except ValueError:
                print("Ошибка ввода. Ожидаются числа.")

    elif choice == '2':
        n = random.randint(2, 4)
        x = round(random.uniform(-2, 2), 2)
        m = 2 * n
        matrix = [[round(random.uniform(-3, 3), 2) for _ in range(m)] for _ in range(n)]
        print(f"\nСгенерированы параметры: n = {n}, x = {x}")
        print(f"Матрица {n}×{m}:")
        for row in matrix:
            print(" ".join(f"{val:7.2f}" for val in row))
        return n, x, matrix

    else:
        examples = [
            (2, 1.5, [[1.2, 0.8, 1.1, 1.3], [1.6, 1.4, 2.0, 0.9]]),
            (3, 0.0, [[-1.0, -2.5, 0.0, -0.5, 1.0, -3.0],
                      [0.1, -0.2, 0.0, 0.3, -0.1, 0.0],
                      [-2.0, -1.0, -3.0, -4.0, -5.0, -2.5]]),
            (2, 2.0, [[1.0, 2.0, 1.5, 1.9], [2.1, 2.0, 1.8, 2.0]]),
            (3, -0.5, [[-1.0, -2.0, -0.5, -0.6, -0.7, -0.8],
                       [0.0, 1.0, -1.0, 2.0, -2.0, 3.0],
                       [-0.5, -0.5, -0.5, -0.5, -0.5, -0.5]]),
            (1, 10.0, [[5.0, 10.0, 7.5]])
        ]
        print("\nГотовые примеры:")
        for idx, (n_val, x_val, mat) in enumerate(examples, 1):
            print(f"{idx}: n = {n_val}, x = {x_val}")
            for row in mat:
                print("   ", " ".join(f"{v:6.2f}" for v in row))
            print()
        while True:
            try:
                num = int(input("Выберите номер примера: "))
                if 1 <= num <= len(examples):
                    n, x, matrix = examples[num-1]
                    return n, x, matrix
                else:
                    print(f"Номер должен быть от 1 до {len(examples)}.")
            except ValueError:
                print("Ошибка ввода. Введите целое число.")

def compute_b(n, x, matrix):
    """Формирует вектор b: 1 если все элементы строки ≤ x, иначе 0."""
    b = []
    for i in range(n):
        if all(val <= x for val in matrix[i]):
            b.append(1)
        else:
            b.append(0)
    return b

def main():
    data = get_params_and_matrix()
    if data is None:
        return
    n, x, matrix = data
    b = compute_b(n, x, matrix)

    print("\n" + "="*60)
    print("РЕЗУЛЬТАТЫ")
    print("="*60)
    print(f"n = {n}, x = {x}")
    print("Матрица:")
    for i, row in enumerate(matrix):
        print(f"Строка {i+1:2d}:", " ".join(f"{val:7.2f}" for val in row))

    print("\nВектор b:")
    for i, val in enumerate(b):
        print(f"  b_{i+1} = {val}")
    print("="*60)

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
