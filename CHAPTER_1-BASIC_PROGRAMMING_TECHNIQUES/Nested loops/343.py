"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
10. Вложенные циклы

343. Даны действительные числа x1, ... ,x17 Найти сумму Найти сумму abs(xi - xj), (1 <= i < j <= 17).
"""


import random

def get_numbers():
    """Выбор способа ввода 17 действительных чисел."""
    print("Выберите способ ввода:")
    print("1 - Ручной ввод")
    print("2 - Случайная генерация")
    print("3 - Готовый пример")
    choice = input("Ваш выбор (1/2/3): ").strip()
    while choice not in ('1', '2', '3'):
        choice = input("Некорректно. Выберите 1, 2 или 3: ")

    if choice == '1':
        try:
            print("Введите 17 действительных чисел x1...x17 через пробел:")
            line = input().strip()
            tokens = line.split()
            if len(tokens) != 17:
                print("Ожидалось 17 чисел.")
                return None
            x = []
            for t in tokens:
                x.append(float(t))
            return x
        except ValueError:
            print("Ошибка ввода.")
            return None

    elif choice == '2':
        x = [random.uniform(-10, 10) for _ in range(17)]
        print("Сгенерированы числа:")
        print(x)
        return x

    else:  # choice == '3'
        examples = [
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
            [1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5],
            [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700]
        ]
        print("Готовые примеры:")
        for idx, ex in enumerate(examples, 1):
            print(f"{idx}: {ex[:5]}... (всего 17)")
        try:
            idx = int(input("Выберите номер примера: "))
            if 1 <= idx <= len(examples):
                x = examples[idx-1]
                # преобразуем в float, если это целые
                x = [float(v) for v in x]
                return x
            else:
                print("Неверный номер.")
                return None
        except ValueError:
            print("Ошибка ввода.")
            return None

def sum_abs_differences(x):
    """Вычисляет сумму |x_i - x_j| для всех i<j."""
    n = len(x)
    total = 0.0
    for i in range(n):
        for j in range(i+1, n):
            total += abs(x[i] - x[j])
    return total

def main():
    x = get_numbers()
    if x is None:
        return
    print("\n" + "="*60)
    print("Входные числа (x1...x17):")
    print(x)
    print("="*60)

    result = sum_abs_differences(x)
    print(f"\nСумма |x_i - x_j| для всех i < j = {result}")

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
