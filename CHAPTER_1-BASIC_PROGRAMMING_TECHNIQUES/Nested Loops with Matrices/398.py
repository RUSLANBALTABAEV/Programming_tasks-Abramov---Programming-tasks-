"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
11. Вложенные циклы в матричных задачах

398. Дана действительная квадратная матрица порядка n. Рассмотрим те элементы, которые расположены в строках, начинающихся с отрицательного элемента. Найти суммы тех из них, которые расположены соответственно ниже, выше и на главной диагонали.
"""


import random

def get_matrix():
    """
    Выбор способа ввода действительной квадратной матрицы порядка n.
    Возвращает (n, matrix).
    """
    print("Задача 398: Суммы элементов строк с отрицательным первым элементом")
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
                n = int(input("Введите порядок матрицы n (> 0): "))
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
                print("Попробуйте ввести матрицу заново.")
            except ValueError:
                print("Ошибка ввода. Ожидает числа.")

    elif choice == '2':
        n =  random.randint(3, 6)
        matrix = [[round(random.uniform(-5, 5), 2) for _ in range(n)] for _ in range(n)]
        print(f"\nСгенерирована матрица порядка {n}:")
        for row in matrix:
            print(" ".join(f"{x:8.2f}" for x in row))
        return n, matrix
    
    else:
        # Готовые примеры
        examples = [
            (4, [
                [-2.0, 1.0, 2.0, 3.0],
                [ 0.5, -1.0, 4.0, 5.0],
                [-3.0, 6.0, -7.0, 8.0],
                [ 1.0, 2.0, 3.0, -4.0]
            ]),
            (3, [
                [-1.5, 2.2, 3.1],
                [ 0.0, -5.5, 1.0],
                [ 4.0, -2.0, -3.3]
            ]),
            (3, [
                [ 1.0, 2.0, 3.0],
                [ 4.0, 5.0, 6.0],
                [ 7.0, 8.0, 9.0]
            ]),
            (5, [
                [-1.1, 0.0, 0.0, 0.0, 0.0],
                [ 2.0, -2.2, 0.0, 0.0, 0.0],
                [ 3.0, 3.0, -3.3, 0.0, 0.0],
                [ 4.0, 4.0, 4.0, -4.4, 0.0],
                [ 5.0, 5.0, 5.0, 5.0, -5.5]
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
                    print(f"Номер должен быть от 1 до {len(examples)}")
            except ValueError:
                print("Ошибка ввода. Введите целое число.")

def main():
    n, matrix = get_matrix()

    sum_below = 0.0   # j < 1 (ниже главное диагонали)
    sum_on_diag = 0.0 # j == 1 (на диагонали)
    sum_above = 0.0   # J > i (выше диагонали)

    rows_processed = []  # для вывода информации

    for i in range(n):
        if matrix[i][0] < 0: # строка начинается с отрицательного элемента
            rows_processed.append(i)
            for j in range(n):
                element = matrix[i][j]
                if j < i:
                    sum_below += element
                elif j == i:
                    sum_on_diag += element
                else:
                    sum_above += element

    # Вывод результатов
    print("\n" + "=" * 60)
    print("РЕЗУЛЬТАТЫ")
    print("=" * 60)
    print(f"Матрица порядка {n}:")
    for i, row in enumerate(matrix):
        print(f"Строка {i+1:2d}:", " ".join(f"{x:8.2f}" for x in row))

    if not rows_processed:
        print("\nСтрок, начинающихся с отрицательного элемента, нет.")
        print("Все три суммы равны 0.")
    else:
        print(f"\nСтроки, начинающиеся с отрицательного элемента: {[i+1 for i in rows_processed]}")
        print("\nСуммы элементов этих строк:")
        print(f"  Ниже главной диагонали (j < i): {sum_below:.2f}")
        print(f"  На главной диагонали (j = i): {sum_on_diag:.2f}")
        print(f"  Выше главной диагонали (j > i): {sum_above:.2f}")
    print("=" * 60)

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
