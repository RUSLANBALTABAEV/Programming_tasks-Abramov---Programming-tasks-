"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
3. Простейшая целочисленная арифметика
63. Определить, верно ли, что при делении неотрицательного
целого числа a на положительное целое число b получается остаток,
равный одному из двух заданных чисел r или s.
"""


def check_remainder(a: int, b: int, r: int, s: int) -> bool:
    """
    Проверяет, равен ли остаток от деления a на b одному из чисел r или s.

    Args:
        a (int): Делимое (неотрицательное число).
        b (int): Делитель (положительное число).
        r (int): Первое число для проверки.
        s (int): Второе число для проверки.

    Returns:
        bool: True, если остаток равен r или s, иначе False.
    """
    remainder = a % b
    return remainder == r or remainder == s


def main() -> None:
    """Основная функция программы."""
    try:
        a = int(input("Введите делимое (a ≥ 0): ").strip())
        b = int(input("Введите делитель (b > 0): ").strip())
        r = int(input("Введите первое число (r): ").strip())
        s = int(input("Введите второе число (s): ").strip())

        if a < 0 or b <= 0:
            print("Ошибка: a должно быть ≥ 0, а b > 0.")
            return

        remainder = a % b
        quotient = a // b

        print(f"\nДеление {a} на {b}:")
        print(f"Остаток: {remainder}")
        print(f"Числа для проверки: r = {r}, s = {s}")

        if check_remainder(a, b, r, s):
            print(f"\n✓ ВЕРНО: остаток {remainder} равен одному из чисел "
                  f"({r} или {s})")
        else:
            print(f"\n✗ НЕВЕРНО: остаток {remainder} не равен ни {r}, ни {s}")

        print("\nПолная информация о делении:")
        print(f"{a} = {b} × {quotient} + {remainder}")
        print(f"Диапазон возможных остатков: [0, {b})")

    except ValueError:
        print("Ошибка: необходимо вводить целые числа.")

    input("\nНажмите Enter, чтобы завершить программу.")


if __name__ == "__main__":
    main()
