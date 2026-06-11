"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
12. Использование процедур 

В задачах этого параграфа будем для краткости говорить просто о процедурах, подразумевая, что решающий задачи сам выберет подходящее средство программирования – подпрограмму, функцию и 
т. д. Этот выбор должен быть сделан с учётом как характера задач, так и особенностей используемого языка программирования.

427. Даны действительные числа а, b, с. Получить 
(max(a, a + b) + max(a, b + c)) / (1 + max(a + b * c, 1, 15).
"""


import random


def get_params():
    """Выбор способа ввода чисел a, b, c."""
    print("Задача 427: Вычисление выражения с max")
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
                a = float(input("Введите действительное число a: "))
                b = float(input("Введите действительное число b: "))
                c = float(input("Введите действительное число c: "))
                return a, b, c
            except ValueError:
                print("Ошибка ввода. Повторите.")

    elif choice == '2':
        a = round(random.uniform(-10, 10), 2)
        b = round(random.uniform(-10, 10), 2)
        c = round(random.uniform(-10, 10), 2)
        print(f"Сгенерированы числа: a = {a}, b = {b}, c = {c}")
        return a, b, c

    else:  # готовые примеры
        examples = [
            (1.0, 2.0, 3.0),
            (0.0, -1.0, 5.0),
            (4.5, 2.3, -1.7),
            (10.0, -5.0, 2.0),
            (0.0, 0.0, 0.0)
        ]
        print("Готовые примеры:")
        for idx, (a_val, b_val, c_val) in enumerate(examples, 1):
            print(f"{idx}: a = {a_val}, b = {b_val}, c = {c_val}")
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
    a, b, c = get_params()

    # Числитель
    term1 = max(a, a + b)
    term2 = max(a, b + c)
    numerator = term1 + term2

    # Знаменатель
    denominator = 1 + max(a + b * c, 1, 15)

    result = numerator / denominator

    print("\nРезультаты:")
    print(f"  max(a, a + b)       = {term1}")
    print(f"  max(a, b + c)       = {term2}")
    print(f"  Числитель         = {numerator}")
    print(f"  max(a + b * c, 1, 15) = {max(a + b * c, 1, 15)}")
    print(f"  Знаменатель       = {denominator}")
    print(f"  Итоговый результат = {result:.6f}")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
