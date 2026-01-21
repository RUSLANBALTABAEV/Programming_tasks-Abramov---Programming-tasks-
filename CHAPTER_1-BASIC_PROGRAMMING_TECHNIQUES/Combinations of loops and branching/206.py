"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
7. Сочетания цикла и разветвления

206. Дано натуральное число n. Найти наибольшее среди чисел k*e^sin^2(k+1) * (k = 1, ..., n), а также сумму всех этих чисел.
"""


import math

def compute_sequence(n):
    """
    Вычисляет последовательность значений k * exp(sin²(k+1)) для k = 1..n
    Возвращает наибольшее значение и сумму всех значений.
    """
    max_value = float('-inf')  # начальное значение для максимума
    total_sum = 0.0
    
    for k in range(1, n + 1):
        # Вычисляем значение: k * e^(sin²(k+1))
        value = k * math.exp(math.sin(k + 1) ** 2)
        
        # Обновляем максимум
        if value > max_value:
            max_value = value
        
        # Добавляем к сумме
        total_sum += value
    
    return max_value, total_sum


# Пример использования
n = 10
max_val, total_sum = compute_sequence(n)

print(f"Для n = {n}:")
print(f"Наибольшее значение: {max_val:.4f}")
print(f"Сумма всех значений: {total_sum:.4f}")

# Более подробный вывод
print("\nДетальные значения последовательности:")
for k in range(1, n + 1):
    value = k * math.exp(math.sin(k + 1) ** 2)
    print(f"k = {k:2}: {k} * e^(sin²({k+1})) = {value:.4f}")
