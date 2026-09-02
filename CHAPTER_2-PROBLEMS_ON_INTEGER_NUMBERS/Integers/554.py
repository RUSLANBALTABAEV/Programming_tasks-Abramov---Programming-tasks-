"""
ГЛАВА 2
ЗАДАЧИ ПО ТЕМАМ
15. Целые числа.

554. Дано натуральное число n. Получить все пифагоровы тройки натуральных чисел, каждое из которых не превосходит n, т.е. все такие тройки натуральных чисел a, b, c, что a * a + b * b = c * c * (a <= b <= c <= n).
"""


import random
import math


def get_n():
    """Выбор способа ввода натурального числа n."""
    print("Задача 554: Поиск всех пифагоровых троек")
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
                n = int(input("Введите натуральное число n (>=3): "))
                if n < 3:
                    print("n должно быть >= 3.")
                    continue
                return n
            except ValueError:
                print("Ошибка ввода. Повторите.")

    elif choice == '2':
        # Случайное n от 5 до 50, чтобы было несколько троек
        n = random.randint(5, 50)
        print(f"\nСгенерировано n = {n}")
        return n

    else:  # готовые примеры
        examples = [10, 20, 30, 50, 100]
        print("\nГотовые примеры n:")
        for idx, val in enumerate(examples, 1):
            print(f"{idx}: n = {val}")
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
    n = get_n()

    # Поиск троек
    triples = []
    # a <= b <= c <= n, поэтому a может быть от 1 до n-2
    for a in range(1, n - 1):
        for b in range(a, n):
            c_sq = a * a + b * b
            c = math.isqrt(c_sq)
            # проверяем, что c_sq является полным квадратом и c <= n
            if c * c == c_sq and c <= n:
                triples.append((a, b, c))

    # Вывод результатов
    print("\nРезультаты:")
    print(f"n = {n}")
    print("-" * 50)

    if triples:
        print(f"Найдено пифагоровых троек (a <= b <= c <= n): {len(triples)}")
        print("Список троек (a, b, c):")
        for a, b, c in triples:
            # Проверка равенства
            print(f"  ({a}, {b}, {c})  |  {a}² + {b}² = {a*a} + {b*b} = {c*c}")
    else:
        print("Пифагоровых троек для заданного n не найдено.")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")