"""
ГЛАВА 2
ЗАДАЧИ ПО ТЕМАМ
16. Системы счисления

584. Получить последовательность dk, dk-1, ..., d0 десятичных цифр числа:
a) 100! + 2 ^ 100;
b) 100! - 2 ^ 100,
т.е. получить такую целочисленную последовательность, в которой каждый член di удовлетворяет условию 0 <= di <= 9 и, дополнительно, dk * 10 ^ k + dk-1 * 10 k - 1 + ... + d0 равно 100! + 2 ^ 100 или  соответственно 100! - 2 ^ 100.
"""


# ==========================================================
# ЗАДАЧА 584: Цифры чисел 100! + 2^100 и 100! - 2^100
# §16. Системы счисления
# ==========================================================

import math


def factorial_digits_le(n):
    """Возвращает список цифр числа n! (младшие разряды первыми)."""
    digits = [1]
    for i in range(2, n + 1):
        carry = 0
        for j in range(len(digits)):
            prod = digits[j] * i + carry
            digits[j] = prod % 10
            carry = prod // 10
        while carry:
            digits.append(carry % 10)
            carry //= 10
    return digits


def power_of_two_digits_le(exp):
    """Возвращает список цифр числа 2^exp (младшие разряды первыми)."""
    digits = [1]
    for _ in range(exp):
        carry = 0
        for j in range(len(digits)):
            prod = digits[j] * 2 + carry
            digits[j] = prod % 10
            carry = prod // 10
        while carry:
            digits.append(carry % 10)
            carry //= 10
    return digits


def add_digits_le(a, b):
    """Сложение двух чисел, заданных массивами цифр (младшие первыми)."""
    res = []
    carry = 0
    for i in range(max(len(a), len(b))):
        val = carry
        if i < len(a):
            val += a[i]
        if i < len(b):
            val += b[i]
        res.append(val % 10)
        carry = val // 10
    if carry:
        res.append(carry)
    return res


def sub_digits_le(a, b):
    """
    Вычитание b из a (предполагается a >= b).
    a, b — массивы цифр (младшие разряды первыми).
    """
    res = []
    borrow = 0
    for i in range(len(a)):
        val = a[i] - borrow
        if i < len(b):
            val -= b[i]
        if val < 0:
            val += 10
            borrow = 1
        else:
            borrow = 0
        res.append(val)
    # Убираем незначащие нули
    while len(res) > 1 and res[-1] == 0:
        res.pop()
    return res


def digits_to_int(digits_le):
    """Преобразует массив цифр (младшие первыми) в целое число."""
    val = 0
    for d in reversed(digits_le):
        val = val * 10 + d
    return val


def print_result(name, digits_le, expected):
    """Выводит результат: цифры, количество, проверку."""
    digits_be = digits_le[::-1]  # старшие разряды первыми
    print(f"\n{name}")
    print("Последовательность цифр (d_k, ..., d_0):")
    if len(digits_be) <= 80:
        print(digits_be)
    else:
        print(f"  первые 40: {digits_be[:40]}")
        print(f"  последние 40: {digits_be[-40:]}")
    print(f"Количество цифр: {len(digits_be)}")
    rebuilt = digits_to_int(digits_le)
    print(f"Проверка: совпадает с ожидаемым значением: {rebuilt == expected}")
    if len(str(expected)) <= 80:
        print(f"Ожидаемое значение: {expected}")
    else:
        s = str(expected)
        groups = [s[max(0, i-5):i] for i in range(len(s), 0, -5)][::-1]
        print("Ожидаемое значение (по 5 цифр):")
        print(" ".join(groups))


def get_choice():
    print("Задача 584: Цифры чисел 100! + 2^100 и 100! - 2^100")
    print("Выберите вариант:")
    print("1 — а) 100! + 2^100")
    print("2 — б) 100! - 2^100")
    print("3 — оба варианта")
    while True:
        ch = input("Ваш выбор (1/2/3): ").strip()
        if ch in ('1', '2', '3'):
            return ch
        print("Ошибка: выберите 1, 2 или 3.")


def main():
    choice = get_choice()

    fact_le = factorial_digits_le(100)
    p2_le = power_of_two_digits_le(100)

    fact = math.factorial(100)
    p2 = 2 ** 100

    if choice in ('1', '3'):
        sum_le = add_digits_le(fact_le, p2_le)
        print_result("а) 100! + 2^100", sum_le, fact + p2)

    if choice in ('2', '3'):
        diff_le = sub_digits_le(fact_le, p2_le)
        print_result("б) 100! - 2^100", diff_le, fact - p2)


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")