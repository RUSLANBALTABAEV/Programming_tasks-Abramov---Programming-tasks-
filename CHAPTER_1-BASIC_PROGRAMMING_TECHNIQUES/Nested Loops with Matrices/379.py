"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
11. Вложенные циклы в матричных задачах

379. Дана действительная матрица размера m*n. Определить числа b1,...,bm, равные соответственно:
а) суммам элементов строк;
б) произведениям элементов строк;
в) наименьшим значениям элементов строк;
г) значениям средних арифметических элементов строк;
д) разностям наибольших и наименьших значений элементов строк.
"""


import random

def get_matrix():
    """Выбор способа ввода размеров и элементов матрицы."""
    print("=== Задача 379: Статистики по строкам матрицы ===")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод")
    print("2 — Случайная генерация")
    print("3 — Готовые примеры")

    choice = input("Ваш выбор (1/2/3): ").strip()
    while choice not in ('1', '2', '3'):
        choice = input("Выберите 1, 2 или 3: ").strip()

    if choice == '1':
        try:
            m = int(input("Введите количество строк m (>0): "))
            n = int(input("Введите количество столбцов n (>0): "))
            if m <= 0 or n <= 0:
                print("Размеры должны быть положительными.")
                return None
            print("Введите матрицу построчно (действительные числа):")
            matrix = []
            for i in range(m):
                row = list(map(float, input(f"Строка {i+1}: ").split()))
                if len(row) != n:
                    print(f"Ошибка: в строке должно быть {n} чисел, получено {len(row)}.")
                    return None
                matrix.append(row)
            return m, n, matrix
        except ValueError:
            print("Ошибка ввода.")
            return None

    elif choice == '2':
        m = random.randint(2, 5)
        n = random.randint(2, 6)
        matrix = [[random.uniform(-10, 10) for _ in range(n)] for _ in range(m)]
        print(f"\nСгенерирована матрица {m}×{n}:")
        for row in matrix:
            print(" ".join(f"{x:8.4f}" for x in row))
        return m, n, matrix

    else:
        examples = [
            (2, 3, [[1, 2, 3], [4, 5, 6]]),
            (3, 2, [[-1.5, 2.3], [3.1, -4.2], [5.7, -6.8]]),
            (2, 4, [[0, 0, 0, 0], [1, -1, 2, -2]]),
            (3, 3, [[1, 1, 1], [2, 2, 2], [3, 3, 3]]),
            (4, 1, [[10], [20], [30], [40]])  # вектор-столбец
        ]
        print("\nГотовые примеры (m, n, матрица):")
        for idx, (m_val, n_val, mat) in enumerate(examples, 1):
            print(f"{idx}: {m_val}×{n_val}, первый элемент {mat[0][0]}")
        try:
            num = int(input("Выберите номер примера: "))
            if 1 <= num <= len(examples):
                m, n, matrix = examples[num-1]
                return m, n, matrix
            else:
                print("Неверный номер!")
                return None
        except ValueError:
            print("Ошибка ввода.")
            return None

def compute_row_stats(matrix):
    """Вычисляет для каждой строки статистики и возвращает списки b1..b5."""
    sums = []
    prods = []
    mins = []
    avgs = []
    ranges = []
    for row in matrix:
        s = sum(row)
        p = 1.0
        for val in row:
            p *= val
        mn = min(row)
        mx = max(row)
        avg = s / len(row)
        rng = mx - mn
        sums.append(s)
        prods.append(p)
        mins.append(mn)
        avgs.append(avg)
        ranges.append(rng)
    return sums, prods, mins, avgs, ranges

def main():
    data = get_matrix()
    if data is None:
        return
    m, n, matrix = data

    sums, prods, mins, avgs, ranges = compute_row_stats(matrix)

    print("\n" + "="*60)
    print("РЕЗУЛЬТАТЫ")
    print("="*60)
    for i in range(m):
        print(f"Строка {i+1}:")
        print(f"  а) Сумма элементов: {sums[i]:.6f}")
        print(f"  б) Произведение элементов: {prods[i]:.6f}")
        print(f"  в) Минимальный элемент: {mins[i]:.6f}")
        print(f"  г) Среднее арифметическое: {avgs[i]:.6f}")
        print(f"  д) Размах (max-min): {ranges[i]:.6f}")
        print("-" * 40)
    print("="*60)

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
