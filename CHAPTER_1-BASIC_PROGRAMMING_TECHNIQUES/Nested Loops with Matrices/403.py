"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
11. Вложенные циклы в матричных задачах

403. Дана целочисленная квадратная матрица порядка 15. Выяснить, имеются ли в матрице ненулевые элементы, и если имеются, то указать индексы:
а) одного из ненулевых элементов;
б) всех ненулевых элементов.
"""


import random

def get_matrix(n = 15):
    """Получение матрицы выбранным способом."""
    print(f"Задача 403: Поиск ненулевых элементов (матрица {n}×{n})")
    print("1 — Ручной ввод")
    print("2 — Случайные числа")
    print("3 — Готовый пример")
    choice = input("Ваш выбор (1/2/3): ").strip()
    while choice not in ('1','2','3'):
        choice = input("Выберите 1, 2 или 3: ").strip()

    if choice == '1':
        print(f"Введите матрицу {n}x{n} построчно (целые числа через пробел):")
        matrix = []
        for i in range(n):
            row = list(map(int, input(f"Строка {i+1}: ").strip()))
            if len(row) != n:
                raise ValueError(f"Ошибка: в строке должен быть {n} чисел.")
            matrix.append(row)
        return matrix
    
    elif choice == '2':
        matrix = [[random.randint(-5, 5) for _ in range(n)] for _ in range(n)]
        print("Сгенерирована матрица (первые 5 строк для просмотра):")
        for row in matrix[:5]:
            print(" ".join(f"{x:3d}" for x in row))
        if n > 5: print("...")
        return matrix
    
    else:
        # Готовый пример: смешанные значения с гарантированными нулями и ненулевыми
        matrix = [[(i + j) % 3 if (i + j) % 4 != 0 else 0 for j in range(n)] for i in range(n)]
        print("Примеры матрицы (первые 5 строк):")
        for row in matrix[:5]:
            print(" ".join(f"{x:3d}" for x in row))
        if n > 5: print("...")
        return matrix
    

def find_nonzero(matrix):
    """Возвращает список всех ненулевых элементов с их индексами (1-based)."""
    nonzero = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != 0:
                nonzero.append((i + 1, j + 1, matrix[i][j]))
    return nonzero


def main():
    n = 15
    matrix = get_matrix(n)
    nonzero_list = find_nonzero(matrix)

    print("\n" + "=" * 60)
    print("РЕЗУЛЬТАТ")
    print("=" * 60)

    if not nonzero_list:
        print("Ненулевых элементов в матрице нет.")
    else:
        # а) Первый найденный ненулевой элемент
        i1, j1, val1 = nonzero_list[0]
        print("а) Один из ненулевых элементов:")
        print(f"  Индексы (строка, столбец): ({i1}, {j1}), значение = {val1}")

        # б) Все ненулевые
        print(f"\nб) Все ненулевые элементы (всего {len(nonzero_list)}):")
        # Сгруппируем по строкам для читаемости
        current_row = 0
        for i, j, val in nonzero_list:
            if i != current_row:
                if current_row != 0:
                    print()
                current_row = i
                print(f"  Строка {i:2d}: ", end=" ")
            print(f"({j}:{val:3d})", end=" ")
        print()

    print("=" * 60)

if __name__ == "__main__":
    main()
    input("\nНажмите Enter для выхода...")
