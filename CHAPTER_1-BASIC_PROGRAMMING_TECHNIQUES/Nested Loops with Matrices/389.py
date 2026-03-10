"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
11. Вложенные циклы в матричных задачах

389. Дана действительная матрица размера n*m, все элементы которой различны. В каждой строке выбирается элемент с наименьшим значением, затем среди этих чисел выбирается наибольшее. Указать индексы элемента с найденным значением.
"""


import random

def get_matrix():
    """Выбор способа ввода матрицы n×m с различными элементами."""
    print("=== Задача 389: Наибольший среди минимальных элементов строк ===")
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
            print("Введите матрицу построчно (действительные числа, все элементы различны):")
            matrix = []
            seen = set()
            for i in range(n):
                row = list(map(float, input(f"Строка {i+1}: ").split()))
                if len(row) != m:
                    print(f"Ошибка: в строке должно быть {m} чисел.")
                    return None
                # Проверка на уникальность в пределах всей матрицы
                for val in row:
                    if val in seen:
                        print(f"Ошибка: элемент {val} уже встречался. Все элементы должны быть различны.")
                        return None
                    seen.add(val)
                matrix.append(row)
            return n, m, matrix
        except ValueError:
            print("Ошибка ввода.")
            return None

    elif choice == '2':
        n = random.randint(2, 6)
        m = random.randint(2, 7)
        # Генерируем уникальные числа с помощью random.sample
        total = n * m
        # Для действительных чисел можно генерировать целые, но чтобы были вещественные, сделаем так:
        # Сгенерируем уникальные целые и поделим на случайные дроби? Проще сделать уникальные целые.
        numbers = random.sample(range(-100, 100), total)  # гарантирует уникальность
        matrix = []
        idx = 0
        for i in range(n):
            row = [float(numbers[idx + j]) for j in range(m)]
            idx += m
            matrix.append(row)
        print(f"\nСгенерирована матрица {n}×{m} (все элементы различны):")
        for row in matrix:
            print(" ".join(f"{x:8.4f}" for x in row))
        return n, m, matrix

    else:
        examples = [
            (2, 3, [[1, 2, 3], [4, 5, 6]]),           # минимумы: 1 и 4, максимум 4 -> (2,1)
            (3, 2, [[-1.5, 2.3], [3.1, -4.2], [5.7, -6.8]]), # минимумы: -1.5, -4.2, -6.8; максимум -1.5 -> (1,1)
            (2, 4, [[10, 20, 30, 40], [5, 15, 25, 35]]),     # минимумы: 10 и 5, максимум 10 -> (1,1)
            (3, 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]]),       # минимумы: 1,4,7; максимум 7 -> (3,1)
            (2, 2, [[0, -1], [-2, 3]])                         # минимумы: -1 и -2; максимум -1 -> (1,2)
        ]
        print("\nГотовые примеры (n, m, матрица):")
        for idx, (n_val, m_val, mat) in enumerate(examples, 1):
            print(f"{idx}: {n_val}×{m_val}, первая строка: {mat[0]}")
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
    n, m, matrix = data

    # Находим минимальные элементы в каждой строке и запоминаем их позиции
    row_mins = []  # список кортежей (значение, строка, столбец)
    for i in range(n):
        min_val = min(matrix[i])
        # Находим столбец этого минимума (так как все элементы различны, он единственный)
        j = matrix[i].index(min_val)
        row_mins.append((min_val, i, j))

    # Среди них выбираем максимальный
    max_of_mins = max(row_mins, key=lambda x: x[0])
    val, i, j = max_of_mins

    print("\n" + "="*50)
    print("РЕЗУЛЬТАТ")
    print("="*50)
    print(f"Минимальные элементы по строкам:")
    for idx, (v, row, col) in enumerate(row_mins):
        print(f"  Строка {row+1}: минимальный = {v:.6f} (столбец {col+1})")
    print(f"\nНаибольший среди них: {val:.6f}")
    print(f"Индексы: строка {i+1}, столбец {j+1}")
    print("="*50)

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
