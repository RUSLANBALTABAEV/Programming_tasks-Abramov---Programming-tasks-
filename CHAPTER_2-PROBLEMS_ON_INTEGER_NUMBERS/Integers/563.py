"""
ГЛАВА 2
ЗАДАЧИ ПО ТЕМАМ
15. Целые числа.

563. Назовем натуральное число палиндром, если его запись читается одинаково с начала и с конца (как, например, 4884, 393, 1). 
а) Найти все меньшие 100 натуральные числа, которые при возведении в квадрат дают палиндром.
б) Найти все меньшие 100 числа - палиндромы, которые при возведении в квадрат также дают палиндромы.
"""


import random


def is_palindrome(num):
    """Проверяет, является ли число палиндромом."""
    s = str(num)
    return s == s[::-1]


def get_bound():
    """Выбор способа ввода верхней границы диапазона (по умолчанию 100)."""
    print("Задача 563: Палиндромы и их квадраты")
    print("Выберите способ ввода верхней границы диапазона:")
    print("1 — Ручной ввод")
    print("2 — Граница по условию задачи (100)")
    print("3 — Готовые примеры")

    while True:
        choice = input("Ваш выбор (1/2/3): ").strip()
        if choice in ('1', '2', '3'):
            break
        print("Ошибка: выберите 1, 2 или 3.")

    if choice == '1':
        while True:
            try:
                b = int(input("Введите верхнюю границу (>=1): "))
                if b < 1:
                    print("Граница должна быть >= 1.")
                    continue
                return b
            except ValueError:
                print("Ошибка ввода. Введите целое число.")

    elif choice == '2':
        print("Используется граница по условию: 100")
        return 100

    else:  # готовые примеры
        examples = [10, 100, 1000, 10000]
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


def solve_a(bound):
    """
    а) Числа x < bound, квадрат которых является палиндромом.
    """
    return [x for x in range(1, bound) if is_palindrome(x * x)]


def solve_b(bound):
    """
    б) Числа x < bound, которые сами палиндромы и их квадрат — палиндром.
    """
    return [x for x in range(1, bound)
            if is_palindrome(x) and is_palindrome(x * x)]


def main():
    bound = get_bound()
    result_a = solve_a(bound)
    result_b = solve_b(bound)

    print(f"\nДиапазон: натуральные числа, меньшие {bound}")
    print("=" * 60)

    # а)
    print(f"а) Числа, квадрат которых — палиндром ({len(result_a)}):")
    if result_a:
        for x in result_a:
            print(f"   {x:>5}  ->  {x}^2 = {x*x}")
    else:
        print("   не найдено")
    print("-" * 60)

    # б)
    print(f"б) Числа-палиндромы, квадрат которых — палиндром ({len(result_b)}):")
    if result_b:
        for x in result_b:
            print(f"   {x:>5}  ->  {x}^2 = {x*x}")
    else:
        print("   не найдено")
    print("=" * 60)


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")