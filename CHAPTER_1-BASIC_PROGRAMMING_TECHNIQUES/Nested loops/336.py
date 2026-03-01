"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
10. Вложенные циклы

336. Даны натуральное число n, действительное число x.
Вычислить:
а) nEi=1 * (2 * i)! + abs(x) / (i * i)!;       б) 1 / n! * nEk=1 * (-1) ^ k * x / (k! + 1)!;
в) nEk=1 * k ^ k * x ^ 2 * k;                  г) nEk=1 * nEm=k * x + k / m.
"""


import math
import random

def get_input():
    """Выбор способа ввода n и x."""
    print("Выберите способ ввода:")
    print("1 - Ручной ввод")
    print("2 - Случайные значения")
    print("3 - Готовый пример")
    choice = input("Ваш выбор (1/2/3): ").strip()
    while choice not in ('1', '2', '3'):
        choice = input("Некорректно. Выберите 1, 2 или 3: ")

    if choice == '1':
        try:
            n = int(input("Введите натуральное число n: "))
            if n <= 0:
                print("n должно быть положительным.")
                return None
            x = float(input("Введите действительное число x: "))
            return n, x
        except ValueError:
            print("Ошибка ввода.")
            return None
    elif choice == '2':
        n = random.randint(1, 8)  # ограничим, чтобы избежать переполнения
        x = random.uniform(-5, 5)
        print(f"Сгенерировано: n = {n}, x = {x:.4f}")
        return n, x
    else:
        examples = [(5, 2.0), (3, -1.5), (7, 0.5), (4, 3.0)]
        print("Готовые примеры:")
        for i, (n_val, x_val) in enumerate(examples, 1):
            print(f"{i}: n = {n_val}, x = {x_val}")
        try:
            idx = int(input("Выберите номер: "))
            if 1 <= idx <= len(examples):
                return examples[idx - 1]
            else:
                print("Неверный номер.")
                return None
        except ValueError:
            print("Ошибка ввода.")
            return None

def main():
    data = get_input()
    if data is None:
        return
    n, x = data
    print(f"\nВычисления для n = {n}, x = {x}\n")

    # a) ∑ ( (2i)! + |x| ) / (i²)!
    sum_a = 0.0
    for i in range(1, n + 1):
        term = (math.factorial(2 * i) + abs(x)) / math.factorial(i * i)
        sum_a += term
    print(f"a) Сумма = {sum_a}")

    # б) (1/n!) ∑ (-1)^k x^k / ( (k+1)! )
    sum_b = 0.0
    for k in range(1, n + 1):
        sign = -1 if k % 2 else 1
        term = sign * (x ** k) / math.factorial(k + 1)
        sum_b += term
    sum_b /= math.factorial(n)
    print(f"б) Сумма = {sum_b}")

    # в) ∑ k^k * x^(2k)
    sum_c = 0.0
    for k in range(1, n + 1):
        sum_c += (k ** k) * (x ** (2 * k))
    print(f"в) Сумма = {sum_c}")

    # г) ∑_{k=1}^n ∑_{m=k}^n (x + k)/m
    sum_d = 0.0
    for k in range(1, n + 1):
        for m in range(k, n + 1):
            sum_d += (x + k) / m
    print(f"г) Сумма = {sum_d}")

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
