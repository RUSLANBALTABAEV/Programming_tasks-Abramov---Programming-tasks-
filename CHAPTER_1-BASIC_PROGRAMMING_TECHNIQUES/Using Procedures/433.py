"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
12. Использование процедур 

В задачах этого параграфа будем для краткости говорить просто о процедурах, подразумевая, что решающий задачи сам выберет подходящее средство программирования – подпрограмму, функцию и 
т. д. Этот выбор должен быть сделан с учётом как характера задач, так и особенностей используемого языка программирования.

433. Даны действительные числа s, t, a0, …, a12. Получить
p * (1) - p * (t) + p * p * (s - t) - p * p * p * (1),
где
p * (x) = a12 * x ^ 12 + a11 * x ^ 11 + ... + a0.
"""


import random


def p(x, coeffs):
    """
    Вычисляет значение полинома p(x) = a0 + a1·x + a2·x² + … + a12·x¹².
    coeffs – список коэффициентов [a0, a1, …, a12].
    """
    result = 0.0
    for i, a in enumerate(coeffs):
        result += a * (x ** i)
    return result


def get_params():
    """Выбор способа ввода чисел s, t и коэффициентов полинома a0…a12."""
    print("Задача 433: p(1) - p(t) + p²(s-t) - p³(1)")
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
                print("Введите 13 коэффициентов a0 a1 … a12 через пробел:")
                coeffs = list(map(float, input().split()))
                if len(coeffs) != 13:
                    print("Ошибка: нужно ровно 13 коэффициентов.")
                    continue
                return s, t, coeffs
            except ValueError:
                print("Ошибка ввода. Повторите.")

    elif choice == '2':
        s = round(random.uniform(-5, 5), 2)
        t = round(random.uniform(-5, 5), 2)
        coeffs = [round(random.uniform(-3, 3), 2) for _ in range(13)]
        print(f"Сгенерированы s = {s}, t = {t}")
        print(f"Коэффициенты: {coeffs}")
        return s, t, coeffs

    else:  # готовые примеры
        examples = [
            (2.0, 1.0,
             [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]),  # p(x)=1 + x^12
            (0.0, 2.0,
             [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]),  # p(x)=x
            (-1.0, 3.0,
             [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]),  # p(x)=x²
        ]
        print("Готовые примеры:")
        for idx, (s_val, t_val, coeffs_arr) in enumerate(examples, 1):
            print(f"{idx}: s = {s_val}, t = {t_val}, coeffs = {coeffs_arr}")
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
    s, t, coeffs = get_params()

    p1 = p(1, coeffs)
    pt = p(t, coeffs)
    pst = p(s - t, coeffs)

    result = p1 - pt + pst ** 2 - p1 ** 3

    print("\nРезультаты:")
    print(f"  p(1)      = {p1:.6f}")
    print(f"  p(t)      = {pt:.6f}")
    print(f"  p(s - t)  = {pst:.6f}")
    print(f"  p(1) - p(t) + p²(s - t) - p³(1) = {result:.6f}")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
