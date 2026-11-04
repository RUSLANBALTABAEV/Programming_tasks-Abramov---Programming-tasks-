"""
ГЛАВА 2
ЗАДАЧИ ПО ТЕМАМ
16. Системы счисления

583. Получить последовательность dk, dk-1, ..., d0 десятичных цифр числа 100!, т.е. такую целочисленную последовательность, в которой каждый член di удовлетворяет условию 0 <= di <= 9 и, дополнительно, dk * 10 ^ k + dk-1 * 10 ^ k - 1 + ... + d0 = 100!.
"""


# ==========================================================
# ЗАДАЧА 583: Последовательность десятичных цифр числа n!
# §16. Системы счисления
# ==========================================================

import math


def factorial_digits_manual(n):
    """
    Возвращает список десятичных цифр числа n! (старшие разряды первыми).
	
    Ручной алгоритм длинной арифметики:
      - начинаем с 1 (младший разряд);
      - для i = 2..n умножаем массив цифр на i с переносом;
      - в конце разворачиваем массив, чтобы старшие разряды шли первыми.
    """
    digits = [1]  # 0! = 1, 1! = 1
    for i in range(2, n + 1):
        carry = 0
        for j in range(len(digits)):
            prod = digits[j] * i + carry
            digits[j] = prod % 10
            carry = prod // 10
        while carry:
            digits.append(carry % 10)
            carry //= 10
    return digits[::-1]


def get_n():
    """Выбор способа ввода n (по умолчанию — 100)."""
    print("Задача 583: Последовательность десятичных цифр числа n!")
    print("Выберите способ ввода n:")
    print("1 — Ручной ввод")
    print("2 — Случайная генерация (1..200)")
    print("3 — По условию (n = 100)")

    while True:
        choice = input("Ваш выбор (1/2/3): ").strip()
        if choice in ('1', '2', '3'):
            break
        print("Ошибка: выберите 1, 2 или 3.")

    if choice == '1':
        while True:
            try:
                n = int(input("Введите n (1 <= n <= 500): "))
                if n < 1 or n > 500:
                    print("n должно быть в диапазоне от 1 до 500.")
                    continue
                return n
            except ValueError:
                print("Ошибка ввода. Введите целое число.")

    elif choice == '2':
        import random
        n = random.randint(1, 200)
        print(f"\nСгенерировано n = {n}")
        return n

    else:
        print("\nИспользуется n = 100 (по условию).")
        return 100


def main():
    n = get_n()

    print(f"\nВычисление {n}! ...")
    print("=" * 70)

    # 1. Ручной алгоритм
    digits_manual = factorial_digits_manual(n)

    # 2. Встроенная проверка
    fact = math.factorial(n)
    digits_direct = [int(ch) for ch in str(fact)]

    # 3. Вывод результата
    print(f"Цифры числа {n}! (d_k, ..., d_0):")
    if len(digits_manual) <= 80:
        print(digits_manual)
    else:
        print(f"  первые 40: {digits_manual[:40]}")
        print(f"  последние 40: {digits_manual[-40:]}")

    print(f"\nКоличество цифр: {len(digits_manual)}")
    print(f"Сумма цифр: {sum(digits_manual)}")

    # 4. Проверка
    print("\n--- Проверка ---")
    print(f"Ручной алгоритм совпадает с math.factorial: "
          f"{digits_manual == digits_direct}")

    reconstructed = 0
    for d in digits_manual:
        reconstructed = reconstructed * 10 + d
    print(f"Восстановленное число из цифр совпадает с {n}!: "
          f"{reconstructed == fact}")

    # 5. Вывод самого числа (для наглядности)
    print(f"\n{n}! =")
    if len(str(fact)) <= 100:
        print(fact)
    else:
        s = str(fact)
        groups = [s[max(0, i - 5):i] for i in range(len(s), 0, -5)][::-1]
        print(" ".join(groups))

    print("=" * 70)


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")