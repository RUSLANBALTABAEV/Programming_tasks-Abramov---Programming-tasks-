"""
ГЛАВА 2
ЗАДАЧИ ПО ТЕМАМ
15. Целые числа.

568. Дано натуральное число m. Вставить между некоторыми цифрами 1, 2, 3, 4, 5, 6, 7, 8, 9 записанными именно в таком порядке, знаки +, - так, чтобы значением получившегося выражения было число m. Например, если m = 122, то подойдет следующая расстановка знаков: 12 + 34 - 5 - 6 + 78 + 9. Если требуемая расстановка знаков невозможна, то сообщить об этом.
"""


import random
from itertools import product


def get_m():
    """Выбор способа ввода натурального числа m."""
    print("Задача 568: Расстановка знаков + и - между цифрами 1..9")
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
                m = int(input("Введите натуральное число m (> 0): "))
                if m <= 0:
                    print("m должно быть > 0.")
                    continue
                return m
            except ValueError:
                print("Ошибка ввода. Повторите.")

    elif choice == '2':
        m = random.randint(1, 500)
        print(f"\nСгенерировано m = {m}")
        return m

    else:  # готовые примеры
        examples = [122, 100, 45, 1, 999]
        print("\nГотовые примеры m:")
        for idx, val in enumerate(examples, 1):
            print(f"{idx}: m = {val}")
        while True:
            try:
                num = int(input("Выберите номер примера: "))
                if 1 <= num <= len(examples):
                    return examples[num - 1]
                else:
                    print(f"Номер должен быть от 1 до {len(examples)}.")
            except ValueError:
                print("Ошибка ввода. Введите целое число.")


def evaluate_expression(expr):
    """
    Вычисляет значение выражения expr, содержащего только цифры и знаки +, -.
    Реализовано без eval() — через ручной разбор строки.
    """
    total = 0
    current = 0
    sign = 1  # +1 для плюса, -1 для минуса
    for ch in expr:
        if ch.isdigit():
            current = current * 10 + int(ch)
        elif ch == '+':
            total += sign * current
            current = 0
            sign = 1
        elif ch == '-':
            total += sign * current
            current = 0
            sign = -1
    total += sign * current  # последний токен
    return total


def find_expressions(m):
    """
    Возвращает список всех выражений, равных m, с расстановкой знаков
    '', '+', '-' между цифрами 1..9 в этом порядке.
    """
    digits = "123456789"
    operators = ['', '+', '-']
    solutions = []

    for combo in product(operators, repeat=8):
        expr = digits[0]
        for i, op in enumerate(combo):
            expr += op + digits[i + 1]
        if evaluate_expression(expr) == m:
            solutions.append(expr)
    return solutions


def main():
    m = get_m()
    solutions = find_expressions(m)

    print(f"\nПоиск выражений, равных {m}:")
    print("-" * 60)

    if solutions:
        print(f"Найдено решений: {len(solutions)}")
        # Показываем первые 10 решений для компактности
        for i, expr in enumerate(solutions[:10], 1):
            print(f"  {i:>2}. {expr} = {m}")
        if len(solutions) > 10:
            print(f"  ... и ещё {len(solutions) - 10} решений.")
    else:
        print(f"Невозможно расставить знаки + и - между цифрами 1..9,")
        print(f"чтобы получить число {m}.")
    print("-" * 60)


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")