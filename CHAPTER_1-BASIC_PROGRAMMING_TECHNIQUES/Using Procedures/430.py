"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
12. Использование процедур 

В задачах этого параграфа будем для краткости говорить просто о процедурах, подразумевая, что решающий задачи сам выберет подходящее средство программирования – подпрограмму, функцию и 
т. д. Этот выбор должен быть сделан с учётом как характера задач, так и особенностей используемого языка программирования.

430. Даны натуральные числа k, l, m, действительные числа 
x1, ..., xk, y1, ..., yl, z1, ..., zm. Получить
t = (max(y1, ..., yl) + max(z1, ..., zm)) / 2
t = при max(x1, ..., xk) >= 0,
t = 1 + (max(x1, ..., xk)) ^ 2 в противном случае.
"""


import random


def compute_t(x, y, z):
    """Вычисляет t по заданному правилу."""
    max_x = max(x) if x else float('-inf')
    max_y = max(y) if y else float('-inf')
    max_z = max(z) if z else float('-inf')

    if max_x >= 0:
        return (max_y + max_z) / 2
    else:
        return 1 + max_x ** 2


def get_arrays():
    """Выбор способа ввода массивов x, y, z."""
    print("Задача 430: Вычисление t по трём массивам")
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
                k = int(input("Введите количество элементов массива x (k): "))
                l = int(input("Введите количество элементов массива y (l): "))
                m = int(input("Введите количество элементов массива z (m): "))
                print(f"Введите {k} действительных чисел для массива x через пробел:")
                x = list(map(float, input().split()))
                if len(x) != k:
                    print("Ошибка: неверное количество чисел.")
                    continue
                print(f"Введите {l} действительных чисел для массива y через пробел:")
                y = list(map(float, input().split()))
                if len(y) != l:
                    print("Ошибка: неверное количество чисел.")
                    continue
                print(f"Введите {m} действительных чисел для массива z через пробел:")
                z = list(map(float, input().split()))
                if len(z) != m:
                    print("Ошибка: неверное количество чисел.")
                    continue
                return x, y, z
            except ValueError:
                print("Ошибка ввода. Повторите.")

    elif choice == '2':
        k = random.randint(3, 7)
        l = random.randint(3, 7)
        m = random.randint(3, 7)
        x = [round(random.uniform(-10, 10), 2) for _ in range(k)]
        y = [round(random.uniform(-10, 10), 2) for _ in range(l)]
        z = [round(random.uniform(-10, 10), 2) for _ in range(m)]
        print(f"Сгенерированы массивы:")
        print(f"x ({k} эл.): {x}")
        print(f"y ({l} эл.): {y}")
        print(f"z ({m} эл.): {z}")
        return x, y, z

    else:  # готовые примеры
        examples = [
            ([3.5, -1.2, 0.0], [2.0, 4.5], [1.0, 3.0, -2.0]),
            ([-5.0, -3.0, -7.0], [10.0, 20.0], [100.0]),
            ([0.0, 1.0], [-2.0, -1.0], [5.5, 6.2, 3.1]),
            ([2.0], [0.0, 0.0], [0.0]),
            ([-1.0], [5.0, 6.0], [7.0, 8.0])
        ]
        print("Готовые примеры:")
        for idx, (x_arr, y_arr, z_arr) in enumerate(examples, 1):
            print(f"{idx}: x = {x_arr}, y = {y_arr}, z = {z_arr}")
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
    x, y, z = get_arrays()
    t = compute_t(x, y, z)
    max_x = max(x) if x else float('-inf')
    max_y = max(y) if y else float('-inf')
    max_z = max(z) if z else float('-inf')

    print("\nРезультаты:")
    print(f"  max(x) = {max_x}")
    print(f"  max(y) = {max_y}")
    print(f"  max(z) = {max_z}")
    condition = max_x >= 0
    print(f"  Условие max(x) >= 0: {condition}")
    print(f"  t = {t:.6f}")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
