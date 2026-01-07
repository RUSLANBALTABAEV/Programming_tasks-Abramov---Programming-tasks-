"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
4. Простейшие циклы

88. Дано натуральное число n.
а) Выяснить, входит ли цифра 3 в запись числа n^2.
б) Поменять порядок цифр числа n на обратный.
в) Переставить первую и последнюю цифры числа n.
г) Приписать по единице в начало и в конец записи числа n.
"""


def contains_digit_3_in_square(n):
    """а) Проверяет, есть ли цифра 3 в n^2"""
    x = n * n
    while x > 0:
        if x % 10 == 3:
            return True
        x //= 10
    return False


def reverse_number(n):
    """б) Переворачивает число n"""
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev


def swap_first_last_digits(n):
    """в) Меняет местами первую и последнюю цифры"""
    if n < 10:
        return n  # однозначное число

    last = n % 10
    temp = n
    power = 1

    while temp >= 10:
        temp //= 10
        power *= 10

    first = temp
    middle = (n % power) // 10

    return last * power + middle * 10 + first


def add_ones_to_ends(n):
    """г) Приписывает 1 в начало и конец числа"""
    temp = n
    power = 1

    while temp > 0:
        power *= 10
        temp //= 10

    return 1 * (power * 10) + n * 10 + 1


def main():
    n = int(input("Введите натуральное число n: "))

    if n < 1:
        print("Ошибка: n должно быть натуральным числом (n ≥ 1)")
        return

    print("\n" + "=" * 70)
    print(f"Число n = {n}")
    print("=" * 70)

    # а)
    print("\nа) Проверка наличия цифры 3 в n²:")
    print(f"n² = {n * n}")
    if contains_digit_3_in_square(n):
        print("Цифра 3 входит в запись n²")
    else:
        print("Цифра 3 НЕ входит в запись n²")

    # б)
    print("\nб) Обратный порядок цифр:")
    print(f"{n} → {reverse_number(n)}")

    # в)
    print("\nв) Перестановка первой и последней цифры:")
    print(f"{n} → {swap_first_last_digits(n)}")

    # г)
    print("\nг) Приписывание единиц в начало и конец:")
    print(f"{n} → {add_ones_to_ends(n)}")

    print("\n" + "=" * 70)


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
