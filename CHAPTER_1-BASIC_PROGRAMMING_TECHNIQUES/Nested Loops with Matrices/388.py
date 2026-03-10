"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
11. Вложенные циклы в матричных задачах

388. В данной квадратной целочисленной матрице порядка 17 указать индексы всех элементов с наибольшим значением.
"""


import random

def get_matrix():
    """Выбор способа ввода целочисленной матрицы 17x17."""
    print("=== Задача 388: Индексы всех элементов с наибольшим значением ===")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод")
    print("2 — Случайная генерация")
    print("3 — Готовые примеры")

    choice = input("Ваш выбор (1/2/3): ").strip()
    while choice not in ('1', '2', '3'):
        choice = input("Выберите 1, 2 или 3: ").strip()

    n = 17

    if choice == '1':
        try:
            print(f"Введите матрицу {n}x{n} построчно (целые числа):")
            matrix = []
            for i in range(n):
                row = list(map(int, input(f"Строка {i+1}: ").split()))
                if len(row) != n:
                    print(f"Ошибка: в строке должно быть {n} чисел, получено {len(row)}.")
                    return None
                matrix.append(row)
            return matrix
        except ValueError:
            print("Ошибка ввода. Введите целые числа.")
            return None

    elif choice == '2':
        matrix = [[random.randint(-100, 100) for _ in range(n)] for _ in range(n)]
        print("\nСгенерирована матрица 17x17 (первые несколько строк):")
        for i in range(min(5, n)):
            print(" ".join(f"{x:4d}" for x in matrix[i][:10]) + "...")
        print("...")
        return matrix

    else:
        examples = [
            # 1. все элементы равны
            [[1]*n for _ in range(n)],
            # 2. возрастающая по строкам
            [[i*j for j in range(1, n+1)] for i in range(1, n+1)],
            # 3. случайная, но с одним большим числом
            [[random.randint(-50, 50) for _ in range(n)] for _ in range(n)],
            # 4. максимум в нескольких местах
            [[ (i+1)*(j+1) % 100 for j in range(n)] for i in range(n)],
            # 5. матрица с отрицательными числами, максимум = 100 в углах
            [[100 if (i==0 and j==0) or (i==n-1 and j==n-1) else -1 for j in range(n)] for i in range(n)]
        ]
        # Подправим пример 3, чтобы не был случайным при каждом запуске – сделаем фиксированным
        examples[2] = [[ (i+1)*2 + (j+1)*3 for j in range(n)] for i in range(n)]
        print("\nГотовые примеры:")
        for idx, ex in enumerate(examples, 1):
            print(f"{idx}: Первая строка: {ex[0][:5]}... (всего {len(ex)}x{len(ex)})")
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
    n = 17  # порядок

    # Поиск максимального значения и сбор индексов
    max_val = float('-inf')
    positions = []
    for i in range(n):
        for j in range(n):
            val = matrix[i][j]
            if val > max_val:
                max_val = val
                positions = [(i, j)]
            elif val == max_val:
                positions.append((i, j))

    print("\n" + "="*50)
    print("РЕЗУЛЬТАТ")
    print("="*50)
    print(f"Наибольшее значение элементов: {max_val}")
    print("Индексы (i, j) всех таких элементов (нумерация с 1):")
    for i, j in positions:
        print(f"  строка {i+1}, столбец {j+1}")
    print(f"Всего найдено: {len(positions)}")
    print("="*50)

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
