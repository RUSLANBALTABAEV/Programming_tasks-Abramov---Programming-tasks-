"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
4. Простейшие циклы

82. Дано действительное число х. Вычислить

(x-2)(x-4)(x-8)...(x-64) / (x-1)(x-3)(x-7)...(x-63)

Числитель: произведение (x - 2^k) для k = 1, 2, 3, 4, 5, 6
Знаменатель: произведение (x - (2^k - 1)) для k = 1, 2, 3, 4, 5, 6
"""


def calculate_fraction(x):
    """
    Вычисляет дробь (x-2)(x-4)(x-8)(x-16)(x-32)(x-64) / (x-1)(x-3)(x-7)(x-15)(x-31)(x-63)
    """
    # Числитель: x-2, x-4, x-8, x-16, x-32, x-64
    numerator = 1
    for k in range(1, 7):
        power = 2 ** k
        numerator *= (x - power)
    
    # Знаменатель: x-1, x-3, x-7, x-15, x-31, x-63
    denominator = 1
    for k in range(1, 7):
        value = 2 ** k - 1
        denominator *= (x - value)
    
    if abs(denominator) < 1e-15:
        return None  # Деление на ноль
    
    return numerator / denominator


def calculate_fraction_detailed(x):
    """
    Вычисляет дробь с детальным выводом
    """
    print(f"Вычисление для x = {x}\n")
    
    # Числитель
    print("Числитель: (x-2)(x-4)(x-8)(x-16)(x-32)(x-64)")
    print(f"{'k':>2} | {'2^k':>4} | {'x - 2^k':>15} | {'Произведение':>20}")
    print("-" * 60)
    
    numerator = 1
    for k in range(1, 7):
        power = 2 ** k
        term = x - power
        numerator *= term
        print(f"{k:2d} | {power:4d} | {term:15.6f} | {numerator:20.6f}")
    
    print(f"\nЧислитель = {numerator:.15f}\n")
    
    # Знаменатель
    print("Знаменатель: (x-1)(x-3)(x-7)(x-15)(x-31)(x-63)")
    print(f"{'k':>2} | {'2^k-1':>5} | {'x - (2^k-1)':>15} | {'Произведение':>20}")
    print("-" * 60)
    
    denominator = 1
    for k in range(1, 7):
        value = 2 ** k - 1
        term = x - value
        denominator *= term
        print(f"{k:2d} | {value:5d} | {term:15.6f} | {denominator:20.6f}")
    
    print(f"\nЗнаменатель = {denominator:.15f}\n")
    
    # Результат
    if abs(denominator) < 1e-15:
        print("ОШИБКА: Деление на ноль!")
        return None
    
    result = numerator / denominator
    print(f"{'='*60}")
    print(f"Результат: {numerator:.6f} / {denominator:.6f} = {result:.15f}")
    
    return result


# ==================== ВВОД ДАННЫХ ====================

print("Введите действительное число x:")
x = float(input("x = "))

print(f"\n{'='*70}")
print(f"Вычисление дроби для x = {x}")
print(f"{'='*70}\n")

# Основное вычисление
result = calculate_fraction(x)

if result is not None:
    print(f"Результат: {result:.15f}")
    print(f"В научной нотации: {result:.6e}\n")
    
    # Детальное вычисление
    print(f"{'='*70}")
    print("--- Детальное вычисление ---\n")
    result_detailed = calculate_fraction_detailed(x)
else:
    print("ОШИБКА: Деление на ноль!")
    print("x не должно быть равно 1, 3, 7, 15, 31 или 63")


# ==================== СТРУКТУРА ВЫРАЖЕНИЯ ====================

print(f"\n{'='*70}")
print("--- Структура выражения ---\n")

print("Числитель содержит множители:")
for k in range(1, 7):
    power = 2 ** k
    print(f"  k={k}: x - {power}")

print("\nЗнаменатель содержит множители:")
for k in range(1, 7):
    value = 2 ** k - 1
    print(f"  k={k}: x - {value}")

print("\nЗамечание: 2^k - 1 = числа Мерсенна (кроме простых)")


# ==================== ПРИМЕРЫ ====================

print(f"\n{'='*70}")
print("--- Примеры для разных значений x ---\n")

test_values = [0, 5, 10, 50, 100, -10, 0.5, 2.5]

print(f"{'x':>8} | {'Числитель':>20} | {'Знаменатель':>20} | {'Результат':>20}")
print("-" * 80)

for x_test in test_values:
    result_test = calculate_fraction(x_test)
    
    # Вычисляем числитель и знаменатель отдельно
    num = 1
    for k in range(1, 7):
        num *= (x_test - 2**k)
    
    den = 1
    for k in range(1, 7):
        den *= (x_test - (2**k - 1))
    
    if result_test is not None:
        print(f"{x_test:8.2f} | {num:20.2f} | {den:20.2f} | {result_test:20.6f}")
    else:
        print(f"{x_test:8.2f} | {num:20.2f} | {den:20.2f} | {'Деление на 0':>20}")


# ==================== ОСОБЫЕ ТОЧКИ ====================

print(f"\n{'='*70}")
print("--- Особые точки (где знаменатель = 0) ---\n")

special_points = [2**k - 1 for k in range(1, 7)]
print("Знаменатель обращается в ноль при x =", special_points)
print("То есть при x = 1, 3, 7, 15, 31, 63")

print("\nЧислитель обращается в ноль при x =", [2**k for k in range(1, 7)])
print("То есть при x = 2, 4, 8, 16, 32, 64")


# ==================== ПОВЕДЕНИЕ ФУНКЦИИ ====================

print(f"\n{'='*70}")
print("--- Поведение функции в разных диапазонах ---\n")

ranges = [
    ("x < 1", 0),
    ("1 < x < 2", 1.5),
    ("2 < x < 3", 2.5),
    ("3 < x < 4", 3.5),
    ("x > 64", 100),
]

print(f"{'Диапазон':>15} | {'x (тестовое)':>15} | {'Результат':>20}")
print("-" * 60)

for range_name, x_test in ranges:
    result_test = calculate_fraction(x_test)
    if result_test is not None:
        print(f"{range_name:>15} | {x_test:15.2f} | {result_test:20.6f}")
    else:
        print(f"{range_name:>15} | {x_test:15.2f} | {'Деление на 0':>20}")


# ==================== АНАЛИЗ ЗНАКОВ ====================

print(f"\n{'='*70}")
print("--- Анализ знаков множителей ---\n")

x_analyze = 10
print(f"Для x = {x_analyze}:\n")

print("Числитель:")
for k in range(1, 7):
    power = 2 ** k
    term = x_analyze - power
    sign = "+" if term > 0 else "-"
    print(f"  x - {power:2d} = {term:6.1f} ({sign})")

print("\nЗнаменатель:")
for k in range(1, 7):
    value = 2 ** k - 1
    term = x_analyze - value
    sign = "+" if term > 0 else "-"
    print(f"  x - {value:2d} = {term:6.1f} ({sign})")


# ==================== АСИМПТОТИКА ====================

print(f"\n{'='*70}")
print("--- Асимптотическое поведение ---\n")

print("При x → ∞:")
print("  Числитель ≈ x^6")
print("  Знаменатель ≈ x^6")
print("  Дробь → 1\n")

print("Проверка для больших x:")
for x_large in [100, 1000, 10000]:
    result_large = calculate_fraction(x_large)
    print(f"  x = {x_large:5d}: результат = {result_large:.10f}")

input("\nНажмите Enter, чтобы завершить программу.")
