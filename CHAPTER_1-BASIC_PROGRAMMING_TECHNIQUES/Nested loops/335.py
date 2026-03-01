"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
10. Вложенные циклы

335. Дано натуральное число n. Вычислить:
а) nEk=1 * k * (k + 1)...k * k;            б) nEk=1 * k ^ k;
в) nEk=1 * 1 / (k * k)!;                   г) nEk=1 * (-1) ^ k * (2 * k * k + 1)!
"""


import math

def main():
    try:
        n = int(input("Введите натуральное число n: "))
        if n <= 0:
            print("n должно быть положительным.")
            return
    except ValueError:
        print("Ошибка ввода.")
        return

    # a) Сумма произведений от k до k^2
    sum_a = 0
    for k in range(1, n + 1):
        prod = 1
        for i in range(k, k * k + 1):
            prod *= i
        sum_a += prod
    print(f"a) Σ_{{k=1}}^{n} [k·(k+1)·…·k²] = {sum_a}")

    # б) Сумма k^k
    sum_b = 0
    for k in range(1, n + 1):
        sum_b += k ** k
    print(f"б) Σ_{{k=1}}^{n} k^k = {sum_b}")

    # в) Сумма 1/((k²)!)
    sum_c = 0.0
    for k in range(1, n + 1):
        sum_c += 1.0 / math.factorial(k * k)
    print(f"в) Σ_{{k=1}}^{n} 1/((k²)!) = {sum_c}")

    # г) Сумма (-1)^k * (2k²+1)!
    sum_d = 0
    for k in range(1, n + 1):
        sign = -1 if k % 2 else 1
        term = sign * math.factorial(2 * k * k + 1)
        sum_d += term
    print(f"г) Σ_{{k=1}}^{n} (-1)^k·(2k²+1)! = {sum_d}")

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
