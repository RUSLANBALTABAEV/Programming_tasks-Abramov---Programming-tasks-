"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
4. Простейшие циклы


112. Даны целые числа n, k, (n ≥ k ≥ 0). Вычислить
(n(n - 1)...(n - k + 1)) / k!.
"""


def main():
    # Ввод целых чисел n и k
    n = int(input("Введите целое число n: "))
    k = int(input("Введите целое число k (0 ≤ k ≤ n): "))
    
    # Проверка условия n ≥ k ≥ 0
    if k < 0 or k > n:
        print("Ошибка: должно выполняться условие n ≥ k ≥ 0")
        return
    
    # Способ 1: вычисление с использованием целочисленного деления
    # и избегание переполнения путем чередования умножения и деления
    result = 1
    
    # Вычисляем C(n, k) = n!/(k!(n-k)!) = n(n-1)...(n-k+1)/k!
    # Оптимизированный способ: уменьшаем числитель и знаменатель одновременно
    for i in range(1, k + 1):
        result = result * (n - k + i) // i
    
    # Вывод результата
    print(f"\nC({n}, {k}) = {n}({n-1})...({n-k+1}) / {k}! = {result}")
    
    # Способ 2: подробное вычисление числителя и знаменателя (для наглядности)
    print("\nПодробное вычисление:")
    numerator = 1
    denominator = 1
    
    # Вычисляем числитель: n(n-1)...(n-k+1)
    print(f"Числитель: {n}", end="")
    for i in range(1, k):
        factor = n - i
        numerator *= factor
        print(f" * {factor}", end="")
    if k > 0:
        numerator *= (n - k + 1)
        print(f" * {n-k+1}" if k > 1 else "", end="")
    else:
        print(" (пустое произведение = 1)", end="")
    
    # Вычисляем знаменатель: k!
    print(f"\nЗнаменатель: {k}!", end="")
    for i in range(1, k + 1):
        denominator *= i
    print(f" = {denominator}")
    
    # Проверка: результат должен совпадать с первым способом
    print(f"Проверка: {numerator} / {denominator} = {numerator / denominator}")
    print(f"Целая часть: {numerator // denominator}")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
