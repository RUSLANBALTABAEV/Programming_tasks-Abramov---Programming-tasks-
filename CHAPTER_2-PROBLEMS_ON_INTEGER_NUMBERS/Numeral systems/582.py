"""
ГЛАВА 2
ЗАДАЧИ ПО ТЕМАМ
16. Системы счисления

582. Получить последовательность d-1, d-2, ..., d-k десятичных цифр числа 2 ^ -200, т.е. такую целочисленную последовательность, в которой каждый член di удовлетворяет условию 0 <= di <= 9 и, дополнительно, d-1 * 10 ^ -1 + d-2 * 10 ^ -2 + ... + d-k * 10 ^ -k = 2 ^ -200.
"""


# ==========================================================
# ЗАДАЧА 582: Последовательность десятичных цифр числа 2^(-exp)
# §16. Системы счисления
# Используется тождество: 2^(-exp) = 5^exp / 10^exp
# ==========================================================

import random
from fractions import Fraction


def power_of_five_digits(exp):
    """
    Возвращает список десятичных цифр числа 5^exp
    (младшие разряды — в начале списка).

    Реализовано «вручную»:
      - начинаем с 1 (5 ^ 0);
      - exp раз умножаем массив цифр на 5 с переносом.
    """
    digits = [1]
    for _ in range(exp):
        carry = 0
        for i in range(len(digits)):
            prod = digits[i] * 5 + carry
            digits[i] = prod % 10
            carry = prod // 10
        while carry:
            digits.append(carry % 10)
            carry //= 10
    return digits


def digits_of_power_of_two_minus(exp):
    """
    Возвращает список d_1, d_2, ..., d_exp десятичных цифр числа 2 ^ (-exp).

    Идея: 2 ^ (-exp) = 5 ^ exp / 10 ^ exp, поэтому дробная часть — это
    десятичная запись 5 ^ exp, дополненная ведущими нулями до exp цифр.
    """
    if exp == 0:
        return [1]  # 2 ^ 0 = 1 = 1.0... — формально, но по условию exp>=1

    digits_le = power_of_five_digits(exp)   # младшие разряды первыми
    digits_be = digits_le[::-1]             # старшие разряды первыми

    # Дополняем ведущими нулями до exp разрядов
    if len(digits_be) < exp:
        digits_be = [0] * (exp - len(digits_be)) + digits_be
    return digits_be


def get_exponent():
    """Выбор способа ввода показателя степени."""
    print("Задача 582: Последовательность десятичных цифр числа 2 ^ (-exp)")
    print("Выберите способ ввода показателя exp:")
    print("1 — Ручной ввод")
    print("2 — Случайная генерация")
    print("3 — Готовые примеры (по условию — 200)")

    while True:
        choice = input("Ваш выбор (1/2/3): ").strip()
        if choice in ('1', '2', '3'):
            break
        print("Ошибка: выберите 1, 2 или 3.")

    if choice == '1':
        while True:
            try:
                exp = int(input("Введите показатель степени exp (1 <= exp <= 500): "))
                if exp < 1 or exp > 500:
                    print("exp должно быть в диапазоне от 1 до 500.")
                    continue
                return exp
            except ValueError:
                print("Ошибка ввода. Введите целое число.")

    elif choice == '2':
        exp = random.randint(1, 200)
        print(f"\nСгенерировано exp = {exp}")
        return exp

    else:  # готовые примеры
        examples = [1, 2, 5, 10, 50, 100, 200]
        print("\nГотовые примеры exp:")
        for idx, val in enumerate(examples, 1):
            print(f"{idx}: exp = {val}")
        while True:
            try:
                num = int(input("Выберите номер примера: "))
                if 1 <= num <= len(examples):
                    return examples[num - 1]
                else:
                    print(f"Номер должен быть от 1 до {len(examples)}.")
            except ValueError:
                print("Ошибка ввода. Введите целое число.")


def main():
    exp = get_exponent()

    print(f"\nПоказатель степени: exp = {exp}")
    print("=" * 70)

    # 1. Ручной алгоритм
    digits_manual = digits_of_power_of_two_minus(exp)

    # 2. Прямое вычисление через str(5**exp) для проверки
    digits_direct = [int(ch) for ch in str(5 ** exp).zfill(exp)]

    # 3. Вывод результата
    print(f"Цифры числа 2^(-{exp}) (d_1, d_2, ..., d_{exp}):")
    if exp <= 50:
        print(digits_manual)
    else:
        # Для длинных последовательностей выводим начало и конец
        print(f"  первые 30: {digits_manual[:30]}")
        print(f"  последние 30: {digits_manual[-30:]}")
    print(f"Количество цифр: {len(digits_manual)}")
    print()

    # 4. Проверка №1: сравнение с прямым вычислением
    print("--- Проверка №1: сравнение с str(5 ^ exp).zfill(exp) ---")
    print(f"Совпадает: {digits_manual == digits_direct}")
    print()

    # 5. Проверка №2: восстановление значения через сумму d_i * 10^(-i)
    print("--- Проверка №2: восстановление значения через сумму ---")
    reconstructed = Fraction(0, 1)
    for i, d in enumerate(digits_manual, 1):
        reconstructed += Fraction(d, 10 ** i)

    exact = Fraction(1, 2 ** exp)
    print(f"Восстановленное значение: {reconstructed}")
    print(f"Точное значение 2 ^ (-{exp}):  {exact}")
    print(f"Совпадает: {reconstructed == exact}")

    print("=" * 70)


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")