"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
10. Вложенные циклы

324. Даны целые числа p и q. Получить все делители числа q, взаимно простые с p.
"""


import math
import random

def get_numbers_by_choice():
    """Выбор способа получения чисел p и q."""
    print("Выберите способ задания чисел p и q:")
    print("1 - Ручной ввод")
    print("2 - Случайные числа")
    print("3 - Готовые числа из списка")
    choice = input("Ваш выбор (1/2/3): ").strip()
    while choice not in ('1', '2', '3'):
        choice = input("Некорректный ввод. Выберите 1, 2 или 3: ").strip()

    if choice == '1':
        while True:
            try:
                p = int(input("Введите целое число p: "))
                q = int(input("Введите целое число q (не равное 0): "))
                if q == 0:
                    print("Число q не может быть нулём (делители нуля не определены).")
                else:
                    return p, q
            except ValueError:
                print("Ошибка ввода. Введите целые числа.")

    elif choice == '2':
        # Генерация случайных чисел в разумных пределах
        p = random.randint(-100, 100)
        q = random.randint(-100, 100)
        while q == 0:
            q = random.randint(-100, 100)  # избегаем нуля
        print(f"Сгенерированы случайные числа: p = {p}, q = {q}")
        return p, q

    else:  # choice == '3'
        predefined = [(15, 60), (-8, 36), (12, 0), (7, 49), (-3, 30)]  # готовые пары
        print("Доступные готовые пары (p, q):")
        for idx, (p_val, q_val) in enumerate(predefined, start=1):
            print(f"{idx} - p = {p_val}, q = {q_val}")
        while True:
            try:
                idx = int(input("Выберите номер пары: "))
                if 1 <= idx <= len(predefined):
                    p, q = predefined[idx - 1]
                    if q == 0:
                        print("Внимание: q = 0, делителей бесконечно много. Выберите другую пару.")
                        continue
                    return p, q
                else:
                    print(f"Введите число от 1 до {len(predefined)}")
            except ValueError:
                print("Ошибка ввода. Введите номер.")

def find_divisors(n):
    """Возвращает все положительные делители числа n (n != 0)."""
    n = abs(n)
    divisors = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return sorted(divisors)

def are_coprime(a, b):
    """Проверяет, являются ли числа a и b взаимно простыми (gcd == 1)."""
    return math.gcd(abs(a), abs(b)) == 1

def main():
    p, q = get_numbers_by_choice()
    all_divisors = find_divisors(q)
    coprime_divisors = [d for d in all_divisors if are_coprime(d, p)]
    print(f"\nЧисло p = {p}, число q = {q}")
    print(f"Все положительные делители q: {all_divisors}")
    print(f"Делители q, взаимно простые с p: {coprime_divisors}")
    print(f"Количество: {len(coprime_divisors)}")

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
