"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
2. Разветвления
48. Даны действительные числа a, b, c (a ≠ 0). 
Выяснить, имеет ли уравнение a * x² + b * x + c = 0 действительные корни. 
Если действительные корни имеются, то найти их. 
В противном случае вывести сообщение, что действительных корней нет.
"""

import math
from typing import Tuple, Optional


def solve_quadratic(a: float, b: float, c: float) -> Tuple[bool, Optional[float], Optional[float], float]:
    """Решает квадратное уравнение a*x² + b*x + c = 0.

    Args:
        a: Коэффициент при x² (a ≠ 0).
        b: Коэффициент при x.
        c: Свободный член.

    Returns:
        Кортеж вида (has_real_roots, x1, x2, discriminant):
        - has_real_roots — True, если есть действительные корни.
        - x1, x2 — корни (или None, если их нет).
        - discriminant — значение дискриминанта.
    """
    discriminant = b**2 - 4 * a * c

    if discriminant < 0:
        return False, None, None, discriminant
    elif discriminant == 0:
        x = -b / (2 * a)
        return True, x, x, discriminant
    else:
        sqrt_d = math.sqrt(discriminant)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return True, x1, x2, discriminant


def main() -> None:
    """Основная функция программы."""
    print("Решение квадратного уравнения a*x² + b*x + c = 0")
    print("=" * 60)

    try:
        a = float(input("Введите коэффициент a (a ≠ 0): "))
        if a == 0:
            print("Ошибка: коэффициент 'a' должен быть отличен от нуля!")
            return

        b = float(input("Введите коэффициент b: "))
        c = float(input("Введите коэффициент c: "))

        print("=" * 60)

        # Формирование уравнения в текстовом виде
        equation = f"{a}x²"
        equation += f" + {b}x" if b >= 0 else f" - {abs(b)}x"
        equation += f" + {c}" if c >= 0 else f" - {abs(c)}"
        equation += " = 0"

        print(f"Уравнение: {equation}")
        print("-" * 60)

        has_roots, x1, x2, d = solve_quadratic(a, b, c)

        print(f"Дискриминант D = b² - 4ac = {b}² - 4·{a}·{c} = {d}")
        print("-" * 60)

        if has_roots:
            print("✓ Уравнение имеет действительные корни")
            if x1 == x2:
                print(f"Один корень (кратности 2): x = {x1}")
            else:
                print(f"Два различных корня:")
                print(f"x₁ = {x1}")
                print(f"x₂ = {x2}")
        else:
            print("✗ Уравнение не имеет действительных корней "
                  "(дискриминант отрицателен)")

        print("=" * 60)

    except ValueError:
        print("Ошибка: необходимо вводить числовые значения.")
    except ZeroDivisionError:
        print("Ошибка: деление на ноль (a не должно быть равно 0).")


if __name__ == "__main__":
    main()

input("\nНажмите Enter, чтобы завершить программу.")
