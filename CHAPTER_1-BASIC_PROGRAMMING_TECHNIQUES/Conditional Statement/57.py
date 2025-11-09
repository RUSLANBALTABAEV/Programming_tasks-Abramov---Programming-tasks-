"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
2. Разветвления
57. Дано действительное число a. Вычислить f(a), если
а) f(x) = x ** 2 при -2<=x<2,
   f(x) = 4 в противном случае;
б) f(x) = x ** 2 + 4 * x + 5 при x <= 2,
   f(x) = 1 / (x ** 2 + 4 * x + 5) в противном случае;
в) f(x) = 0 при x <= 0,
   f(x) = x при 0<x<=1,
   f(x) = x ** 4 в остальных случаях;
г) f(x) = 0 при x <= 0,
   f(x) = x ** 2 - x при 0 < x <= 1,
   f(x) = x ** 2 - sin(pi * x ** 2) в остальных случаях.
"""

import math


def function_a(x):
    """
    Вычисляет f(x) для варианта а):
    f(x) = x²     при -2 ≤ x < 2
    f(x) = 4      в противном случае
    
    Args:
        x (float): Аргумент функции
    
    Returns:
        float: Значение функции
    """
    if -2 <= x < 2:
        return x ** 2
    else:
        return 4


def function_b(x):
    """
    Вычисляет f(x) для варианта б):
    f(x) = x² + 4x + 5           при x ≤ 2
    f(x) = 1 / (x² + 4x + 5)     в противном случае
    
    Args:
        x (float): Аргумент функции
    
    Returns:
        float: Значение функции
    """
    if x <= 2:
        return x ** 2 + 4 * x + 5
    else:
        denominator = x ** 2 + 4 * x + 5
        if denominator == 0:
            raise ValueError("Деление на ноль")
        return 1 / denominator


def function_c(x):
    """
    Вычисляет f(x) для варианта в):
    f(x) = 0      при x ≤ 0
    f(x) = x      при 0 < x ≤ 1
    f(x) = x⁴     в остальных случаях
    
    Args:
        x (float): Аргумент функции
    
    Returns:
        float: Значение функции
    """
    if x <= 0:
        return 0
    elif 0 < x <= 1:
        return x
    else:
        return x ** 4


def function_d(x):
    """
    Вычисляет f(x) для варианта г):
    f(x) = 0                при x ≤ 0
    f(x) = x² - x           при 0 < x ≤ 1
    f(x) = x² - sin(πx²)    в остальных случаях
    
    Args:
        x (float): Аргумент функции
    
    Returns:
        float: Значение функции
    """
    if x <= 0:
        return 0
    elif 0 < x <= 1:
        return x ** 2 - x
    else:
        return x ** 2 - math.sin(math.pi * x ** 2)


def print_function_formula(variant):
    """Выводит формулу для выбранного варианта функции."""
    formulas = {
        'a': [
            "f(x) = x²     при -2 ≤ x < 2",
            "f(x) = 4      в противном случае"
        ],
        'b': [
            "f(x) = x² + 4x + 5         при x ≤ 2",
            "f(x) = 1 / (x² + 4x + 5)   в противном случае"
        ],
        'c': [
            "f(x) = 0      при x ≤ 0",
            "f(x) = x      при 0 < x ≤ 1",
            "f(x) = x⁴     в остальных случаях"
        ],
        'd': [
            "f(x) = 0                при x ≤ 0",
            "f(x) = x² - x           при 0 < x ≤ 1",
            "f(x) = x² - sin(πx²)    в остальных случаях"
        ]
    }
    
    print("Формула функции:")
    for line in formulas[variant]:
        print(f"  {line}")


def main():
    """Основная функция программы."""
    print("Вычисление кусочно-заданных функций")
    print("=" * 75)
    
    # Выбор варианта
    print("Выберите вариант функции:")
    print("  а) f(x) = {x² при -2≤x<2; 4 в противном случае}")
    print("  б) f(x) = {x²+4x+5 при x≤2; 1/(x²+4x+5) в противном случае}")
    print("  в) f(x) = {0 при x≤0; x при 0<x≤1; x⁴ в остальных случаях}")
    print("  г) f(x) = {0 при x≤0; x²-x при 0<x≤1; x²-sin(πx²) в остальных}")
    print()
    
    variant = input("Введите вариант (а, б, в, г): ").lower().strip()
    
    if variant not in ['а', 'б', 'в', 'г', 'a', 'b', 'c', 'd']:
        print("Ошибка: неверный вариант!")
        return
    
    # Приводим к латинским буквам
    variant_map = {'а': 'a', 'б': 'b', 'в': 'c', 'г': 'd'}
    if variant in variant_map:
        variant = variant_map[variant]
    
    print("=" * 75)
    
    try:
        # Ввод значения a
        a = float(input("Введите значение a: "))
        
        print("=" * 75)
        
        # Выводим формулу
        print_function_formula(variant)
        print("-" * 75)
        
        # Вычисляем значение функции
        functions = {
            'a': function_a,
            'b': function_b,
            'c': function_c,
            'd': function_d
        }
        
        result = functions[variant](a)
        
        # Определяем, какое условие выполнилось
        condition_info = ""
        if variant == 'a':
            if -2 <= a < 2:
                condition_info = f"Условие: -2 ≤ {a} < 2 выполняется → f({a}) = {a}² = {result}"
            else:
                condition_info = f"Условие: {a} ∉ [-2, 2) → f({a}) = 4"
        
        elif variant == 'b':
            if a <= 2:
                condition_info = (f"Условие: {a} ≤ 2 выполняется → "
                                f"f({a}) = {a}² + 4·{a} + 5 = {result}")
            else:
                denominator = a ** 2 + 4 * a + 5
                condition_info = (f"Условие: {a} > 2 → "
                                f"f({a}) = 1 / ({a}² + 4·{a} + 5) = 1 / {denominator} = {result}")
        
        elif variant == 'c':
            if a <= 0:
                condition_info = f"Условие: {a} ≤ 0 выполняется → f({a}) = 0"
            elif 0 < a <= 1:
                condition_info = f"Условие: 0 < {a} ≤ 1 выполняется → f({a}) = {a}"
            else:
                condition_info = f"Условие: {a} > 1 → f({a}) = {a}⁴ = {result}"
        
        elif variant == 'd':
            if a <= 0:
                condition_info = f"Условие: {a} ≤ 0 выполняется → f({a}) = 0"
            elif 0 < a <= 1:
                condition_info = (f"Условие: 0 < {a} ≤ 1 выполняется → "
                                f"f({a}) = {a}² - {a} = {result}")
            else:
                sin_value = math.sin(math.pi * a ** 2)
                condition_info = (f"Условие: {a} > 1 → "
                                f"f({a}) = {a}² - sin(π·{a}²) = {a**2} - {sin_value} = {result}")
        
        print(condition_info)
        print("-" * 75)
        print(f"ОТВЕТ: f({a}) = {result:.6f}")
        print("=" * 75)
        
    except ValueError as e:
        if "could not convert" in str(e):
            print("Ошибка: необходимо вводить число!")
        else:
            print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()

input("\nНажмите Enter, чтобы завершить программу.")
