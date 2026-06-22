"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
12. Использование процедур 

В задачах этого параграфа будем для краткости говорить просто о процедурах, подразумевая, что решающий задачи сам выберет подходящее средство программирования – подпрограмму, функцию и 
т. д. Этот выбор должен быть сделан с учётом как характера задач, так и особенностей используемого языка программирования.

441. Дано натуральное число n. Среди чисел 1,2, ..., n найти все те, которые можно представить в виде суммы квадратов двух натуральных чисел. (Определить процедуру, позволяющую распознавать полные квадраты.)
"""


import math
import random


def is_perfect_square(x):
    """Проверяет, является ли число x полным квадратом натурального числа."""
    if x < 0:
        return False
    root = math.isqrt(x)
    return root * root == x


def get_n():
    """Выбор способа ввода натурального числа n."""
    print("Задача 441: Числа, представимые суммой квадратов двух натуральных чисел")
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
        n = random.randint(10, 100)
        print(f"Сгенерировано n = {n}")
        return n

    else:  # готовые примеры
        examples = [10, 25, 50, 100]
        print("Готовые примеры n:", examples)
        while True:
            try:
                num = int(input("Выберите номер примера (1-4): "))
                if 1 <= num <= len(examples):
                    return examples[num - 1]
                else:
                    print("Номер от 1 до 4.")
            except ValueError:
                print("Введите целое число.")


def main():
    n = get_n()
    result = []

    for target in range(1, n + 1):
        found = False
        max_a = int(math.isqrt(target))
        for a in range(1, max_a + 1):
            remainder = target - a * a
            if remainder < 1:  # b должно быть натуральным (>=1)
                continue
            if is_perfect_square(remainder):
                result.append(target)
                found = True
                break  # нашли, переходим к следующему target

    print(f"\nЧисла от 1 до {n}, представимые как сумма квадратов двух натуральных чисел:")
    if result:
        print(*result)
    else:
        print("Таких чисел нет.")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
