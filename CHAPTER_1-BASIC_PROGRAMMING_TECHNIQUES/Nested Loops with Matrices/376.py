"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
11. Вложенные циклы в матричных задачах

376. Даны натуральное число m, целые числа a1,...,am и целочисленная квадратная матрица порядка m. Строку с номером i матрицы назовем отмеченной, если ai > 0, и неотмеченной в противном случае.
а) Нужно все элементы, расположенные в отмеченных строках матрицы, преобразовать по правилу: отрицательные элементы заменить на -1, положительные – на 1, а нулевые оставить без изменения.
б) Подсчитать число отрицательных элементов матрицы, расположенных в отмеченных строках.
"""


import random

def get_input():
    """Выбор способа ввода m, массива a и матрицы."""
    print("=== Задача 376: Обработка отмеченных строк матрицы ===")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод")
    print("2 — Случайная генерация")
    print("3 — Готовые примеры")

    choice = input("Ваш выбор (1/2/3): ").strip()
    while choice not in ('1', '2', '3'):
        choice = input("Выберите 1, 2 или 3: ").strip()

    if choice == '1':
        try:
            m = int(input("Введите натуральное число m: "))
            if m <= 0:
                print("m должно быть положительным.")
                return None
            print(f"Введите {m} целых чисел a1...a{m} через пробел:")
            a_line = input().strip()
            a = list(map(int, a_line.split()))
            if len(a) != m:
                print(f"Ожидалось {m} чисел, получено {len(a)}.")
                return None
            print(f"Введите матрицу {m}x{m} построчно (целые числа):")
            matrix = []
            for i in range(m):
                row = list(map(int, input(f"Строка {i+1}: ").split()))
                if len(row) != m:
                    print(f"Ошибка: в строке должно быть {m} чисел.")
                    return None
                matrix.append(row)
            return m, a, matrix
        except ValueError:
            print("Ошибка ввода. Введите целые числа.")
            return None

    elif choice == '2':
        m = random.randint(2, 6)
        a = [random.randint(-3, 5) for _ in range(m)]
        matrix = [[random.randint(-5, 5) for _ in range(m)] for _ in range(m)]
        print(f"\nСгенерировано: m = {m}")
        print("a =", a)
        print("Матрица:")
        for row in matrix:
            print(" ".join(f"{x:4d}" for x in row))
        return m, a, matrix

    else:
        examples = [
            (3, [1, -2, 3], [[1, -2, 3], [4, -5, 6], [-7, 8, 0]]),
            (4, [0, 5, -1, 2], [[-1, 2, -3, 4], [5, -6, 7, -8], [9, 10, -11, 12], [-13, 14, -15, 16]]),
            (2, [1, 1], [[-1, 0], [2, -3]]),
            (3, [-1, -2, -3], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            (2, [0, 0], [[0, 0], [0, 0]])  # все нули, отмеченных нет
        ]
        print("\nГотовые примеры:")
        for idx, (m_val, a_val, mat) in enumerate(examples, 1):
            print(f"{idx}: m={m_val}, a={a_val}, первая строка матрицы: {mat[0]}")
        try:
            num = int(input("Выберите номер примера: "))
            if 1 <= num <= len(examples):
                m, a, matrix = examples[num-1]
                return m, a, matrix
            else:
                print("Неверный номер!")
                return None
        except ValueError:
            print("Ошибка ввода.")
            return None

def main():
    data = get_input()
    if data is None:
        return
    m, a, matrix = data

    # Определяем отмеченные строки (индексы с 0, но a_i соответствует i+1)
    marked = [a[i] > 0 for i in range(m)]

    print("\n" + "="*50)
    print("Исходные данные:")
    print(f"m = {m}")
    print("a =", a)
    print("Отмеченные строки:", [i+1 for i, flag in enumerate(marked) if flag])
    print("Исходная матрица:")
    for row in matrix:
        print(" ".join(f"{x:4d}" for x in row))
    print("="*50)

    # а) Преобразование элементов в отмеченных строках
    transformed = [row[:] for row in matrix]  # копия
    for i in range(m):
        if marked[i]:
            for j in range(m):
                if transformed[i][j] < 0:
                    transformed[i][j] = -1
                elif transformed[i][j] > 0:
                    transformed[i][j] = 1
                # ноль оставляем без изменения

    print("\nа) Матрица после преобразования отмеченных строк:")
    for row in transformed:
        print(" ".join(f"{x:4d}" for x in row))

    # б) Подсчёт отрицательных элементов в отмеченных строках исходной матрицы
    neg_count = 0
    for i in range(m):
        if marked[i]:
            for j in range(m):
                if matrix[i][j] < 0:
                    neg_count += 1

    print(f"\nб) Число отрицательных элементов в отмеченных строках исходной матрицы: {neg_count}")
    print("="*50)

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
