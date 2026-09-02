"""
ГЛАВА 2
ЗАДАЧИ ПО ТЕМАМ
15. Целые числа.

556. Для чисел Фибоначчи u0,u1, ... (см. задачу 144)
справедлива формула Бине
uk = 1 / sqrt(5) * ((1 + sqrt(5)) / 2) - 1 / sqrt(5) * pow(((1 - sqrt(5)) / 2), k), k = 0, 1, ...
Так как abs((1 - sqrt(5)) / 2) < 1, то для больших k выполнено приближенное равенство 
uk = 1 / sqrt(5) * pow((1 + sqrt(5) / 2), k).
Вычислить и округлить до целого все числа pow((1 + sqrt(5) / 2), k)
(k = 0, 1, ..., 15). Вычислить u0, u1, ..., u15 по формулам uo = 0; u1 = 1; uk = uk-1 + uk-2 * (k = 2, 3, ...) и сравнить результаты. 
"""


import math


def exact_fibonacci(n):
    """
    Вычисляет числа Фибоначчи u0..un точно по рекуррентной формуле.
    Возвращает список.
    """
    if n < 0:
        return []
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[:n + 1]


def binet_fibonacci(n):
    """
    Вычисляет числа Фибоначчи по формуле Бине (приближённо),
    округляя результат до целого.
    Возвращает список.
    """
    phi = (1 + math.sqrt(5)) / 2
    result = []
    for k in range(n + 1):
        value = (1 / math.sqrt(5)) * (phi ** k)
        result.append(round(value))
    return result


def print_comparison(n):
    """
    Выводит таблицу сравнения точных и приближённых значений.
    """
    exact = exact_fibonacci(n)
    approx = binet_fibonacci(n)

    print(f"{'k':>3} | {'u_k (точное)':>14} | {'u_k (Бине, окр.)':>18} | {'Разница':>10}")
    print("-" * 60)

    for k in range(n + 1):
        exact_val = exact[k]
        approx_val = approx[k]
        diff = exact_val - approx_val
        diff_str = "0" if diff == 0 else f"{diff:+d}"
        print(f"{k:>3} | {exact_val:>14} | {approx_val:>18} | {diff_str:>10}")

    match = sum(1 for i in range(n + 1) if exact[i] == approx[i])
    print("-" * 60)
    print(f"Совпадений: {match} из {n + 1}")


def main():
    print("=== ЗАДАЧА 556: Формула Бине и сравнение с точным вычислением ===\n")
    max_k = 15   # по условию

    print("Точные числа Фибоначчи (по рекуррентной формуле):")
    exact = exact_fibonacci(max_k)
    print(f"  {exact}\n")

    print("Приближённые числа Фибоначчи (по формуле Бине, округлённые):")
    approx = binet_fibonacci(max_k)
    print(f"  {approx}\n")

    print("Таблица сравнения:")
    print_comparison(max_k)

    print("\nВывод: округлённые значения по формуле Бине совпадают с точными")
    print("для всех k от 0 до 15, что подтверждает корректность приближения.")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")