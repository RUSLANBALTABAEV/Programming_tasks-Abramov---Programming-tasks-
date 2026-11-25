"""
ГЛАВА 2
ЗАДАЧИ ПО ТЕМАМ
16. Системы счисления

588. Дано натуральное число p. Получить последовательность a0, ... an, каждый член которой равен –1, 0 или 1, такую что p = an * 3 ^ n + ... + a1 * 3 + a0 * (an != 0).
"""


# ==========================================================
# ЗАДАЧА 588: Уравновешенная троичная система счисления
# §16. Системы счисления
# ==========================================================

import random


def get_params():
    """Выбор способа ввода числа p."""
    print("Задача 588: Представление числа p в уравновешенной троичной системе")
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
                return p
            except ValueError:
                print("Ошибка ввода. Введите целое число.")

    elif choice == '2':
        p = random.randint(1, 100000)
        print(f"\nСгенерировано: p = {p}")
        return p

    else:  # готовые примеры
        examples = [5, 8, 10, 42, 1000, 12345]
        print("\nГотовые примеры (p):")
        for idx, pv in enumerate(examples, 1):
            print(f"{idx}: p = {pv}")
        while True:
            try:
                num = int(input("Выберите номер примера: "))
                if 1 <= num <= len(examples):
                    return examples[num - 1]
                else:
                    print(f"Номер должен быть от 1 до {len(examples)}.")
            except ValueError:
                print("Ошибка ввода. Введите целое число.")


def to_balanced_ternary(p):
    """
    Возвращает список цифр (a_n, ..., a_0) числа p в уравновешенной
    троичной системе. Цифры могут быть -1, 0 или 1.

    Алгоритм: делим p на 3.
    - Если остаток 0, цифра 0.
    - Если остаток 1, цифра 1, отнимаем 1 и делим на 3.
    - Если остаток 2 (это -1 по модулю 3), цифра -1, прибавляем 1 и делим на 3.
    """
    if p <= 0:
        raise ValueError("p должно быть натуральным (p > 0)")

    digits = []
    while p > 0:
        remainder = p % 3
        if remainder == 0:
            digits.append(0)
            p = p // 3
        elif remainder == 1:
            digits.append(1)
            p = (p - 1) // 3
        else:  # remainder == 2
            digits.append(-1)
            p = (p + 1) // 3
            
    return digits[::-1]  # старшие разряды — первыми


def digits_to_string(digits):
    """
    Преобразует список цифр в строковое представление.
    Для наглядности -1 заменяется на символ 'T' (или '-').
    """
    # Используем 'T' для -1 (от слова True/Two) или '-' для минуса
    return "".join('1' if d == 1 else ('0' if d == 0 else 'T') for d in digits)


def power_decomposition(p, digits):
    """Возвращает строку-разложение p = a_n * 3^n + ... + a_0."""
    n = len(digits) - 1
    terms = []
    for i, d in enumerate(digits):
        if d == 0:
            continue
        power = n - i
        if power == 0:
            terms.append(f"({d})" if d == -1 else f"{d}")
        elif power == 1:
            terms.append(f"({d}) * 3" if d == -1 else f"{d} * 3")
        else:
            terms.append(f"({d}) * 3^{power}" if d == -1 else f"{d} * 3^{power}")
            
    if not terms:
        return f"{p} = 0"
    return f"{p} = " + " + ".join(terms)


def main():
    p = get_params()
    digits = to_balanced_ternary(p)

    print(f"\nИсходные данные: p = {p}")
    print("=" * 60)

    # 1. Последовательность цифр
    print(f"Последовательность цифр (a_n, ..., a_0):")
    print(f"  {digits}")
    print(f"Количество разрядов: {len(digits)}")

    # 2. Строковое представление
    string_repr = digits_to_string(digits)
    print(f"\nЗапись в уравновешенной троичной системе: {string_repr}")
    print("  (где T обозначает -1)")

    # 3. Разложение в сумму степеней
    print(f"\nРазложение:")
    print(f"  {power_decomposition(p, digits)}")

    # 4. Проверки
    print("\n--- Проверка ---")

    # 4.1. Схема Горнера: собираем число обратно (база 3)
    reconstructed = 0
    for d in digits:
        reconstructed = reconstructed * 3 + d
    print(f"Сборка по схеме Горнера: {reconstructed}  (совпадает: {reconstructed == p})")

    # 4.2. Проверка по формуле a_n*3^n + ... + a_0
    n = len(digits) - 1
    formula_value = sum(d * (3 ** (n - i)) for i, d in enumerate(digits))
    print(f"Проверка по формуле суммы: {formula_value}  (совпадает: {formula_value == p})")

    print("=" * 60)


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")