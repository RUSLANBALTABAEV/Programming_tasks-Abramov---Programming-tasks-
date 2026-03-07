"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
11. Вложенные циклы в матричных задачах

373. Даны натуральное число n, действительная матрица размером n*9. Найти среднее арифметическое:
а) каждого из столбцов;
б) каждого из столбцов, имеющих четные номера.
"""


import random

def get_matrix():
    """Выбор способа ввода n и матрицы n×9."""
    print("=== Задача 373: Средние арифметические столбцов матрицы ===")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод")
    print("2 — Случайная генерация")
    print("3 — Готовые примеры")

    choice = input("Ваш выбор (1/2/3): ").strip()
    while choice not in ('1', '2', '3'):
        choice = input("Выберите 1, 2 или 3: ").strip()

    if choice == '1':
        try:
            n = int(input("Введите натуральное число n (количество строк): "))
            if n <= 0:
                print("n должно быть положительным.")
                return None
            print("Введите матрицу построчно (9 действительных чисел в строке):")
            matrix = []
            for i in range(n):
                row = list(map(float, input(f"Строка {i+1}: ").split()))
                if len(row) != 9:
                    print(f"Ошибка: в строке должно быть 9 чисел, получено {len(row)}.")
                    return None
                matrix.append(row)
            return n, matrix
        except ValueError:
            print("Ошибка ввода.")
            return None

    elif choice == '2':
        n = random.randint(2, 10)
        matrix = [[random.uniform(-10, 10) for _ in range(9)] for _ in range(n)]
        print(f"\nСгенерирована матрица {n}×9:")
        for row in matrix:
            print(" ".join(f"{x:8.4f}" for x in row))
        return n, matrix

    else:
        examples = [
            (3, [[1,2,3,4,5,6,7,8,9], [9,8,7,6,5,4,3,2,1], [1,1,1,1,1,1,1,1,1]]),
            (4, [[i*j for j in range(1,10)] for i in range(1,5)]),
            (2, [[0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5],
                 [10, 20, 30, 40, 50, 60, 70, 80, 90]])
        ]
        print("\nГотовые примеры:")
        for idx, (n_val, mat_val) in enumerate(examples, 1):
            print(f"{idx}: n={n_val}, первая строка: {mat_val[0]}")
        try:
            num = int(input("Выберите номер примера: "))
            if 1 <= num <= len(examples):
                n, matrix = examples[num-1]
                return n, matrix
            else:
                print("Неверный номер!")
                return None
        except ValueError:
            print("Ошибка ввода.")
            return None

def main():
    data = get_matrix()
    if data is None:
        return
    n, matrix = data

    # Вычисление средних арифметических для всех столбцов
    col_means = [0.0] * 9
    for j in range(9):
        total = 0.0
        for i in range(n):
            total += matrix[i][j]
        col_means[j] = total / n

    # Средние для четных столбцов (номера 2,4,6,8 => индексы 1,3,5,7)
    even_means = [col_means[j] for j in range(1, 9, 2)]

    print("\n" + "="*60)
    print("РЕЗУЛЬТАТ")
    print("="*60)
    print("а) Средние арифметические каждого столбца:")
    for j in range(9):
        print(f"Столбец {j+1}: {col_means[j]:.6f}")
    print("\nб) Средние арифметические столбцов с четными номерами (2,4,6,8):")
    for idx, val in enumerate(even_means):
        print(f"Столбец {2*(idx+1)}: {val:.6f}")
    print("="*60)

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
