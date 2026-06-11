"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
12. Использование процедур 

В задачах этого параграфа будем для краткости говорить просто о процедурах, подразумевая, что решающий задачи сам выберет подходящее средство программирования – подпрограмму, функцию и 
т. д. Этот выбор должен быть сделан с учётом как характера задач, так и особенностей используемого языка программирования.

424. Даны действительные числа s, t. Получить
f(t, - 2 * s, 1.17) + f(2.2, t, s - t),
где
f(a, b, c) = (2 * a - b - sin(c)) / (5 + abs(c))
"""


import math
import random


def f(a, b, c):
    """Вычисляет значение f(a,b,c) = (2a - b - sin c) / (5 + |c|)."""
    numerator = 2 * a - b - math.sin(c)
    denominator = 5 + abs(c)
    return numerator / denominator


def get_params():
    """Выбор способа ввода чисел s и t."""
    print("Задача 424: Вычисление f(t,-2s,1.17) + f(2.2,t,s-t)")
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
                s = float(input("Введите действительное число s: "))
                t = float(input("Введите действительное число t: "))
                return s, t
            except ValueError:
                print("Ошибка ввода. Повторите.")

    elif choice == '2':
        s = round(random.uniform(-5, 5), 2)
        t = round(random.uniform(-5, 5), 2)
        print(f"Сгенерированы числа: s = {s}, t = {t}")
        return s, t

    else:  # готовые примеры
        examples = [
            (1.0, 2.0),
            (0.0, -1.0),
            (3.5, -2.7),
            (0.5, 0.5),
            (-4.0, 6.0)
        ]
        print("Готовые примеры:")
        for idx, (s_val, t_val) in enumerate(examples, 1):
            print(f"{idx}: s = {s_val}, t = {t_val}")
        while True:
            try:
                num = int(input("Выберите номер примера: "))
                if 1 <= num <= len(examples):
                    return examples[num-1]
                else:
                    print(f"Номер должен быть от 1 до {len(examples)}.")
            except ValueError:
                print("Ошибка ввода. Введите целое число.")


def main():
    s, t = get_params()

    term1 = f(t, -2 * s, 1.17)
    term2 = f(2.2, t, s - t)
    result = term1 + term2

    print("\nРезультаты:")
    print(f"  f(t, -2s, 1.17) = {term1:.6f}")
    print(f"  f(2.2, t, s-t)  = {term2:.6f}")
    print(f"  Итоговая сумма    = {result:.6f}")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
