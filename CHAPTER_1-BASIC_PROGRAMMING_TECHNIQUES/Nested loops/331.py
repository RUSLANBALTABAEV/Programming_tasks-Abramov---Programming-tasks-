"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
10. Вложенные циклы

331. Дано натуральное число n. Можно ли представить его в виде суммы трех квадратов натуральных чисел? Если можно, то 
а) указать тройку x,y,z таких натуральных чисел, что n = x * x + y * y + z * z,
б) указать все тройки x,y,z таких натуральных чисел, что n = x * x + y * y + z * z.
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
        predefined = [3, 6, 9, 27, 30, 50, 100, 1729]
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

def find_one_triple(n):
    """Возвращает одну тройку (x,y,z) с x≤y≤z такую, что x²+y²+z²=n, или None."""
    max_x = int(math.isqrt(n))
    for x in range(1, max_x + 1):
        rem_xy = n - x * x
        if rem_xy < 2:          # нужно ещё два квадрата (минимум 1+1=2)
            continue
        max_y = int(math.isqrt(rem_xy))
        for y in range(x, max_y + 1):
            rem = rem_xy - y * y
            if rem < 1:
                continue
            z = int(math.isqrt(rem))
            if z * z == rem and z >= y:
                return (x, y, z)
    return None

def find_all_triples(n):
    """Возвращает список всех троек (x,y,z) с x≤y≤z, удовлетворяющих условию."""
    triples = []
    max_x = int(math.isqrt(n))
    for x in range(1, max_x + 1):
        rem_xy = n - x * x
        if rem_xy < 2:
            continue
        max_y = int(math.isqrt(rem_xy))
        for y in range(x, max_y + 1):
            rem = rem_xy - y * y
            if rem < 1:
                continue
            z = int(math.isqrt(rem))
            if z * z == rem and z >= y:
                triples.append((x, y, z))
    return triples

def main():
    n = get_n_by_choice()
    print(f"\nЗаданное число n = {n}")

    if n < 3:
        print("Число меньше 3, невозможно представить в виде суммы трёх квадратов натуральных чисел.")
        return

    one = find_one_triple(n)
    if one is None:
        print(f"Число {n} нельзя представить в виде суммы трёх квадратов натуральных чисел.")
    else:
        print(f"Число {n} можно представить.")
        print(f"а) Одна тройка: {one[0]}² + {one[1]}² + {one[2]}² = {one[0]**2 + one[1]**2 + one[2]**2}")
        all_triples = find_all_triples(n)
        print("б) Все тройки (с точностью до порядка, x ≤ y ≤ z):")
        for t in all_triples:
            print(f"   {t[0]}² + {t[1]}² + {t[2]}² = {t[0]**2 + t[1]**2 + t[2]**2}")

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
