"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
4. Простейшие циклы

87. Даны натуральные n, m.
Получить сумму m последних цифр числа n.
"""


def sum_last_digits(n, m):
    """Возвращает сумму m последних цифр числа n"""
    s = 0
    count = 0

    while n > 0 and count < m:
        s += n % 10      # последняя цифра
        n //= 10         # убираем последнюю цифру
        count += 1

    return s


def main():
    print("Введите натуральные числа n и m:")
    n = int(input("n = "))
    m = int(input("m = "))

    if n < 1 or m < 1:
        print("Ошибка: n и m должны быть натуральными числами (≥ 1)")
        return

    result = sum_last_digits(n, m)

    print("\n" + "=" * 60)
    print(f"Число n = {n}")
    print(f"Количество последних цифр m = {m}")
    print(f"Сумма m последних цифр = {result}")
    print("=" * 60)


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
