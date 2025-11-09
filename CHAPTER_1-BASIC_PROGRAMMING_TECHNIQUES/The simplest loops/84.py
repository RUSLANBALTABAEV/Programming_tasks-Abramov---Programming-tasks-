"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
4. Простейшие циклы

84. Даны натуральное n, действительное х. Вычислить:
а) sin x + sin² x + ... + sin^n x
б) sin x + sin x² + ... + sin x^n
в) sin x + sin(sin x) + ... + sin(sin(...sin x)) (n вложенных sin) 
"""


import math

def calculate_a(x, n):
    """
    а) Вычисляет sin x + sin² x + ... + sin^n x
    Это геометрическая прогрессия со знаменателем sin x
    """
    result = 0
    sin_x = math.sin(x)
    
    for i in range(1, n + 1):
        result += sin_x ** i
    
    return result


def calculate_b(x, n):
    """
    б) Вычисляет sin x + sin x² + ... + sin x^n
    """
    result = 0
    
    for i in range(1, n + 1):
        result += math.sin(x ** i)
    
    return result


def calculate_c(x, n):
    """
    в) Вычисляет sin x + sin(sin x) + ... + sin(sin(...sin x))
    n раз применить функцию sin
    """
    result = 0
    current = x
    
    for i in range(n):
        current = math.sin(current)
        result += current
    
    return result


def calculate_a_detailed(x, n):
    """Детальное вычисление а)"""
    print(f"а) sin x + sin² x + ... + sin^{n} x\n")
    print(f"sin({x}) = {math.sin(x):.10f}\n")
    print(f"{'i':>3} | {'sin^i x':>20} | {'Частичная сумма':>20}")
    print("-" * 50)
    
    result = 0
    sin_x = math.sin(x)
    
    for i in range(1, n + 1):
        term = sin_x ** i
        result += term
        print(f"{i:3d} | {term:20.10f} | {result:20.10f}")
    
    return result


def calculate_b_detailed(x, n):
    """Детальное вычисление б)"""
    print(f"б) sin x + sin x² + ... + sin x^{n}\n")
    print(f"{'i':>3} | {'x^i':>20} | {'sin(x^i)':>20} | {'Частичная сумма':>20}")
    print("-" * 75)
    
    result = 0
    
    for i in range(1, n + 1):
        x_power = x ** i
        term = math.sin(x_power)
        result += term
        print(f"{i:3d} | {x_power:20.10f} | {term:20.10f} | {result:20.10f}")
    
    return result


def calculate_c_detailed(x, n):
    """Детальное вычисление в)"""
    print(f"в) sin x + sin(sin x) + ... + sin(sin(...sin x)) ({n} применений sin)\n")
    print(f"{'i':>3} | {'Аргумент':>20} | {'sin(аргумент)':>20} | {'Частичная сумма':>20}")
    print("-" * 75)
    
    result = 0
    current = x
    
    for i in range(n):
        prev = current
        current = math.sin(current)
        result += current
        print(f"{i+1:3d} | {prev:20.10f} | {current:20.10f} | {result:20.10f}")
    
    return result


# ==================== ВВОД ДАННЫХ ====================

print("Введите натуральное число n и действительное число x:")
n = int(input("n = "))
x = float(input("x = "))

if n < 1:
    print("Ошибка: n должно быть натуральным числом (n ≥ 1)")
else:
    print(f"\n{'='*80}")
    print(f"Вычисление для n = {n}, x = {x}")
    print(f"{'='*80}\n")
    
    # а) sin x + sin² x + ... + sin^n x
    result_a = calculate_a(x, n)
    print(f"а) sin x + sin² x + ... + sin^{n} x = {result_a:.15f}\n")
    
    # б) sin x + sin x² + ... + sin x^n
    result_b = calculate_b(x, n)
    print(f"б) sin x + sin x² + ... + sin x^{n} = {result_b:.15f}\n")
    
    # в) sin x + sin(sin x) + ... (n раз)
    result_c = calculate_c(x, n)
    print(f"в) sin x + sin(sin x) + ... ({n} применений) = {result_c:.15f}\n")
    
    # Детальное вычисление (если n небольшое)
    if n <= 10:
        print(f"{'='*80}")
        print("--- Детальное вычисление ---\n")
        
        print(f"{'='*80}")
        result_a_det = calculate_a_detailed(x, n)
        
        print(f"\n{'='*80}")
        result_b_det = calculate_b_detailed(x, n)
        
        print(f"\n{'='*80}")
        result_c_det = calculate_c_detailed(x, n)


# ==================== ПРИМЕРЫ ====================

print(f"\n{'='*80}")
print("--- Примеры для разных значений ---\n")

test_cases = [
    (5, 1.0),
    (10, 0.5),
    (5, math.pi/6),
    (10, math.pi/4),
    (5, math.pi/2),
]

print(f"{'n':>3} | {'x':>10} | {'а) Σsin^i x':>20} | {'б) Σsin(x^i)':>20} | {'в) Σsin^(i)(x)':>20}")
print("-" * 85)

for n_test, x_test in test_cases:
    a_res = calculate_a(x_test, n_test)
    b_res = calculate_b(x_test, n_test)
    c_res = calculate_c(x_test, n_test)
    
    x_label = f"{x_test:.4f}"
    if abs(x_test - math.pi/6) < 0.001:
        x_label = "π/6"
    elif abs(x_test - math.pi/4) < 0.001:
        x_label = "π/4"
    elif abs(x_test - math.pi/2) < 0.001:
        x_label = "π/2"
    
    print(f"{n_test:3d} | {x_label:>10} | {a_res:20.10f} | {b_res:20.10f} | {c_res:20.10f}")


# ==================== АНАЛИЗ ЧАСТЕЙ ====================

print(f"\n{'='*80}")
print("--- Анализ каждой части ---\n")

print("а) sin x + sin² x + ... + sin^n x")
print("   Это геометрическая прогрессия со знаменателем q = sin x")
print("   Сумма = sin x · (1 - sin^n x) / (1 - sin x), если sin x ≠ 1")
print()

# Проверка формулы для геометрической прогрессии
x_test = 1.0
n_test = 10
sin_x = math.sin(x_test)

if abs(sin_x - 1) > 0.0001:
    # Формула для геометрической прогрессии
    geometric_sum = sin_x * (1 - sin_x ** n_test) / (1 - sin_x)
    direct_sum = calculate_a(x_test, n_test)
    
    print(f"Проверка для x={x_test}, n={n_test}:")
    print(f"  По формуле геом. прогрессии: {geometric_sum:.10f}")
    print(f"  Прямое вычисление:           {direct_sum:.10f}")
    print(f"  Разница:                     {abs(geometric_sum - direct_sum):.15e}")
    print()

print("б) sin x + sin x² + ... + sin x^n")
print("   Каждый член: sin(x^i), где x возводится в степень i")
print("   При |x| < 1: x^i быстро уменьшается")
print("   При |x| > 1: x^i быстро растет (может переполниться)")
print()

print("в) sin x + sin(sin x) + ... + sin(sin(...sin x))")
print("   Вложенное применение функции sin")
print("   Последовательность sin^(i)(x) сходится к 0 для любого x")
print("   (неподвижная точка уравнения sin(t) = t это t = 0)")
print()


# ==================== СХОДИМОСТЬ ДЛЯ ЧАСТИ в) ====================

print(f"{'='*80}")
print("--- Сходимость для части в) ---\n")

print("Последовательность sin(sin(...sin(x))) сходится к 0:")
print(f"{'n':>5} | {'x=1':>15} | {'x=π/2':>15} | {'x=2':>15}")
print("-" * 55)

for n_conv in [1, 2, 5, 10, 20, 50, 100]:
    current_1 = 1.0
    current_pi2 = math.pi / 2
    current_2 = 2.0
    
    for _ in range(n_conv):
        current_1 = math.sin(current_1)
        current_pi2 = math.sin(current_pi2)
        current_2 = math.sin(current_2)
    
    print(f"{n_conv:5d} | {current_1:15.10f} | {current_pi2:15.10f} | {current_2:15.10f}")

print("\nВсе последовательности стремятся к 0!")


# ==================== РОСТ СУММ ====================

print(f"\n{'='*80}")
print("--- Рост сумм при увеличении n ---\n")

print("Для x = 1.0:")
print(f"{'n':>5} | {'а) Σsin^i x':>20} | {'б) Σsin(x^i)':>20} | {'в) Σsin^(i)(x)':>20}")
print("-" * 75)

x_growth = 1.0
for n_growth in [1, 2, 5, 10, 20, 50, 100]:
    a_growth = calculate_a(x_growth, n_growth)
    b_growth = calculate_b(x_growth, n_growth)
    c_growth = calculate_c(x_growth, n_growth)
    print(f"{n_growth:5d} | {a_growth:20.10f} | {b_growth:20.10f} | {c_growth:20.10f}")


# ==================== СПЕЦИАЛЬНЫЕ СЛУЧАИ ====================

print(f"\n{'='*80}")
print("--- Специальные случаи ---\n")

print("1. При x = 0:")
print(f"   а) Все sin^i(0) = 0, сумма = 0")
print(f"   б) Все sin(0^i) = 0, сумма = 0")
print(f"   в) Все sin^(i)(0) = 0, сумма = 0")
print()

print("2. При x = π/2:")
x_pi2 = math.pi / 2
print(f"   sin(π/2) = 1")
print(f"   а) 1 + 1 + 1 + ... = n = {n}")
print(f"   б) sin(π/2) + sin((π/2)²) + ... = {calculate_b(x_pi2, 5):.6f} (для n=5)")
print(f"   в) 1 + sin(1) + sin(sin(1)) + ... = {calculate_c(x_pi2, 5):.6f} (для n=5)")
print()

print("3. При x = π:")
x_pi = math.pi
print(f"   sin(π) ≈ 0")
print(f"   а) ≈ 0 (малые члены)")
print(f"   б) sin(π) + sin(π²) + ... = {calculate_b(x_pi, 5):.6f} (для n=5)")
print(f"   в) ≈ 0 + sin(0) + sin(sin(0)) + ... ≈ 0")


# ==================== ИНТЕРЕСНЫЕ НАБЛЮДЕНИЯ ====================

print(f"\n{'='*80}")
print("--- Интересные наблюдения ---\n")

print("1. Часть а) - геометрическая прогрессия:")
print("   При |sin x| < 1 ряд сходится к sin x / (1 - sin x)")
print("   При sin x = 1 (x = π/2 + 2πk) сумма = n")
print()

print("2. Часть б) - очень быстрый рост аргумента:")
print("   При x > 1: x^10 может быть огромным числом!")
print(f"   Например, 2^10 = {2**10}")
print(f"              10^10 = {10**10}")
print()

print("3. Часть в) - сходится к константе:")
print("   Сумма стремится к конечному пределу")
print("   Зависит от начального x, но всегда конечна")
print(f"   Для x=1, n=100: {calculate_c(1, 100):.10f}")

input("\nНажмите Enter, чтобы завершить программу.")
