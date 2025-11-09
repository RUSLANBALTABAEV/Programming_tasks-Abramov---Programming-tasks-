"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
3. Простейшая целочисленная арифметика
68. Дано натуральное число n (n ≤ 9999).
а) Является ли это число палиндромом (перевёртышем) —
   например, 2222, 6116, 0440.
б) Содержит ли число ровно три одинаковые цифры —
   например, 6676, 4544, 0006.
в) Верно ли, что все четыре цифры различны?
"""

from collections import Counter


def is_palindrome(num: int) -> bool:
    """
    Проверяет, является ли число палиндромом (перевёртышем)
    с учётом ведущих нулей до четырёх разрядов.

    Args:
        num (int): Натуральное число (1 ≤ num ≤ 9999).

    Returns:
        bool: True, если число палиндром, иначе False.
    """
    s = str(num).zfill(4)
    return s == s[::-1]


def has_exactly_three_same(num: int) -> bool:
    """
    Проверяет, содержит ли число ровно три одинаковые цифры.

    Args:
        num (int): Натуральное число (1 ≤ num ≤ 9999).

    Returns:
        bool: True, если число содержит ровно три одинаковые цифры.
    """
    s = str(num).zfill(4)
    counts = Counter(s)
    return any(count == 3 for count in counts.values())


def all_digits_different(num: int) -> bool:
    """
    Проверяет, все ли цифры числа различны.

    Args:
        num (int): Натуральное число (1 ≤ num ≤ 9999).

    Returns:
        bool: True, если все цифры различны.
    """
    s = str(num).zfill(4)
    return len(set(s)) == 4


def analyze_number(n: int) -> None:
    """
    Анализирует число: выводит информацию о палиндроме,
    трёх одинаковых цифрах и уникальности всех цифр.

    Args:
        n (int): Натуральное число (1 ≤ n ≤ 9999).
    """
    if not (1 <= n <= 9999):
        print("Ошибка: число должно быть от 1 до 9999.")
        return

    s = str(n).zfill(4)
    print(f"\n{'=' * 60}")
    print(f"Анализ числа: n = {n} → цифры: {' '.join(s)}")
    print(f"{'=' * 60}")

    # а) Палиндром
    reversed_s = s[::-1]
    palindrome = is_palindrome(n)
    print("\nа) Является ли палиндромом?")
    print(f"   Обратное число: {reversed_s}")
    print(f"   Ответ: {'ДА ✓' if palindrome else 'НЕТ ✗'}")

    # б) Три одинаковые цифры
    counts = Counter(s)
    has_three = any(count == 3 for count in counts.values())
    print("\nб) Содержит ли ровно три одинаковые цифры?")
    print(f"   Распределение цифр: {dict(counts)}")
    print(f"   Ответ: {'ДА ✓' if has_three else 'НЕТ ✗'}")
    if has_three:
        for digit, count in counts.items():
            if count == 3:
                print(f"   (Цифра '{digit}' встречается 3 раза)")

    # в) Все цифры различны
    different = len(counts) == 4
    print("\nв) Все ли четыре цифры различны?")
    print(f"   Различных цифр: {len(counts)}")
    print(f"   Ответ: {'ДА ✓' if different else 'НЕТ ✗'}")


def main() -> None:
    """Основная функция программы."""
    try:
        n = int(input("Введите натуральное число (n ≤ 9999): ").strip())
        analyze_number(n)

        print(f"\n{'=' * 60}")
        print("--- Примеры ---\n")

        test_numbers = [
            (2222, "Палиндром"),
            (6116, "Палиндром"),
            (440, "Палиндром (0440)"),
            (6676, "Три 6-ки"),
            (4544, "Три 4-ки"),
            (6, "Три 0-ля (0006)"),
            (1234, "Все разные"),
            (5678, "Все разные"),
        ]

        for num, desc in test_numbers:
            print(f"n = {num} ({desc}):")
            print(f"  а) Палиндром: {'ДА' if is_palindrome(num) else 'НЕТ'}")
            print(f"  б) Ровно 3 одинаковые: "
                  f"{'ДА' if has_exactly_three_same(num) else 'НЕТ'}")
            print(f"  в) Все разные: "
                  f"{'ДА' if all_digits_different(num) else 'НЕТ'}")
            print()
    except ValueError:
        print("Ошибка: введите корректное целое число.")

    input("\nНажмите Enter, чтобы завершить программу.")


if __name__ == "__main__":
    main()
