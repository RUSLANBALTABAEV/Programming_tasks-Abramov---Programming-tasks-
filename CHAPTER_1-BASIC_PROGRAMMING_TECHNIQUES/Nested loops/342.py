"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
10. Вложенные циклы

342. Даны действительные числа x, y1, ... ,y25. В последовательности y1, ... ,y25 найти два члена, среднее арифметическое которых ближе всего к x.
"""


import random
import math

def get_input():
    """Выбор способа ввода x и последовательности y."""
    print("Выберите способ ввода:")
    print("1 - Ручной ввод")
    print("2 - Случайная генерация")
    print("3 - Готовый пример")
    choice = input("Ваш выбор (1/2/3): ").strip()
    while choice not in ('1', '2', '3'):
        choice = input("Некорректно. Выберите 1, 2 или 3: ")

    if choice == '1':
        try:
            x = float(input("Введите действительное число x: "))
            print("Введите 25 действительных чисел y1...y25 через пробел:")
            line = input().strip()
            tokens = line.split()
            if len(tokens) != 25:
                print("Ожидалось 25 чисел.")
                return None
            y = []
            for t in tokens:
                y.append(float(t))
            return x, y
        except ValueError:
            print("Ошибка ввода.")
            return None

    elif choice == '2':
        x = random.uniform(-10, 10)
        y = [random.uniform(-10, 10) for _ in range(25)]
        print(f"Сгенерировано: x = {x:.4f}")
        print("y = [", ", ".join(f"{val:.4f}" for val in y[:5]), "...] (всего 25)")
        return x, y

    else:  # choice == '3'
        examples = [
            (5.0, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]),
            (0.0, [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]),
            (3.14, [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5]),
            (2.5, [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]),
            (100.0, [90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114])
        ]
        print("Готовые примеры (x, y):")
        for idx, (x_val, y_val) in enumerate(examples, 1):
            print(f"{idx}: x = {x_val}, y = {y_val[:5]}... (всего 25)")
        try:
            idx = int(input("Выберите номер примера: "))
            if 1 <= idx <= len(examples):
                x, y = examples[idx-1]
                # преобразуем y в float, если они int
                y = [float(v) for v in y]
                return x, y
            else:
                print("Неверный номер.")
                return None
        except ValueError:
            print("Ошибка ввода.")
            return None

def find_closest_pair(x, y):
    """Находит пару индексов (i, j) с i<j, среднее арифметическое которых ближе всего к x."""
    best_diff = float('inf')
    best_pair = None
    n = len(y)
    for i in range(n):
        for j in range(i+1, n):
            avg = (y[i] + y[j]) / 2
            diff = abs(avg - x)
            if diff < best_diff:
                best_diff = diff
                best_pair = (i, j)
    return best_pair, best_diff

def main():
    data = get_input()
    if data is None:
        return
    x, y = data
    print("\n" + "="*60)
    print(f"x = {x}")
    print("y =", y)
    print("="*60)

    (i, j), best_diff = find_closest_pair(x, y)
    avg = (y[i] + y[j]) / 2
    print(f"\nПара с индексом {i+1} и {j+1} (значения {y[i]} и {y[j]})")
    print(f"Среднее арифметическое = {avg}")
    print(f"Отклонение от x = {abs(avg - x)}")
    print(f"Это ближайшее к {x} значение среди всех пар.")

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
