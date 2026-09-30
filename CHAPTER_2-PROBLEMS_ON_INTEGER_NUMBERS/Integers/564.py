"""
ГЛАВА 2
ЗАДАЧИ ПО ТЕМАМ
15. Целые числа.

564. Рассмотрим некоторое натуральное число n. Если это не палиндром, то изменим порядок его цифр на обратный и сложим исходное число с получившимся. Если сумма не палиндром, то над ней повторяется то же действие и т.д.. пока не получится палиндром. До настоящего времени неизвестно, завершается ли этот процесс для любого натурального n.
Даны натуральные числа k, l, m (k <= 1). Проверить, верно ли, что для любого натурального числа из диапазона от k до 1 процесс завершается не позднее, чем после m таких действий.
"""


def is_palindrome(n):
    """Проверяет, является ли число n палиндромом."""
    s = str(n)
    return s == s[::-1]


def reverse_number(n):
    """Возвращает число, полученное перестановкой цифр числа n в обратном порядке."""
    return int(str(n)[::-1])


def steps_to_palindrome(n, max_steps):
    """
    Выполняет процесс «перевернуть и сложить» не более max_steps раз.
    Возвращает число шагов до получения палиндрома или None,
    если за max_steps шагов палиндром не был получен.
    """
    for step in range(max_steps + 1):
        if is_palindrome(n):
            return step
        if step < max_steps:  # не делаем лишнего сложения после последнего шага
            n = n + reverse_number(n)
    return None


def get_params():
    """Выбор способа ввода k, l, m."""
    print("Задача 564: Проверка гипотезы о палиндромах")
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
                k = int(input("Введите начало диапазона k (k >= 1): "))
                l = int(input("Введите конец диапазона l (l >= k): "))
                m = int(input("Введите максимальное число шагов m (m >= 0): "))
                if k < 1 or l < k or m < 0:
                    print("Должно выполняться: 1 <= k <= l, m >= 0.")
                    continue
                return k, l, m
            except ValueError:
                print("Ошибка ввода. Введите целые числа.")

    elif choice == '2':
        k = random.randint(1, 50)
        l = k + random.randint(0, 50)
        m = random.randint(0, 10)
        print(f"\nСгенерированы: k = {k}, l = {l}, m = {m}")
        return k, l, m

    else:  # готовые примеры
        examples = [
            (1, 20, 5),
            (1, 100, 10),
            (89, 99, 24),   # 89 требует 24 шага до палиндрома
            (1, 10, 0),
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
        steps = steps_to_palindrome(n, m)
        if steps is None:
            failures.append(n)
        elif steps > max_steps_observed:
            max_steps_observed = steps

    print(f"\nДиапазон: [{k}; {l}]")
    print(f"Максимальное число шагов m = {m}")
    print("-" * 50)

    if not failures:
        print("Утверждение ВЕРНО:")
        print(f"  Для всех чисел диапазона палиндром получен не позднее чем за {m} шагов.")
        print(f"  Максимальное наблюдённое число шагов: {max_steps_observed}")
    else:
        print("Утверждение НЕВЕРНО.")
        print(f"  Числа, для которых процесс не завершился за {m} шагов:")
        for num in failures[:20]:  # ограничим вывод 20 числами
            print(f"    {num}")
        if len(failures) > 20:
            print(f"    ... и ещё {len(failures) - 20}")
        print(f"\n  Всего таких чисел: {len(failures)}")


if __name__ == "__main__":
    import random
    main()
    input("\nНажмите Enter, чтобы завершить программу.")