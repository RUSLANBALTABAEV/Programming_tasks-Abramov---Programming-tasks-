"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
11. Вложенные циклы в матричных задачах

382. Дана действительная матрица размера 6*9. Найти среднее арифметическое наибольшего и наименьшего значений ее элементов.
"""


import random

def get_matrix():
    """Выбор способа ввода матрицы 6x9."""
    print("=== Задача 382: Среднее арифметическое min и max элементов матрицы 6x9 ===")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод")
    print("2 — Случайная генерация")
    print("3 — Готовые примеры")

    choice = input("Ваш выбор (1/2/3): ").strip()
    while choice not in ('1', '2', '3'):
        choice = input("Выберите 1, 2 или 3: ").strip()

    n_rows, n_cols = 6, 9

    if choice == '1':
        try:
            print(f"Введите матрицу {n_rows}x{n_cols} построчно (действительные числа):")
            matrix = []
            for i in range(n_rows):
                row = list(map(float, input(f"Строка {i+1}: ").split()))
                if len(row) != n_cols:
                    print(f"Ошибка: в строке должно быть {n_cols} чисел, получено {len(row)}.")
                    return None
                matrix.append(row)
            return matrix
        except ValueError:
            print("Ошибка ввода. Введите действительные числа.")
            return None

    elif choice == '2':
        matrix = [[random.uniform(-100, 100) for _ in range(n_cols)] for _ in range(n_rows)]
        print("\nСгенерирована матрица 6x9:")
        for row in matrix:
            print(" ".join(f"{x:8.4f}" for x in row))
        return matrix

    else:
        examples = [
            [[1,2,3,4,5,6,7,8,9]]*6,  # 6 одинаковых строк
            [[i*j for j in range(1,10)] for i in range(1,7)],
            [[0]*9 for _ in range(6)],  # все нули
            [[random.uniform(-10,10) for _ in range(9)] for _ in range(6)],  # случайный, но фиксированный
            [[1, -1, 2, -2, 3, -3, 4, -4, 5]]*6
        ]
        # Для определённости зафиксируем последний пример как конкретный
        examples[3] = [[1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5],
                       [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5],
                       [10, 20, 30, 40, 50, 60, 70, 80, 90],
                       [11, 12, 13, 14, 15, 16, 17, 18, 19],
                       [21, 22, 23, 24, 25, 26, 27, 28, 29],
                       [31, 32, 33, 34, 35, 36, 37, 38, 39]]
        print("\nГотовые примеры:")
        for idx, ex in enumerate(examples, 1):
            print(f"{idx}: Первая строка: {ex[0][:4]}...")
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

    # Находим минимум и максимум
    all_elements = [val for row in matrix for val in row]
    min_val = min(all_elements)
    max_val = max(all_elements)
    avg = (min_val + max_val) / 2

    print("\n" + "="*60)
    print("РЕЗУЛЬТАТ")
    print("="*60)
    print(f"Минимальный элемент: {min_val:.6f}")
    print(f"Максимальный элемент: {max_val:.6f}")
    print(f"Среднее арифметическое min и max: {avg:.6f}")
    print("="*60)

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
