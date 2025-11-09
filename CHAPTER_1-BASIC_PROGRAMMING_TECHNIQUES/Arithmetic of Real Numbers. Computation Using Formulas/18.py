"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЕМЫ ПРОГРАММИРОВАНИЯ
18. Треугольник задан величинами своих углов и радиусом
описанной окружности. Найти стороны треугольника.
"""

from math import sin, radians

try:
    # Ввод данных
    angle_A = float(input("Введите угол A (в градусах): "))
    angle_B = float(input("Введите угол B (в градусах): "))
    angle_C = float(input("Введите угол C (в градусах): "))
    r = float(input("Введите радиус описанной окружности: "))

    # Проверка корректности
    if r <= 0:
        raise ValueError("Радиус должен быть положительным!")
    if not (0 < angle_A < 180 and 0 < angle_B < 180 and 0 < angle_C < 180):
        raise ValueError("Углы должны быть больше 0 и меньше 180 градусов!")
    if abs((angle_A + angle_B + angle_C) - 180) > 1e-6:
        raise ValueError("Сумма углов треугольника должна быть равна 180°!")

    # Перевод углов в радианы
    angle_A_rad = radians(angle_A)
    angle_B_rad = radians(angle_B)
    angle_C_rad = radians(angle_C)

    # Вычисление сторон
    side_a = 2 * r * sin(angle_A_rad)
    side_b = 2 * r * sin(angle_B_rad)
    side_c = 2 * r * sin(angle_C_rad)

    # Вывод результатов
    print(f"Сторона a: {side_a:.2f}")
    print(f"Сторона b: {side_b:.2f}")
    print(f"Сторона c: {side_c:.2f}")

except ValueError as e:
    print("Ошибка:", e)

input("Нажмите любую клавишу, чтобы завершить программу.")
