"""
ГЛАВА 2
ЗАДАЧИ ПО ТЕМАМ
15. Целые числа.

565. Рассмотрим некоторое натуральное число n (n > 1). Если оно четно, то разделим его на 2, иначе умножим на 3 и прибавим 1. Если полученное число не равно 1, то повторяется то же действие и т.д., пока не получится 1. До настоящего времени неизвестно, завершается ли этот процесс для любого n > 1.
Даны натуральное числа k, l, m (1 < k <= l). Проверить, верно ли, что для любого натурального n из диапазона от k до l процесс завершается не позднее, чем после m таких действий.
"""


import random


def collatz_steps(n, limit):
    """
    Выполняет процесс Коллатца для числа n.
    Возвращает количество шагов до достижения 1, если это произошло
    не позднее чем за limit шагов. Иначе возвращает None.
    """
    steps = 0
    while n != 1:
        if steps >= limit:   # лимит исчерпан, 1 не достигнута
            return None
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps


def get_params():
    """Выбор способа ввода параметров k, l, m."""
    print("Задача 565: Проверка гипотезы Коллатца")
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
                k = int(input("Введите начало диапазона k (k > 1): "))
                l = int(input("Введите конец диапазона l (l >= k): "))
                m = int(input("Введите максимальное число шагов m (m >= 1): "))
                if k <= 1 or l < k or m < 1:
                    print("Должно выполняться: 1 < k <= l, m >= 1.")
                    continue
                return k, l, m
            except ValueError:
                print("Ошибка ввода. Введите целые числа.")

    elif choice == '2':
        k = random.randint(2, 50)
        l = k + random.randint(0, 50)
        m = random.randint(1, 20)
        print(f"\nСгенерированы: k = {k}, l = {l}, m = {m}")
        return k, l, m

    else:  # готовые примеры
        examples = [
            (2, 20, 10),
            (2, 100, 30),
            (27, 27, 111),   # n = 27 требует ровно 111 шагов
            (2, 50, 5),      # заведомо мало шагов, будут "провалы"
        ]
        print("\nГотовые примеры (k, l, m):")
        for idx, (kv, lv, mv) in enumerate(examples, 1):
            print(f"{idx}: k={kv}, l={lv}, m={mv}")
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
    k, l, m = get_params()

    failures = []
    max_steps_observed = 0

    for n in range(k, l + 1):
        steps = collatz_steps(n, m)
        if steps is None:
            failures.append(n)
        elif steps > max_steps_observed:
            max_steps_observed = steps

    print(f"\nДиапазон: [{k}; {l}]")
    print(f"Максимальное допустимое число шагов m = {m}")
    print("-" * 50)

    if not failures:
        print("Утверждение ВЕРНО:")
        print(f"  Для всех чисел диапазона 1 достигнута не позднее чем за {m} шагов.")
        print(f"  Максимальное наблюдённое число шагов: {max_steps_observed}")
    else:
        print("Утверждение НЕВЕРНО.")
        print(f"  Числа, для которых процесс не завершился за {m} шагов:")
        for num in failures[:20]:
            print(f"    {num}")
        if len(failures) > 20:
            print(f"    ... и ещё {len(failures) - 20}")
        print(f"\n  Всего таких чисел: {len(failures)}")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")