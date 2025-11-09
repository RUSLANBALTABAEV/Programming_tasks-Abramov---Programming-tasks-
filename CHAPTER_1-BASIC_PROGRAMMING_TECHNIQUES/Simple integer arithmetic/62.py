"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
3. Простейшая целочисленная арифметика
62. Определить, является ли данное целое число чётным.
"""


def is_even(n: int) -> bool:
    """
    Проверяет, является ли число чётным.

    Args:
        n (int): Проверяемое целое число.

    Returns:
        bool: True, если число чётное, иначе False.
    """
    return n % 2 == 0


def main() -> None:
    """Основная функция программы."""
    try:
        number = int(input("Введите целое число: ").strip())

        if is_even(number):
            print(f"Число {number} является чётным")
        else:
            print(f"Число {number} является нечётным")

        print("\n--- Примеры ---")
        numbers = [24, 37, 100, 15, 0, -8]

        for num in numbers:
            parity = "чётное" if is_even(num) else "нечётное"
            print(f"{num} — {parity}")

    except ValueError:
        print("Ошибка: необходимо ввести целое число.")

    input("\nНажмите Enter, чтобы завершить программу.")


if __name__ == "__main__":
    main()
