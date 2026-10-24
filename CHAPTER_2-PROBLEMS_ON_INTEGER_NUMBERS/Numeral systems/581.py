"""
ГЛАВА 2
ЗАДАЧИ ПО ТЕМАМ
16. Системы счисления

581. Получить последовательность dk, dk-1, ..., d0 десятичных цифр числа 2 ^ 200, т.е. такую целочисленную последовательность, в которой каждый член di удовлетворяет условию 0 <= di <= 9 и, дополнительно, dk * 10 ^ k + dk-1 * 10 ^ k - 1 + ... + d0 = 2 ^ 200.
"""


# ==========================================================
# ЗАДАЧА 581: Последовательность десятичных цифр числа 2^200
# §16. Системы счисления
# ==========================================================

import random


def power_of_two_digits(exp):
    """
    Возвращает список десятичных цифр числа 2^exp
    (старшие разряды — первыми).

    Реализовано «вручную»:
      - начинаем с 1 (это 2 ^ 0);
      - exp раз умножаем массив цифр на 2 с переносом;
      - храним цифры в обратном порядке (младшие разряды — в начале),
        в конце разворачиваем.

    Сложность: O(exp * K), где K — количество цифр результата.
    """
    digits = [1]  # 2 ^ 0 = 1
    for _ in range(exp):
        carry = 0
        for i in range(len(digits)):
            prod = digits[i] * 2 + carry
            digits[i] = prod % 10
            carry = prod // 10
        while carry:
            digits.append(carry % 10)
            carry //= 10
    return digits[::-1]  # старшие разряды — первыми


def get_exponent():
    """Выбор способа ввода показателя степени."""
    print("Задача 581: Последовательность десятичных цифр числа 2^exp")
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
                exp = int(input("Введите показатель степени exp (0 <= exp <= 500): "))
                if exp < 0 or exp > 500:
                    print("exp должно быть в диапазоне от 0 до 500.")
                    continue
                return exp
            except ValueError:
                print("Ошибка ввода. Введите целое число.")

    elif choice == '2':
        exp = random.randint(1, 200)
        print(f"\nСгенерировано exp = {exp}")
        return exp

    else:  # готовые примеры
        examples = [0, 1, 10, 50, 100, 200, 300]
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
    print("=" * 60)

    # 1. Ручной алгоритм (основной)
    digits_manual = power_of_two_digits(exp)

    # 2. Встроенная проверка
    n = 2 ** exp
    digits_direct = [int(ch) for ch in str(n)]

    # 3. Вывод результата
    print(f"Число 2 ^ {exp} =")
    if len(str(n)) <= 100:
        print(n)
    else:
        s = str(n)
        groups = [s[max(0, i - 5):i] for i in range(len(s), 0, -5)][::-1]
        print(" ".join(groups))

    print()
    print("Последовательность цифр (d_k, ..., d_0):")
    print(digits_manual)

    print()
    print(f"Количество цифр: {len(digits_manual)}")

    # 4. Проверка
    print("\n--- Проверка ---")
    print(f"Ручной алгоритм совпадает с прямым вычислением: "
          f"{digits_manual == digits_direct}")

    reconstructed = 0
    for d in digits_manual:
        reconstructed = reconstructed * 10 + d
    print(f"Восстановленное число из цифр: "
          f"{'совпадает с 2 ^ exp' if reconstructed == n else 'НЕ СОВПАДАЕТ'}")

    digit_sum = sum(digits_manual)
    print(f"Сумма всех цифр числа 2 ^ {exp}: {digit_sum}")

    print("=" * 60)


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")