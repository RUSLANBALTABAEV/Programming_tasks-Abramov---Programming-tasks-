"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
2. Разветвления
53. Даны действительные числа a, b, c, d, e, f, g, h. Известно, что
точки (e, f) и (g, h) различны. Известно также, что точки (a, b) и (c, d)
не лежат на прямой l, проходящей через точки (e, f) и (g, h). Прямая l
разбивает координатную плоскость на две полуплоскости. Выяснить,
верно ли, что точки (a, b) и (c, d) принадлежат одной и той же
полуплоскости*). *) В этой задаче, как и в ряде следующих задач, надо воспользоваться
тем, что уравнением прямой, проходящей через две различные точки
(e, f) и (g, h), является уравнение

(x - e)(h - f)-(y - f)(g - e) = 0.
"""


def calculate_line_equation_coefficients(e, f, g, h):
    """
    Вычисляет коэффициенты уравнения прямой через две точки.
    
    Уравнение: (x - e)(h - f) - (y - f)(g - e) = 0
    Раскрываем: (h-f)x - (g-e)y + [(g-e)f - (h-f)e] = 0
    Форма: Ax + By + C = 0
    
    Args:
        e, f: Координаты первой точки
        g, h: Координаты второй точки
    
    Returns:
        tuple: (A, B, C) - коэффициенты уравнения прямой
    """
    A = h - f
    B = -(g - e)
    C = (g - e) * f - (h - f) * e
    
    return A, B, C


def evaluate_point_on_line(A, B, C, x, y):
    """
    Вычисляет значение Ax + By + C для точки (x, y).
    
    Args:
        A, B, C: Коэффициенты уравнения прямой
        x, y: Координаты точки
    
    Returns:
        float: Значение Ax + By + C
    """
    return A * x + B * y + C


def points_on_same_side(e, f, g, h, a, b, c, d):
    """
    Определяет, принадлежат ли точки (a, b) и (c, d) одной полуплоскости.
    
    Args:
        e, f: Координаты первой точки прямой
        g, h: Координаты второй точки прямой
        a, b: Координаты первой проверяемой точки
        c, d: Координаты второй проверяемой точки
    
    Returns:
        tuple: (same_side, value1, value2, A, B, C)
    """
    # Проверяем, что точки (e, f) и (g, h) различны
    if e == g and f == h:
        return None, None, None, None, None, None
    
    # Получаем коэффициенты уравнения прямой
    A, B, C = calculate_line_equation_coefficients(e, f, g, h)
    
    # Вычисляем значения для обеих точек
    value1 = evaluate_point_on_line(A, B, C, a, b)
    value2 = evaluate_point_on_line(A, B, C, c, d)
    
    # Точки на одной стороне, если произведение положительно
    same_side = value1 * value2 > 0
    
    return same_side, value1, value2, A, B, C


def main():
    """Основная функция программы."""
    print("Определение положения точек относительно прямой")
    print("через две заданные точки")
    print("=" * 75)
    
    try:
        # Ввод координат точек, определяющих прямую
        print("Введите координаты точек, через которые проходит прямая l:")
        print("Первая точка (e, f):")
        e = float(input("  e = "))
        f = float(input("  f = "))
        
        print("Вторая точка (g, h):")
        g = float(input("  g = "))
        h = float(input("  h = "))
        
        # Проверка, что точки различны
        if e == g and f == h:
            print("Ошибка: точки (e, f) и (g, h) должны быть различны!")
            return
        
        print()
        
        # Ввод проверяемых точек
        print("Введите координаты проверяемых точек:")
        print("Первая точка (a, b):")
        a = float(input("  a = "))
        b = float(input("  b = "))
        
        print("Вторая точка (c, d):")
        c = float(input("  c = "))
        d = float(input("  d = "))
        
        # Проверка, что точки не лежат на прямой
        print()
        print("Проверка условий:")
        if (a == e and b == f) or (a == g and b == h):
            print("⚠ Точка (a, b) совпадает с одной из точек прямой!")
            return
        if (c == e and d == f) or (c == g and d == h):
            print("⚠ Точка (c, d) совпадает с одной из точек прямой!")
            return
        
        print("=" * 75)
        
        # Выводим данные
        print(f"Прямая l проходит через точки:")
        print(f"  P₁ = ({e}, {f})")
        print(f"  P₂ = ({g}, {h})")
        print()
        print(f"Проверяемые точки:")
        print(f"  A = ({a}, {b})")
        print(f"  B = ({c}, {d})")
        print("-" * 75)
        
        # Определяем положение точек
        result = points_on_same_side(e, f, g, h, a, b, c, d)
        same_side, value1, value2, A, B, C = result
        
        if same_side is None:
            print("Ошибка в вычислениях!")
            return
        
        # Выводим уравнение прямой
        print("Уравнение прямой l через точки P₁ и P₂:")
        print(f"  (x - {e})(h - f) - (y - {f})(g - e) = 0")
        print(f"  (x - {e})({h} - {f}) - (y - {f})({g} - {e}) = 0")
        print(f"  (x - {e})·{h - f} - (y - {f})·{g - e} = 0")
        print()
        
        # Стандартная форма
        line_eq = ""
        if A != 0:
            if A == 1:
                line_eq += "x"
            elif A == -1:
                line_eq += "-x"
            else:
                line_eq += f"{A}x"
        
        if B != 0:
            if line_eq:
                if B > 0:
                    if B == 1:
                        line_eq += " + y"
                    else:
                        line_eq += f" + {B}y"
                else:
                    if B == -1:
                        line_eq += " - y"
                    else:
                        line_eq += f" - {abs(B)}y"
            else:
                if B == 1:
                    line_eq += "y"
                elif B == -1:
                    line_eq += "-y"
                else:
                    line_eq += f"{B}y"
        
        if C != 0:
            if C > 0:
                line_eq += f" + {C}"
            else:
                line_eq += f" - {abs(C)}"
        
        line_eq += " = 0"
        print(f"Стандартная форма: {line_eq}")
        print("-" * 75)
        
        # Подстановка точек
        print("Подстановка точек в уравнение:")
        print(f"  Для точки A({a}, {b}): "
              f"{A}·{a} + {B}·{b} + {C} = {value1:.6f}")
        print(f"  Для точки B({c}, {d}): "
              f"{A}·{c} + {B}·{d} + {C} = {value2:.6f}")
        print("-" * 75)
        
        # Анализ положения точек
        if value1 == 0:
            print(f"⚠ Точка A лежит НА прямой l")
        elif value1 > 0:
            print(f"Точка A: значение положительно ({value1:.6f} > 0)")
        else:
            print(f"Точка A: значение отрицательно ({value1:.6f} < 0)")
        
        if value2 == 0:
            print(f"⚠ Точка B лежит НА прямой l")
        elif value2 > 0:
            print(f"Точка B: значение положительно ({value2:.6f} > 0)")
        else:
            print(f"Точка B: значение отрицательно ({value2:.6f} < 0)")
        
        print("-" * 75)
        
        # Проверка на прямой
        if value1 == 0 or value2 == 0:
            print("⚠ Одна или обе точки лежат на прямой")
            print("  Условие задачи нарушено!")
        else:
            # Результат
            product = value1 * value2
            print(f"Произведение значений: "
                  f"{value1:.6f} × {value2:.6f} = {product:.6f}")
            print()
            
            if same_side:
                print("✓ Точки принадлежат ОДНОЙ И ТОЙ ЖЕ полуплоскости")
                print("  (произведение положительно, знаки одинаковы)")
            else:
                print("✗ Точки принадлежат РАЗНЫМ полуплоскостям")
                print("  (произведение отрицательно, знаки различны)")
        
        print("=" * 75)
        
    except ValueError:
        print("Ошибка: необходимо вводить числа!")


if __name__ == "__main__":
    main()

input("\nНажмите Enter, чтобы завершить программу.")
