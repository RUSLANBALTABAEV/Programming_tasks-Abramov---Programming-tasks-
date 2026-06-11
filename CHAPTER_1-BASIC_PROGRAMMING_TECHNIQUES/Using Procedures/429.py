"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
12. Использование процедур 

В задачах этого параграфа будем для краткости говорить просто о процедурах, подразумевая, что решающий задачи сам выберет подходящее средство программирования – подпрограмму, функцию и 
т. д. Этот выбор должен быть сделан с учётом как характера задач, так и особенностей используемого языка программирования.

429. Даны натуральные числа n, m, целые числа a1, ..., an, b1, ..., bm, c1, ..., c30. Получить
l = min(b1, ..., bm) + min(c1, ..., c30)
l = при abs(min(a1,....,an)) > 10,
l = 1 + (max(c1,...,c30)) * (max(c1,...,c30)) в противном случае. 
"""


import random


def compute_l(a, b, c):
    """Вычисляет l согласно условию задачи."""
    min_a = min(a) if a else 0
    min_b = min(b) if b else 0
    min_c = min(c) if c else 0
    max_c = max(c) if c else 0

    if abs(min_a) > 10:
        return min_b + min_c
    else:
        return 1 + max_c * max_c


def get_arrays():
    """Выбор способа ввода массивов a, b, c."""
    print("Задача 429: Вычисление l по массивам")
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
                n = int(input("Введите количество элементов массива a (n): "))
                m = int(input("Введите количество элементов массива b (m): "))
                print(f"Введите {n} целых чисел для массива a через пробел:")
                a = list(map(int, input().split()))
                if len(a) != n:
                    print("Ошибка: неверное количество чисел.")
                    continue
                print(f"Введите {m} целых чисел для массива b через пробел:")
                b = list(map(int, input().split()))
                if len(b) != m:
                    print("Ошибка: неверное количество чисел.")
                    continue
                print("Введите 30 целых чисел для массива c через пробел:")
                c = list(map(int, input().split()))
                if len(c) != 30:
                    print("Ошибка: должно быть ровно 30 чисел.")
                    continue
                return a, b, c
            except ValueError:
                print("Ошибка ввода. Повторите.")

    elif choice == '2':
        n = random.randint(3, 8)
        m = random.randint(3, 8)
        a = [random.randint(-20, 20) for _ in range(n)]
        b = [random.randint(-10, 10) for _ in range(m)]
        c = [random.randint(-5, 15) for _ in range(30)]
        print(f"Сгенерированы массивы:")
        print(f"a ({n} эл.): {a}")
        print(f"b ({m} эл.): {b}")
        print(f"c (30 эл.): {c}")
        return a, b, c

    else:  # готовые примеры
        examples = [
            ([12, -5, 3], [7, 2, -1, 4], [1,2,3,4,5,6,7,8,9,10,
                                           -1,-2,-3,-4,-5,-6,-7,-8,-9,-10,
                                           0,0,0,0,0,0,0,0,0,0]),
            ([-3, 0, 8], [10, 20], [5,5,5,5,5,5,5,5,5,5,
                                     5,5,5,5,5,5,5,5,5,5,
                                     5,5,5,5,5,5,5,5,5,5]),
            ([100, 200], [1,2,3], [0,0,0,0,0,0,0,0,0,0,
                                   0,0,0,0,0,0,0,0,0,0,
                                   0,0,0,0,0,0,0,0,0,0])
        ]
        print("Готовые примеры:")
        for idx, (a_arr, b_arr, c_arr) in enumerate(examples, 1):
            print(f"{idx}: a = {a_arr}, b = {b_arr}, c = {c_arr[:5]}... (первые 5 из 30)")
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
    a, b, c = get_arrays()
    l = compute_l(a, b, c)
    print("\nРезультаты:")
    print(f"  min(a) = {min(a)}, |min(a)| = {abs(min(a))}")
    print(f"  min(b) = {min(b)}, min(c) = {min(c)}, max(c) = {max(c)}")
    print(f"  l = {l}")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
