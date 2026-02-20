"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
10. Вложенные циклы

318. Дано натуральное число n. Получить f0f1 … fn, где
fi = 1 / (i * i + 1) + 1 / (i * i + 2) + ... + 1 / (i * i + i + 1).
"""


import random

def compute_f_i(i):
    """Вычисляет f_i = sum_{k=1}^{i+1} 1/(i^2 + k)"""
    total = 0.0
    for k in range(1, i + 2):  # от 1 до i+1 включительно
        total += 1.0 / (i * i + k)
    return total

def main():
    print("Задача 318. Вычислить f_i для i=0..n, где f_i = 1/(i^2+1) + ... + 1/(i^2+i+1).")
    
    # Выбор способа ввода
    print("\nВыберите способ задания n:")
    print("1. Ввести n вручную")
    print("2. Использовать готовый пример (несколько значений n)")
    
    while True:
        try:
            choice = int(input("Ваш выбор (1-2): "))
            if 1 <= choice <= 2:
                break
            else:
                print("Ошибка: введите 1 или 2.")
        except ValueError:
            print("Ошибка: введите целое число.")
    
    n_values = []
    if choice == 1:
        while True:
            try:
                n = int(input("Введите натуральное число n: "))
                if n >= 0:  # 0 считается натуральным? В условии натуральное обычно положительное, но f_0 есть. Будем считать n>=0.
                    n_values = [n]
                    break
                else:
                    print("Ошибка: n должно быть неотрицательным.")
            except ValueError:
                print("Ошибка: введите целое число.")
    else:
        # Готовые примеры
        examples = [0, 1, 2, 3, 5, 10]
        print("Выберите n из списка:")
        for i, ex in enumerate(examples, 1):
            print(f"{i}. n = {ex}")
        while True:
            try:
                ex_choice = int(input("Ваш выбор (1-{}): ".format(len(examples))))
                if 1 <= ex_choice <= len(examples):
                    n = examples[ex_choice-1]
                    n_values = [n]
                    break
                else:
                    print(f"Ошибка: введите число от 1 до {len(examples)}.")
            except ValueError:
                print("Ошибка: введите целое число.")
    
    for n in n_values:
        print(f"\nРезультаты для n = {n}:")
        print("i\tf_i")
        print("-" * 20)
        for i in range(n + 1):
            f = compute_f_i(i)
            print(f"{i}\t{f:.10f}")

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
