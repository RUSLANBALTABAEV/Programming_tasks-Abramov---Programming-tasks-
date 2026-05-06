"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
11. Вложенные циклы в матричных задачах

404. Даны натуральные числа i, j, действительная матрица размера 18x24 (1 <= i < j <= 24). Поменять в матрице местами i-й и j-й столбцы.
"""


import random

ROWS = 18
COLS = 24

def get_matrix():
    """Выбор способа ввода матрицы 18×24."""
    print(f"Задача 404: Обмен местами i-го и j-го столбцов (матрица {ROWS}×{COLS})")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод (432 числа, будьте внимательны)")
    print("2 — Случайные числа")
    print("3 — Готовый пример (элементы вида <номер строки > *100 + <номер столбца>)")

    while True:
        choice = input("Ваш выбор (1/2/3): ").strip()
        if choice in ('1', '2', '3'):
            break
        print("Ошибка: выберите 1, 2 или 3.")

    if choice == '1':
        while True:
            try:
                print(f"Введите матрицу {ROWS}x{COLS} построчно (действительные числа через пробел):")
                matrix = []
                for k in range(ROWS):
                    row = list(map(float, input(f"Строка {k + 1}: ").split()))
                    if len(row) != COLS:
                        print(f"Ошибка: в строке должен быть {COLS} чисел. Повторите ввод всей матрицы.")
                        break
                    matrix.append(row)
                else:
                    return matrix
            except ValueError:
                print("Ошибка ввода. Ожидает число.")

    elif choice == '2':
        matrix = [[round(random.uniform(-10, 10), 2) for _ in range(COLS)] for _ in range(ROWS)]
        print("\nСгенерирована матрица (первые 5 строк):")
        for row in matrix[:5]:
            print(" ".join(f"{x:7.2f}" for x in row))
        if ROWS > 5:
            print("...")
        return matrix
    
    else:
         # Готовый пример: элементы матрицы вычисляются как (i+1)*100 + (j+1)
        matrix = [[ (i + 1) * 100 + (j + 1) for j in range(COLS)] for i in range(ROWS)]
        print("\nГотовый пример (первые 5 строк):")
        for row in matrix[:5]:
            print(" ".join(f"{x:6d}" for x in row))
        print("...")
        return matrix


def swap_columns(matrix, i, j):
    """Меняет местами i-й и j-й столбцы (индексы с 1)."""
    for row in matrix:
        row[i-1], row[j-1] = row[j-1], row[i-1]


def main():
    matrix = get_matrix()

    # Ввод индексов столбцов
    while True:
        try:
            i = int(input(f"\nВведите номер первого столбца i (1..{COLS - 1}): "))
            j = int(input(f"Введите номер второго столбца j (i+1..{COLS}): "))
            if 1 <= i <= COLS:
                break
            else:
                print(f"Ошибка: должен быть 1 <= i < j <= {COLS}.")
        except ValueError:
            print("Ошибка ввода. Введите целые числа.")

    # Сохраняем копию для вывода (только первые строки)
    def show_partial(mat, rows = 5):
        for r in mat[:rows]:
            print(" ".join(f"{x:8.2f}" if isinstance(x, float) else f"{x:8d}" for x in r))
            if len(mat) > rows:
                print("...")

    print("\nИсходная матрица (первые 5 строк):")
    show_partial(matrix)

    swap_columns(matrix, i, j)

    print(f"\nМатрица после замены столбцов {i} и {j} (первые 5 строк):")
    show_partial(matrix)

    print("\nОбмен выполнен успешно.")

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
