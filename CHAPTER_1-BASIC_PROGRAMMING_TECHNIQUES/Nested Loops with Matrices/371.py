"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
11. Вложенные циклы в матричных задачах

371. Дана действительная квадратная матрица |aij|i,j=1,...,n.
Получить две квадратные матрицы |bij|i,j=1,...,n,|cij|i,j=1,...,n, для которых 
bij = aij при j >= i, и cij = aij при j < i,
bij = aij при j < i, и cij = -aij при j >= i.
"""


import random

def get_matrix():
    """Выбор способа ввода размера n и матрицы a."""
    print("=== Задача 371: Преобразование матрицы a в b и c ===")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод")
    print("2 — Случайная генерация")
    print("3 — Готовые примеры")

    choice = input("Ваш выбор (1/2/3): ").strip()
    while choice not in ('1', '2', '3'):
        choice = input("Выберите 1, 2 или 3: ").strip()

    if choice == '1':
        try:
            n = int(input("Введите размер матрицы n (натуральное): "))
            if n <= 0:
                print("n должно быть положительным.")
                return None
            print("Введите элементы матрицы a по строкам (действительные числа):")
            a = []
            for i in range(n):
                row = list(map(float, input(f"Строка {i+1}: ").split()))
                if len(row) != n:
                    print(f"Ожидалось {n} чисел в строке.")
                    return None
                a.append(row)
            return n, a
        except ValueError:
            print("Ошибка ввода.")
            return None

    elif choice == '2':
        n = random.randint(2, 6)
        a = [[random.uniform(-10, 10) for _ in range(n)] for _ in range(n)]
        print(f"\nСгенерирована матрица {n}x{n}:")
        for row in a:
            print(" ".join(f"{x:8.4f}" for x in row))
        return n, a

    else:
        examples = [
            (3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            (2, [[1.5, -2.3], [0.1, 4.7]]),
            (4, [[i*j for j in range(1,5)] for i in range(1,5)]),
            (3, [[0, -1, 2], [3, -4, 5], [-6, 7, -8]])
        ]
        print("\nГотовые примеры:")
        for idx, (n_val, a_val) in enumerate(examples, 1):
            print(f"{idx}: n={n_val}, a = {a_val[0]} ...")
        try:
            num = int(input("Выберите номер примера: "))
            if 1 <= num <= len(examples):
                n, a = examples[num-1]
                return n, a
            else:
                print("Неверный номер!")
                return None
        except ValueError:
            print("Ошибка ввода.")
            return None

def compute_b(a, n):
    b = [[0.0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if j >= i:  # j ≥ i (индексы с 0 соответствуют i+1, j+1)
                b[i][j] = a[i][j]
            else:
                b[i][j] = a[j][i]
    return b

def compute_c(a, n):
    c = [[0.0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if j < i:  # j < i
                c[i][j] = a[i][j]
            else:      # j ≥ i
                c[i][j] = -a[i][j]
    return c

def print_matrix(mat, name):
    print(f"\nМатрица {name}:")
    for row in mat:
        print(" ".join(f"{x:8.4f}" for x in row))

def main():
    data = get_matrix()
    if data is None:
        return
    n, a = data
    print("\nИсходная матрица a:")
    for row in a:
        print(" ".join(f"{x:8.4f}" for x in row))

    b = compute_b(a, n)
    c = compute_c(a, n)

    print_matrix(b, "b (j≥i: a_ij, иначе a_ji)")
    print_matrix(c, "c (j<i: a_ij, иначе -a_ij)")

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
