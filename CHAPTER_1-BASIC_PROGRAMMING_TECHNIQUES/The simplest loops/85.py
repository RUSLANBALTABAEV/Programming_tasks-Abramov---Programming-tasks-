"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
4. Простейшие циклы

85. Даны действительные числа a, h, натуральное число n.
Вычислить
f(a) + 2 * f(a + h) + 2 * f(a + 2 * h) + ... + 2 * f(a + (n - 1) * h) + f(a + n * h),
где
f(x) = (x ** 2 + 1) * cos(x) ** 2.
"""

import math
from typing import List, Tuple


def f(x: float) -> float:
    """Вычисляет f(x) = (x² + 1) * cos²(x)."""
    return (x ** 2 + 1) * (math.cos(x)) ** 2


def calculate_sum(a: float, h: float, n: int) -> float:
    """
    Вычисляет сумму для метода трапеций.
    
    Args:
        a: Начальная точка
        h: Шаг
        n: Количество разбиений
        
    Returns:
        Сумма f(a) + 2f(a+h) + ... + f(a+nh)
    """
    result = f(a)  # Первый член
    
    # Средние члены: 2f(a+ih) для i = 1, 2, ..., n-1
    for i in range(1, n):
        result += 2 * f(a + i * h)
    
    result += f(a + n * h)  # Последний член
    
    return result


def calculate_sum_detailed(a: float, h: float, n: int) -> float:
    """
    Вычисляет сумму с детальным выводом.
    
    Args:
        a: Начальная точка
        h: Шаг
        n: Количество разбиений
        
    Returns:
        Сумма с подробным выводом вычислений
    """
    print(f"Вычисление для a = {a}, h = {h}, n = {n}\n")
    print("f(x) = (x² + 1) * cos²(x)\n")
    
    headers = ["i", "x = a+ih", "f(x)", "Коэфф", "Вклад"]
    print(f"{headers[0]:>3} | {headers[1]:>15} | {headers[2]:>20} | {headers[3]:>6} | {headers[4]:>20}")
    print("-" * 80)
    
    result = 0.0
    
    # Первый член
    x0 = a
    fx0 = f(x0)
    result += fx0
    print(f"{0:3d} | {x0:15.6f} | {fx0:20.10f} | {1:6d} | {fx0:20.10f}")
    
    # Средние члены
    for i in range(1, n):
        xi = a + i * h
        fxi = f(xi)
        contribution = 2 * fxi
        result += contribution
        print(f"{i:3d} | {xi:15.6f} | {fxi:20.10f} | {2:6d} | {contribution:20.10f}")
    
    # Последний член
    xn = a + n * h
    fxn = f(xn)
    result += fxn
    print(f"{n:3d} | {xn:15.6f} | {fxn:20.10f} | {1:6d} | {fxn:20.10f}")
    
    print(f"\n{'=' * 80}")
    print(f"Сумма = {result:.15f}")
    
    return result


def trapezoidal_integral(a: float, b: float, n: int) -> float:
    """
    Вычисляет интеграл от a до b функции f(x) методом трапеций.
    
    Args:
        a: Нижний предел интегрирования
        b: Верхний предел интегрирования
        n: Количество разбиений
        
    Returns:
        Приближенное значение интеграла
    """
    h = (b - a) / n
    sum_trapezoid = calculate_sum(a, h, n)
    return (h / 2) * sum_trapezoid


def get_user_input() -> Tuple[float, float, int]:
    """Получает и проверяет ввод пользователя."""
    print("Введите действительные числа a, h и натуральное число n:")
    
    try:
        a = float(input("a = "))
        h = float(input("h = "))
        n = int(input("n = "))
        
        if n < 1:
            raise ValueError("n должно быть натуральным числом (n ≥ 1)")
            
        return a, h, n
        
    except ValueError as e:
        print(f"Ошибка ввода: {e}")
        raise


def run_examples() -> None:
    """Запускает примеры для разных значений параметров."""
    test_cases = [
        (0.0, 0.1, 10),
        (0.0, 0.5, 10),
        (0.0, 1.0, 5),
        (1.0, 0.5, 8),
        (-1.0, 0.2, 10),
    ]
    
    print(f"{'a':>6} | {'h':>6} | {'n':>4} | {'b = a+nh':>12} | {'Сумма':>20} | {'Интеграл≈':>20}")
    print("-" * 95)
    
    for a_test, h_test, n_test in test_cases:
        sum_test = calculate_sum(a_test, h_test, n_test)
        integral_test = (h_test / 2) * sum_test
        b_test = a_test + n_test * h_test
        print(f"{a_test:6.2f} | {h_test:6.2f} | {n_test:4d} | {b_test:12.2f} | {sum_test:20.6f} | {integral_test:20.6f}")


def analyze_accuracy() -> None:
    """Анализирует точность метода трапеций."""
    a_acc = 0.0
    b_acc = math.pi
    
    print(f"{'n':>6} | {'h':>12} | {'Интеграл≈':>20} | {'Изменение':>20}")
    print("-" * 70)
    
    prev_integral = 0.0
    for n_acc in [5, 10, 20, 50, 100, 200, 500]:
        h_acc = (b_acc - a_acc) / n_acc
        integral_acc = trapezoidal_integral(a_acc, b_acc, n_acc)
        change = integral_acc - prev_integral if n_acc > 5 else 0.0
        print(f"{n_acc:6d} | {h_acc:12.6f} | {integral_acc:20.10f} | {change:20.10f}")
        prev_integral = integral_acc


def analyze_function() -> None:
    """Анализирует свойства функции f(x)."""
    print("График функции в некоторых точках:")
    print(f"{'x':>10} | {'x²+1':>12} | {'cos²x':>12} | {'f(x)':>15}")
    print("-" * 60)
    
    points = [
        (0, "0"),
        (math.pi / 6, "π/6"),
        (math.pi / 4, "π/4"),
        (math.pi / 3, "π/3"),
        (math.pi / 2, "π/2"),
        (2 * math.pi / 3, "2π/3"),
        (math.pi, "π"),
    ]
    
    for x_val, label in points:
        term1 = x_val ** 2 + 1
        term2 = math.cos(x_val) ** 2
        fx = f(x_val)
        print(f"{label:>10} | {term1:12.6f} | {term2:12.6f} | {fx:15.6f}")


def compare_methods() -> None:
    """Сравнивает разные методы численного интегрирования."""
    a_comp = 0.0
    b_comp = math.pi
    n_comp = 50
    
    # Метод трапеций
    integral_trap = trapezoidal_integral(a_comp, b_comp, n_comp)
    
    # Метод прямоугольников (левых)
    h_comp = (b_comp - a_comp) / n_comp
    integral_left = sum(f(a_comp + i * h_comp) for i in range(n_comp)) * h_comp
    
    # Метод прямоугольников (средних точек)
    integral_mid = sum(f(a_comp + (i + 0.5) * h_comp) for i in range(n_comp)) * h_comp
    
    print(f"Интеграл от {a_comp} до {b_comp:.4f} (n={n_comp}):")
    print(f"  Метод трапеций:           {integral_trap:.10f}")
    print(f"  Метод прямоугольников:    {integral_left:.10f} (левые)")
    print(f"  Метод средних точек:      {integral_mid:.10f}")


def main() -> None:
    """Основная функция программы."""
    try:
        a, h, n = get_user_input()
        
        print(f"\n{'=' * 80}")
        print(f"Вычисление суммы для a = {a}, h = {h}, n = {n}")
        print(f"{'=' * 80}\n")
        
        # Основное вычисление
        result = calculate_sum(a, h, n)
        print(f"Сумма: {result:.15f}")
        print(f"В научной нотации: {result:.6e}\n")
        
        # Интервал интегрирования
        b = a + n * h
        print(f"Интервал: [{a}, {b}]")
        print(f"Количество разбиений: {n}")
        print(f"Шаг: h = {h}\n")
        
        # Приближённое значение интеграла
        integral_value = (h / 2) * result
        print("Приближённое значение интеграла:")
        print(f"∫[{a}, {b}] f(x)dx ≈ (h/2) × сумма = {h/2} × {result:.6f} = {integral_value:.15f}\n")
        
        # Детальное вычисление (если n небольшое)
        if n <= 10:
            print(f"{'=' * 80}")
            print("--- Детальное вычисление ---\n")
            calculate_sum_detailed(a, h, n)
        
        # Дополнительные разделы
        print(f"\n{'=' * 80}")
        print("--- О формуле трапеций ---\n")
        print("Формула трапеций для численного интегрирования:")
        print("∫[a, b] f(x)dx ≈ (h/2) × [f(a) + 2f(a+h) + 2f(a+2h) + ... + 2f(a+(n-1)h) + f(a+nh)]")
        
        print(f"\n{'=' * 80}")
        print("--- Примеры для разных значений ---\n")
        run_examples()
        
        print(f"\n{'=' * 80}")
        print("--- Точность метода трапеций ---\n")
        analyze_accuracy()
        
        print(f"\n{'=' * 80}")
        print("--- Анализ функции f(x) = (x²+1)cos²x ---\n")
        analyze_function()
        
        print(f"\n{'=' * 80}")
        print("--- Сравнение методов численного интегрирования ---\n")
        compare_methods()
        
        print(f"\n{'=' * 80}")
        print("--- Интересные факты ---\n")
        print("1. Формула трапеций - один из простейших методов численного интегрирования")
        print("2. Погрешность метода: E ≤ (b-a)³ / (12n²) × max|f''(x)|")
        print("3. Коэффициенты 1, 2, 2, ..., 2, 1 соответствуют весам трапеций")
        
        input("\nНажмите Enter, чтобы завершить программу.")
        
    except ValueError:
        print("Программа завершена из-за ошибки ввода.")
    except KeyboardInterrupt:
        print("\nПрограмма прервана пользователем.")


if __name__ == "__main__":
    main()
