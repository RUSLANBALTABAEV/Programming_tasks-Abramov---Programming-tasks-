"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
11. Вложенные циклы в матричных задачах

416. Даны две целочисленные квадратные матрицы порядка n. В каждой из матриц закодировано изображение прямоугольной области экрана размером n×n точек с координатами левого верхнего угла 0, 0 (см. предыдущую задачу). В отличие от предыдущей задачи, все элементы обеих матриц — это числа, равные нулю, если точка — часть изображения. Получить на экране изображение, являющееся: 
а) пересечением изображений, закодированных в первой и второй матрицах;
б) объединением изображений, закодированных в первой и второй матрицах.
""" 


import random


def get_matrices():
    """Получение двух квадратных матриц порядка n."""
    print("Задача 416: Пересечение и объединение изображений")
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
                n = int(input("Введите порядок матриц n (> 0): "))
                if n <= 0:
                    print("Порядок должен быть положительным.")
                    continue
                print("Первая матрица (0 — точка изображения, любое другое число — фон):")
                mat1 = []
                for i in range(n):
                    row = list(map(int, input(f"Строка {i+1}: ").split()))
                    if len(row) != n:
                        print(f"Ошибка: в строке должно быть {n} чисел.")
                        break
                    mat1.append(row)
                else:
                    print("Вторая матрица:")
                    mat2 = []
                    for i in range(n):
                        row = list(map(int, input(f"Строка {i+1}: ").split()))
                        if len(row) != n:
                            print(f"Ошибка: в строке должно быть {n} чисел.")
                            break
                        mat2.append(row)
                    else:
                        return n, mat1, mat2
                print("Попробуйте ввести матрицы заново.")
            except ValueError:
                print("Ошибка ввода. Ожидаются целые числа.")

    elif choice == '2':
        n = random.randint(5, 12)
        # Создаём два «изображения»: случайно ставим 0 (точка объекта) с вероятностью ~30%
        mat1 = [[0 if random.random() < 0.3 else random.randint(1, 5) for _ in range(n)] for _ in range(n)]
        mat2 = [[0 if random.random() < 0.3 else random.randint(1, 5) for _ in range(n)] for _ in range(n)]
        print(f"\nСгенерированы две матрицы порядка {n}.")
        print("Первая матрица (первые 5 строк):")
        for row in mat1[:5]:
            print(" ".join(f"{x:2d}" for x in row))
        if n > 5: print("...")
        print("Вторая матрица (первые 5 строк):")
        for row in mat2[:5]:
            print(" ".join(f"{x:2d}" for x in row))
        if n > 5: print("...")
        return n, mat1, mat2

    else:
        # Готовые примеры: квадраты, пересекающиеся и смещённые
        examples = [
            (5,
             [ # матрица 1: квадрат 2x2 в левом верхнем углу
                [0, 0, 1, 1, 1],
                [0, 0, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1]
             ],
             [ # матрица 2: квадрат 2x2 в центре
                [1, 1, 1, 1, 1],
                [1, 1, 0, 0, 1],
                [1, 1, 0, 0, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1]
             ]),
            (6,
             [ # матрица 1: горизонтальная полоса сверху
                [0, 0, 0, 0, 1, 1],
                [0, 0, 0, 0, 1, 1],
                [0, 0, 0, 0, 1, 1],
                [1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1]
             ],
             [ # матрица 2: вертикальная полоса слева
                [0, 0, 0, 1, 1, 1],
                [0, 0, 0, 1, 1, 1],
                [0, 0, 0, 1, 1, 1],
                [0, 0, 0, 1, 1, 1],
                [1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1]
             ])
        ]
        print("\nГотовые примеры:")
        for idx, (n_val, m1, m2) in enumerate(examples, 1):
            print(f"{idx}: порядок {n_val}")
            print("   Первая матрица:")
            for row in m1:
                print("   ", " ".join(f"{x:2d}" for x in row))
            print("   Вторая матрица:")
            for row in m2:
                print("   ", " ".join(f"{x:2d}" for x in row))
        while True:
            try:
                num = int(input("Выберите номер примера: "))
                if 1 <= num <= len(examples):
                    n, m1, m2 = examples[num-1]
                    return n, m1, m2
                else:
                    print(f"Номер должен быть от 1 до {len(examples)}.")
            except ValueError:
                print("Ошибка ввода. Введите целое число.")


def compute_intersection(n, mat1, mat2):
    """Возвращает матрицу пересечения: точка = 0, если в обоих матрицах 0."""
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if mat1[i][j] == 0 and mat2[i][j] == 0:
                res[i][j] = 0
            else:
                res[i][j] = 1   # не ноль, чтобы не путать с точкой изображения
    return res


def compute_union(n, mat1, mat2):
    """Возвращает матрицу объединения: точка = 0, если хотя бы в одной матрице 0."""
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if mat1[i][j] == 0 or mat2[i][j] == 0:
                res[i][j] = 0
            else:
                res[i][j] = 1
    return res


def render_text_image(matrix, title):
    """Выводит в консоль изображение, используя символы: 0 -> '##', не 0 -> '  '."""
    print(f"\n{title}")
    for row in matrix:
        line = ""
        for val in row:
            if val == 0:
                line += "##"   # точка изображения
            else:
                line += "  "   # фон
        print(line)
    print()


def main():
    n, mat1, mat2 = get_matrices()

    intersection = compute_intersection(n, mat1, mat2)
    union = compute_union(n, mat1, mat2)

    print("\n" + "=" * 40)
    print("РЕЗУЛЬТАТЫ")
    print("=" * 40)

    render_text_image(mat1, "Первое изображение (0 — объект):")
    render_text_image(mat2, "Второе изображение (0 — объект):")
    render_text_image(intersection, "а) Пересечение (объект там, где оба 0):")
    render_text_image(union, "б) Объединение (объект там, где хотя бы один 0):")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
