"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
10. Вложенные циклы

322. Найти натуральное число от 1 до 10 000 с максимальной суммой делителей.
"""


def sum_of_divisors(n):
    """Возвращает сумму всех положительных делителей числа n."""
    total = 0
    # Перебор делителей до корня из n
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:  # чтобы не удваивать квадратный корень
                total += n // i
    return total

def main():
    max_sum = 0
    best_number = 0
    for num in range(1, 10001):
        s = sum_of_divisors(num)
        if s > max_sum:
            max_sum = s
            best_number = num
    print(f"Число с максимальной суммой делителей (от 1 до 10000): {best_number}")
    print(f"Сумма его делителей: {max_sum}")

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
