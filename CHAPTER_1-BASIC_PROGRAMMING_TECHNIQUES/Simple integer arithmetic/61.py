"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
3. Простейшая целочисленная арифметика
61. Дано действительное число x. Получить целую часть числа x;
затем – число x, округленное до ближайшего целого; затем – число x
без дробных цифр.
"""

import math


def floor_function(x: float) -> int:
    """
    Вычисляет целую часть числа x (функция пола/floor).

    Целая часть [x] — это наибольшее целое число, не превосходящее x.

    Args:
        x (float): Входное число.

    Returns:
        int: Целая часть числа x.
    """
    return math.floor(x)


def round_function(x: float) -> int:
    """
    Вычисляет число x, округлённое до ближайшего целого.

    Обычное округление:
    если дробная часть >= 0.5, округляем вверх, иначе — вниз.

    Args:
        x (float): Входное число.

    Returns:
        int: Число, округлённое до ближайшего целого.
    """
    return round(x)


def fractional_part(x: float) -> float:
    """
    Вычисляет дробную часть числа x.

    Дробная часть {x} = x - [x].

    Args:
        x (float): Входное число.

    Returns:
        float: Дробная часть числа x.
    """
    floor_part = math.floor(x)
    return x - floor_part


def main() -> None:
    """Основная функция программы."""
    print("Вычисление целой части числа")
    print("=" * 75)

    print("Определение:")
    print("  Целой частью числа x, обозначаемой [x], называется")
    print("  наибольшее целое число, не превосходящее x.\n")

    print("Примеры:")
    print("  [3.14] = 3")
    print("  [3] = 3")
    print("  [-3.14] = -4  (так как -4 < -3.14 < -3)")
    print("  [-3] = -3")
    print("=" * 75)

    try:
        # Ввод числа
        x = float(input("Введите число x: ").strip())
        print("=" * 75)

        # Вычисляем значения
        floor_part = floor_function(x)
        rounded = round_function(x)
        frac_part = fractional_part(x)

        # Выводим результаты
        print(f"Входное число: x = {x}")
        print("-" * 75)

        print("Результаты:\n")

        print("1. ЦЕЛАЯ ЧАСТЬ [x]:")
        print(f"   [x] = [{x}] = {floor_part}\n")

        print("2. ОКРУГЛЁННОЕ ЗНАЧЕНИЕ (до ближайшего целого):")
        print(f"   round(x) = round({x}) = {rounded}\n")

        print("3. ДРОБНАЯ ЧАСТЬ {x} = x - [x]:")
        print(f"   {{x}} = {x} - {floor_part} = {frac_part:.10f}\n")

        print("-" * 75)
        print("Проверка:")
        print(f"  [x] + {{x}} = {floor_part} + {frac_part:.10f} "
              f"= {floor_part + frac_part}")
        print(f"  Это равно исходному числу x = {x}: "
              f"{abs((floor_part + frac_part) - x) < 1e-10}\n")

        print("-" * 75)
        print("Важное замечание о отрицательных числах:\n")

        if x < 0 and x != int(x):
            print(f"Число x = {x} отрицательное и не целое.")
            print(f"[x] = {floor_part} (наибольшее целое ≤ {x})")
            print("Это НЕ то же самое, что отбросить дробную часть!")
            print(f"Если бы просто отбросили дробную часть, "
                  f"получили бы {int(x)}")

        print("=" * 75)
        print("\nТаблица примеров функции пола для разных чисел:")
        print("-" * 75)
        print(f"{'x':>10} | {'[x]':>10} | {'{x}':>10} | {'Описание':>30}")
        print("-" * 75)

        test_values = [3.14, 3.0, 3.99, -3.14, -3.0, 0.5, -0.5]

        for val in test_values:
            floor_val = math.floor(val)
            frac_val = val - floor_val

            if val > 0:
                desc = "Положительное число"
            elif val < 0:
                desc = "Отрицательное число"
            else:
                desc = "Нуль"

            if val == int(val):
                desc += " (целое)"

            print(f"{val:>10} | {floor_val:>10} | {frac_val:>10.4f} "
                  f"| {desc:>30}")

        print("-" * 75)
        print("=" * 75)

    except ValueError:
        print("Ошибка: необходимо вводить число!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()

input("\nНажмите Enter, чтобы завершить программу.")
