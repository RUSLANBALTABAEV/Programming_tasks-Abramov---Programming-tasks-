"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
12. Использование процедур 

В задачах этого параграфа будем для краткости говорить просто о процедурах, подразумевая, что решающий задачи сам выберет подходящее средство программирования – подпрограмму, функцию и 
т. д. Этот выбор должен быть сделан с учётом как характера задач, так и особенностей используемого языка программирования.

458. Даны неотрицательные целые числа n, m; вычислить 

A(n, m), где 

A(n,m) = m + 1,           если n = 0,
A(n - 1, A(n, m - 1)),    если n != 0, m = 0,
A(n - 1, A(n, m - 1)),    если n > 0, m > 0

(это - так называемая функция Аккермана).

Использовать программу, включающую рекурсивную процедуру.
"""


import sys
import random

sys.setrecursionlimit(1000000)


def ackermann(n, m):
    """Рекурсивная процедура вычисления функции Аккермана."""
    if n == 0:
        return m + 1
    elif n > 0 and m == 0:
        return ackermann(n - 1, 1)
    else:
        return ackermann(n - 1, ackermann(n, m - 1))


def get_params():
    print("Задача 458: Функция Аккермана (рекурсивная)")
    print("⚠️ Функция очень быстро растёт: для n=4 используйте m=0 или 1,")
    print("   для n=3 — m не более 10.")
    print("1 — Ручной ввод, 2 — Случайная генерация, 3 — Готовые примеры")
    while True:
        choice = input("Ваш выбор (1/2/3): ").strip()
        if choice in ('1','2','3'):
            break
        print("Ошибка: выберите 1, 2 или 3.")

    if choice == '1':
        while True:
            try:
                n = int(input("n: "))
                m = int(input("m: "))
                if n < 0 or m < 0:
                    print("Числа должны быть неотрицательными.")
                    continue
                return n, m
            except ValueError:
                print("Ошибка ввода.")
    elif choice == '2':
        n = random.randint(0, 3)
        if n == 3:
            m = random.randint(0, 6)
        elif n == 2:
            m = random.randint(0, 12)
        else:
            m = random.randint(0, 15)
        print(f"Сгенерированы n = {n}, m = {m}")
        return n, m
    else:
        examples = [(0,0), (1,2), (2,3), (3,4), (2,10), (3,6)]
        print("Примеры:", examples)
        num = int(input("Номер примера: "))
        return examples[num-1]


def main():
    n, m = get_params()
    try:
        result = ackermann(n, m)
        print(f"\nA({n}, {m}) = {result}")
    except RecursionError:
        print("Ошибка: превышена глубина рекурсии. Попробуйте меньшие значения n, m.")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
