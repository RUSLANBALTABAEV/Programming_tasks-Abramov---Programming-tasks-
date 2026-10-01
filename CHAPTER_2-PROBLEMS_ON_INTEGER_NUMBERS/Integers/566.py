"""
ГЛАВА 2
ЗАДАЧИ ПО ТЕМАМ
15. Целые числа.

566. Найти все простые несократимые дроби, заключенные между 0 и 1, знаменатели которых не превышают 7 (дробь задается двумя натуральными числами - числителем и знаменателем).
"""


import math
import random


def get_bound():
    """Выбор способа ввода верхней границы знаменателя."""
    print("Задача 566: Несократимые дроби между 0 и 1")
    print("Выберите способ ввода верхней границы знаменателя:")
    print("1 — Ручной ввод")
    print("2 — Граница по условию задачи (7)")
    print("3 — Готовые примеры")

    while True:
        choice = input("Ваш выбор (1/2/3): ").strip()
        if choice in ('1', '2', '3'):
            break
        print("Ошибка: выберите 1, 2 или 3.")

    if choice == '1':
        while True:
            try:
                bound = int(input("Введите верхнюю границу знаменателя (>=2): "))
                if bound < 2:
                    print("Граница должна быть >= 2.")
                    continue
                return bound
            except ValueError:
                print("Ошибка ввода. Введите целое число.")

    elif choice == '2':
        print("Используется граница по условию: 7")
        return 7

    else:  # готовые примеры
        examples = [3, 5, 7, 10]
        print("\nГотовые примеры верхней границы:")
        for idx, val in enumerate(examples, 1):
            print(f"{idx}: {val}")
        while True:
            try:
                num = int(input("Выберите номер примера: "))
                if 1 <= num <= len(examples):
                    return examples[num - 1]
                else:
                    print(f"Номер должен быть от 1 до {len(examples)}.")
            except ValueError:
                print("Ошибка ввода. Введите целое число.")


def find_fractions(bound):
    """
    Находит все несократимые дроби num/denom, где 0 < num/denom < 1
    и знаменатель denom не превышает bound.
    Возвращает список кортежей (num, denom), отсортированный по значению дроби.
    """
    fractions = []
    for denom in range(2, bound + 1):
        for num in range(1, denom):        # num < denom, чтобы дробь была < 1
            if math.gcd(num, denom) == 1:  # несократимость
                fractions.append((num, denom))
    # Сортировка по значению дроби (num/denom)
    fractions.sort(key=lambda f: f[0] / f[1])
    return fractions


def main():
    bound = get_bound()
    fractions = find_fractions(bound)

    print(f"\nЗнаменатели не превышают {bound}")
    print("=" * 60)

    if fractions:
        print(f"Найдено несократимых дробей, заключённых между 0 и 1: {len(fractions)}\n")
        # Выводим дроби с их приближённым значением
        for i, (num, denom) in enumerate(fractions, 1):
            value = num / denom
            print(f"  {i:>3}. {num}/{denom}  ≈ {value:.6f}")

        print("\nВ компактном виде:")
        print("  " + ", ".join(f"{n}/{d}" for n, d in fractions))
    else:
        print("Дробей, удовлетворяющих условию, не найдено.")
    print("=" * 60)


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")