"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
12. Использование процедур 

В задачах этого параграфа будем для краткости говорить просто о процедурах, подразумевая, что решающий задачи сам выберет подходящее средство программирования – подпрограмму, функцию и 
т. д. Этот выбор должен быть сделан с учётом как характера задач, так и особенностей используемого языка программирования.

428. Даны действительные числа a, b. Получить 
u = min(a, b), v = min(a * b, a + b), min(u + v * v, 3.14).
"""


import random


def get_params():
    """Выбор способа ввода чисел a и b."""
    print("Задача 428: u = min(a, b), v = min(ab, a + b), min(u + v², 3.14)")
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
                return a, b
            except ValueError:
                print("Ошибка ввода. Повторите.")

    elif choice == '2':
        a = round(random.uniform(-10, 10), 2)
        b = round(random.uniform(-10, 10), 2)
        print(f"Сгенерированы числа: a = {a}, b = {b}")
        return a, b

    else:  # готовые примеры
        examples = [
            (2.0, 3.0),
            (-1.5, 4.0),
            (0.0, 0.0),
            (3.14, 1.0),
            (-5.0, -5.0)
        ]
        print("Готовые примеры:")
        for idx, (a_val, b_val) in enumerate(examples, 1):
            print(f"{idx}: a = {a_val}, b = {b_val}")
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
    a, b = get_params()

    u = min(a, b)
    v = min(a * b, a + b)
    result = min(u + v * v, 3.14)

    print("\nРезультаты:")
    print(f"  u = min(a, b)      = min({a}, {b}) = {u}")
    print(f"  v = min(a * b, a + b)  = min({a * b}, {a + b}) = {v}")
    print(f"  min(u + v², 3.14)  = min({u} + {v}², 3.14) = {result:.6f}")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
