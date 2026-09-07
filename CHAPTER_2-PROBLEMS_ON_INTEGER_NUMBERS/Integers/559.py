"""
ГЛАВА 2
ЗАДАЧИ ПО ТЕМАМ
15. Целые числа.

559. Дано натуральное число n. Найти все меньше n числа Мерсена. (Простое число называется числом Мерсена, если оно может быть представлено в виде 2 ^ p - 1, где p - тоже простое число.)
"""


import random
import math


def get_n():
    """Выбор способа ввода натурального числа n."""
    print("Задача 559: Числа Мерсена")
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
        n = random.randint(10, 1000)
        print(f"\nСгенерировано n = {n}")
        return n

    else:  # готовые примеры
        examples = [10, 100, 500, 1000]
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


def sieve_of_eratosthenes(limit):
    """Возвращает список всех простых чисел, меньших limit."""
    if limit < 2:
        return []
    is_prime = bytearray(b'\x01') * limit
    is_prime[0] = is_prime[1] = 0

    for i in range(2, int(math.isqrt(limit)) + 1):
        if is_prime[i]:
            start = i * i
            step = i
            count = ((limit - 1 - start) // step) + 1
            is_prime[start:limit:step] = b'\x00' * count

    return [i for i in range(2, limit) if is_prime[i]]


def is_prime_simple(num):
    """Проверяет простоту числа (для больших чисел Мерсена)."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def main():
    n = get_n()

    # Максимальная степень p, при которой 2^p - 1 < n
    max_p = int(math.log2(n))

    # Находим все простые p <= max_p
    primes_p = sieve_of_eratosthenes(max_p + 1)

    mersenne_primes = []
    for p in primes_p:
        m = (1 << p) - 1  # 2^p - 1
        if m >= n:
            continue
        if is_prime_simple(m):
            mersenne_primes.append(m)

    print("\nРезультаты:")
    print(f"n = {n}")
    print(f"Простые показатели p (<= {max_p}): {primes_p}")
    print("-" * 50)
    if mersenne_primes:
        print(f"Числа Мерсена, меньшие {n}:")
        for m in mersenne_primes:
            print(f"  {m}")
        print(f"Всего найдено: {len(mersenne_primes)}")
    else:
        print("Чисел Мерсена, удовлетворяющих условию, не найдено.")
    print("-" * 50)


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")