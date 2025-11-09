"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЕМЫ ПРОГРАММИРОВАНИЯ
1. Арифметика действительных чисел. Вычисление по формулам.
11. Даны x, y, z. Вычислить a, b, если:
a = log(abs((y - sqrt(abs(x))) * (x - y / (z + x ** 2 / 4))))
b = x - (x ** 2) / factorial(3) + (x ** 5) / factorial(5)
"""

from math import sqrt, log, factorial

# Ввод данных
x = float(input("Введите x: "))
y = float(input("Введите y: "))
z = float(input("Введите z: "))

# Вычисления 
a = log(abs((y - sqrt(abs(x))) * (x - y / (z + x ** 2 / 4))))
b = x - (x ** 2) / factorial(3) + (x ** 5) / factorial(5)

# Вывод результатов
print(f"a = {a:.4f}")
print(f"b = {b:.4f}")

input("Нажмите любую клавишу, чтобы завершить программу.")
