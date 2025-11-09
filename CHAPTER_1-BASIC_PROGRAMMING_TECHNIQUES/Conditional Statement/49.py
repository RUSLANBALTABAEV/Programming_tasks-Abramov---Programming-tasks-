"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
2. Разветвления
49. Дано действительное число h. 
Выяснить, имеет ли уравнение a*x² + b*x + c = 0 действительные корни, если

a = sqrt((abs(sin(8*h) + 17)) / (1 - sin(4*h)*cos(h² + 18))²)
b = 1 - sqrt(3 / (3 + abs(tan(a*h²) - sin(a*h))))
c = a*h²*sin(b*h) + b*h³*cos(a*h)

Если действительные корни существуют, то найти их. В противном
случае ответом должно служить сообщение, что действительных
корней нет.
"""

import math


def calculate_coefficients(h: float):
    """Вычисляет коэффициенты квадратного уравнения по заданным формулам."""
    try:
        # a
        denominator_a = (1 - math.sin(4 * h) * math.cos(h**2 + 18)) ** 2
        if denominator_a == 0:
            return None, None, None

        a = math.sqrt(abs(math.sin(8 * h) + 17) / denominator_a)

        # b
        denominator_b = 3 + abs(math.tan(a * h**2) - math.sin(a * h))
        b = 1 - math.sqrt(3 / denominator_b)

        # c
        c = a * h**2 * math.sin(b * h) + b * h**3 * math.cos(a * h)

        return a, b, c
    except (ValueError, ZeroDivisionError):
        return None, None, None


def solve_quadratic(a: float, b: float, c: float):
    """Решает квадратное уравнение и возвращает информацию о корнях."""
    if a == 0:
        return None, None, None, None

    d = b**2 - 4 * a * c

    if d < 0:
        return False, d, None, None
    elif d == 0:
        x = -b / (2 * a)
        return True, d, x, x
    else:
        sqrt_d = math.sqrt(d)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        return True, d, x1, x2


def main():
    """Основная функция программы."""
    print("Проверка существования действительных корней уравнения a*x² + b*x + c = 0")
    print("=" * 70)

    try:
        h = float(input("Введите значение h: "))
        print("=" * 70)

        a, b, c = calculate_coefficients(h)
        if a is None:
            print("Ошибка: невозможно вычислить коэффициенты.")
            print("(деление на ноль или извлечение корня из отрицательного числа)")
            return

        print(f"a = {a:.6f}")
        print(f"b = {b:.6f}")
        print(f"c = {c:.6f}")
        print("-" * 70)

        equation = f"{a:.4f}x²"
        equation += f" {'+' if b >= 0 else '-'} {abs(b):.4f}x"
        equation += f" {'+' if c >= 0 else '-'} {abs(c):.4f} = 0"
        print(f"Уравнение: {equation}")
        print("-" * 70)

        has_roots, d, x1, x2 = solve_quadratic(a, b, c)

        if has_roots is None:
            print("Ошибка: a = 0, уравнение не является квадратным.")
            return

        print(f"Дискриминант D = {d:.6f}")
        print("-" * 70)

        if has_roots:
            print("✓ Уравнение имеет действительные корни.")
            if x1 == x2:
                print(f"Один корень: x = {x1:.6f}")
            else:
                print(f"x₁ = {x1:.6f}")
                print(f"x₂ = {x2:.6f}")
        else:
            print("✗ Уравнение не имеет действительных корней (D < 0).")

        print("=" * 70)

    except ValueError:
        print("Ошибка: необходимо вводить число!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()

input("\nНажмите Enter, чтобы завершить программу.")
