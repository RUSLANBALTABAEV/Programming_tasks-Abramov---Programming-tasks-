"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
7. Сочетания цикла и разветвления

242. Дано натуральное число n. Вычислить

nEk=0 * (-1)^k*(k-1) / 2 / k!.
"""


def main():
    n = int(input("Введите натуральное число n: "))
    total = 0.0
    factorial = 1  # 0! = 1
    
    for k in range(0, n + 1):
        if k > 0:
            factorial *= k  # вычисляем k! итеративно
        term = ((-1) ** k) * (k - 1) / (2 * factorial)
        total += term
    
    print(f"Сумма: {total}")

if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
