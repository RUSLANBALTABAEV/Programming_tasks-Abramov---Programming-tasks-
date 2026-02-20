"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
10. Вложенные циклы

319. Даны действительные числа a1,… , a24. Получить последовательность b1, …, b10, где b1 = a1 + a2 + ... + a24, b2 = a1 * a1 + a2 * a2 + ... + a24 * a24, ... , b10 = a1 ^ 10 + a2 ^ 10 + ... + a24 ^ 10.
"""


import random

def main():
    print("Задача 319. Вычислить b1..b10, где b_k = сумма a_i^k для i=1..24.")
    
    # Выбор способа ввода
    print("\nВыберите способ задания чисел a1..a24:")
    print("1. Ввести числа вручную")
    print("2. Сгенерировать случайные числа")
    print("3. Использовать готовый пример")
    
    while True:
        try:
            choice = int(input("Ваш выбор (1-3): "))
            if 1 <= choice <= 3:
                break
            else:
                print("Ошибка: введите 1, 2 или 3.")
        except ValueError:
            print("Ошибка: введите целое число.")
    
    n = 24
    a = []
    
    if choice == 1:
        print(f"\nВведите {n} действительных чисел:")
        for i in range(n):
            while True:
                try:
                    val = float(input(f"a_{i+1}: "))
                    a.append(val)
                    break
                except ValueError:
                    print("Ошибка: введите действительное число.")
    
    elif choice == 2:
        random.seed()
        a = [random.uniform(-10, 10) for _ in range(n)]
        print(f"\nСгенерированы случайные числа:")
        for i, val in enumerate(a, 1):
            print(f"a_{i:2} = {val:8.4f}")
    
    else:
        # Готовые примеры
        examples = [
            [1] * 24,  # все единицы
            [i for i in range(1, 25)],  # 1..24
            [i/10 for i in range(24)],  # 0.0, 0.1, ..., 2.3
            [random.uniform(-5, 5) for _ in range(24)]  # случайные, но фиксированные
        ]
        print("Выберите готовый набор:")
        desc = ["Все единицы", "Числа 1..24", "Дроби 0.0, 0.1, ..., 2.3", "Случайные (фиксированные)"]
        for idx, d in enumerate(desc, 1):
            print(f"{idx}. {d}")
        while True:
            try:
                ex_choice = int(input("Ваш выбор (1-4): "))
                if 1 <= ex_choice <= len(examples):
                    a = examples[ex_choice-1]
                    break
                else:
                    print("Ошибка: введите число от 1 до 4.")
            except ValueError:
                print("Ошибка: введите целое число.")
    
    # Вычисление b_k
    b = []
    print("\nВычисление степенных сумм:")
    for k in range(1, 11):
        total = 0.0
        for val in a:
            total += val ** k
        b.append(total)
        print(f"b_{k} = {total:.6f}")

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
