"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
4. Простейшие циклы

79. Вычислить (1+sin 0.1)(1+sin 0.2)…(1+sin 10).
"""


import math

def calculate_product():
    """
    Вычисляет произведение (1+sin 0.1)(1+sin 0.2)...(1+sin 10)
    """
    product = 1
    x = 0.1
    
    while x <= 10:
        term = 1 + math.sin(x)
        product *= term
        x += 0.1
    
    return product


def calculate_product_detailed():
    """
    Вычисляет произведение с детальным выводом
    """
    product = 1
    x = 0.1
    step = 0
    
    print(f"{'Шаг':>4} | {'x':>6} | {'sin(x)':>10} | {'1+sin(x)':>12} | {'Произведение':>15}")
    print("-" * 65)
    
    while x <= 10:
        sin_x = math.sin(x)
        term = 1 + sin_x
        product *= term
        step += 1
        
        # Выводим каждый 10-й шаг для краткости
        if step % 10 == 0 or step <= 5 or x >= 9.9:
            print(f"{step:4d} | {x:6.2f} | {sin_x:10.6f} | {term:12.8f} | {product:15.8f}")
        
        x += 0.1
    
    return product


# ==================== ОСНОВНОЕ ВЫЧИСЛЕНИЕ ====================

print("Вычисление произведения (1+sin 0.1)(1+sin 0.2)...(1+sin 10)")
print(f"{'='*70}\n")

result = calculate_product()
print(f"Результат: {result:.15f}")
print(f"В научной нотации: {result:.6e}\n")


# ==================== ДЕТАЛЬНОЕ ВЫЧИСЛЕНИЕ ====================

print(f"{'='*70}")
print("--- Детальное вычисление (каждый 10-й шаг) ---\n")

result_detailed = calculate_product_detailed()

print(f"\n{'='*70}")
print(f"Итоговое произведение: {result_detailed:.15f}")


# ==================== АНАЛИЗ ====================

print(f"\n{'='*70}")
print("--- Анализ ---\n")

# Подсчет количества множителей
count = 0
x = 0.1
while x <= 10:
    count += 1
    x += 0.1

print(f"Количество множителей: {count}")
print(f"Диапазон x: от 0.1 до 10.0")
print(f"Шаг: 0.1\n")

# Минимальное и максимальное значение sin(x) в диапазоне
x = 0.1
min_sin = float('inf')
max_sin = float('-inf')
min_x = 0
max_x = 0

while x <= 10:
    sin_x = math.sin(x)
    if sin_x < min_sin:
        min_sin = sin_x
        min_x = x
    if sin_x > max_sin:
        max_sin = sin_x
        max_x = x
    x += 0.1

print(f"Минимальное значение sin(x): {min_sin:.6f} при x ≈ {min_x:.2f}")
print(f"Максимальное значение sin(x): {max_sin:.6f} при x ≈ {max_x:.2f}")
print(f"\nМинимальное значение (1+sin(x)): {1 + min_sin:.6f}")
print(f"Максимальное значение (1+sin(x)): {1 + max_sin:.6f}")


# ==================== ГРАФИК (текстовый) ====================

print(f"\n{'='*70}")
print("--- График sin(x) на отрезке [0.1, 10] ---\n")

print("Значения sin(x) для некоторых точек:")
print(f"{'x':>6} | {'sin(x)':>10} | {'1+sin(x)':>12} | Визуализация")
print("-" * 65)

x = 0
while x <= 10:
    sin_x = math.sin(x)
    term = 1 + sin_x
    
    # Текстовая визуализация
    # Масштаб: sin(x) от -1 до 1, отображаем как полоску
    bar_length = int((sin_x + 1) * 20)  # от 0 до 40
    bar = "█" * bar_length
    
    print(f"{x:6.2f} | {sin_x:10.6f} | {term:12.8f} | {bar}")
    
    x += 1

print(f"\n{'='*70}")


# ==================== СРАВНЕНИЕ С ДРУГИМИ МЕТОДАМИ ====================

print("--- Альтернативные вычисления ---\n")

# Метод 1: через цикл for
product_for = 1
for i in range(1, 101):
    x = i * 0.1
    product_for *= (1 + math.sin(x))

print(f"Через цикл for: {product_for:.15f}")

# Метод 2: через list comprehension и math.prod (Python 3.8+)
import functools
values = [1 + math.sin(i * 0.1) for i in range(1, 101)]
product_list = functools.reduce(lambda a, b: a * b, values)

print(f"Через reduce: {product_list:.15f}")

# Проверка
print(f"\nВсе методы дают одинаковый результат: {abs(result - product_for) < 1e-10 and abs(result - product_list) < 1e-10}")


# ==================== ПЕРВЫЕ И ПОСЛЕДНИЕ МНОЖИТЕЛИ ====================

print(f"\n{'='*70}")
print("--- Первые и последние множители ---\n")

print("Первые 10 множителей:")
for i in range(1, 11):
    x = i * 0.1
    sin_x = math.sin(x)
    term = 1 + sin_x
    print(f"  x={x:.1f}: 1 + sin({x:.1f}) = 1 + {sin_x:.6f} = {term:.8f}")

print("\nПоследние 10 множителей:")
for i in range(91, 101):
    x = i * 0.1
    sin_x = math.sin(x)
    term = 1 + sin_x
    print(f"  x={x:.1f}: 1 + sin({x:.1f}) = 1 + {sin_x:.6f} = {term:.8f}")


# ==================== ИНТЕРЕСНЫЕ НАБЛЮДЕНИЯ ====================

print(f"\n{'='*70}")
print("--- Интересные наблюдения ---\n")

print(f"1. Функция sin(x) колеблется от -1 до 1")
print(f"   Поэтому (1 + sin(x)) колеблется от 0 до 2")
print(f"\n2. На отрезке [0.1, 10] функция sin(x) делает примерно:")
print(f"   10 / (2π) ≈ {10 / (2 * math.pi):.2f} полных периодов")
print(f"\n3. Произведение {count} множителей, каждый из которых близок к 1,")
print(f"   дает результат порядка {result:.2e}")
print(f"\n4. Логарифм произведения:")
log_product = sum(math.log(1 + math.sin(i * 0.1)) for i in range(1, 101))
print(f"   ln(произведение) = {log_product:.6f}")
print(f"   e^({log_product:.6f}) = {math.exp(log_product):.15f}")

input("\nНажмите Enter, чтобы завершить программу.")
