"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
11. Вложенные циклы в матричных задачах

405. Даны натуральное число n, действительная квадратная матрица порядка n. Построить последовательность b1, ..., bn из нулей и единиц, в которой bi = 1 тогда и только тогда, когда в i-строке матрицы есть хотя бы один отрицательный элемент.
"""


import random

def get_matrix():
    """Выбор способа ввода действительной квадратной матрицы порядка n."""
    print("Задача 405: Есть ли отрицательный элемент в строке?")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод")
    print("2 — Случайные числа")
    print("3 — Готовые примеры")

    while True:
        choice = input("Ваш выбор (1/2/3): ").strip()
        if choice in ('1', '2', '3'):
            break
        print("Ошибка: выберите 1, 2 или 3.")

    if choice == '1':
        while True:
            try:
                n = int(input("Введите порядок матрицы n (> 0): "))
                if n <= 0:
                    print("Порядок должен быть положительным.")
                    continue
                print(f"Введите матрицу {n}x{n} построчно (действительные числа через пробел):")
                matrix = []
                for i in range(n):
                    row = list(map(float, input(f"Строка {i + 1}: ").split()))
                    if len(row) != n:
                        print(f"Ошибка: в строке должен быть {n} чисел.")
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
        print(f"\nСгенерировано матрица порядка {n}:")
        for row in matrix:
            print(" ".join(f"{x:8.2f}" for x in row))
        return n, matrix
    
    else:
        # Готовые примеры
        examples = [
            (3, [[ 1.0,  2.0,  3.0],
                 [-4.0,  5.0,  6.0],
                 [ 0.0, -1.0,  2.0]]),
            (4, [[ 1.5, -2.2,  0.0,  3.1],
                 [ 4.0,  5.0,  6.0,  7.0],
                 [-1.0, -2.0, -3.0, -4.0],
                 [ 0.0,  0.0,  0.0,  0.0]]),
            (2, [[ 1.0, 2.0],
                 [-3.0, 4.0]]),
            (3, [[ 1.0, 2.0, 3.0],
                 [ 4.0, 5.0, 6.0],
                 [ 7.0, 8.0, 9.0]])  # нет отрицательных
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

    # Построение вектора b
    b = []
    for i in range(n):
        # проверяем, есть ли в строке хотя бы один отрицательный элемент
        if any(x < 0 for x in matrix[i]):
            b.append(1)
        else:
            b.append(0)

    # Вывод результатов
    print("\n" + "=" * 60)
    print("РЕЗУЛЬТАТЫ")
    print("=" * 60)
    print(f"Матрица порядка {n}:")
    for i, row in enumerate(matrix):
        print(f"Строка {i+1:2d}:", " ".join(f"{x:8.2f}" for x in row))

    print("\nВектор b (1 - есть отрицательный элемент, 0 - нет):")
    for i, val in enumerate(b):
        print(f"  b_{i + 1} = {val}")
    print("=" * 60)

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
