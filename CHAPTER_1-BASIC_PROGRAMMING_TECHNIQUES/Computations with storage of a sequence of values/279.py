"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
9. Вычисления с хранением последовательности значений

279. Даны действительные числа a1, …, an, b1, …, bn. Вычислить (a1+bn)(a2+bn-1)...(an+b1).
"""


def main():
    # Ввод количества элементов n
    while True:
        try:
            n = int(input("Введите количество элементов n: "))
            if n <= 0:
                print("Ошибка: n должно быть натуральным числом.")
            else:
                break
        except ValueError:
            print("Ошибка: введите целое положительное число.")

    # Ввод последовательности a
    print(f"\nВведите {n} действительных чисел для последовательности a:")
    a = []
    for i in range(n):
        while True:
            try:
                value = float(input(f"a_{i+1}: "))
                a.append(value)
                break
            except ValueError:
                print("Ошибка: введите действительное число.")

    # Ввод последовательности b
    print(f"\nВведите {n} действительных чисел для последовательности b:")
    b = []
    for i in range(n):
        while True:
            try:
                value = float(input(f"b_{i+1}: "))
                b.append(value)
                break
            except ValueError:
                print("Ошибка: введите действительное число.")

    # Вычисление произведения (a_1 + b_n) * (a_2 + b_{n-1}) * ... * (a_n + b_1)
    product = 1.0
    print("\nВычисление произведения:")
    for i in range(n):
        term = a[i] + b[n-1-i]  # b_{n-1-i} соответствует b_{n-i} в математической записи
        product *= term
        print(f"({a[i]:.3f} + {b[n-1-i]:.3f}) = {term:.3f}")

    print(f"\nРезультат произведения: {product:.6f}")

if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
