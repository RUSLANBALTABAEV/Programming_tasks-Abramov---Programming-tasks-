"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
10. Вложенные циклы

325. Дано натуральное число n. Получить все простые делители этого числа.
"""


import math
import random

def get_n_by_choice():
    """Выбор способа получения числа n."""
    print("Выберите способ задания числа n:")
    print("1 - Ручной ввод")
    print("2 - Случайное число")
    print("3 - Готовое число из списка")
    choice = input("Ваш выбор (1/2/3): ").strip()
    while choice not in ('1', '2', '3'):
        choice = input("Некорректный ввод. Выберите 1, 2 или 3: ").strip()

    if choice == '1':
        while True:
            try:
                n = int(input("Введите натуральное число n (>0): "))
                if n > 0:
                    return n
                else:
                    print("Число должно быть положительным.")
            except ValueError:
                print("Ошибка ввода. Введите целое число.")

    elif choice == '2':
        # Генерация случайного числа от 2 до 1000 (можно изменить)
        n = random.randint(2, 1000)
        print(f"Сгенерировано случайное число n = {n}")
        return n

    else:  # choice == '3'
        predefined = [12, 30, 100, 256, 997, 1000]  # готовые числа
        print("Доступные готовые числа:")
        for idx, val in enumerate(predefined, start=1):
            print(f"{idx} - {val}")
        while True:
            try:
                idx = int(input("Выберите номер числа: "))
                if 1 <= idx <= len(predefined):
                    return predefined[idx - 1]
                else:
                    print(f"Введите число от 1 до {len(predefined)}")
            except ValueError:
                print("Ошибка ввода. Введите номер.")

def prime_factors(n):
    """Возвращает множество простых делителей числа n."""
    factors = set()
    # Проверка делимости на 2 отдельно
    while n % 2 == 0:
        factors.add(2)
        n //= 2
    # Проверка нечётных делителей
    d = 3
    while d * d <= n:
        while n % d == 0:
            factors.add(d)
            n //= d
        d += 2
    # Если остаток больше 1, то он тоже простой
    if n > 1:
        factors.add(n)
    return sorted(factors)  # возвращаем отсортированный список

def main():
    n = get_n_by_choice()
    factors = prime_factors(n)
    print(f"\nПростые делители числа {n}: {factors}")
    if not factors:
        print("У числа нет простых делителей (такое возможно только для n=1).")
    else:
        print(f"Количество простых делителей: {len(factors)}")

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
