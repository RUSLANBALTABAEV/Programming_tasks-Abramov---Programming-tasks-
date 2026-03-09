"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
11. Вложенные циклы в матричных задачах

374. Дано натуральное число n. Выяснить, сколько положительных элементов содержит матрица [aij]i,j=1,...,n, если
а) aij=sin(i + j / 2);
б) aij=cos(i * i + n);
в) aij=sin((i * i - j * j) / n).
"""


import math
import random

def get_n():
    """Выбор способа ввода n."""
    print("=== Задача 374: Подсчёт положительных элементов матрицы ===")
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
                print("Ошибка: n должно быть положительным.")
                return None
            return n
        except ValueError:
            print("Ошибка ввода.")
            return None

    elif choice == '2':
        n = random.randint(1, 15)
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

def count_positive_a(n):
    """Подсчёт положительных элементов для пункта a: sin(i + j/2)."""
    cnt = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            val = math.sin(i + j/2.0)
            if val > 0:
                cnt += 1
    return cnt

def count_positive_b(n):
    """Подсчёт положительных элементов для пункта б: cos(i^2 + n)."""
    cnt = 0
    for i in range(1, n+1):
        arg = i*i + n
        val = math.cos(arg)
        for j in range(1, n+1):  # j не используется в формуле, но матрица квадратная
            if val > 0:
                cnt += 1
    return cnt

def count_positive_c(n):
    """Подсчёт положительных элементов для пункта в: sin((i^2 - j^2)/n)."""
    cnt = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            val = math.sin((i*i - j*j) / n)
            if val > 0:
                cnt += 1
    return cnt

def main():
    n = get_n()
    if n is None:
        return
    print(f"\nn = {n}")
    cnt_a = count_positive_a(n)
    cnt_b = count_positive_b(n)
    cnt_c = count_positive_c(n)
    total = n * n
    print("\n" + "="*50)
    print("РЕЗУЛЬТАТ")
    print("="*50)
    print(f"Всего элементов в матрице: {total}")
    print(f"а) Положительных элементов sin(i + j/2): {cnt_a}")
    print(f"б) Положительных элементов cos(i^2 + n): {cnt_b}")
    print(f"в) Положительных элементов sin((i^2 - j^2)/n): {cnt_c}")
    print("="*50)

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
