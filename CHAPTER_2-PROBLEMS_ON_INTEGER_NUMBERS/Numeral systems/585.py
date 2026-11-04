"""
ГЛАВА 2
ЗАДАЧИ ПО ТЕМАМ
16. Системы счисления

585. Дано натуральное число p. Получить двоичное представление числа p в виде последовательности a0, ..., an нулей и единиц такой, что p = an * 2 ^ n + ... + a1 * 2 + a0 (an != 0).
"""


# ==========================================================
# ЗАДАЧА 585: Двоичное представление числа p
# §16. Системы счисления
# ==========================================================

import random


def get_p():
    """Выбор способа ввода числа p."""
    print("Задача 585: Двоичное представление числа p")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод")
    print("2 — Случайная генерация")
    print("3 — Готовые примеры")

    while True:
        choice = input("Ваш выбор (1/2/3): ").strip()
        if choice in ('1', '2', '3'):
            break
        print("Ошибка: выберите 1, 2 или 3.")

    if choice == '1':
        while True:
            try:
                p = int(input("Введите натуральное число p (> 0): "))
                if p <= 0:
                    print("p должно быть натуральным (p > 0).")
                    continue
                return p
            except ValueError:
                print("Ошибка ввода. Введите целое число.")

    elif choice == '2':
        p = random.randint(1, 1000)
        print(f"\nСгенерировано p = {p}")
        return p

    else:  # готовые примеры
        examples = [1, 2, 3, 5, 10, 15, 100, 255, 256, 1023]
        print("\nГотовые примеры p:")
        for idx, val in enumerate(examples, 1):
            print(f"{idx}: p = {val}")
        while True:
            try:
                num = int(input("Выберите номер примера: "))
                if 1 <= num <= len(examples):
                    return examples[num - 1]
                else:
                    print(f"Номер должен быть от 1 до {len(examples)}.")
            except ValueError:
                print("Ошибка ввода. Введите целое число.")


def to_binary_digits(p):
    """
    Возвращает список цифр (a_n, a_{n-1}, ..., a_0) двоичного представления p.
    Старший разряд a_n всегда равен 1 (при p > 0).
    """
    if p <= 0:
        raise ValueError("p должно быть натуральным (p > 0)")
    bits = []
    while p > 0:
        bits.append(p % 2)   # остаток от деления на 2 — младшая цифра
        p //= 2
    return bits[::-1]        # старшие разряды — первыми


def power_decomposition(digits):
    """
    Возвращает строку-разложение числа в сумму степеней двойки
    по его двоичным цифрам (старшие — первыми).
    """
    terms = []
    n = len(digits) - 1
    for i, d in enumerate(digits):
        if d == 1:
            power = n - i
            if power == 0:
                terms.append("1")
            elif power == 1:
                terms.append("2")
            else:
                terms.append(f"2 ^ {power}")
    return " + ".join(terms)


def main():
    p = get_p()
    digits = to_binary_digits(p)

    print(f"\nИсходное число: p = {p}")
    print("=" * 60)

    # 1. Двоичное представление
    binary_str = "".join(map(str, digits))
    print(f"Двоичное представление: {binary_str}")
    if len(digits) <= 60:
        print(f"Последовательность (a_n, ..., a_0): {digits}")
    else:
        print(f"Последовательность (первые 30): {digits[:30]}")
        print(f"Последовательность (последние 30): {digits[-30:]}")

    # 2. Статистика
    n_bits = len(digits)
    n_ones = sum(digits)
    n_zeros = n_bits - n_ones
    print(f"\nКоличество разрядов: {n_bits}")
    print(f"Единиц: {n_ones}, нулей: {n_zeros}")

    # 3. Разложение в сумму степеней двойки
    decomposition = power_decomposition(digits)
    if len(decomposition) <= 100:
        print(f"\nРазложение: {p} = {decomposition}")
    else:
        print(f"\nРазложение (первые 100 символов):")
        print(f"  {p} = {decomposition[:100]}...")

    # 4. Проверки
    print("\n--- Проверка ---")
    builtin_bits = [int(ch) for ch in bin(p)[2:]]
    print(f"Совпадает с bin(p)[2:]: {digits == builtin_bits}")

    reconstructed = 0
    for d in digits:
        reconstructed = reconstructed * 2 + d
    print(f"Восстановленное значение из цифр: {reconstructed}")
    print(f"Совпадает с p: {reconstructed == p}")

    # 5. Проверка через формулу an*2^n + ... + a0
    n = len(digits) - 1
    formula_value = sum(d * (2 ** (n - i)) for i, d in enumerate(digits))
    print(f"Проверка по формуле a_n * 2^n + ... + a_0 = {formula_value}")
    print(f"Совпадает с p: {formula_value == p}")

    print("=" * 60)


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")