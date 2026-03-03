"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
10. Вложенные циклы

348. Даны целые числа a1, ... ,an,b1, ... , bn*). Верно ли, что эти две последовательности отличаются не более чем порядком следования членов?
*) В этой и некоторых из следующих задач этого параграфа надо иметь *) В этой и некоторых из следующих задач этого параграфа надо иметь
"""


import random
from collections import Counter

def get_sequences():
    """Выбор способа ввода n, a и b."""
    print("Выберите способ ввода:")
    print("1 - Ручной ввод")
    print("2 - Случайная генерация")
    print("3 - Готовый пример")
    choice = input("Ваш выбор (1/2/3): ").strip()
    while choice not in ('1', '2', '3'):
        choice = input("Некорректно. Выберите 1, 2 или 3: ")

    if choice == '1':
        try:
            n = int(input("Введите натуральное число n (>0): "))
            if n <= 0:
                print("n должно быть положительным.")
                return None
            print("Введите целые числа a1...an через пробел:")
            a_line = input().strip()
            a_tokens = a_line.split()
            if len(a_tokens) != n:
                print(f"Ожидалось {n} чисел, получено {len(a_tokens)}.")
                return None
            a = [int(t) for t in a_tokens]

            print("Введите целые числа b1...bn через пробел:")
            b_line = input().strip()
            b_tokens = b_line.split()
            if len(b_tokens) != n:
                print(f"Ожидалось {n} чисел, получено {len(b_tokens)}.")
                return None
            b = [int(t) for t in b_tokens]
            return n, a, b
        except ValueError:
            print("Ошибка ввода.")
            return None

    elif choice == '2':
        n = random.randint(3, 10)
        a = [random.randint(-10, 10) for _ in range(n)]
        # С вероятностью 0.5 делаем b перестановкой a, иначе случайный
        if random.choice([True, False]):
            b = a[:]
            random.shuffle(b)
        else:
            b = [random.randint(-10, 10) for _ in range(n)]
        print(f"Сгенерировано: n = {n}")
        print("a =", a)
        print("b =", b)
        return n, a, b

    else:  # choice == '3'
        examples = [
            (3, [1, 2, 3], [3, 2, 1]),
            (4, [1, 1, 2, 2], [2, 1, 2, 1]),
            (5, [10, 20, 30, 40, 50], [50, 40, 30, 20, 10]),
            (3, [1, 2, 3], [4, 5, 6]),
            (2, [1, 1], [1, 1]),
            (2, [1, 2], [1, 1])
        ]
        print("Готовые примеры (n, a, b):")
        for idx, (n_val, a_val, b_val) in enumerate(examples, 1):
            print(f"{idx}: n = {n_val}, a = {a_val}, b = {b_val}")
        try:
            idx = int(input("Выберите номер примера: "))
            if 1 <= idx <= len(examples):
                n, a, b = examples[idx-1]
                return n, a, b
            else:
                print("Неверный номер.")
                return None
        except ValueError:
            print("Ошибка ввода.")
            return None

def main():
    data = get_sequences()
    if data is None:
        return
    n, a, b = data
    print("\n" + "="*60)
    print(f"n = {n}")
    print("a =", a)
    print("b =", b)
    print("="*60)

    # Проверка: являются ли a и b перестановками друг друга
    if Counter(a) == Counter(b):
        print("\nДа, последовательности отличаются не более чем порядком следования членов.")
    else:
        print("\nНет, последовательности не являются перестановками друг друга.")

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
