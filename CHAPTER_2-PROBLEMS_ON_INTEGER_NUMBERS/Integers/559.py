"""
ГЛАВА 2
ЗАДАЧИ ПО ТЕМАМ
15. Целые числа.

559. Дано натуральное число n. С помощью решета Эратосфена (см. предыдущую задачу) найти четверки меньших n простых чисел, принадлежащих одному десятку (например, 11, 13, 17, 19).
"""


import random
import math


def get_n():
    """Выбор способа ввода натурального числа n."""
    print("Задача 559: Четверки простых чисел в одном десятке")
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
        examples = [20, 50, 100, 200]
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
    """Возвращает список всех простых чисел, меньших n."""
    if n < 2:
        return []
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
    prime_set = set(primes)

    print(f"\nВсего простых чисел меньше {n}: {len(primes)}")

    quadruplets = []
    # Для каждого десятка (10k+1 ... 10k+9) проверяем, являются ли
    # все четыре возможных простых числа (10k+1,10k+3,10k+7,10k+9) простыми.
    max_k = (n - 10) // 10
    for k in range(1, max_k + 1):
        p1 = 10 * k + 1
        p2 = 10 * k + 3
        p3 = 10 * k + 7
        p4 = 10 * k + 9
        if p1 in prime_set and p2 in prime_set and p3 in prime_set and p4 in prime_set:
            quadruplets.append((p1, p2, p3, p4))

    print("\nРезультаты:")
    print("-" * 50)
    if quadruplets:
        print(f"Найдено четверок простых чисел в одном десятке: {len(quadruplets)}")
        for q in quadruplets:
            print(f"  {q[0]}, {q[1]}, {q[2]}, {q[3]}")
    else:
        print("Четверок простых чисел, принадлежащих одному десятку, не найдено.")
    print("-" * 50)


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")