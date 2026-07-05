"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
12. Использование процедур 

В задачах этого параграфа будем для краткости говорить просто о процедурах, подразумевая, что решающий задачи сам выберет подходящее средство программирования – подпрограмму, функцию и 
т. д. Этот выбор должен быть сделан с учётом как характера задач, так и особенностей используемого языка программирования.

457. Даны натуральные числа a, c, m. Получить f(m), где 
f(n) = n, если 0 <= n <= 9, 
f(n) = g(n) * f(n - 1 - g(n)) + n в противном случае.
g(n) = остаток от деления an+c на 10.

Использовать программу, включающую рекурсивную процедуру вычисления f(n).
"""


import sys
import random

sys.setrecursionlimit(10000)   # увеличенный лимит рекурсии


def g(n, a, c):
    """g(n) = (a * n + c) % 10."""
    return (a * n + c) % 10


def f(n, a, c):
    """Рекурсивная процедура вычисления f(n)."""
    if 0 <= n <= 9:
        return n
    gn = g(n, a, c)
    return gn * f(n - 1 - gn, a, c) + n


def get_params():
    """Выбор способа ввода натуральных чисел a, c, m."""
    print("Задача 457: Рекурсивное вычисление f(m)")
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
                a = int(input("Введите натуральное число a: "))
                c = int(input("Введите натуральное число c: "))
                m = int(input("Введите натуральное число m: "))
                if a < 0 or c < 0 or m < 0:
                    print("Все числа должны быть неотрицательными.")
                    continue
                return a, c, m
            except ValueError:
                print("Ошибка ввода.")

    elif choice == '2':
        a = random.randint(1, 10)
        c = random.randint(0, 10)
        m = random.randint(10, 50)   # не слишком большие, чтобы рекурсия не затянулась
        print(f"Сгенерированы: a = {a}, c = {c}, m = {m}")
        return a, c, m

    else:  # готовые примеры
        examples = [
            (3, 1, 15),
            (2, 0, 20),
            (7, 4, 12),
            (5, 9, 30)
        ]
        print("Готовые примеры (a, c, m):")
        for idx, (av, cv, mv) in enumerate(examples, 1):
            print(f"{idx}: a = {av}, c = {cv}, m = {mv}")
        while True:
            try:
                num = int(input("Выберите номер примера: "))
                if 1 <= num <= len(examples):
                    return examples[num - 1]
                else:
                    print(f"Номер от 1 до {len(examples)}.")
            except ValueError:
                print("Введите целое число.")


def main():
    a, c, m = get_params()
    try:
        result = f(m, a, c)
        print(f"\nf({m}) = {result}")
    except RecursionError:
        print("Ошибка: достигнута максимальная глубина рекурсии. Попробуйте меньшие значения m.")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
