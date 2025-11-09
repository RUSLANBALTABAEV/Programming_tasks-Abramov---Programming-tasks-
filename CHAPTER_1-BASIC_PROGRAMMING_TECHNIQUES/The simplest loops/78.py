"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
4. Простейшие циклы

78. Даны действительное число a и натуральное число n. Вычислить:

а) a ** n
б) a(a + 1)(a + 2)...(a + n – 1)
в) 1 / a + 1 / (a * (a + 1)) + ... + 1 / (a * (a + 1)...(a + n))
г) 1 / a + 1 / a ** 2 + 1 / a ** 4 + ... + 1 / a ** (2 ** n)
д) a(a - n)(a - 2n)...(a - n ** 2)
"""


def calculate_a(a: float, n: int) -> float:
    """
    Вычисляет выражение а) a^n.
    Возвращает значение a, возведённое в степень n.
    """
    return a ** n


def calculate_b(a: float, n: int) -> float:
    """
    Вычисляет выражение б) a(a + 1)(a + 2)...(a + n - 1).
    Это произведение n последовательных членов, начиная с a.
    """
    result = 1
    for i in range(n):
        result *= a + i
    return result


def calculate_c(a: float, n: int) -> float:
    """
    Вычисляет выражение в)
    1 / a + 1 / (a * (a + 1)) + ... + 1 / (a * (a + 1)...(a + n)).

    Последовательность знаменателей растёт за счёт умножения на (a + i).
    """
    result = 0
    product = 1

    for i in range(n + 1):
        # Первый множитель — это просто a
        product = a if i == 0 else product * (a + i)

        # Прибавляем очередной член ряда
        result += 1 / product

    return result


def calculate_d(a: float, n: int) -> float:
    """
    Вычисляет выражение г)
    1 / a + 1 / a² + 1 / a⁴ + ... + 1 / a^(2^n).

    Здесь показатель степени растёт по степеням двойки.
    """
    result = 0
    for i in range(n + 1):
        result += 1 / (a ** (2 ** i))
    return result


def calculate_e(a: float, n: int) -> float:
    """
    Вычисляет выражение д)
    a(a - n)(a - 2n)...(a - n²).

    Здесь каждый следующий множитель уменьшается на n, n*2 и т. д.
    """
    result = 1
    for i in range(n + 1):
        result *= a - i * n
    return result


def main() -> None:
    """
    Основная функция программы.

    Запрашивает входные данные, вычисляет пять выражений и
    выводит результаты в читаемом виде.
    """
    print("Введите действительное число a и натуральное число n:")

    # Безопасное чтение входных данных
    try:
        a = float(input("a = "))
        n = int(input("n = "))
    except ValueError:
        print("Ошибка: введены некорректные данные.")
        return

    # Проверка корректности n
    if n < 1:
        print("Ошибка: n должно быть натуральным числом (n ≥ 1).")
        return

    # Предупреждение о возможных делениях на ноль
    if a == 0:
        print("Предупреждение: a = 0 может привести к делению на ноль.")

    print("\n" + "=" * 70)
    print(f"Вычисление выражений для a = {a}, n = {n}")
    print("=" * 70 + "\n")

    # а) Вычисление степени
    result_a = calculate_a(a, n)
    print(f"а) a^n = {a}^{n} = {result_a:.10f}")

    # б) Произведение последовательных членов
    result_b = calculate_b(a, n)
    print(f"\nб) a(a+1)...(a+{n - 1}) = {result_b:.10f}")

    # в) Сумма обратных произведений
    try:
        result_c = calculate_c(a, n)
        print(f"\nв) сумма = {result_c:.10f}")
    except ZeroDivisionError:
        print("\nв) Ошибка: деление на ноль")

    # г) Сумма степеней двойки
    try:
        result_d = calculate_d(a, n)
        print(f"\nг) сумма = {result_d:.10f}")
    except ZeroDivisionError:
        print("\nг) Ошибка: деление на ноль")

    # д) Произведение с шагом n
    result_e = calculate_e(a, n)
    print(f"\nд) произведение = {result_e:.10f}")

    # Завершение программы
    input("\nНажмите Enter, чтобы завершить программу.")


# Точка входа
if __name__ == "__main__":
    main()
