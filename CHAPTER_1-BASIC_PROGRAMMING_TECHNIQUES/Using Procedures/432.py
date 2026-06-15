"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
12. Использование процедур 

В задачах этого параграфа будем для краткости говорить просто о процедурах, подразумевая, что решающий задачи сам выберет подходящее средство программирования – подпрограмму, функцию и 
т. д. Этот выбор должен быть сделан с учётом как характера задач, так и особенностей используемого языка программирования.

432. Даны действительные числа a0, ..., a6. Получить для x=1, 3, 4 значения p(x + 1) - p(x), где 
p * (y) = a6 * y ^ 6 + a5 * y ^ 5 + ... + a0.
"""


import random


def p(y, coeffs):
    """
    Вычисляет значение полинома p(y) = a0 + a1*y + a2*y^2 + ... + a6*y^6.
    coeffs: список [a0, a1, a2, a3, a4, a5, a6].
    """
    result = 0.0
    for i, a in enumerate(coeffs):
        result += a * (y ** i)
    return result


def get_coeffs():
    """Выбор способа ввода коэффициентов a0..a6."""
    print("Задача 432: p(x + 1) - p(x) для x = 1, 3, 4")
    print("Выберите способ ввода коэффициентов:")
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
                print("Введите 7 действительных чисел a0 a1 ... a6 через пробел:")
                coeffs = list(map(float, input().split()))
                if len(coeffs) != 7:
                    print("Ошибка: нужно ровно 7 чисел.")
                    continue
                return coeffs
            except ValueError:
                print("Ошибка ввода. Повторите.")

    elif choice == '2':
        coeffs = [round(random.uniform(-5, 5), 2) for _ in range(7)]
        print(f"Сгенерированы коэффициенты: {coeffs}")
        return coeffs

    else:  # готовые примеры
        examples = [
            [1.0, 2.0, 3.0, 0.0, 0.0, 0.0, 0.0],  # 1 + 2y + 3y²
            [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0],  # y + y^6
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0],  # y^6
            [1.0, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0], # знакопеременный
        ]
        print("Готовые примеры коэффициентов:")
        for idx, coeffs in enumerate(examples, 1):
            print(f"{idx}: {coeffs}")
        while True:
            try:
                num = int(input("Выберите номер примера: "))
                if 1 <= num <= len(examples):
                    return examples[num - 1]
                else:
                    print(f"Номер должен быть от 1 до {len(examples)}.")
            except ValueError:
                print("Ошибка ввода. Введите целое число.")


def main():
    coeffs = get_coeffs()

    print("\nКоэффициенты полинома (a0..a6):", coeffs)

    x_values = [1, 3, 4]
    print("\nРезультаты:")
    for x in x_values:
        diff = p(x + 1, coeffs) - p(x, coeffs)
        print(f"  p({x+1}) - p({x}) = {diff:.6f}")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
