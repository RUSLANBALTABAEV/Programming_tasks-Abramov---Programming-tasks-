"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
11. Вложенные циклы в матричных задачах

391. Даны натуральное число n, целочисленная матрица [aij]i=1,2;j=1,...,m. Найти сумму тех из элементов a2j * (j=1,..,m), для которых a1j имеет значение наибольшего среди значений a11, a12, .., a1m.
"""


import random

def get_matrix():
    """Выбор способа ввода целочисленной матрицы 2×m."""
    print("=== Задача 391: Сумма элементов второй строки по условию ===")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод")
    print("2 — Случайная генерация")
    print("3 — Готовые примеры")

    while True:
        choice = input("Ваш выбор (1/2/3): ").strip()
        if choice in ('1', '2', '3'):
            break
        print("Ошибка: выберите 1, 2 или 3.")

    if choice == '1':
        while True:
            try:
                m = int(input("Введите количество столбцов m (>0): "))
                if m <= 0:
                    print("Количество столбцов должно быть положительным.")
                    continue
                print("Введите элементы первой строки (целые числа через пробел):")
                row1 = list(map(int, input().split()))
                if len(row1) != m:
                    print(f"Ошибка: ожидалось {m} чисел.")
                    continue
                print("Введите элементы второй строки (целые числа через пробел):")
                row2 = list(map(int, input().split()))
                if len(row2) != m:
                    print(f"Ошибка: ожидалось {m} чисел.")
                    continue
                return m, [row1, row2]
            except ValueError:
                print("Ошибка ввода. Ожидаются целые числа.")

    elif choice == '2':
        m = random.randint(3, 8)
        row1 = [random.randint(-10, 10) for _ in range(m)]
        row2 = [random.randint(-10, 10) for _ in range(m)]
        print(f"\nСгенерирована матрица 2×{m}:")
        print(" ".join(f"{x:4d}" for x in row1))
        print(" ".join(f"{x:4d}" for x in row2))
        return m, [row1, row2]

    else:
        examples = [
            (5, [[3, 7, 2, 9, 5], [1, 2, 3, 4, 5]]),
            (4, [[-2, 5, 5, -1], [10, 20, 30, 40]]),
            (6, [[0, -3, 0, 7, 7, 2], [5, 5, 5, 5, 5, 5]]),
            (3, [[1, 2, 3], [100, 200, 300]]),
            (7, [[-5, -5, -5, -5, -5, -5, -5], [1, 2, 3, 4, 5, 6, 7]])
        ]
        print("\nГотовые примеры:")
        for idx, (m_val, mat) in enumerate(examples, 1):
            print(f"{idx}: 2×{m_val}")
            print("   Строка 1:", " ".join(f"{x:4d}" for x in mat[0]))
            print("   Строка 2:", " ".join(f"{x:4d}" for x in mat[1]))
        while True:
            try:
                num = int(input("Выберите номер примера: "))
                if 1 <= num <= len(examples):
                    m, matrix = examples[num-1]
                    return m, matrix
                else:
                    print(f"Номер должен быть от 1 до {len(examples)}.")
            except ValueError:
                print("Ошибка ввода. Введите целое число.")

def main():
    data = get_matrix()
    if data is None:
        return
    m, matrix = data
    row1, row2 = matrix[0], matrix[1]

    # Находим максимальное значение в первой строке
    max_val = max(row1)

    # Суммируем элементы второй строки, для которых элемент первой строки равен max_val
    total = 0
    indices = []
    for j in range(m):
        if row1[j] == max_val:
            total += row2[j]
            indices.append(j)

    print("\n" + "="*60)
    print("РЕЗУЛЬТАТЫ")
    print("="*60)
    print(f"Матрица 2×{m}:")
    print("Строка 1:", " ".join(f"{x:4d}" for x in row1))
    print("Строка 2:", " ".join(f"{x:4d}" for x in row2))
    print(f"Максимальный элемент первой строки: {max_val}")
    if indices:
        print(f"Позиции (столбцы) с максимальным элементом: {[j+1 for j in indices]}")
        print(f"Соответствующие элементы второй строки: {[row2[j] for j in indices]}")
        print(f"Их сумма: {total}")
    else:
        print("Максимальный элемент не найден (невозможная ситуация).")
    print("="*60)

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
