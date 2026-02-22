"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
10. Вложенные циклы

327. Даны натуральные числа a, b (a <= b). Получить все простые числа p, удовлетворяющие неравенствам a <= p <= b.
"""


import math
import random

def get_bounds_by_choice():
    """Выбор способа получения границ a и b."""
    print("Выберите способ задания границ a и b (a ≤ b):")
    print("1 - Ручной ввод")
    print("2 - Случайные числа")
    print("3 - Готовые числа из списка")
    choice = input("Ваш выбор (1/2/3): ").strip()
    while choice not in ('1', '2', '3'):
        choice = input("Некорректный ввод. Выберите 1, 2 или 3: ").strip()

    if choice == '1':
        while True:
            try:
                a = int(input("Введите натуральное число a (>0): "))
                b = int(input("Введите натуральное число b (≥ a): "))
                if a <= 0 or b <= 0:
                    print("Числа должны быть положительными.")
                elif a > b:
                    print("Ошибка: a должно быть ≤ b.")
                else:
                    return a, b
            except ValueError:
                print("Ошибка ввода. Введите целые числа.")

    elif choice == '2':
        # Генерация случайных чисел в разумных пределах
        a = random.randint(1, 100)
        b = random.randint(a, 200)  # чтобы b было ≥ a
        print(f"Сгенерированы случайные границы: a = {a}, b = {b}")
        return a, b

    else:  # choice == '3'
        predefined = [(1, 10), (10, 50), (100, 200), (2, 2), (997, 1000)]  # готовые пары
        print("Доступные готовые пары (a, b):")
        for idx, (a_val, b_val) in enumerate(predefined, start=1):
            print(f"{idx} - a = {a_val}, b = {b_val}")
        while True:
            try:
                idx = int(input("Выберите номер пары: "))
                if 1 <= idx <= len(predefined):
                    return predefined[idx - 1]
                else:
                    print(f"Введите число от 1 до {len(predefined)}")
            except ValueError:
                print("Ошибка ввода. Введите номер.")

def primes_in_range(a, b):
    """Возвращает список всех простых чисел в отрезке [a, b] (включительно)."""
    if a > b or a < 1:
        return []
    # Создаём булевый массив для чисел от a до b
    size = b - a + 1
    is_prime = [True] * size
    # Решето Эратосфена по простым числам до sqrt(b)
    limit = int(math.isqrt(b))
    for p in range(2, limit + 1):
        # Находим первое кратное p в отрезке [a, b]
        start = ((a + p - 1) // p) * p
        for multiple in range(start, b + 1, p):
            if multiple != p:  # не вычёркиваем само p, если оно попадает в диапазон
                is_prime[multiple - a] = False
    # Собираем простые числа
    primes = []
    for i in range(size):
        if is_prime[i]:
            num = a + i
            if num > 1:  # 1 не простое
                primes.append(num)
    return primes

def main():
    a, b = get_bounds_by_choice()
    primes = primes_in_range(a, b)
    print(f"\nПростые числа в диапазоне от {a} до {b}:")
    if primes:
        print(primes)
        print(f"Количество: {len(primes)}")
    else:
        print("Простых чисел в указанном диапазоне нет.")

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
