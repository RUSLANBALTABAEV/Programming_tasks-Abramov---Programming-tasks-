"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
4. Простейшие циклы

93. Пусть
       x0 = c; x1 = d;
xk = q * xk - 1 + r * xk - 2 + b; k = 2,3, ...

Даны действительные q, r, b, c, d, натуральное n (n ≥ 2). Получить xn.
"""


def main():
    q = float(input("Введите q: "))
    r = float(input("Введите r: "))
    b = float(input("Введите b: "))
    c = float(input("Введите c (x0): "))
    d = float(input("Введите d (x1): "))
    n = int(input("Введите n (n ≥ 2): "))

    x0 = c
    x1 = d

    for k in range(2, n + 1):
        x = q * x1 + r * x0 + b
        x0, x1 = x1, x

    print(f"x_{n} = {x1}")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
