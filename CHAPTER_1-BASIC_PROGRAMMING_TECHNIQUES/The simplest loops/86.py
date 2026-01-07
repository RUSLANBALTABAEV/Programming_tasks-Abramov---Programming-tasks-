"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
4. Простейшие циклы

86. Дано натуральное число n.
а) Сколько цифр в числе n.
б) Чему равна сумма его цифр?
в) Найти первую цифру числа n.
г) Найти знакочередующуюся сумму цифр числа n (пусть запись n в десятичной системе есть akak-1…a0; найти ak - ak-1+…+(-1)k a0).
"""

def count_digits(n):
    return len(str(n))


def sum_digits(n):
    return sum(int(d) for d in str(n))


def first_digit(n):
    return int(str(n)[0])


def alternating_sum(n):
    digits = [int(d) for d in str(n)]
    result = 0
    for i, digit in enumerate(digits):
        result += digit if i % 2 == 0 else -digit
    return result


def analyze_number_detailed(n):
    digits = [int(d) for d in str(n)]

    print(f"Число: n = {n}")
    print(f"Десятичная запись: {' '.join(map(str, digits))}\n")

    print(f"а) Количество цифр: {count_digits(n)}")
    print(f"б) Сумма цифр: {sum_digits(n)}")
    print(f"в) Первая цифра: {first_digit(n)}")

    print("\nг) Знакочередующаяся сумма:")
    terms = []
    for i, d in enumerate(digits):
        if i == 0:
            terms.append(str(d))
        else:
            terms.append(("+ " if i % 2 == 0 else "- ") + str(d))

    print("   " + "".join(terms))
    print(f"   = {alternating_sum(n)}")


def digital_root(n):
    while n >= 10:
        n = sum_digits(n)
    return n


def max_digit(n):
    return max(int(d) for d in str(n))


def min_digit(n):
    return min(int(d) for d in str(n))


def product_digits(n):
    result = 1
    for d in str(n):
        result *= int(d)
    return result


def main():
    n = int(input("Введите натуральное число n: "))

    if n < 1:
        print("Ошибка: n должно быть натуральным числом (n ≥ 1)")
        return

    print("\n" + "=" * 70)
    print(f"Анализ числа n = {n}")
    print("=" * 70 + "\n")

    analyze_number_detailed(n)

    print("\n" + "=" * 70)
    print("--- Примеры ---\n")

    test_numbers = [5, 42, 123, 9876, 12345, 111111, 100, 2024]
    print(f"{'n':>8} | {'Цифр':>5} | {'Сумма':>6} | {'Первая':>7} | {'Знакочер.':>10}")
    print("-" * 55)

    for num in test_numbers:
        print(f"{num:8d} | {count_digits(num):5d} | {sum_digits(num):6d} | "
              f"{first_digit(num):7d} | {alternating_sum(num):10d}")

    print("\n" + "=" * 70)
    print("--- Дополнительно ---\n")

    for num in [123, 456, 9876]:
        print(f"n = {num}")
        print(f"  Макс. цифра: {max_digit(num)}")
        print(f"  Мин. цифра: {min_digit(num)}")
        print(f"  Произведение цифр: {product_digits(num)}")
        print(f"  Цифровой корень: {digital_root(num)}\n")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
