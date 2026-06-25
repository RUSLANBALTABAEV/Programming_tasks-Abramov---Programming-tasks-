"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
12. Использование процедур 

В задачах этого параграфа будем для краткости говорить просто о процедурах, подразумевая, что решающий задачи сам выберет подходящее средство программирования – подпрограмму, функцию и 
т. д. Этот выбор должен быть сделан с учётом как характера задач, так и особенностей используемого языка программирования.

446. Дано натуральное число n. Выяснить, имеются ли среди чисел n, n + 1, …, 2n близнецы, т.е. простые числа, разность между которыми равна двум. (Определить процедуру, позволяющую распознавать простые числа.)
"""


import math
import random


def is_prime(x):
    """Процедура проверки простоты числа x."""
    if x <= 1:
        return False
    if x <= 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    i = 5
    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        i += 6
    return True


def get_n():
    """Выбор способа ввода натурального числа n."""
    print("Задача 446: Поиск чисел-близнецов в интервале [n, 2n]")
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
                n = int(input("Введите натуральное число n: "))
                if n <= 0:
                    print("n должно быть > 0.")
                    continue
                return n
            except ValueError:
                print("Ошибка ввода.")

    elif choice == '2':
        n = random.randint(1, 50)
        print(f"Сгенерировано n = {n}")
        return n

    else:  # готовые примеры
        examples = [1, 3, 10, 20, 100]
        print("Готовые примеры n:", examples)
        while True:
            try:
                num = int(input("Выберите номер примера (1-5): "))
                if 1 <= num <= len(examples):
                    return examples[num - 1]
                else:
                    print("Номер от 1 до 5.")
            except ValueError:
                print("Введите целое число.")


def main():
    n = get_n()
    pairs = []

    for x in range(n, 2 * n):  # x до 2n-1, x+2 <= 2n
        if is_prime(x) and is_prime(x + 2) and x + 2 <= 2 * n:
            pairs.append((x, x + 2))

    print(f"\nДиапазон: {n} .. {2 * n}")
    if pairs:
        print("Найдены числа-близнецы:")
        for p1, p2 in pairs:
            print(f"  {p1} и {p2}")
    else:
        print("Чисел-близнецов в этом диапазоне нет.")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
