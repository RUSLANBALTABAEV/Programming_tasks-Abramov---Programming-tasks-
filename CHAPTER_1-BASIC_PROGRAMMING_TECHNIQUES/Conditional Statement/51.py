"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
2. Разветвления
51. Даны действительные числа a, b, c (a ≠ 0).
Полностью исследовать биквадратное уравнение:

    a * x⁴ + b * x² + c = 0

Если действительных корней нет, то должно быть выдано сообщение об этом.
Иначе должны быть выданы два или четыре корня.
"""

import math


def solve_biquadratic(a, b, c):
    """
    Решает биквадратное уравнение a·x⁴ + b·x² + c = 0.

    Метод: замена t = x², получаем квадратное уравнение a·t² + b·t + c = 0.

    Args:
        a (float): коэффициент при x⁴ (a ≠ 0)
        b (float): коэффициент при x²
        c (float): свободный член

    Returns:
        tuple:
            has_real_roots (bool): есть ли действительные корни
            roots (list[float]): список действительных корней
            discriminant (float): дискриминант квадратного уравнения
            t1 (float | None): первый корень t
            t2 (float | None): второй корень t
    """
    discriminant = b**2 - 4 * a * c
    roots = []
    t1, t2 = None, None

    if discriminant < 0:
        return False, roots, discriminant, t1, t2

    if discriminant == 0:
        t1 = t2 = -b / (2 * a)
        t_values = [t1]
    else:
        sqrt_d = math.sqrt(discriminant)
        t1 = (-b + sqrt_d) / (2 * a)
        t2 = (-b - sqrt_d) / (2 * a)
        t_values = [t1, t2]

    for t in t_values:
        if t > 0:
            x = math.sqrt(t)
            roots.extend([-x, x])
        elif t == 0:
            roots.append(0)

    roots.sort()
    has_real_roots = bool(roots)

    return has_real_roots, roots, discriminant, t1, t2


def main():
    """Основная функция программы."""
    print("ПОЛНОЕ ИССЛЕДОВАНИЕ БИКВАДРАТНОГО УРАВНЕНИЯ")
    print("=" * 75)

    try:
        a = float(input("Введите коэффициент a (a ≠ 0): "))
        if a == 0:
            print("Ошибка: коэффициент a должен быть отличен от нуля!")
            return

        b = float(input("Введите коэффициент b: "))
        c = float(input("Введите коэффициент c: "))

        print("=" * 75)

        # Отображаем уравнение
        sign_b = '+' if b >= 0 else '-'
        sign_c = '+' if c >= 0 else '-'
        print(f"Исходное уравнение: {a:.4f}x⁴ {sign_b} {abs(b):.4f}x² "
              f"{sign_c} {abs(c):.4f} = 0")
        print("-" * 75)

        has_roots, roots, d, t1, t2 = solve_biquadratic(a, b, c)

        print(f"Замена: t = x² → {a:.4f}t² + {b:.4f}t + {c:.4f} = 0")
        print(f"Дискриминант: D = b² - 4ac = {d:.6f}")
        print("-" * 75)

        # Корни квадратного уравнения по t
        if d < 0:
            print("Квадратное уравнение не имеет действительных корней (D < 0).")
        elif d == 0:
            print(f"Один корень: t = {t1:.6f}")
        else:
            print(f"Два корня: t₁ = {t1:.6f}, t₂ = {t2:.6f}")

        print("-" * 75)

        # Анализ действительных корней по x
        if has_roots:
            print("✓ Биквадратное уравнение имеет действительные корни:")
            for i, root in enumerate(roots, 1):
                print(f"  x{i} = {root:.6f}")
        else:
            print("✗ Биквадратное уравнение не имеет действительных корней.")
            if d < 0:
                print("Причина: дискриминант отрицателен.")
            else:
                print("Причина: t₁ и t₂ отрицательны (x² = t < 0).")

        print("=" * 75)

    except ValueError:
        print("Ошибка: необходимо вводить числовые значения.")
    except Exception as exc:
        print(f"Произошла ошибка: {exc}")


if __name__ == "__main__":
    main()

input("\nНажмите Enter, чтобы завершить программу.")
