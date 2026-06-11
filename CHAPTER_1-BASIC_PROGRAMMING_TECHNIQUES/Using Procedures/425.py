"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
12. Использование процедур 

В задачах этого параграфа будем для краткости говорить просто о процедурах, подразумевая, что решающий задачи сам выберет подходящее средство программирования – подпрограмму, функцию и 
т. д. Этот выбор должен быть сделан с учётом как характера задач, так и особенностей используемого языка программирования.

425. Даны действительные числа s, t. Получить
g(1.2, s) + g(t, s) - g(2 * s - 1, s * t),
где
g(a, b) = (a * a + b * b) / (a * a + 2 * a * b + 3 * b * b + 4).
"""


import random


def g(a, b):
    """Вычисляет g(a,b) = (a² + b²) / (a² + 2ab + 3b² + 4)."""
    numerator = a * a + b * b
    denominator = a * a + 2 * a * b + 3 * b * b + 4
    return numerator / denominator


def get_params():
    """Выбор способа ввода чисел s и t."""
    print("Задача 425: g(1.2, s) + g(t, s) - g(2s - 1, s * t)")
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

    term1 = g(1.2, s)
    term2 = g(t, s)
    term3 = g(2 * s - 1, s * t)
    result = term1 + term2 - term3

    print("\nРезультаты:")
    print(f"  g(1.2, s)      = {term1:.6f}")
    print(f"  g(t, s)        = {term2:.6f}")
    print(f"  g(2s - 1, s * t)   = {term3:.6f}")
    print(f"  Итоговый результат = {result:.6f}")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
