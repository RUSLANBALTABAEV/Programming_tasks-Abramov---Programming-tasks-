"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
10. Вложенные циклы

323. Дано натуральное число n. Получить все натуральные числа, меньшие n и взаимно простые с ним.
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
        # Генерация случайного числа от 2 до 500 (можно изменить диапазон)
        n = random.randint(2, 500)
        print(f"Сгенерировано случайное число n = {n}")
        return n

    else:  # choice == '3'
        predefined = [12, 30, 100, 256, 1000]  # готовые числа
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

def find_coprimes(n):
    """Возвращает список чисел от 1 до n-1, взаимно простых с n."""
    return [i for i in range(1, n) if math.gcd(i, n) == 1]

def main():
    n = get_n_by_choice()
    coprimes = find_coprimes(n)
    print(f"\nЧисла, меньшие {n} и взаимно простые с ним:")
    print(coprimes)
    print(f"Всего таких чисел: {len(coprimes)} (функция Эйлера φ({n}) = {len(coprimes)})")

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
