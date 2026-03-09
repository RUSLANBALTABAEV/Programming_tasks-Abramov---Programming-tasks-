"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
11. Вложенные циклы в матричных задачах

377. Дана действительная квадратная матрица порядка 12. 
Заменить нулями все ее элементы, расположенные на главной диагонали и выше нее.
"""


import random

def get_matrix():
    """Выбор способа ввода матрицы 12x12."""
    print("=== Задача 377: Обнуление главной диагонали и выше ===")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод")
    print("2 — Случайная генерация")
    print("3 — Готовый пример")

    choice = input("Ваш выбор (1/2/3): ").strip()
    while choice not in ('1', '2', '3'):
        choice = input("Выберите 1, 2 или 3: ").strip()

    n = 12  # порядок матрицы

    if choice == '1':
        try:
            print(f"Введите матрицу {n}x{n} построчно (действительные числа):")
            matrix = []
            for i in range(n):
                row = list(map(float, input(f"Строка {i+1}: ").split()))
                if len(row) != n:
                    print(f"Ошибка: в строке должно быть {n} чисел.")
                    return None
                matrix.append(row)
            return matrix
        except ValueError:
            print("Ошибка ввода.")
            return None

    elif choice == '2':
        matrix = [[random.uniform(-10, 10) for _ in range(n)] for _ in range(n)]
        print("\nСгенерирована матрица 12x12:")
        for row in matrix:
            print(" ".join(f"{x:8.4f}" for x in row))
        return matrix

    else:
        examples = [
            [[i+j for j in range(1,13)] for i in range(1,13)],
            [[i*j for j in range(1,13)] for i in range(1,13)],
            [[1.5 * i - 2.3 * j for j in range(1,13)] for i in range(1,13)]
        ]
        print("\nГотовые примеры:")
        for idx, ex in enumerate(examples, 1):
            print(f"{idx}: Первая строка: {ex[0][:5]}...")
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
    matrix = get_matrix()
    if matrix is None:
        return

    n = 12
    print("\nИсходная матрица:")
    for row in matrix:
        print(" ".join(f"{x:8.4f}" for x in row))

    # Обнуление элементов на главной диагонали и выше (i <= j)
    for i in range(n):
        for j in range(i, n):  # j от i до n-1 включительно
            matrix[i][j] = 0.0

    print("\nМатрица после обнуления (главная диагональ и выше):")
    for row in matrix:
        print(" ".join(f"{x:8.4f}" for x in row))

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
