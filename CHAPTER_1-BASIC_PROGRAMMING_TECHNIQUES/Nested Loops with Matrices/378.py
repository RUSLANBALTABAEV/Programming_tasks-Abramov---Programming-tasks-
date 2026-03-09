"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
11. Вложенные циклы в матричных задачах

378. Даны действительные числа x1,...,x8. Получить действительную квадратную матрицу порядка 8:
а) [x1  x2 ... x8              ]
   [x1 * x1 x2 * x2 ... x8 * x8];
   [...  ...    ...         ...]
   [x1 ^ 8 x2 ^ 8   ... x8 ^ 8 ]


б) [1    1      ... 1        ]
   [x1  x2      ... x8       ].
   [... ...    ... ...       ]
   [x1 ^ 7 x2 ^ 7 ... x8 ^ 7 ]
   [x1 ^ 7  x2 ^ 7 ... x8 ^ 7]
"""


import random

def get_x():
    """Выбор способа ввода 8 действительных чисел x1..x8."""
    print("=== Задача 378: Построение матриц из степеней ===")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод")
    print("2 — Случайная генерация")
    print("3 — Готовые примеры")

    choice = input("Ваш выбор (1/2/3): ").strip()
    while choice not in ('1', '2', '3'):
        choice = input("Выберите 1, 2 или 3: ").strip()

    if choice == '1':
        try:
            print("Введите 8 действительных чисел x1...x8 через пробел:")
            line = input().strip()
            tokens = line.split()
            if len(tokens) != 8:
                print("Ожидалось 8 чисел.")
                return None
            x = [float(t) for t in tokens]
            return x
        except ValueError:
            print("Ошибка ввода. Введите действительные числа.")
            return None

    elif choice == '2':
        x = [random.uniform(-5, 5) for _ in range(8)]
        print("\nСгенерированы числа:")
        print("x =", [round(v, 4) for v in x])
        return x

    else:
        examples = [
            [1, 2, 3, 4, 5, 6, 7, 8],
            [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5],
            [-1, 0, 1, 2, 3, 4, 5, 6],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [2, 4, 6, 8, 10, 12, 14, 16]
        ]
        print("\nГотовые примеры:")
        for i, ex in enumerate(examples, 1):
            print(f"{i}. {ex}")
        try:
            num = int(input("Выберите номер примера: "))
            if 1 <= num <= len(examples):
                return examples[num-1]
            else:
                print("Неверный номер!")
                return None
        except ValueError:
            print("Ошибка ввода.")
            return None

def matrix_a(x):
    """Строит матрицу a[i][j] = x[j]^(i+1) (i,j от 0 до 7)."""
    n = 8
    a = [[0.0]*n for _ in range(n)]
    for i in range(n):
        power = i + 1
        for j in range(n):
            a[i][j] = x[j] ** power
    return a

def matrix_b(x):
    """Строит матрицу b: первая строка единицы, затем степени 1..7."""
    n = 8
    b = [[0.0]*n for _ in range(n)]
    for j in range(n):
        b[0][j] = 1.0
    for i in range(1, n):
        power = i  # i от 1 до 7
        for j in range(n):
            b[i][j] = x[j] ** power
    return b

def print_matrix(mat, name):
    print(f"\nМатрица {name}:")
    for row in mat:
        print(" ".join(f"{val:12.6f}" for val in row))

def main():
    x = get_x()
    if x is None:
        return
    print("\nИсходные числа x1..x8:")
    for i, val in enumerate(x, 1):
        print(f"x{i} = {val}")

    A = matrix_a(x)
    B = matrix_b(x)

    print_matrix(A, "A (степени 1..8)")
    print_matrix(B, "B (первые единицы, затем степени 1..7)")

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
