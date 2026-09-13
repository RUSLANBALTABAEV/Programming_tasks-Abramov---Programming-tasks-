"""
ГЛАВА 2
ЗАДАЧИ ПО ТЕМАМ
15. Целые числа.

560. Два натуральных числа называют дружественными, если каждое их них равно сумме всех делителей другого, кроме самого этого числа. Найти все пары дружественных чисел, лежащих в диапазоне от 200 до 300.
"""


import random
import math


def get_bounds():
    """Выбор способа ввода границ диапазона (по умолчанию 200..300)."""
    print("Задача 560: Дружественные числа в заданном диапазоне")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод границ диапазона")
    print("2 — Диапазон по условию задачи (200..300)")
    print("3 — Готовые примеры (диапазоны с известными парами)")

    while True:
        choice = input("Ваш выбор (1/2/3): ").strip()
        if choice in ('1', '2', '3'):
            break
        print("Ошибка: выберите 1, 2 или 3.")

    if choice == '1':
        while True:
            try:
                start = int(input("Введите начало диапазона (>=1): "))
                end = int(input("Введите конец диапазона (>= start): "))
                if start < 1 or end < start:
                    print("Некорректный диапазон. Повторите.")
                    continue
                return start, end
            except ValueError:
                print("Ошибка ввода. Введите целые числа.")

    elif choice == '2':
        print("Используется диапазон из условия: 200..300")
        return 200, 300

    else:  # готовые примеры
        examples = [
            (1, 1500),      # содержит пары (220,284), (1184,1210)
            (200, 300),     # пара (220,284)
            (1000, 2000),   # пара (1184,1210)
            (1, 100),       # пар нет
        ]
        print("\nГотовые примеры диапазонов:")
        for idx, (s, e) in enumerate(examples, 1):
            print(f"{idx}: [{s}; {e}]")
        while True:
            try:
                num = int(input("Выберите номер примера: "))
                if 1 <= num <= len(examples):
                    return examples[num - 1]
                else:
                    print(f"Номер должен быть от 1 до {len(examples)}.")
            except ValueError:
                print("Ошибка ввода. Введите целое число.")


def sum_proper_divisors(n):
    """Возвращает сумму собственных делителей числа n (все делители, кроме n)."""
    if n <= 1:
        return 0
    total = 1
    limit = int(math.isqrt(n))
    for i in range(2, limit + 1):
        if n % i == 0:
            total += i
            other = n // i
            if other != i:
                total += other
    return total


def find_amicable_pairs(start, end):
    """
    Находит все пары дружественных чисел (a, b) с a < b,
    оба числа которых лежат в диапазоне [start; end].
    """
    # Предварительно вычисляем суммы собственных делителей для всех чисел
    # до end включительно (для проверки sums[b] может потребоваться
    # значение делителя b, лежащего в диапазоне, поэтому end достаточно).
    sums = [0] * (end + 1)
    for i in range(1, end + 1):
        sums[i] = sum_proper_divisors(i)

    pairs = []
    for a in range(start, end + 1):
        b = sums[a]
        if b > a and b <= end and sums[b] == a:
            pairs.append((a, b))
    return pairs


def main():
    start, end = get_bounds()
    pairs = find_amicable_pairs(start, end)

    print(f"\nДиапазон поиска: [{start}; {end}]")
    print("-" * 50)

    if pairs:
        print(f"Найдено пар дружественных чисел: {len(pairs)}")
        for a, b in pairs:
            print(f"  {a} и {b}")
    else:
        print("В указанном диапазоне дружественных пар не найдено.")
    print("-" * 50)


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")