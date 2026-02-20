"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
10. Вложенные циклы

317. Даны действительные числа a1,…, a10. Вычислить a1 + a2 * a2 + ... + a10 ^ a10.
"""


import random

def main():
    print("Задача 317. Вычислить a1 + a2^2 + a3^3 + ... + a10^10.")
    
    # Выбор способа ввода
    print("\nВыберите способ задания чисел:")
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
    
    n = 10
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
        a = [random.uniform(-5, 5) for _ in range(n)]
        print(f"\nСгенерированы случайные числа:")
        for i, val in enumerate(a, 1):
            print(f"a_{i} = {val:.4f}")
    
    else:
        # Готовые примеры
        examples = [
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5],
            [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
        ]
        print("Выберите готовый набор:")
        for idx, ex in enumerate(examples, 1):
            print(f"{idx}. {ex[:3]}... (всего {len(ex)} чисел)")
        while True:
            try:
                ex_choice = int(input("Ваш выбор (1-3): "))
                if 1 <= ex_choice <= len(examples):
                    a = examples[ex_choice-1]
                    break
                else:
                    print("Ошибка: введите число от 1 до 3.")
            except ValueError:
                print("Ошибка: введите целое число.")
    
    # Вычисление суммы
    total = 0.0
    print("\nВычисление:")
    for i, val in enumerate(a, start=1):
        term = val ** i
        total += term
        print(f"a_{i}^{i} = {val:.6f}^{i} = {term:.6f}")
    
    print(f"\nРезультат: {total:.6f}")

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
