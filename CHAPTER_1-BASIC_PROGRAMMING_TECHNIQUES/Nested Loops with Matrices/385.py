"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
11. Вложенные циклы в матричных задачах

385. В данной действительной квадратной матрице порядка n найти сумму элементов строки, в которой расположен элемент с наименьшим значением. Предполагается, что такой элемент единственный.
"""


import random

def get_matrix():
    """Выбор способа ввода n и квадратной матрицы."""
    print("=== Задача 385: Сумма строки с наименьшим элементом ===")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод")
    print("2 — Случайная генерация")
    print("3 — Готовые примеры")

    choice = input("Ваш выбор (1/2/3): ").strip()
    while choice not in ('1', '2', '3'):
        choice = input("Выберите 1, 2 или 3: ").strip()

    if choice == '1':
        try:
            n = int(input("Введите порядок матрицы n (натуральное): "))
            if n <= 0:
                print("n должно быть положительным.")
                return None
            print("Введите матрицу построчно (действительные числа):")
            matrix = []
            for i in range(n):
                row = list(map(float, input(f"Строка {i+1}: ").split()))
                if len(row) != n:
                    print(f"Ошибка: в строке должно быть {n} чисел, получено {len(row)}.")
                    return None
                matrix.append(row)
            return n, matrix
        except ValueError:
            print("Ошибка ввода.")
            return None

    elif choice == '2':
        n = random.randint(2, 8)
        matrix = [[random.uniform(-10, 10) for _ in range(n)] for _ in range(n)]
        print(f"\nСгенерирована матрица {n}×{n}:")
        for row in matrix:
            print(" ".join(f"{x:8.4f}" for x in row))
        return n, matrix

    else:
        examples = [
            (3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            (2, [[-1.5, 2.3], [3.1, -4.2]]),
            (3, [[0, 0, 0], [0, -1, 0], [0, 0, 0]]),
            (4, [[i*j for j in range(1,5)] for i in range(1,5)]),
            (2, [[5, 5], [5, 5]])  # здесь все равны, но по условию элемент единственный — для демо
        ]
        print("\nГотовые примеры (n, матрица):")
        for idx, (n_val, mat) in enumerate(examples, 1):
            print(f"{idx}: n={n_val}, первая строка: {mat[0][:3]}")
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

    # Поиск минимального элемента и его строки
    min_val = float('inf')
    min_row = -1
    for i in range(n):
        for j in range(n):
            if matrix[i][j] < min_val:
                min_val = matrix[i][j]
                min_row = i

    # Проверка на уникальность минимального (хотя бы предупреждение)
    count_min = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == min_val:
                count_min += 1
    if count_min > 1:
        print(f"\nВнимание: найдено {count_min} элементов с минимальным значением {min_val:.6f}. Используется первый найденный (строка {min_row+1}).")

    # Сумма элементов строки с индексом min_row
    row_sum = sum(matrix[min_row])

    print("\n" + "="*50)
    print("РЕЗУЛЬТАТ")
    print("="*50)
    print(f"Наименьший элемент матрицы: {min_val:.6f}")
    print(f"Он находится в строке № {min_row+1}")
    print(f"Сумма элементов этой строки: {row_sum:.6f}")
    print("="*50)

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
