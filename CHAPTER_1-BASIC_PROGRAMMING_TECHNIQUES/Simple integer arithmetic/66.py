"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
3. Простейшая целочисленная арифметика
66. Даны целые числа k, m и действительные числа x, y, z.
Если k < m², k = m² или k > m², то соответственно:
— заменить модулем x, y или z;
— два других значения уменьшить на 0.5.
"""


def modify_values(k: int, m: int, x: float, y: float, z: float) -> tuple[float, float, float]:
    """
    Модифицирует значения x, y, z в зависимости от отношения k и m².

    Args:
        k (int): Целое число.
        m (int): Целое число.
        x (float): Действительное число.
        y (float): Действительное число.
        z (float): Действительное число.

    Returns:
        tuple[float, float, float]: Новые значения (x, y, z) после преобразования.
    """
    m_squared = m ** 2

    if k < m_squared:
        # При k < m²: берём модуль x, уменьшаем y и z на 0.5
        return abs(x), y - 0.5, z - 0.5
    elif k == m_squared:
        # При k = m²: берём модуль y, уменьшаем x и z на 0.5
        return x - 0.5, abs(y), z - 0.5
    else:  # k > m²
        # При k > m²: берём модуль z, уменьшаем x и y на 0.5
        return x - 0.5, y - 0.5, abs(z)


def main() -> None:
    """Основная функция программы."""
    try:
        print("Введите целые числа k и m:")
        k = int(input("k = ").strip())
        m = int(input("m = ").strip())

        print("\nВведите действительные числа x, y, z:")
        x = float(input("x = ").strip())
        y = float(input("y = ").strip())
        z = float(input("z = ").strip())

        m_squared = m ** 2

        print(f"\n{'=' * 50}")
        print("Исходные данные:")
        print(f"k = {k}, m = {m}, m² = {m_squared}")
        print(f"x = {x}, y = {y}, z = {z}")
        print(f"{'=' * 50}")

        # Преобразование значений
        x_new, y_new, z_new = modify_values(k, m, x, y, z)

        # Определяем, какое условие сработало
        if k < m_squared:
            cond = f"k < m² ({k} < {m_squared})"
            action = "|x|, y-0.5, z-0.5"
        elif k == m_squared:
            cond = f"k = m² ({k} = {m_squared})"
            action = "x-0.5, |y|, z-0.5"
        else:
            cond = f"k > m² ({k} > {m_squared})"
            action = "x-0.5, y-0.5, |z|"

        print(f"\nУсловие: {cond}")
        print(f"Действие: {action}")
        print("\nПреобразованные значения:")
        print(f"x = {x_new}")
        print(f"y = {y_new}")
        print(f"z = {z_new}")

        # Примеры
        print(f"\n{'=' * 50}")
        print("--- Примеры ---")
        test_cases = [
            (10, 4, 3.5, -2.1, 1.2),   # k < m²: 10 < 16
            (16, 4, 3.5, -2.1, 1.2),   # k = m²: 16 = 16
            (20, 4, 3.5, -2.1, 1.2),   # k > m²: 20 > 16
        ]

        for k_val, m_val, x_val, y_val, z_val in test_cases:
            x_mod, y_mod, z_mod = modify_values(k_val, m_val, x_val, y_val, z_val)
            relation = "<" if k_val < m_val ** 2 else "=" if k_val == m_val ** 2 else ">"
            print(f"\nk={k_val}, m={m_val} (k {relation} m²={m_val ** 2})")
            print(f"({x_val}, {y_val}, {z_val}) → ({x_mod}, {y_mod}, {z_mod})")

    except ValueError:
        print("Ошибка: необходимо вводить числовые значения.")

    input("\nНажмите Enter, чтобы завершить программу.")


if __name__ == "__main__":
    main()
