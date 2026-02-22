"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
10. Вложенные циклы

320. Вычислить 10Ek=1 * k * k * k * 15El=1 * (k - l) * (k - l).
"""


def main():
    total = 0
    for k in range(1, 11):
        inner_sum = 0
        for l in range(1, 16):
            inner_sum += (k - l) ** 2
        total += k ** 3 * inner_sum
    print("Результат вычисления:", total)

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
