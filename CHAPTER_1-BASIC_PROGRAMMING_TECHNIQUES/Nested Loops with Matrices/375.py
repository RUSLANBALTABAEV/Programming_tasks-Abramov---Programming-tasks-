"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
11. Вложенные циклы в матричных задачах

375. Дана действительная матрица размера n*m, в которой не все элементы равны нулю. Получить новую матрицу путем деления всех элементов данной матрицы на ее наибольший по модулю элемент.
"""


import random

def get_matrix():
    """Выбор способа ввода размеров и элементов матрицы."""
    print("=== Задача 375: Нормировка матрицы по максимальному модулю ===")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод")
    print("2 — Случайная генерация")
    print("3 — Готовые примеры")

    choice = input("Ваш выбор (1/2/3): ").strip()
    while choice not in ('1', '2', '3'):
        choice = input("Выберите 1, 2 или 3: ").strip()

    if choice == '1':
        try:
            n = int(input("Введите количество строк n (>0): "))
            m = int(input("Введите количество столбцов m (>0): "))
            if n <= 0 or m <= 0:
                print("Размеры должны быть положительными.")
                return None
            print("Введите матрицу построчно (действительные числа):")
            matrix = []
            for i in range(n):
                row = list(map(float, input(f"Строка {i+1}: ").split()))
                if len(row) != m:
                    print(f"Ошибка: в строке должно быть {m} чисел, получено {len(row)}.")
                    return None
                matrix.append(row)
            return n, m, matrix
        except ValueError:
            print("Ошибка ввода.")
            return None

    elif choice == '2':
        n = random.randint(1, 5)
        m = random.randint(1, 6)
        matrix = [[random.uniform(-10, 10) for _ in range(m)] for _ in range(n)]
        # Гарантируем, что не все нули, хотя random может дать все нули маловероятно, но подстрахуемся
        all_zero = True
        for row in matrix:
            for val in row:
                if val != 0:
                    all_zero = False
                    break
            if not all_zero:
                break
        if all_zero:
            matrix[0][0] = 1.0  # делаем не все нули
        print(f"\nСгенерирована матрица {n}×{m}:")
        for row in matrix:
            print(" ".join(f"{x:8.4f}" for x in row))
        return n, m, matrix

    else:
        examples = [
            (2, 3, [[1, 2, 3], [4, 5, 6]]),
            (3, 2, [[-1, 2], [3, -4], [5, -6]]),
            (2, 2, [[0, 0], [0, 5]]),
            (3, 3, [[1.5, -2.3, 0.1], [0, 4.7, -1.2], [3.3, -0.5, 2.2]]),
            (1, 4, [[10, -20, 30, -40]])
        ]
        print("\nГотовые примеры (n, m, матрица):")
        for idx, (n_val, m_val, mat) in enumerate(examples, 1):
            print(f"{idx}: {n_val}×{m_val}, первый элемент {mat[0][0]}")
        try:
            num = int(input("Выберите номер примера: "))
            if 1 <= num <= len(examples):
                n, m, matrix = examples[num-1]
                return n, m, matrix
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
    n, m, a = data

    # Поиск максимального по модулю элемента
    max_abs = 0.0
    for i in range(n):
        for j in range(m):
            if abs(a[i][j]) > max_abs:
                max_abs = abs(a[i][j])

    if max_abs == 0:
        print("Ошибка: все элементы равны нулю, деление невозможно.")
        return

    # Формирование новой матрицы
    b = [[0.0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            b[i][j] = a[i][j] / max_abs

    print("\n" + "="*60)
    print("Исходная матрица:")
    for i in range(n):
        print(" ".join(f"{a[i][j]:10.6f}" for j in range(m)))
    print(f"\nМаксимальный по модулю элемент: {max_abs:.6f}")
    print("\nНормированная матрица (деление на max_abs):")
    for i in range(n):
        print(" ".join(f"{b[i][j]:10.6f}" for j in range(m)))
    print("="*60)

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
