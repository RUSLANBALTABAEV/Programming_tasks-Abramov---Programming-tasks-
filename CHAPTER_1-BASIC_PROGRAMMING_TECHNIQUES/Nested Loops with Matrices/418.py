"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
418. Пусть A1, A2, … — последовательность квадратных матриц из нулей и единиц такая, что порядок матрицы Ai равен 3i и 
1)   |-       -|
     | 1  0  1 |
A1 = | 0  1  0 |;
     | 1  0  1 |
     |-       -|
2) При i > 1 имеет место
     |-                -|
     | Ai-1  0     Ai-1 |
Ai = | 0     Ai-1     0 |,
     | Ai-1  0     Ai-1 |
     |-                -|
где 0 обозначает часть матрицы, заполненную нулями.
Дано натуральное число n. Построить изображение квадратной
области экрана, закодированное в матрице An (см. задачу 415). Левый
верхний угол области должен совпадать с левым верхним углом
экрана. Опробовать различные способы использования цвета при построении изображения. Если фоновый цвет имеет номер 0, а остальные цвета — номера 1, …, k, то при обработке элемента aij ≠ 0 можно, например, брать цвет с номером l + 1, где l равно остатку от деления i^2 + j^3 на k, и т.д.  
""" 


import random


def build_matrix(n):
    """Возвращает матрицу A_n как список списков."""
    if n == 1:
        return [
            [1, 0, 1],
            [0, 1, 0],
            [1, 0, 1]
        ]
    else:
        prev = build_matrix(n - 1)
        size = len(prev)          # 3^(n-1)
        current_size = size * 3   # 3^n

        A = [[0 for _ in range(current_size)] for _ in range(current_size)]

        # Верхний левый
        for i in range(size):
            for j in range(size):
                A[i][j] = prev[i][j]

        # Верхний правый
        for i in range(size):
            for j in range(size):
                A[i][j + 2 * size] = prev[i][j]

        # Центральный
        for i in range(size):
            for j in range(size):
                A[i + size][j + size] = prev[i][j]

        # Нижний левый
        for i in range(size):
            for j in range(size):
                A[i + 2 * size][j] = prev[i][j]

        # Нижний правый
        for i in range(size):
            for j in range(size):
                A[i + 2 * size][j + 2 * size] = prev[i][j]

        return A


def get_color_matrix(A, n, k, mode):
    """
    Создаёт матрицу цветов C того же размера, что и A.
    Цвет фона = 0. Если A[i][j] == 1, то цвет пикселя равен l+1,
    где l вычисляется по выбранному правилу (mode) и l ∈ [0, k-1].
    """
    size = 3 ** n
    C = [[0 for _ in range(size)] for _ in range(size)]

    for i in range(size):
        for j in range(size):
            if A[i][j] == 1:
                if mode == 1:
                    l = (i * i + j * j * j) % k      # i^2 + j^3
                elif mode == 2:
                    l = (i * j) % k
                elif mode == 3:
                    l = (i + j) % k
                elif mode == 4:
                    l = abs(i - j) % k
                elif mode == 5:
                    block_size = 3 ** (n - 1) if n > 0 else 1
                    l = (i // block_size + j // block_size) % k
                else:
                    l = 0
                C[i][j] = l + 1   # цвет от 1 до k
    return C


def visualize_matrix_text(A, C=None, max_size=81):
    """
    Выводит матрицу в консоль псевдографикой.
    A – матрица из 0 и 1.
    C – матрица цветов (0 – фон, 1..k – цвета); если None, то просто 0/1.
    max_size – если размер матрицы больше, выводится только левый верхний угол.
    """
    size = len(A)

    if size > max_size:
        print(f"ВНИМАНИЕ: Размер матрицы слишком велик для вывода целиком ({size}x{size})")
        print(f"Выводится верхний левый угол размером {max_size}x{max_size}\n")
        limit = max_size
    else:
        limit = size

    if C is None:
        # Чёрно-белый вывод: 1 -> '██', 0 -> '  '
        for i in range(limit):
            row_str = ''.join('██' if A[i][j] == 1 else '  ' for j in range(limit))
            print(row_str)
        return

    # Символы для отображения цветов (10 цветов)
    symbols = [' ', '.', '*', '#', '@', 'O', 'X', 'H', 'M', 'W']
    for i in range(limit):
        row_str = ''
        for j in range(limit):
            if A[i][j] == 1:
                color_code = C[i][j]
                if 0 <= color_code <= 9:
                    char = symbols[color_code]
                else:
                    char = chr(ord('a') + (color_code - 10) % 26)
                row_str += char * 2   # удваиваем для сохранения пропорций
            else:
                row_str += '  '
        print(row_str)


def get_params():
    """Выбор способа ввода: ручной, случайный или готовые примеры."""
    print("Задача 418: Построение изображения A_n (ковёр Серпинского)")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод параметров")
    print("2 — Случайный выбор параметров")
    print("3 — Готовые примеры")

    while True:
        choice = input("Ваш выбор (1/2/3): ").strip()
        if choice in ('1', '2', '3'):
            break
        print("Ошибка: выберите 1, 2 или 3.")

    if choice == '1':
        # Ручной ввод n и параметров раскраски
        while True:
            try:
                n = int(input("Введите уровень фрактала n (>=1): "))
                if n < 1:
                    print("n должно быть >= 1.")
                    continue
                break
            except ValueError:
                print("Ошибка ввода. Требуется целое число.")

        use_color = input("Использовать цветную раскраску (y/n)? ").strip().lower()
        if use_color == 'y':
            k = 2
            while True:
                try:
                    k = int(input("Введите количество цветов k (>=2): "))
                    if k < 2:
                        print("Минимум 2 цвета.")
                        continue
                    break
                except ValueError:
                    print("Ошибка ввода. Введите целое число.")

            print("\nВыберите способ раскраски:")
            print("1. (i^2 + j^3) % k")
            print("2. (i * j) % k")
            print("3. (i + j) % k")
            print("4. |i - j| % k")
            print("5. Блочная окраска")
            mode = 1
            while True:
                try:
                    mode = int(input("Ваш выбор (1-5): "))
                    if 1 <= mode <= 5:
                        break
                    print("Введите число от 1 до 5.")
                except ValueError:
                    print("Ошибка ввода. Введите целое число.")
            color_on = True
        else:
            k = 2
            mode = 1
            color_on = False
        return n, color_on, k, mode

    elif choice == '2':
        # Случайная генерация
        n = random.randint(1, 4)
        color_on = random.choice([True, False])
        k = random.randint(2, 10) if color_on else 2
        mode = random.randint(1, 5) if color_on else 1
        print(f"\nСлучайно выбраны параметры: n={n}, цвет={'да' if color_on else 'нет'}", end="")
        if color_on:
            print(f", k={k}, способ раскраски={mode}")
        else:
            print()
        return n, color_on, k, mode

    else:  # choice == '3'
        # Готовые примеры
        examples = [
            (2, True, 8, 1,  "n=2, цветная, k=8, (i^2+j^3)%k"),
            (2, False, 2, 1, "n=2, чёрно-белая"),
            (3, True, 5, 5,  "n=3, цветная, k=5, блочная окраска"),
            (3, True, 16, 2, "n=3, цветная, k=16, (i*j)%k"),
            (4, False, 2, 1, "n=4, чёрно-белая (ограниченный вывод)"),
        ]
        print("\nГотовые примеры:")
        for idx, (n_val, col, kval, m_val, desc) in enumerate(examples, 1):
            print(f"{idx}: {desc}")
        while True:
            try:
                num = int(input("Выберите номер примера: "))
                if 1 <= num <= len(examples):
                    n, color_on, k, mode, _ = examples[num - 1]
                    return n, color_on, k, mode
                else:
                    print(f"Номер должен быть от 1 до {len(examples)}.")
            except ValueError:
                print("Ошибка ввода. Введите целое число.")


def main():
    n, color_on, k, mode = get_params()

    print(f"\nГенерация матрицы A_{n} размером {3**n}x{3**n}...")
    A = build_matrix(n)
    print("Матрица сгенерирована.\n")

    if color_on:
        print("Вычисление цветовой матрицы...")
        C = get_color_matrix(A, n, k, mode)
        print("Визуализация:")
        visualize_matrix_text(A, C)
    else:
        print("Визуализация:")
        visualize_matrix_text(A, None)


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
