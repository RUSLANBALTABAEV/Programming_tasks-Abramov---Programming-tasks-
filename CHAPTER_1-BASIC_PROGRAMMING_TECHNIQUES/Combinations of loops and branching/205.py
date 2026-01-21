"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
7. Сочетания цикла и разветвления

205. Даны натуральное число n, действительные числа a1, ... , an. 
Получить max(|a1|, ..., |an|) и sqrt(a1^2 + ... + an^2).
"""


import math

def calculate_metrics(n, a):
    """
    n: натуральное число (длина последовательности)
    a: список действительных чисел [a₁, a₂, ..., aₙ]
    Возвращает два значения:
    1) max(|a₁|, ..., |aₙ|) - максимальный модуль
    2) sqrt(a₁² + ... + aₙ²) - евклидова норма
    """
    # 1) Максимальный модуль
    max_abs = max(abs(x) for x in a)
    
    # 2) Евклидова норма (корень из суммы квадратов)
    sum_of_squares = sum(x**2 for x in a)
    euclidean_norm = math.sqrt(sum_of_squares)
    
    return max_abs, euclidean_norm


# Пример использования
n = 5
a = [1.5, -2.3, 4.7, 0.8, -3.2]

max_abs, euclidean_norm = calculate_metrics(n, a)
print(f"Последовательность: {a}")
print(f"a) max(|a₁|, ..., |aₙ|) = {max_abs:.4f}")
print(f"б) sqrt(a₁² + ... + aₙ²) = {euclidean_norm:.4f}")

# Более подробный вывод с промежуточными вычислениями
print("\nДетальный расчет:")
print("Модули элементов:", [abs(x) for x in a])
print("Максимальный модуль:", max(abs(x) for x in a))

print("\nКвадраты элементов:", [x**2 for x in a])
print("Сумма квадратов:", sum(x**2 for x in a))
print("Корень из суммы квадратов:", math.sqrt(sum(x**2 for x in a)))
