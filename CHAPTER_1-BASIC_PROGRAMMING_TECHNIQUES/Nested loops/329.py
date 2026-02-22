"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
10. Вложенные циклы

329. Даны натуральные числа n, m. Получить все меньшие n натуральные числа, квадрат суммы цифр которых равен m.
"""


import random

def get_numbers_by_choice():
    """Выбор способа получения чисел n и m."""
    print("Выберите способ задания чисел n и m (n > 0, m ≥ 0):")
    print("1 - Ручной ввод")
    print("2 - Случайные числа")
    print("3 - Готовые числа из списка")
    choice = input("Ваш выбор (1/2/3): ").strip()
    while choice not in ('1', '2', '3'):
        choice = input("Некорректный ввод. Выберите 1, 2 или 3: ").strip()

    if choice == '1':
        while True:
            try:
                n = int(input("Введите натуральное число n (>0): "))
                m = int(input("Введите целое неотрицательное число m: "))
                if n <= 0:
                    print("n должно быть положительным.")
                elif m < 0:
                    print("m должно быть неотрицательным.")
                else:
                    return n, m
            except ValueError:
                print("Ошибка ввода. Введите целые числа.")

    elif choice == '2':
        # Генерация случайных чисел в разумных пределах
        n = random.randint(1, 1000)
        m = random.randint(0, 100)  # квадрат суммы цифр редко бывает большим
        print(f"Сгенерированы случайные числа: n = {n}, m = {m}")
        return n, m

    else:  # choice == '3'
        predefined = [(100, 9), (500, 16), (50, 25), (1000, 49), (200, 0)]  # готовые пары
        print("Доступные готовые пары (n, m):")
        for idx, (n_val, m_val) in enumerate(predefined, start=1):
            print(f"{idx} - n = {n_val}, m = {m_val}")
        while True:
            try:
                idx = int(input("Выберите номер пары: "))
                if 1 <= idx <= len(predefined):
                    return predefined[idx - 1]
                else:
                    print(f"Введите число от 1 до {len(predefined)}")
            except ValueError:
                print("Ошибка ввода. Введите номер.")

def digit_sum(num):
    """Возвращает сумму цифр числа."""
    return sum(int(d) for d in str(num))

def find_numbers(n, m):
    """Возвращает список чисел от 1 до n-1, для которых (сумма цифр)^2 == m."""
    result = []
    for x in range(1, n):
        if digit_sum(x) ** 2 == m:
            result.append(x)
    return result

def main():
    n, m = get_numbers_by_choice()
    numbers = find_numbers(n, m)
    print(f"\nЧисла меньше {n}, квадрат суммы цифр которых равен {m}:")
    if numbers:
        print(numbers)
        print(f"Количество: {len(numbers)}")
    else:
        print("Таких чисел нет.")

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
