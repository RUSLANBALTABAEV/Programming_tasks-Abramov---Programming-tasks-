"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЕМЫ ПРОГРАММИРОВАНИЯ
21. Даны действительные числа c, d. Вычислить выражение:
abs(
    sin(abs(c * x1 ** 3 + d * x2 ** 2 - c * d)) ** 3 /
    sqrt((c * x1 ** 3 + d * x2 ** 2 - x1) ** 2 + pi)
) + tan(c * x1 ** 3 + d * x2 ** 2 - x1),
где x1 — больший, а x2 — меньший корни уравнения:
x ** 2 - 3x - abs(c * d) = 0.
"""

from math import sqrt, sin, tan, pi


def main():
    # Ввод данных
    c = float(input("Введите значение числа c: "))
    d = float(input("Введите значение числа d: "))

    # Вычисление дискриминанта
    D = 9 + 4 * abs(c * d)

    # Вычисление корней
    x1 = (3 + sqrt(D)) / 2
    x2 = (3 - sqrt(D)) / 2

    # Вычисление выражения
    numerator = sin(abs(c * x1 ** 3 + d * x2 ** 2 - c * d)) ** 3
    denominator = sqrt((c * x1 ** 3 + d * x2 ** 2 - x1) ** 2 + pi)
    result = abs(numerator / denominator) + tan(c * x1 ** 3 + d * x2 ** 2 - x1)

    # Вывод результата
    print(f"\nРезультат вычисления: {result:.4f}")

    input("Нажмите любую клавишу, чтобы завершить программу.")


if __name__ == "__main__":
    main()
