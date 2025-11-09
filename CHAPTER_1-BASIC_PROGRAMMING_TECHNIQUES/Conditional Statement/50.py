"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
2. Разветвления
50. Даны действительные числа a1, b1, c1, a2, b2, c2.
Выяснить, верно ли, что |a1 * b2 - a2 * b1| >= 0.0001, и если верно,
то найти решение системы линейных уравнений:

    a1 * x + b1 * y + c1 = 0
    a2 * x + b2 * y + c2 = 0

(при выполнении выписанного неравенства система заведомо
совместна и имеет единственное решение).
"""


def calculate_determinant(a1, b1, a2, b2):
    """Вычисляет главный определитель системы."""
    return a1 * b2 - a2 * b1


def solve_linear_system(a1, b1, c1, a2, b2, c2):
    """
    Решает систему линейных уравнений методом Крамера.

    Args:
        a1, b1, c1: Коэффициенты первого уравнения
        a2, b2, c2: Коэффициенты второго уравнения

    Returns:
        tuple: (has_solution, x, y, determinant)
            has_solution (bool): есть ли единственное решение
            x, y (float | None): координаты решения
            determinant (float): главный определитель
    """
    det = calculate_determinant(a1, b1, a2, b2)

    if abs(det) < 0.0001:
        return False, None, None, det

    # Метод Крамера
    det_x = calculate_determinant(-c1, b1, -c2, b2)
    det_y = calculate_determinant(a1, -c1, a2, -c2)

    x = det_x / det
    y = det_y / det

    return True, x, y, det


def format_equation(a, b, c):
    """Возвращает аккуратно отформатированное уравнение."""
    sign_b = '+' if b >= 0 else '-'
    sign_c = '+' if c >= 0 else '-'
    return f"{a:.4f}x {sign_b} {abs(b):.4f}y {sign_c} {abs(c):.4f} = 0"


def main():
    """Основная функция программы."""
    print("РЕШЕНИЕ СИСТЕМЫ ЛИНЕЙНЫХ УРАВНЕНИЙ")
    print("a₁x + b₁y + c₁ = 0")
    print("a₂x + b₂y + c₂ = 0")
    print("=" * 70)

    try:
        # Ввод коэффициентов
        print("Коэффициенты первого уравнения:")
        a1 = float(input("  Введите a₁: "))
        b1 = float(input("  Введите b₁: "))
        c1 = float(input("  Введите c₁: "))

        print("\nКоэффициенты второго уравнения:")
        a2 = float(input("  Введите a₂: "))
        b2 = float(input("  Введите b₂: "))
        c2 = float(input("  Введите c₂: "))

        print("=" * 70)
        print("Система уравнений:")
        print(" ", format_equation(a1, b1, c1))
        print(" ", format_equation(a2, b2, c2))
        print("-" * 70)

        has_solution, x, y, det = solve_linear_system(a1, b1, c1, a2, b2, c2)

        print(f"Главный определитель: D = a₁b₂ - a₂b₁ = {det:.6f}")
        print(f"Модуль определителя: |D| = {abs(det):.6f}")
        print("-" * 70)

        if abs(det) >= 0.0001:
            print(f"✓ Условие |D| ≥ 0.0001 выполняется "
                  f"({abs(det):.6f} ≥ 0.0001)")
        else:
            print(f"✗ Условие |D| ≥ 0.0001 НЕ выполняется "
                  f"({abs(det):.6f} < 0.0001)")
        print("-" * 70)

        if has_solution:
            print("✓ Система имеет ЕДИНСТВЕННОЕ решение:")
            print(f"  x = {x:.6f}")
            print(f"  y = {y:.6f}")
            print()
            # Проверка решения
            check1 = a1 * x + b1 * y + c1
            check2 = a2 * x + b2 * y + c2
            print("Проверка подстановкой:")
            print(f"  a₁x + b₁y + c₁ = {check1:.6f}")
            print(f"  a₂x + b₂y + c₂ = {check2:.6f}")
        else:
            print("✗ Система НЕ имеет единственного решения.")
            print("  Возможные варианты:")
            print("  • Уравнения параллельны (нет решений)")
            print("  • Уравнения совпадают (бесконечно много решений)")

        print("=" * 70)

    except ValueError:
        print("Ошибка: необходимо вводить числа!")
    except ZeroDivisionError:
        print("Ошибка: деление на ноль!")
    except Exception as exc:
        print(f"Произошла непредвиденная ошибка: {exc}")


if __name__ == "__main__":
    main()

input("\nНажмите Enter, чтобы завершить программу.")
