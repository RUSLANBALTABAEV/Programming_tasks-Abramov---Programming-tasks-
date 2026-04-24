"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
11. Вложенные циклы в матричных задачах

396. Дана действительная квадратная матрица порядка n. Построить последовательность действительных чисел a1,...,an по правилу: если в i-й строке матрицы элемент, принадлежащий главной диагонали, отрицателен, то ai равно сумме элементов i-й строки, предшествующих первому отрицательному элементу; в противном случае ai равно сумме последних элементов i-й строки, начиная с первого по порядку неотрицательного элемента.
"""


import random

def get_matrix():
    """Выбор способа ввода квадратной матрицы порядка n."""
    print("Задача 396: Построение последовательности по диагональному элементу")
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
                n = int(input("Введите порядок матрицы n (>0): "))
                if n <= 0:
                    print("Порядок должен быть положительным.")
                    continue
                print(f"Введите матрицу {n}x{n} построчно (действительные числа через пробел):")
                matrix = []
                for i in range(n):
                    row = list(map(float, input(f"Строка {i+1}: ").split()))
                    if len(row) != n:
                        print(f"Ошибка: в строке должен быть {n} чисел.")
                        break
                    matrix.append(row)
                else:
                    return n, matrix
                print("Попробуйте ввести матрицу занова.")
            except ValueError:
                print("Ошибка ввода. Ожидает числа.")

    elif choice == '2':
        n = random.randint(3, 5)
        matrix = [[round(random.uniform(-5, 5), 2) for _ in range(n)] for _ in range(n)]
        print(f"\nСгенерированная матрица порядка {n}:")
        for row in matrix:
            print(" ".join(f"{x:8.2f}" for x in row))
        return n, matrix
    
    else:
        examples = [
            (3, [[-1.2, 2.5, -3.0],
                 [ 0.5, -0.8, 1.0],
                 [ 1.0, 2.0, -4.0]]),
            (4, [[ 2.0, -3.0, 1.5, 4.0],
                 [-1.0,  0.0, 2.0, -5.0],
                 [ 3.0,  1.0, 0.5, -2.0],
                 [-2.0, -2.0, -2.0, 6.0]]),
            (3, [[ 1.0,  2.0, 3.0],
                 [-4.0, -5.0, 0.0],
                 [ 0.0, -1.0, 2.0]]),
            (4, [[ 0.0,  0.0,  0.0,  0.0],
                 [-1.0, -1.0, -1.0, -1.0],
                 [ 2.0,  3.0, -4.0,  5.0],
                 [-3.0, -3.0, -3.0, -3.0]]),
            (3, [[ 1.5, -2.0, 0.0],
                 [-2.0,  1.0, 3.0],
                 [ 0.0,  0.0, 0.0]])
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
                    n, matrix = examples[num - 1]
                    return n, matrix
                else:
                    print(f"Номер должен быть от 1 до {len(examples)}.")
            except ValueError:
                print("Ошибка ввода. Введите целое число.")

def compute_sequence(n, matrix):
    """
    Вычисляет последовательность a_1 ... a_n по правилам:
    - если диагональный элемент < 0: сумма элементов строки до первого отрицательного (не включая его)
    - иначе: сумма элементов от первого неотрицательного до конца строки (включительно)
    """
    a = []
    for i in range(n):
        diag = matrix[i][i]
        if diag < 0:
            # Сумма элементов, предшествующих первому отрицательному
            sum_before = 0.0
            for val in matrix[i]:
                if val < 0:
                    break
                sum_before += val
            a.append(sum_before)
        else:
            # Сумма последних элементов начиная с первого неотрицательного
            first_non_neg_idx = -1
            for j, val in enumerate(matrix[i]):
                if val >= 0:
                    first_non_neg_idx = j
                    break
            # По условию, если diag >= 0, то хотя бы один неотрицательный точно существует (сам diag)
            sum_from = sum(matrix[i][first_non_neg_idx:]) if first_non_neg_idx != -1 else 0.0
            a.append(sum_from)
    return a

def main():
    data = get_matrix()
    if data is None:
        return
    n, matrix = data

    seq = compute_sequence(n, matrix)

    print("\n" + "=" * 60)
    print("РЕЗУЛЬТАТЫ")
    print("=" * 60)
    print(f"Матрица порядка {n}:")
    for i, row in enumerate(matrix):
        print(f"Строка {i+1:2d}:", " ".join(f"{x:8.2f}" for x in row))

    print("\nДиагональные элементы и получения последовательность:")
    for i in range(n):
        diag = matrix[i][i]
        print(f"  a_{i+1} = {seq[i]:.4f} (диагональ = {diag:.2f}, {'< 0' if diag < 0 else '>= 0'})")
    print("=" * 60)

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
