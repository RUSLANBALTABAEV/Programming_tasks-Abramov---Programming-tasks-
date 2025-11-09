"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
4. Простейшие циклы

81. Даны действительные числа x, a и натуральное число n.
Вычислить выражение:

((...((x + a)² + a)² + ... + a)² + a)² + a

где n — количество скобок (итераций).
"""

from math import isnan


def calculate_nested(x: float, a: float, n: int) -> float:
    """
    Вычисляет выражение с n вложенными скобками:
    ((...((x + a)^2 + a)^2 + ... + a)^2 + a)

    Алгоритм:
    1. Начинаем с result = x
    2. n раз выполняем: result = (result + a)^2 + a
    3. Возвращаем итоговое значение
    """
    result = x
    for _ in range(n):
        result = (result + a) ** 2 + a
    return result


def calculate_nested_detailed(x: float, a: float, n: int) -> float:
    """
    Вычисляет выражение с детальным выводом каждого шага:
    Показывает промежуточные значения result, result + a, (result + a)^2 и (result + a)^2 + a.
    """
    result = x

    print(f"{'Шаг':>4} | {'result до':>20} | {'result + a':>20} | {'(result+a)²':>20} | {'+ a':>20}")
    print("-" * 95)
    print(f"{'0':>4} | {result:20.6f} | {'-':>20} | {'-':>20} | {'-':>20}")

    for i in range(n):
        step1 = result + a
        step2 = step1 ** 2
        step3 = step2 + a

        print(f"{i + 1:4d} | {result:20.6f} | {step1:20.6f} | {step2:20.6f} | {step3:20.6f}")
        result = step3

    return result


def main() -> None:
    """Главная функция программы."""
    print("Введите действительные числа x, a и натуральное число n:")
    x = float(input("x = "))
    a = float(input("a = "))
    n = int(input("n (количество скобок) = "))

    if n < 1:
        print("Ошибка: n должно быть натуральным числом (n ≥ 1)")
        return

    print(f"\n{'=' * 85}")
    print(f"Вычисление выражения для x = {x}, a = {a}, n = {n}")
    print(f"{'=' * 85}\n")

    result = calculate_nested(x, a, n)
    print(f"Результат: {result:.15f}")
    print(f"В научной нотации: {result:.6e}\n")

    # Детальный вывод только для небольших n
    if n <= 10:
        print(f"{'=' * 85}")
        print("--- Детальное вычисление каждого шага ---\n")
        result_detailed = calculate_nested_detailed(x, a, n)
        print(f"\nИтоговый результат: {result_detailed:.15f}")

    # Примеры для разных значений
    print(f"\n{'=' * 85}")
    print("--- Примеры для разных значений ---\n")

    test_cases = [
        (1, 1, 1),
        (1, 1, 2),
        (1, 1, 3),
        (0, 1, 3),
        (2, 0.5, 3),
        (0, 0, 5),
        (1, -0.5, 3),
    ]

    print(f"{'x':>6} | {'a':>6} | {'n':>3} | {'Результат':>20}")
    print("-" * 45)

    for x_val, a_val, n_val in test_cases:
        res = calculate_nested(x_val, a_val, n_val)
        res_str = f"{res:20.6f}" if not isnan(res) else "NaN".center(20)
        print(f"{x_val:6.2f} | {a_val:6.2f} | {n_val:3d} | {res_str}")

    # Анализ роста
    print(f"\n{'=' * 85}")
    print("--- Анализ роста результата ---\n")
    print("Как растёт результат при увеличении n (для x = 1, a = 1):")
    print(f"{'n':>3} | {'Результат':>40} | {'Изменение':>40}")
    print("-" * 90)

    prev_result = 1
    for n_test in range(1, 11):
        res = calculate_nested(1, 1, n_test)
        delta = res - prev_result if n_test > 1 else 0

        # Безопасное форматирование для очень больших чисел
        try:
            print(f"{n_test:3d} | {res:40.6e} | {delta:40.6e}")
        except OverflowError:
            print(f"{n_test:3d} | {str(res):>40} | {str(delta):>40}")

        prev_result = res

    # Пошаговое объяснение
    print(f"\n{'=' * 85}")
    print("--- Пошаговое объяснение для x = 1, a = 1, n = 3 ---\n")

    x_ex, a_ex, n_ex = 1, 1, 3
    result_ex = x_ex
    print(f"Начальное значение: result = {x_ex}\n")

    for i in range(n_ex):
        print(f"Шаг {i + 1}:")
        print(f"  result = {result_ex}")
        print(f"  result + a = {result_ex} + {a_ex} = {result_ex + a_ex}")
        print(f"  (result + a)² = ({result_ex + a_ex})² = {(result_ex + a_ex) ** 2}")
        result_ex = (result_ex + a_ex) ** 2 + a_ex
        print(f"  (result + a)² + a = {(result_ex - a_ex)} + {a_ex} = {result_ex}\n")

    print(f"Итоговый результат: {result_ex}")

    # Формула и структура
    print(f"\n{'=' * 85}")
    print("--- Формула и структура ---\n")

    print("Рекуррентное соотношение:")
    print("  f₀(x) = x")
    print("  fᵢ(x) = (fᵢ₋₁(x) + a)² + a\n")

    print("Пример для x = 1, a = 1:")
    for i in range(1, 4):
        print(f"  n = {i}: результат = {calculate_nested(1, 1, i)}")

    # Влияние параметров
    print(f"\n{'=' * 85}")
    print("--- Влияние параметров ---\n")

    print("1. Влияние x (при a = 1, n = 3):")
    for x_test in [0, 0.5, 1, 2, 5]:
        res = calculate_nested(x_test, 1, 3)
        print(f"   x = {x_test:4.1f}: результат = {res:15.2f}")

    print("\n2. Влияние a (при x = 1, n = 3):")
    for a_test in [0, 0.5, 1, 1.5, 2]:
        res = calculate_nested(1, a_test, 3)
        print(f"   a = {a_test:4.1f}: результат = {res:15.2f}")

    print("\n3. Влияние n (при x = 1, a = 1):")
    for n_test in range(1, 8):
        res = calculate_nested(1, 1, n_test)
        print(f"   n = {n_test}: результат = {res:.0e}")

    input("\nНажмите Enter, чтобы завершить программу.")


if __name__ == "__main__":
    main()
