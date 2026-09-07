"""
ГЛАВА 2
ЗАДАЧИ ПО ТЕМАМ
15. Целые числа.

557. Дано натуральное число n (n >= 2). Найти все меньшие n простые числа, используя решето Эратосфена. Решетом Эратосфена называют следующий способ. Выпишем подряд все целые числа от 2 до n. Первое простое число 2. Подчеркнем его, а все большие числа, кратные 2, зачеркнем. Первое из оставшихся чисел 3. Подчеркнём, его как простое, а все большие числа, кратные 3, зачеркнем. Первое число из оставшихся теперь 5, так как 4 уже зачеркнуто. Подчеркнем его как простое, а все большие числа, кратные 5, зачеркнем и т.д.:
3, 4, 5, 6, 7, 8, 9, 10,
"""


import random
import math


def get_n():
    """Выбор способа ввода натурального числа n."""
    print("Задача 557: Решето Эратосфена")
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
                n = int(input("Введите натуральное число n (>=2): "))
                if n < 2:
                    print("n должно быть >= 2.")
                    continue
                return n
            except ValueError:
                print("Ошибка ввода. Повторите.")

    elif choice == '2':
        n = random.randint(20, 100)
        print(f"\nСгенерировано n = {n}")
        return n

    else:  # готовые примеры
        examples = [30, 50, 100]
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


def sieve_of_eratosthenes(n):
    """
    Возвращает список всех простых чисел, меньших n.
    Классический алгоритм «Решето Эратосфена».
    """
    if n < 2:
        return []

    # Байтовый массив: 1 – простое, 0 – составное
    is_prime = bytearray(b'\x01') * n
    is_prime[0] = is_prime[1] = 0

    limit = int(math.isqrt(n))
    for i in range(2, limit + 1):
        if is_prime[i]:
            start = i * i
            step = i
            count = ((n - 1 - start) // step) + 1
            is_prime[start:n:step] = b'\x00' * count

    return [i for i in range(2, n) if is_prime[i]]


def main():
    n = get_n()
    primes = sieve_of_eratosthenes(n)

    print("\nРезультаты:")
    print(f"n = {n}")
    print("-" * 50)
    if primes:
        print(f"Простые числа, меньшие {n}:")
        # Выводим по 10 чисел в строке для компактности
        for i in range(0, len(primes), 10):
            chunk = primes[i:i+10]
            print("  " + ", ".join(map(str, chunk)))
        print(f"\nКоличество простых чисел: {len(primes)}")
    else:
        print(f"Простых чисел, меньших {n}, нет.")
    print("-" * 50)


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")