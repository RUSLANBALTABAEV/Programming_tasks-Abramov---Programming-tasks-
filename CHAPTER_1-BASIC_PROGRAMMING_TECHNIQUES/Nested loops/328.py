"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
10. Вложенные циклы

328. Найти 100 первых простых чисел.
"""


def is_prime(num, primes):
    """Проверяет, является ли num простым, используя список найденных простых."""
    for p in primes:
        if p * p > num:
            break
        if num % p == 0:
            return False
    return True

def main():
    count = 100
    primes = []
    num = 2
    while len(primes) < count:
        if is_prime(num, primes):
            primes.append(num)
        num += 1
    print(f"Первые {count} простых чисел:")
    # Вывод по 10 чисел в строке
    for i in range(0, len(primes), 10):
        print(" ".join(f"{p:3d}" for p in primes[i:i+10]))

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
