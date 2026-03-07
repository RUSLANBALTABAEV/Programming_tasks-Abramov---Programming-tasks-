"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
11. Вложенные циклы в матричных задачах

367. Даны целые числа a1, a2, a3. Получить целочисленную матрицу |bij|i,j=1,2,3, для которой bij = ai - 3 * aj.
"""


import random

def get_input():
    """Выбор способа ввода трёх целых чисел a1, a2, a3."""
    print("=== Задача 367: Формирование матрицы b_ij = a_i - 3a_j ===")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод")
    print("2 — Случайная генерация")
    print("3 — Готовые примеры")

    choice = input("Ваш выбор (1/2/3): ").strip()
    while choice not in ('1', '2', '3'):
        choice = input("Выберите 1, 2 или 3: ").strip()

    if choice == '1':
        try:
            a = []
            print("Введите три целых числа a1, a2, a3 через пробел:")
            line = input().strip()
            tokens = line.split()
            if len(tokens) != 3:
                print("Ожидалось ровно 3 числа.")
                return None
            for t in tokens:
                a.append(int(t))
            return a
        except ValueError:
            print("Ошибка ввода. Введите целые числа.")
            return None

    elif choice == '2':
        a = [random.randint(-10, 10) for _ in range(3)]
        print(f"Сгенерированы числа: a1 = {a[0]}, a2 = {a[1]}, a3 = {a[2]}")
        return a

    else:
        examples = [
            [1, 2, 3],
            [5, -2, 0],
            [10, 10, 10],
            [-5, -5, -5],
            [3, 1, 4]
        ]
        print("\nГотовые примеры:")
        for i, ex in enumerate(examples, 1):
            print(f"{i}. a1={ex[0]}, a2={ex[1]}, a3={ex[2]}")
        try:
            num = int(input("Выберите номер примера: "))
            if 1 <= num <= len(examples):
                return examples[num-1]
            else:
                print("Неверный номер!")
                return None
        except ValueError:
            print("Ошибка ввода.")
            return None

def main():
    a = get_input()
    if a is None:
        return

    # Формирование матрицы 3x3
    n = 3
    b = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            b[i][j] = a[i] - 3 * a[j]

    print("\n" + "="*50)
    print("Исходные числа a1, a2, a3:", a)
    print("Матрица b (размер 3x3):")
    for i in range(n):
        row = " ".join(f"{b[i][j]:5d}" for j in range(n))
        print(row)
    print("="*50)

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
