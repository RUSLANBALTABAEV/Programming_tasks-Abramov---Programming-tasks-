"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
7. Сочетания цикла и разветвления

241. Даны натуральное число n, действительное число x.
Вычислить 
(-1) ^ abs(sqrt(1)) / 1 * x + (-1) ^ abs(sqrt(2)) / 2 * x * x + ... + (-1) ^ abs(sqrt(n)) / n * x ^ n.
"""


def main():
    import math
    n = int(input("Введите натуральное число n: "))
    x = float(input("Введите действительное число x: "))
    total = 0.0
    for k in range(1, n + 1):
        exponent = math.floor(math.sqrt(k))
        sign = (-1) ** exponent
        term = sign / k * (x ** k)
        total += term
    print(f"Сумма: {total}")

if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
