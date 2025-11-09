"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
4. Простейшие циклы

83. Дано действительное число a. Найти:
а) среди чисел 1, 1+1/2, 1+1/2+1/3,... первое, большее a;
б) такое наименьшее n, что 1+1/2+...+1/n > a.
"""

import math


def find_first_greater(a, max_iter=10_000_000):
    """
    Находит первое число в последовательности 1, 1+1/2, 1+1/2+1/3, ...
    которое больше a.

    Возвращает (n, сумма) или использует приближение при слишком большом a.
    """
    sum_harmonic = 0.0
    n = 0

    while sum_harmonic <= a:
        n += 1
        sum_harmonic += 1 / n
        if n >= max_iter:
            print(
                f"\n⚠️ Предупреждение: достигнут предел {max_iter:,} итераций.\n"
                f"Используется приближение: Hₙ ≈ ln(n) + γ"
            )
            gamma = 0.5772156649
            n_approx = math.ceil(math.exp(a - gamma))
            sum_approx = math.log(n_approx) + gamma
            return n_approx, sum_approx

    return n, sum_harmonic


def calculate_harmonic_sum(n):
    """Вычисляет сумму 1 + 1/2 + ... + 1/n"""
    return sum(1 / i for i in range(1, n + 1))


def show_harmonic_sequence(max_terms=10):
    """Показывает первые члены последовательности"""
    print("Последовательность частичных сумм гармонического ряда:")
    print(f"{'n':>5} | {'1/n':>10} | {'Частичная сумма':>20}")
    print("-" * 45)

    sum_h = 0
    for n in range(1, max_terms + 1):
        term = 1 / n
        sum_h += term
        print(f"{n:5d} | {term:10.6f} | {sum_h:20.10f}")


def main():
    print("Введите действительное число a:")
    a = float(input("a = "))

    print(f"\n{'=' * 70}")
    print(f"Поиск для a = {a}")
    print(f"{'=' * 70}\n")

    n, sum_a = find_first_greater(a)

    print(f"а) Первое число, большее {a}:")
    print(f"   n = {n:,}")
    print(f"   Сумма = {sum_a:.10f}")

    if n > 1:
        prev_sum = calculate_harmonic_sum(n - 1)
        print(f"   Предыдущая сумма (n={n-1:,}) = {prev_sum:.10f}")

    print(f"\n{'=' * 70}")
    print("Первые 10 членов ряда:")
    show_harmonic_sequence(10)

    print(f"\n{'=' * 70}")
    print("Приближение Hₙ ≈ ln(n) + γ")
    gamma = 0.5772156649
    approx = math.log(n) + gamma
    print(f"Hₙ (приблизительно) = {approx:.10f}")
    print(f"Разница = {abs(sum_a - approx):.10f}")

    print("\nГармонический ряд растёт очень медленно:")
    print("H₁₀ ≈ 2.93, H₁₀₀ ≈ 5.19, H₁₀₀₀₀₀ ≈ 14.39")

    input("\nНажмите Enter, чтобы завершить программу.")


if __name__ == "__main__":
    main()
