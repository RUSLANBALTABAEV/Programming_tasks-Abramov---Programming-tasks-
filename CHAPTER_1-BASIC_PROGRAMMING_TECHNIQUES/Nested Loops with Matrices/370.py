"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
11. Вложенные циклы в матричных задачах

370. Дано натуральное число n. Получить действительную матрицу |aij)i,j=1,...,n, для которой
а) aij = 1 / (i + j);
б) aij = sin(i + j) при i < j
   aij = 1 при i = j
   ai = asin((i + j) / (2 * i + 3 * j)) в остальных случаях.
"""


import math
import random

def get_n():
    """Выбор способа ввода n."""
    print("Выберите способ ввода n:")
    print("1 — Ручной ввод")
    print("2 — Случайная генерация")
    print("3 — Готовые примеры")

    choice = input("Ваш выбор (1/2/3): ").strip()
    while choice not in ('1', '2', '3'):
        choice = input("Выберите 1, 2 или 3: ").strip()

    if choice == '1':
        try:
            n = int(input("Введите натуральное число n: "))
            if n <= 0:
                print("n должно быть положительным.")
                return None
            return n
        except ValueError:
            print("Ошибка ввода.")
            return None

    elif choice == '2':
        n = random.randint(1, 10)
        print(f"Сгенерировано n = {n}")
        return n

    else:
        examples = [3, 5, 7, 10, 12]
        print("Готовые примеры:")
        for i, val in enumerate(examples, 1):
            print(f"{i}. n = {val}")
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

def matrix_a(n):
    """Возвращает матрицу a[i][j] = 1/(i+j) (индексы с 1)."""
    a = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            a[i][j] = 1.0 / ( (i+1) + (j+1) )
    return a

def matrix_b(n):
    """Возвращает матрицу b по заданным условиям."""
    b = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i < j:
                b[i][j] = math.sin(i+1 + j+1)
            elif i == j:
                b[i][j] = 1.0
            else:  # i > j
                arg = (i+1 + j+1) / (2*(i+1) + 3*(j+1))
                b[i][j] = math.asin(arg)
    return b

def print_matrix(mat, name):
    print(f"\nМатрица {name}:")
    for row in mat:
        print(" ".join(f"{val:8.4f}" for val in row))

def main():
    n = get_n()
    if n is None:
        return
    print(f"\nn = {n}")
    mat_a = matrix_a(n)
    mat_b = matrix_b(n)
    print_matrix(mat_a, "a (1/(i+j))")
    print_matrix(mat_b, "b (по условию)")

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
