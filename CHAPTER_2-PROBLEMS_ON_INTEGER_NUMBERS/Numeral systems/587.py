"""
ГЛАВА 2
ЗАДАЧИ ПО ТЕМАМ
16. Системы счисления

587. Даны действительное число x и натуральное число q (0 <= x < 1, q >= 2). Получить пять цифр q-ичного представления числа x, т.е. получить последовательность целых неотрицательных a-1, ..., a-5 такую, что x = a-1 * q - 1 + ... + a-5 * q ^ -5 + r, 0 <= ai <= q - 1, r < q ^ -5.
"""


# ==========================================================
# ЗАДАЧА 587: Получение 5 цифр дробной части в q-ичной системе
# §16. Системы счисления
# ==========================================================

import random

DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # для q <= 36


def get_params():
    """Выбор способа ввода x и q."""
    print("Задача 587: 5 цифр q-ичного представления дробного числа x")
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
                x = float(input("Введите действительное число x (0 <= x < 1): "))
                if not (0 <= x < 1):
                    print("x должно быть в диапазоне [0, 1).")
                    continue
                q = int(input("Введите основание q (2 <= q <= 36): "))
                if q < 2 or q > 36:
                    print("q должно быть в диапазоне от 2 до 36.")
                    continue
                return x, q
            except ValueError:
                print("Ошибка ввода. Проверьте формат чисел.")

    elif choice == '2':
        # Генерируем случайное дробное число
        x = random.random()
        q = random.randint(2, 36)
        print(f"\nСгенерированы: x = {x:.6f}, q = {q}")
        return x, q

    else:  # готовые примеры
        examples = [
            (0.5, 2),
            (0.1, 3),
            (0.123, 10),
            (0.75, 16),
            (0.999, 7),
            (0.31415926, 4),
        ]
        print("\nГотовые примеры (x, q):")
        for idx, (xv, qv) in enumerate(examples, 1):
            print(f"{idx}: x = {xv}, q = {qv}")
        while True:
            try:
                num = int(input("Выберите номер примера: "))
                if 1 <= num <= len(examples):
                    return examples[num - 1]
                else:
                    print(f"Номер должен быть от 1 до {len(examples)}.")
            except ValueError:
                print("Ошибка ввода. Введите целое число.")


def to_base_q_fraction(x, q, count=5):
    """
    Возвращает список из `count` цифр (a_1, ..., a_count) и остаток r.
    Алгоритм: умножаем дробную часть на q, целая часть — очередная цифра.
    """
    if not (0 <= x < 1):
        raise ValueError("x должно быть в диапазоне [0, 1)")
    if q < 2:
        raise ValueError("q должно быть >= 2")

    digits = []
    remainder = x
    for _ in range(count):
        remainder *= q
        digit = int(remainder)  # отбрасываем дробную часть (floor)
        digits.append(digit)
        remainder -= digit      # оставляем только дробную часть

    # Истинный остаток r = remainder * q^(-count)
    r = remainder * (q ** (-count))
    return digits, r


def digits_to_string(digits, q):
    """
    Преобразует список цифр в строковое представление (после запятой).
    Для q > 10 использует буквы A, B, C, ...
    """
    if q <= 36:
        return "".join(DIGITS[d] for d in digits)
    else:
        # Для оснований > 36 используем формат [d]
        return "".join(f"[{d}]" for d in digits)


def power_decomposition(x, digits, q, r):
    """Возвращает строку-разложение x = a_1*q^(-1) + ... + a_5*q^(-5) + r."""
    terms = []
    for i, d in enumerate(digits):
        power = -(i + 1)
        if power == -1:
            terms.append(f"{d} * {q}^(-1)")
        else:
            terms.append(f"{d} * {q}^({power})")
    
    # Формируем красивую строку
    decomp = f"{x} = " + " + ".join(terms) + f" + r"
    return decomp


def main():
    x, q = get_params()
    digits, r = to_base_q_fraction(x, q, count=5)

    print(f"\nИсходные данные: x = {x}, q = {q}")
    print("=" * 60)

    # 1. Последовательность цифр
    print(f"Последовательность цифр (a_1, ..., a_5):")
    print(f"  {digits}")
    print(f"Количество цифр: {len(digits)}")

    # 2. Строковое представление
    string_repr = digits_to_string(digits, q)
    print(f"\nДробная часть в {q}-ичной системе: 0.{string_repr}")

    # 3. Разложение в сумму отрицательных степеней
    print(f"\nРазложение:")
    print(f"  {power_decomposition(x, digits, q, r)}")

    # 4. Проверки
    print("\n--- Проверка ---")

    # 4.1. Сборка числа обратно
    reconstructed = sum(d * (q ** -(i + 1)) for i, d in enumerate(digits))
    print(f"Сумма цифр без остатка: {reconstructed:.10f}")
    print(f"Исходное x:            {x:.10f}")

    # 4.2. Проверка формулы x = reconstructed + r
    total = reconstructed + r
    print(f"Сложение с остатком r: {total:.10f}  (совпадает: {abs(total - x) < 1e-9})")

    # 4.3. Проверка условия r < q^(-5)
    limit = q ** (-5)
    print(f"Остаток r: {r:.10e}")
    print(f"Граница q^(-5): {limit:.10e}")
    print(f"Условие r < q^(-5): {r < limit + 1e-15}")  # +epsilon для погрешности float

    print("=" * 60)


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")