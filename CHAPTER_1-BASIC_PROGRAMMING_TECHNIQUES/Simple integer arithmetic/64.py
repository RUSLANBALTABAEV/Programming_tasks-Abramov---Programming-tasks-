"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
3. Простейшая целочисленная арифметика
64. Дано натуральное число n (n > 99). Определить число сотен в нём.
"""


def get_hundreds_digit(num: int) -> int | None:
    """
    Возвращает цифру в разряде сотен заданного числа.

    Args:
        num (int): Натуральное число (n > 99).

    Returns:
        int | None: Цифра в разряде сотен, если число > 99,
        иначе None.
    """
    if num <= 99:
        return None
    return (num // 100) % 10


def print_digit_breakdown(num: int) -> None:
    """
    Выводит разряды числа справа налево: единицы, десятки, сотни и т.д.

    Args:
        num (int): Целое число для анализа.
    """
    str_n = str(num)
    names = [
        "единиц", "десятков", "сотен",
        "тысяч", "десятков тысяч", "сотен тысяч", "миллионов"
    ]

    for i, digit in enumerate(reversed(str_n)):
        name = names[i] if i < len(names) else f"10^{i}"
        print(f"Разряд {name}: {digit}")


def main() -> None:
    """Основная функция программы."""
    try:
        n = int(input("Введите натуральное число (n > 99): ").strip())

        if n <= 99:
            print("Ошибка: число должно быть больше 99.")
            return

        hundreds = get_hundreds_digit(n)

        print(f"\nЧисло: {n}")
        print(f"Цифра в разряде сотен: {hundreds}\n")

        print("Разложение по разрядам:")
        print_digit_breakdown(n)

        # Примеры
        print("\n" + "=" * 40)
        print("--- Примеры ---")
        examples = [345, 2056, 7821, 100, 999, 12345]
        for num in examples:
            h = get_hundreds_digit(num)
            if h is not None:
                print(f"n = {num:5d} → сотни = {h}")
            else:
                print(f"n = {num:5d} → число слишком маленькое")

    except ValueError:
        print("Ошибка: необходимо вводить целое число.")

    input("\nНажмите Enter, чтобы завершить программу.")


if __name__ == "__main__":
    main()
