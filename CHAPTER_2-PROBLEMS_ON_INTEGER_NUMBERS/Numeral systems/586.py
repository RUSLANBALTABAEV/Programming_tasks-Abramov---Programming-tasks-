"""
ГЛАВА 2
ЗАДАЧИ ПО ТЕМАМ
16. Системы счисления

586. Даны натуральные числа p и q(q >= 2). Получить q-ичное представление числа p в виде такой последовательности a0, ..., an целых неотрицательных чисел что ai < q (i = 0, ..., n) и p = an * q ^ n + ... + a1 * q + a0  (an != 0)
"""


# ==========================================================
# ЗАДАЧА 586: Перевод числа p в q-ичную систему счисления
# §16. Системы счисления
# ==========================================================

import random

DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # для q <= 36


def get_params():
    """Выбор способа ввода p и q."""
    print("Задача 586: Перевод числа p в q-ичную систему счисления")
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
                    print("p должно быть > 0.")
                    continue
                q = int(input("Введите основание q (2 <= q <= 36): "))
                if q < 2 or q > 36:
                    print("q должно быть в диапазоне от 2 до 36.")
                    continue
                return p, q
            except ValueError:
                print("Ошибка ввода. Введите целые числа.")

    elif choice == '2':
        p = random.randint(1, 100000)
        q = random.randint(2, 36)
        print(f"\nСгенерированы: p = {p}, q = {q}")
        return p, q

    else:  # готовые примеры
        examples = [
            (255, 2),
            (255, 8),
            (255, 16),
            (1000, 7),
            (12345, 3),
            (10 ** 9, 36),
        ]
        print("\nГотовые примеры (p, q):")
        for idx, (pv, qv) in enumerate(examples, 1):
            print(f"{idx}: p = {pv}, q = {qv}")
        while True:
            try:
                num = int(input("Выберите номер примера: "))
                if 1 <= num <= len(examples):
                    return examples[num - 1]
                else:
                    print(f"Номер должен быть от 1 до {len(examples)}.")
            except ValueError:
                print("Ошибка ввода. Введите целое число.")


def to_base_q(p, q):
    """
    Возвращает список цифр (a_n, ..., a_0) числа p в системе счисления
    с основанием q. Старший разряд a_n != 0 (при p > 0).

    Алгоритм: последовательно делим p на q и собираем остатки,
    пока p не станет равным нулю. Разворачиваем результат.
    """
    if p <= 0:
        raise ValueError("p должно быть натуральным (p > 0)")
    if q < 2:
        raise ValueError("q должно быть >= 2")

    digits = []
    while p > 0:
        digits.append(p % q)  # остаток — младшая цифра
        p //= q
    return digits[::-1]  # старшие разряды — первыми


def digits_to_string(digits, q):
    """
    Преобразует список цифр в строковое представление.
    Для q > 10 использует буквы A, B, C, ... (до Z для q = 36).
    """
    if q <= 36:
        return "".join(DIGITS[d] for d in digits)
    else:
        # Для оснований > 36 используем формат [d] через разделитель
        return "".join(f"[{d}]" for d in digits)


def power_decomposition(p, digits, q):
    """Возвращает строку-разложение p = a_n * q^n + ... + a_0."""
    n = len(digits) - 1
    terms = []
    for i, d in enumerate(digits):
        if d == 0:
            continue
        power = n - i
        if power == 0:
            terms.append(f"{d}")
        elif power == 1:
            terms.append(f"{d} * {q}")
        else:
            terms.append(f"{d} * {q}^{power}")
    return f"{p} = " + " + ".join(terms)


def main():
    p, q = get_params()
    digits = to_base_q(p, q)

    print(f"\nИсходные данные: p = {p}, q = {q}")
    print("=" * 60)

    # 1. Двоичное/восьмеричное/etc. представление в виде списка
    print(f"Последовательность цифр (a_n, ..., a_0):")
    if len(digits) <= 60:
        print(f"  {digits}")
    else:
        print(f"  первые 30: {digits[:30]}")
        print(f"  последние 30: {digits[-30:]}")
    print(f"Количество разрядов: {len(digits)}")

    # 2. Строковое представление
    string_repr = digits_to_string(digits, q)
    print(f"\nЗапись в {q}-ичной системе: {string_repr}")

    # 3. Разложение в сумму степеней
    print(f"\nРазложение:")
    print(f"  {power_decomposition(p, digits, q)}")

    # 4. Проверки
    print("\n--- Проверка ---")

    # 4.1. Схема Горнера: собираем число обратно
    reconstructed = 0
    for d in digits:
        reconstructed = reconstructed * q + d
    print(f"Сборка по схеме Горнера: {reconstructed}  (совпадает: {reconstructed == p})")

    # 4.2. Независимая проверка через int(string, q)
    if q <= 36:
        builtin_value = int(string_repr, q)
        print(f"Проверка через int('{string_repr}', {q}): {builtin_value}  (совпадает: {builtin_value == p})")

    # 4.3. Проверка по формуле a_n*q^n + ... + a_0
    n = len(digits) - 1
    formula_value = sum(d * (q ** (n - i)) for i, d in enumerate(digits))
    print(f"Проверка по формуле a_n * q^n + ... + a_0: {formula_value}  (совпадает: {formula_value == p})")

    print("=" * 60)


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")