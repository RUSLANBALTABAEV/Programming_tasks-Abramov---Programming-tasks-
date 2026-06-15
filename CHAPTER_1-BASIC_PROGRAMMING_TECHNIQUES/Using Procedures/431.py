"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
12. Использование процедур 

В задачах этого параграфа будем для краткости говорить просто о процедурах, подразумевая, что решающий задачи сам выберет подходящее средство программирования – подпрограмму, функцию и 
т. д. Этот выбор должен быть сделан с учётом как характера задач, так и особенностей используемого языка программирования.

431. Даны действительные числа s, t. Получить 
h(s, t) + max(h ^ 2 * (s - t, s * t), h ^ 4 * (s - t, s + t)) + h(1, 1),
где
h * (a, b) = a / (1 + b * b) + b / (1 + a * a) - (a - b) * (a - b) * (a - b).
"""


import random


def h(a, b):
    """Вычисляет h(a,b) = a/(1+b²) + b/(1+a²) - (a-b)³."""
    return a / (1 + b * b) + b / (1 + a * a) - (a - b) ** 3


def get_params():
    """Выбор способа ввода чисел s и t."""
    print("Задача 431: h(s, t) + max(h²(s - t, s * t), h⁴(s - t, s + t) ) + h(1,1)")
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

    h1 = h(s, t)                        # h(s,t)
    h2 = h(s - t, s * t)                # h(s-t, s*t)
    h3 = h(s - t, s + t)                # h(s-t, s+t)
    h4 = h(1, 1)                        # h(1,1)

    term2 = max(h2 ** 2, h3 ** 4)       # max( h²(...), h⁴(...) )
    result = h1 + term2 + h4

    print("\nРезультаты:")
    print(f"  h(s, t)            = {h1:.6f}")
    print(f"  h(s - t, s * t)    = {h2:.6f}   (квадрат = {h2 ** 2:.6f})")
    print(f"  h(s - t, s + t)    = {h3:.6f}   (4-я степень = {h3 ** 4:.6f})")
    print(f"  max(квадрат, 4-я)  = {term2:.6f}")
    print(f"  h(1, 1)            = {h4:.6f}")
    print(f"  Итоговый результат = {result:.6f}")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
