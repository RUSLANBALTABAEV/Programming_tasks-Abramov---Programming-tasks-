"""
ГЛАВА 2
ЗАДАЧИ ПО ТЕМАМ
15. Целые числа.

561. Дано натуральное число n. Среди чисел 1, ..., n найти все такие, запись которых совпадает с последними цифрами записи их квадрата (как, например, 6 * 6 = 36, 25 * 25 = 625 и т.д.).
"""


import random


def get_n():
    """Выбор способа ввода натурального числа n."""
    print("Задача 561: Автоморфные числа")
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
                n = int(input("Введите натуральное число n (>=1): "))
                if n < 1:
                    print("n должно быть >= 1.")
                    continue
                return n
            except ValueError:
                print("Ошибка ввода. Повторите.")

    elif choice == '2':
        n = random.randint(10, 10000)
        print(f"\nСгенерировано n = {n}")
        return n

    else:  # готовые примеры
        examples = [10, 100, 1000, 10000]
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


def is_automorphic(k):
    """
    Проверяет, является ли число k автоморфным:
    запись числа k совпадает с последними цифрами записи k^2.
    """
    digits = len(str(k))
    mod = 10 ** digits
    return (k * k) % mod == k


def main():
    n = get_n()
    automorphic = [k for k in range(1, n + 1) if is_automorphic(k)]

    print("\nРезультаты:")
    print(f"n = {n}")
    print("-" * 50)
    if automorphic:
        print("Автоморфные числа в диапазоне от 1 до n:")
        # Выводим по 10 чисел в строке
        for i in range(0, len(automorphic), 10):
            chunk = automorphic[i:i+10]
            print("  " + ", ".join(map(str, chunk)))
        print(f"\nКоличество найденных чисел: {len(automorphic)}")
    else:
        print("Автоморфных чисел в заданном диапазоне не найдено.")
    print("-" * 50)


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")