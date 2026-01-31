"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
9. Вычисления с хранением последовательности значений

282. Даны действительные числа a1, a2, …, a2n. Получить:
а) a1, an+1, a2, an+2, …, an, a2n;
б) a1, a2n, a2, a2n-1, a3, …, an, an+1;
в) a1+ a2n, a2+ a2n-1, …, an+ an+1.
"""


def main():
    # Ввод числа n
    while True:
        try:
            n = int(input("Введите натуральное число n: "))
            if n <= 0:
                print("Ошибка: n должно быть натуральным числом (больше 0).")
            else:
                break
        except ValueError:
            print("Ошибка: введите целое положительное число.")

    # Ввод 2n действительных чисел
    total = 2 * n
    a = []
    for i in range(total):
        while True:
            try:
                value = float(input(f"Введите действительное число a_{i+1}: "))
                a.append(value)
                break
            except ValueError:
                print("Ошибка: введите действительное число (например, 3.14).")

    print(f"\nИсходная последовательность: {a}")

    # а) a1, a_{n+1}, a2, a_{n+2}, ..., a_n, a_{2n}
    result_a = []
    for i in range(n):
        result_a.append(a[i])           # a_i
        result_a.append(a[i + n])       # a_{n+i}
    print("\nа) Новая последовательность:")
    print(result_a)

    # б) a1, a_{2n}, a2, a_{2n-1}, ..., a_n, a_{n+1}
    result_b = []
    for i in range(n):
        result_b.append(a[i])           # a_{i+1} (первая половина)
        result_b.append(a[total - 1 - i])  # a_{2n - i} (обратный порядок из второй половины)
    print("\nб) Новая последовательность:")
    print(result_b)

    # в) a1 + a_{2n}, a2 + a_{2n-1}, ..., a_n + a_{n+1}
    result_c = []
    for i in range(n):
        result_c.append(a[i] + a[total - 1 - i])
    print("\nв) Суммы пар:")
    print(result_c)

if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
