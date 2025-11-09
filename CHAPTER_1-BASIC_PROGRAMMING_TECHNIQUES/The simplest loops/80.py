"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
4. Простейшие циклы

80. Дано действительное число x. Вычислить:

x - x³/3! + x⁵/5! - x⁷/7! + x⁹/9! - x¹¹/11! + x¹³/13!

Это первые 7 членов ряда Тейлора для sin(x).
"""

import math


def factorial(n: int) -> int:
    """Вычисляет факториал числа n."""
    if n <= 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def calculate_series(x: float) -> float:
    """
    Вычисляет сумму:
    x - x³/3! + x⁵/5! - x⁷/7! + x⁹/9! - x¹¹/11! + x¹³/13!
    """
    result = 0.0
    for i in range(7):
        power = 2 * i + 1
        sign = (-1) ** i
        result += sign * (x ** power) / factorial(power)
    return result


def calculate_series_detailed(x: float) -> float:
    """Выводит подробное вычисление каждого члена ряда."""
    print(f"Вычисление для x = {x}\n")
    print(
        f"{'i':>2} | {'Степень':>7} | {'Факториал':>12} | {'Знак':>5} | "
        f"{'Член ряда':>20} | {'Сумма':>20}"
    )
    print("-" * 95)

    result = 0.0
    for i in range(7):
        power = 2 * i + 1
        fact = factorial(power)
        sign = (-1) ** i
        term = sign * (x ** power) / fact
        result += term
        sign_str = "+" if sign > 0 else "-"
        print(
            f"{i:2d} | {power:7d} | {fact:12d} | {sign_str:>5} | "
            f"{term:20.10f} | {result:20.10f}"
        )
    return result


def main() -> None:
    """Основная функция программы."""
    print("Введите действительное число x:")
    x = float(input("x = "))

    print(f"\n{'=' * 95}")
    print(f"Вычисление ряда Тейлора для x = {x}")
    print(f"{'=' * 95}\n")

    # Основное вычисление
    result = calculate_series(x)
    sin_x = math.sin(x)
    diff = abs(result - sin_x)
    rel_error = diff / abs(sin_x) * 100 if sin_x != 0 else 0

    print(f"Результат вычисления ряда: {result:.15f}")
    print(f"Значение sin({x}):         {sin_x:.15f}")
    print(f"Абсолютная ошибка:         {diff:.15e}")
    print(f"Относительная ошибка:      {rel_error:.10f}%\n")

    # Детальное вычисление
    print(f"{'=' * 95}")
    print("--- Детальное вычисление каждого члена ---\n")
    result_detailed = calculate_series_detailed(x)

    print(f"\n{'=' * 95}")
    print(f"Итоговая сумма: {result_detailed:.15f}")
    print(f"sin({x}) =      {sin_x:.15f}")

    # Формула
    print(f"\n{'=' * 95}")
    print("--- Формула ряда Тейлора для sin(x) ---\n")

    print("Полный ряд Тейлора для sin(x):")
    print("sin(x) = Σ(n=0..∞) [(-1)^n · x^(2n+1) / (2n+1)!]")
    print("Вычисляем первые 7 членов (n = 0..6):\n")

    for i in range(7):
        power = 2 * i + 1
        fact = factorial(power)
        sign = "+" if i % 2 == 0 else "-"
        print(f"  n={i}: {sign} x^{power}/{fact}")

    # Примеры
    print(f"\n{'=' * 95}")
    print("--- Примеры для разных значений x ---\n")

    test_values = [
        0,
        0.5,
        1,
        math.pi / 6,
        math.pi / 4,
        math.pi / 3,
        math.pi / 2,
        math.pi,
        2 * math.pi,
    ]

    print(
        f"{'x':>10} | {'Приближение':>20} | {'sin(x)':>20} | "
        f"{'Ошибка':>15} | {'Отн. %':>12}"
    )
    print("-" * 95)

    for x_test in test_values:
        approx = calculate_series(x_test)
        exact = math.sin(x_test)
        error = abs(approx - exact)
        rel_error = error / abs(exact) * 100 if exact != 0 else 0

        label = {
            math.pi / 6: "π/6",
            math.pi / 4: "π/4",
            math.pi / 3: "π/3",
            math.pi / 2: "π/2",
            math.pi: "π",
            2 * math.pi: "2π",
        }.get(x_test, f"{x_test:.6f}")

        print(
            f"{label:>10} | {approx:20.10f} | {exact:20.10f} | "
            f"{error:15.10e} | {rel_error:12.6f}"
        )

    # Сходимость
    print(f"\n{'=' * 95}")
    print("--- Сходимость ряда (добавление членов) ---\n")

    print("Для x = 1.0, последовательное добавление членов:")
    print(f"{'Членов':>7} | {'Приближение':>20} | {'sin(1)':>20} | {'Ошибка':>15}")
    print("-" * 70)

    x_conv = 1.0
    exact_sin = math.sin(x_conv)

    for num_terms in range(1, 8):
        partial_sum = sum(
            (-1) ** i * (x_conv ** (2 * i + 1)) / factorial(2 * i + 1)
            for i in range(num_terms)
        )
        error = abs(partial_sum - exact_sin)
        print(
            f"{num_terms:7d} | {partial_sum:20.10f} | "
            f"{exact_sin:20.10f} | {error:15.10e}"
        )

    # Точность при разных x
    print(f"\n{'=' * 95}")
    print("--- Точность приближения при разных x ---\n")

    print(f"{'x':>10} | {'Ошибка %':>15}")
    print("-" * 30)

    for x_test in [0.1, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]:
        approx = calculate_series(x_test)
        exact = math.sin(x_test)
        rel_error = abs(approx - exact) / abs(exact) * 100 if exact != 0 else 0
        print(f"{x_test:10.1f} | {rel_error:15.8f}")

    print("\nЗамечание: Точность уменьшается с ростом |x|.")
    print("Для лучшей точности при больших x нужно больше членов ряда.")

    # Интересные факты
    print(f"\n{'=' * 95}")
    print("--- Интересные факты ---\n")

    print("1. Ряд Тейлора для sin(x) сходится для всех x.\n")
    print("2. При x = π/2 ≈ 1.5708:")
    x_pi2 = math.pi / 2
    approx_pi2 = calculate_series(x_pi2)
    exact_pi2 = math.sin(x_pi2)
    print(f"   Приближение: {approx_pi2:.10f}")
    print(f"   Точное:      {exact_pi2:.10f} (должно быть 1)")
    print(f"   Ошибка:      {abs(approx_pi2 - exact_pi2):.10e}\n")

    print("3. Факториалы растут очень быстро:")
    for n in [1, 3, 5, 7, 9, 11, 13]:
        print(f"   {n}! = {factorial(n):,}")

    print("\n4. Члены ряда быстро уменьшаются (для малых x):")
    print("   Для x = 1:")
    for i in range(7):
        power = 2 * i + 1
        term = (1.0 ** power) / factorial(power)
        print(f"   x^{power}/{factorial(power)} ≈ {term:.10e}")

    input("\nНажмите Enter, чтобы завершить программу.")


if __name__ == "__main__":
    main()
