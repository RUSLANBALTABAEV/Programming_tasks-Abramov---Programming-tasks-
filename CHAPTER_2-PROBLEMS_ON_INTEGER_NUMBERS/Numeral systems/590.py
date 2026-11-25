"""
ГЛАВА 2
ЗАДАЧИ ПО ТЕМАМ
16. Системы счисления

590. Получить все меньшие 10 ^ 6 натуральные числа, которые являются палиндромами (см. задачу 563) как в десятичной так и в как в десятичной так и в
"""


# ==========================================================
# ЗАДАЧА 590: Двойные палиндромы (в 10-чной и 2-чной системах)
# §16. Системы счисления
# ==========================================================

import random


def is_palindrome(num, base):
    """
    Проверяет, является ли число палиндромом в заданной системе счисления.
    base: 10 (десятичная) или 2 (двоичная).
    """
    if base == 10:
        s = str(num)
    elif base == 2:
        s = bin(num)[2:]  # отбрасываем префикс '0b'
    else:
        raise ValueError("Поддерживаются только системы с основанием 2 и 10")
    
    return s == s[::-1]


def get_params():
    """Выбор способа ввода верхней границы диапазона (по умолчанию 10^6)."""
    print("Задача 590: Двойные палиндромы (десятичный и двоичный)")
    print("Выберите способ ввода верхней границы диапазона:")
    print("1 — Ручной ввод")
    print("2 — Граница по условию задачи (10^6)")
    print("3 — Готовые примеры")

    while True:
        choice = input("Ваш выбор (1/2/3): ").strip()
        if choice in ('1', '2', '3'):
            break
        print("Ошибка: выберите 1, 2 или 3.")

    if choice == '1':
        while True:
            try:
                b = int(input("Введите верхнюю границу (>= 1): "))
                if b < 1:
                    print("Граница должна быть >= 1.")
                    continue
                return b
            except ValueError:
                print("Ошибка ввода. Введите целое число.")

    elif choice == '2':
        print("Используется граница по условию: 10^6 = 1000000")
        return 10 ** 6

    else:  # готовые примеры
        examples = [100, 1000, 10000, 100000]
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


def find_double_palindromes(bound):
    """
    Находит все натуральные числа x < bound, которые являются палиндромами
    как в десятичной, так и в двоичной системах.
    
    Оптимизация: сначала проверяем десятичный палиндром (это быстрее 
    отсекает большинство чисел), и только потом — двоичный.
    """
    results = []
    for x in range(1, bound):
        if is_palindrome(x, 10) and is_palindrome(x, 2):
            results.append(x)
    return results


def main():
    bound = get_params()
    results = find_double_palindromes(bound)

    print(f"\nДиапазон поиска: натуральные числа, меньшие {bound}")
    print("=" * 60)

    # Вывод результатов
    print(f"Найдено чисел-палиндромов в обеих системах: {len(results)}")
    print("-" * 60)
    
    if results:
        print(f"{'Число (10)':>12} | {'Двоичное представление (2)':^30}")
        print("-" * 60)
        for x in results:
            bin_str = bin(x)[2:]
            print(f"{x:>12} | {bin_str:^30}")
    else:
        print("   не найдено")
    print("=" * 60)

    # Проверки
    print("\n--- Проверка ---")
    
    # 1. Проверка, что все числа удовлетворяют условиям
    all_valid = True
    for x in results:
        dec_ok = is_palindrome(x, 10)
        bin_ok = is_palindrome(x, 2)
        if not (dec_ok and bin_ok):
            all_valid = False
            print(f"Ошибка: {x} не является двойным палиндромом!")
            break
            
    print(f"Все найденные числа удовлетворяют условиям: {all_valid}")

    # 2. Проверка диапазона
    if results:
        min_val, max_val = min(results), max(results)
        print(f"Минимальное найденное число: {min_val}")
        print(f"Максимальное найденное число: {max_val} (меньше {bound}: {max_val < bound})")

    print("=" * 60)


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")