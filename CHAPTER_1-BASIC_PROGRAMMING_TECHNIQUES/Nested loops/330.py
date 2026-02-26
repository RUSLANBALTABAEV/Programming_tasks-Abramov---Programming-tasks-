"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
10. Вложенные циклы

330. Натуральное число называется совершенным, если оно
равно сумме всех своих делителей, за исключением себя самого. Число 6 – совершенное, так как 6 = 1+2+3. Число 8 – не совершенное, так как 8 != 1+2+4.Дано натуральное число n. Получить все совершенные числа, меньшие n.
"""


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
        # Генерация случайного числа от 1 до 10000
        n = random.randint(1, 10000)
        print(f"Сгенерировано случайное число n = {n}")
        return n

    else:  # choice == '3'
        predefined = [10, 100, 500, 1000, 5000, 10000]  # готовые числа
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

def sum_of_proper_divisors(num):
    """Возвращает сумму собственных делителей числа num (делители, кроме самого числа)."""
    if num < 2:
        return 0
    total = 1  # 1 является делителем для всех чисел >1
    # Перебор делителей до корня из num
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            total += i
            if i != num // i:  # чтобы не удваивать квадратный корень
                total += num // i
    return total

def find_perfect_numbers(limit):
    """Возвращает список совершенных чисел, меньших limit."""
    perfects = []
    for candidate in range(2, limit):
        if sum_of_proper_divisors(candidate) == candidate:
            perfects.append(candidate)
    return perfects

def main():
    n = get_n_by_choice()
    perfects = find_perfect_numbers(n)
    print(f"\nСовершенные числа, меньшие {n}:")
    if perfects:
        print(perfects)
        print(f"Количество: {len(perfects)}")
    else:
        print("Совершенных чисел в указанном диапазоне нет.")

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
