"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
10. Вложенные циклы

332. Известно, что любое натуральное число можно представить в виде суммы не более чем четырех квадратов натуральных чисел или, что то же самое, в виде суммы четырех квадратов неотрицательных целых чисел (теорема Лагранжа). Дано натуральное n; указать такие неотрицательные x,y,z,t, что n = x * x + y * y + t * t.
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
        n = random.randint(1, 1000)
        print(f"Сгенерировано случайное число n = {n}")
        return n

    else:  # choice == '3'
        predefined = [1, 2, 3, 7, 15, 23, 30, 100, 1729]
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

def find_four_squares(n):
    """
    Возвращает кортеж (x, y, z, t) неотрицательных целых чисел,
    таких что x^2 + y^2 + z^2 + t^2 = n.
    Гарантируется существование по теореме Лагранжа.
    """
    max_x = int(math.isqrt(n))
    for x in range(max_x + 1):
        rem1 = n - x * x
        max_y = int(math.isqrt(rem1))
        for y in range(max_y + 1):
            rem2 = rem1 - y * y
            max_z = int(math.isqrt(rem2))
            for z in range(max_z + 1):
                rem3 = rem2 - z * z
                t = int(math.isqrt(rem3))
                if t * t == rem3:
                    # Возвращаем в порядке неубывания для удобства
                    result = sorted([x, y, z, t])
                    return tuple(result)
    # Теоретически сюда никогда не попадём
    return None

def main():
    n = get_n_by_choice()
    print(f"\nЗаданное число n = {n}")

    representation = find_four_squares(n)
    if representation:
        x, y, z, t = representation
        print(f"Представление в виде суммы четырёх квадратов:")
        print(f"{n} = {x}² + {y}² + {z}² + {t}²")
        print(f"Проверка: {x**2} + {y**2} + {z**2} + {t**2} = {x**2 + y**2 + z**2 + t**2}")
    else:
        # Не должно случиться
        print("Ошибка: представление не найдено.")

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
