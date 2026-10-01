"""
ГЛАВА 2
ЗАДАЧИ ПО ТЕМАМ
15. Целые числа.

567. Дано натуральное число n. Выяснить, можно ли представить n! в виде произведения трех последовательных целых чисел.
"""


import math
import random


def get_n():
    """Выбор способа ввода натурального числа n."""
    print("Задача 567: Представление n! в виде произведения трёх")
    print("последовательных целых чисел")
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
                n = int(input("Введите натуральное число n (>=1): "))
                if n < 1:
                    print("n должно быть >= 1.")
                    continue
                return n
            except ValueError:
                print("Ошибка ввода. Повторите.")

    elif choice == '2':
        n = random.randint(1, 30)
        print(f"\nСгенерировано n = {n}")
        return n

    else:  # готовые примеры
        examples = [1, 2, 3, 4, 5, 6, 7, 10, 20]
        print("\nГотовые примеры n:")
        for idx, val in enumerate(examples, 1):
            print(f"{idx}: n = {val}")
        while True:
            try:
                num = int(input("Выберите номер примера: "))
                if 1 <= num <= len(examples):
                    return examples[num - 1]
                else:
                    print(f"Номер должен быть от 1 до {len(examples)}.")
            except ValueError:
                print("Ошибка ввода. Введите целое число.")


def integer_cuberoot(n):
    """
    Возвращает floor(n^(1/3)) для целого n >= 0.
    Работает через бинарный поиск, что безопасно для больших чисел.
    """
    if n < 0:
        raise ValueError("n должно быть неотрицательным")
    if n == 0:
        return 0

    low, high = 0, 1
    while high ** 3 <= n:
        high *= 2
    while low < high:
        mid = (low + high) // 2
        if mid ** 3 <= n:
            low = mid + 1
        else:
            high = mid
    return low - 1


def can_be_product_of_three_consecutive(fact):
    """
    Проверяет, можно ли fact представить как m*(m-1)*(m+1).
    Возвращает m, если можно, иначе None.
    """
    if fact < 6:   # минимальное произведение 1*2*3 = 6
        return None
    r = integer_cuberoot(fact)
    # m очень близко к кубическому корню; берём небольшой запас
    for m in range(max(2, r - 2), r + 4):
        if m * (m - 1) * (m + 1) == fact:
            return m
    return None


def main():
    n = get_n()
    fact = math.factorial(n)

    print(f"\n{n}! = {fact}")

    m = can_be_product_of_three_consecutive(fact)
    print("-" * 50)
    if m is not None:
        print(f"Да, {n}! можно представить в виде произведения")
        print("трёх последовательных целых чисел:")
        print(f"  {n}! = {m-1} * {m} * {m+1}")
    else:
        print(f"Нет, {n}! нельзя представить в виде произведения")
        print("трёх последовательных целых чисел.")
    print("-" * 50)


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")