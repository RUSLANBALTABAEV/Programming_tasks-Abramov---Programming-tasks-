"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
2. Разветвления
58. Дано действительное число a. Для функций f(x), графики
которых представлены на рис. 1,a - 1,г, вычислить f(a).
"""


def function_a(x):
    """
    Функция а): кусочно-заданная функция из двух ветвей
    y = -x     при x < 0
    y = -x²    при x ≥ 0
    
    Args:
        x (float): Аргумент функции
    
    Returns:
        float: Значение функции
    """
    if x < 0:
        return -x
    else:
        return -x ** 2


def function_b(x):
    """
    Функция б): кусочно-заданная функция из трех частей
    y = 1/x²   при x < 0
    y = 1      при x = 0 (разрыв, но доопределим как 1)
    y = x²     при 0 < x ≤ 2
    y = 4      при x > 2
    
    Args:
        x (float): Аргумент функции
    
    Returns:
        float: Значение функции
    """
    if x < 0:
        return 1 / (x ** 2)
    elif x == 0:
        # В точке x=0 функция имеет разрыв, график показывает значение 1
        return 1
    elif 0 < x <= 2:
        return x ** 2
    else:  # x > 2
        return 4


def function_c(x):
    """
    Функция в): периодическая функция (зигзаг)
    На отрезке [-2, 2] имеет вид |x| с периодом 2
    y = |x + 2k| для x ∈ [-1+2k, 1+2k], где k - целое
    
    Упрощенная версия для основного периода [-2, 2]:
    y = |x|     при -1 ≤ x ≤ 1
    с периодичностью 2
    
    Args:
        x (float): Аргумент функции
    
    Returns:
        float: Значение функции
    """
    # Приводим x к основному периоду [-1, 1]
    # Период = 2
    x_mod = ((x + 1) % 2) - 1
    return abs(x_mod)


def function_d(x):
    """
    Функция г): кусочно-линейная функция
    y = 1      при x ≤ 0
    y = 1 - x  при 0 < x ≤ 1
    y = 0      при 1 < x ≤ 2
    y = x - 3  при 2 < x ≤ 3
    y = 0      при x > 3 (или продолжение)
    
    Args:
        x (float): Аргумент функции
    
    Returns:
        float: Значение функции
    """
    if x <= 0:
        return 1
    elif 0 < x <= 1:
        return 1 - x
    elif 1 < x <= 2:
        return 0
    elif 2 < x <= 3:
        return x - 3
    else:  # x > 3
        return 0


def describe_function(variant):
    """Возвращает описание функции для выбранного варианта."""
    descriptions = {
        'a': [
            "График а):",
            "  y = -x     при x < 0  (прямая с наклоном -1)",
            "  y = -x²    при x ≥ 0  (парабола, ветви вниз)"
        ],
        'b': [
            "График б):",
            "  y = 1/x²   при x < 0  (гипербола)",
            "  y = x²     при 0 < x ≤ 2  (парабола)",
            "  y = 4      при x > 2  (горизонтальная прямая)"
        ],
        'c': [
            "График в):",
            "  Периодическая функция с периодом 2",
            "  Зигзагообразная функция (модуль с периодом)"
        ],
        'd': [
            "График г):",
            "  y = 1      при x ≤ 0",
            "  y = 1 - x  при 0 < x ≤ 1",
            "  y = 0      при 1 < x ≤ 2",
            "  y = x - 3  при 2 < x ≤ 3"
        ]
    }
    return descriptions.get(variant, [])


def main():
    """Основная функция программы."""
    print("Вычисление значений функций по графикам")
    print("=" * 75)
    
    print("Доступные варианты функций:")
    print("  а) Комбинация прямой и параболы")
    print("  б) Гипербола и парабола с постоянной частью")
    print("  в) Периодическая зигзагообразная функция")
    print("  г) Кусочно-линейная функция")
    print()
    
    variant = input("Выберите вариант (а, б, в, г): ").lower().strip()
    
    # Приводим к латинским буквам
    variant_map = {'а': 'a', 'б': 'b', 'в': 'c', 'г': 'd'}
    if variant in variant_map:
        variant = variant_map[variant]
    
    if variant not in ['a', 'b', 'c', 'd']:
        print("Ошибка: неверный вариант!")
        return
    
    print("=" * 75)
    
    try:
        # Ввод значения a
        a = float(input("Введите значение a: "))
        
        print("=" * 75)
        
        # Выводим описание функции
        description = describe_function(variant)
        for line in description:
            print(line)
        
        print("-" * 75)
        
        # Вычисляем значение функции
        functions = {
            'a': function_a,
            'b': function_b,
            'c': function_c,
            'd': function_d
        }
        
        result = functions[variant](a)
        
        # Выводим детальную информацию о вычислении
        print(f"Вычисление для x = {a}:")
        print()
        
        if variant == 'a':
            if a < 0:
                print(f"  Условие: x < 0 ({a} < 0)")
                print(f"  Используется формула: y = -x")
                print(f"  f({a}) = -({a}) = {result}")
            else:
                print(f"  Условие: x ≥ 0 ({a} ≥ 0)")
                print(f"  Используется формула: y = -x²")
                print(f"  f({a}) = -({a})² = {result}")
        
        elif variant == 'b':
            if a < 0:
                print(f"  Условие: x < 0 ({a} < 0)")
                print(f"  Используется формула: y = 1/x²")
                print(f"  f({a}) = 1/({a})² = {result}")
            elif a == 0:
                print(f"  Условие: x = 0")
                print(f"  По графику: y = 1 (точка разрыва)")
                print(f"  f({a}) = {result}")
            elif 0 < a <= 2:
                print(f"  Условие: 0 < x ≤ 2 ({a} ∈ (0, 2])")
                print(f"  Используется формула: y = x²")
                print(f"  f({a}) = ({a})² = {result}")
            else:
                print(f"  Условие: x > 2 ({a} > 2)")
                print(f"  Используется формула: y = 4")
                print(f"  f({a}) = {result}")
        
        elif variant == 'c':
            print(f"  Периодическая функция с периодом 2")
            print(f"  f({a}) = {result}")
        
        elif variant == 'd':
            if a <= 0:
                print(f"  Условие: x ≤ 0 ({a} ≤ 0)")
                print(f"  Используется формула: y = 1")
                print(f"  f({a}) = {result}")
            elif 0 < a <= 1:
                print(f"  Условие: 0 < x ≤ 1 ({a} ∈ (0, 1])")
                print(f"  Используется формула: y = 1 - x")
                print(f"  f({a}) = 1 - {a} = {result}")
            elif 1 < a <= 2:
                print(f"  Условие: 1 < x ≤ 2 ({a} ∈ (1, 2])")
                print(f"  Используется формула: y = 0")
                print(f"  f({a}) = {result}")
            elif 2 < a <= 3:
                print(f"  Условие: 2 < x ≤ 3 ({a} ∈ (2, 3])")
                print(f"  Используется формула: y = x - 3")
                print(f"  f({a}) = {a} - 3 = {result}")
            else:
                print(f"  Условие: x > 3 ({a} > 3)")
                print(f"  f({a}) = {result}")
        
        print("-" * 75)
        print(f"ОТВЕТ: f({a}) = {result:.6f}")
        print("=" * 75)
        
    except ValueError as e:
        if "could not convert" in str(e):
            print("Ошибка: необходимо вводить число!")
        else:
            print(f"Ошибка вычисления: {e}")
    except ZeroDivisionError:
        print("Ошибка: деление на ноль!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()

input("\nНажмите Enter, чтобы завершить программу.")
