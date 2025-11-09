"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
4. Простейшие циклы

77. Дано натуральное число n. Вычислить:

а) 2 ** n;
б) n!;
в) (1 + 1 / 1²) * (1 + 1 / 2²) * ... * (1 + 1 / n²);
г) 1 / sin(1) + 1 / (sin(1) + sin(2)) + ... + 1 / (sin(1) + ... + sin(n));
д) √(2 + √(2 + ... + √(2))) — n вложенных корней;
е) (cos(1)/sin(1)) * ((cos(1)+cos(2))/(sin(1)+sin(2))) * ... *
   ((cos(1)+...+cos(n))/(sin(1)+...+sin(n)));
ж) √(3 + √(6 + ... + √(3·(n−1) + √(3·n)))).
"""

import math


def calculate_a(n):
    """а) Возвращает 2^n"""
    return 2 ** n


def calculate_b(n):
    """б) Возвращает n! (факториал)"""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def calculate_c(n):
    """в) Вычисляет произведение (1 + 1/1²)(1 + 1/2²)...(1 + 1/n²)"""
    result = 1
    for i in range(1, n + 1):
        result *= (1 + 1 / (i ** 2))
    return result


def calculate_d(n):
    """г) Вычисляет сумму 1/sin(1) + 1/(sin(1)+sin(2)) + ... + 1/(sin(1)+...+sin(n))"""
    result = 0
    cumulative_sum = 0
    for i in range(1, n + 1):
        cumulative_sum += math.sin(i)
        result += 1 / cumulative_sum
    return result


def calculate_e(n):
    """д) Вычисляет √(2 + √(2 + ... + √(2))) — n вложенных корней"""
    result = 0
    for i in range(n):
        result = math.sqrt(2 + result)
    return result


def calculate_f(n):
    """е) Вычисляет произведение:
       (cos(1)/sin(1)) * ((cos(1)+cos(2))/(sin(1)+sin(2))) * ... * ((cos(1)+...+cos(n))/(sin(1)+...+sin(n)))
    """
    result = 1
    sum_cos = 0
    sum_sin = 0
    for i in range(1, n + 1):
        sum_cos += math.cos(i)
        sum_sin += math.sin(i)
        result *= sum_cos / sum_sin
    return result


def calculate_g(n):
    """ж) Вычисляет вложенные корни:
       √(3 + √(6 + ... + √(3·(n−1) + √(3·n))))
    """
    result = 0
    for i in range(n, 0, -1):
        result = math.sqrt(3 * i + result)
    return result


# ==================== ВВОД ДАННЫХ ====================

print("Введите натуральное число n:")
n = int(input("n = "))

if n < 1:
    print("Ошибка: n должно быть натуральным числом (n ≥ 1)")
else:
    print(f"\n{'='*70}")
    print(f"Вычисление выражений для n = {n}")
    print(f"{'='*70}\n")

    # а) 2^n
    result_a = calculate_a(n)
    print(f"а) 2^n = 2^{n} = {result_a}")

    # б) n!
    result_b = calculate_b(n)
    print(f"\nб) n! = {n}! = {result_b}")

    # в) Произведение (1 + 1/i²)
    result_c = calculate_c(n)
    print(f"\nв) (1 + 1/1²)(1 + 1/2²)...(1 + 1/{n}²) = {result_c:.10f}")

    # г) Сумма с синусами
    try:
        result_d = calculate_d(n)
        print(f"\nг) 1/sin(1) + 1/(sin(1)+sin(2)) + ... + 1/(sin(1)+...+sin({n})) = {result_d:.10f}")
    except ZeroDivisionError:
        print(f"\nг) Ошибка: деление на ноль (сумма синусов = 0)")

    # д) Вложенные корни √(2 + √(2 + ...))
    result_e = calculate_e(n)
    print(f"\nд) √(2 + √(2 + ... + √(2))) ({n} корней) = {result_e:.10f}")

    # е) Произведение с cos/sin
    try:
        result_f = calculate_f(n)
        print(f"\nе) (cos(1)/sin(1)) * ... * ((cos(1)+...+cos({n}))/(sin(1)+...+sin({n}))) = {result_f:.10f}")
    except ZeroDivisionError:
        print(f"\nе) Ошибка: деление на ноль (сумма синусов = 0)")

    # ж) Вложенные корни с множителем 3
    result_g = calculate_g(n)
    print(f"\nж) √(3 + √(6 + ... + √(3·({n}−1) + √(3·{n})))) = {result_g:.10f}")


# ==================== ПРИМЕРЫ ДЛЯ РАЗНЫХ n ====================

print(f"\n{'='*70}")
print("--- Примеры для n от 1 до 10 ---\n")

print(f"{'n':>3} | {'2^n':>10} | {'n!':>15} | {'в)':>12} | {'д)':>12} | {'ж)':>12}")
print("-" * 70)

for test_n in range(1, 11):
    a = calculate_a(test_n)
    b = calculate_b(test_n)
    c = calculate_c(test_n)
    e = calculate_e(test_n)
    g = calculate_g(test_n)

    print(f"{test_n:3d} | {a:10d} | {b:15d} | {c:12.6f} | {e:12.8f} | {g:12.8f}")


# ==================== ПОДРОБНЫЙ ВЫВОД ДЛЯ МАЛЫХ n ====================

print(f"\n{'='*70}")
print(f"--- Детальное вычисление для n = {min(n, 5)} ---\n")

detail_n = min(n, 5)

# б) Факториал
print("б) Факториал:")
fact = 1
for i in range(1, detail_n + 1):
    fact *= i
    print(f"   {i}! = {fact}")

# в) Произведение (1 + 1/i²)
print(f"\nв) Произведение (1 + 1/i²):")
prod = 1
for i in range(1, detail_n + 1):
    term = 1 + 1 / (i ** 2)
    prod *= term
    print(f"   i = {i}: (1 + 1/{i}²) = {term:.6f}, произведение = {prod:.6f}")

# д) Вложенные корни √(2 + √(2 + ...))
print(f"\nд) Вложенные корни √(2 + √(2 + ... + √(2))):")
nested = 0
for i in range(1, detail_n + 1):
    nested = math.sqrt(2 + nested)
    print(f"   Шаг {i}: √(2 + ...) = {nested:.8f}")

# ж) Вложенные корни √(3 + √(6 + ...))
print(f"\nж) Вложенные корни √(3 + √(6 + ... + √(3·n))):")
nested_g = 0
steps = []
for i in range(detail_n, 0, -1):
    nested_g = math.sqrt(3 * i + nested_g)
    steps.append((i, nested_g))

for i, value in reversed(steps):
    print(f"   Шаг (с конца) i = {i}: √(3·{i} + ...) = {value:.8f}")


# ==================== ДОПОЛНИТЕЛЬНЫЕ НАБЛЮДЕНИЯ ====================

print(f"\n{'='*70}")
print("--- Интересные факты ---\n")

print("а) Степени двойки (2^n):")
for i in range(1, 11):
    print(f"   2^{i} = {2**i}")

print(f"\nб) Факториалы растут очень быстро:")
print(f"   10! = {calculate_b(10):,}")
print(f"   20! = {calculate_b(20):,}")

print(f"\nд) Предел вложенных корней √(2 + √(2 + ...)) стремится к 2")
print(f"   При n = 10: {calculate_e(10):.10f}")
print(f"   При n = 50: {calculate_e(50):.10f}")

print(f"\nж) Вложенные корни √(3 + √(6 + ...)) при больших n:")
print(f"   n = 5:  {calculate_g(5):.10f}")
print(f"   n = 10: {calculate_g(10):.10f}")
print(f"   n = 20: {calculate_g(20):.10f}")

input("\nНажмите Enter, чтобы завершить программу.")
