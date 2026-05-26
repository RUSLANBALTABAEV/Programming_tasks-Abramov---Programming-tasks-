"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
11. Вложенные циклы в матричных задачах

419. Дана символьная квадратная матрица порядка 10. Заменить буквой a все ее элементы, расположенные выше главной диагонали.
""" 


import random


def get_matrix():
    """Выбор способа ввода символьной матрицы 10×10."""
    N = 10
    print("Задача 419: Замена элементов выше главной диагонали на 'a'")
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
            print(f"Введите {N} строк по {N} символов (без пробелов):")
            matrix = []
            for i in range(N):
                row_str = input(f"Строка {i+1}: ").strip()
                if len(row_str) != N:
                    print(f"Ошибка: в строке должно быть ровно {N} символов.")
                    break
                # Преобразуем строку в список символов
                matrix.append(list(row_str))
            else:
                return matrix
            print("Попробуйте ввести матрицу заново.")

    elif choice == '2':
        # Случайные заглавные латинские буквы
        matrix = [[chr(random.randint(65, 90)) for _ in range(N)] for _ in range(N)]
        print("\nСгенерирована матрица 10×10:")
        for row in matrix:
            print(" ".join(row))
        return matrix

    else:
        # Готовые примеры
        examples = [
            [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
             ['K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T'],
             ['U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D'],
             ['E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N'],
             ['O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X'],
             ['Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
             ['I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R'],
             ['S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B'],
             ['C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'],
             ['M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V']],

            [['x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7'],
             ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],
             ['k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'],
             ['u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3'],
             ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
             ['K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T'],
             ['U', 'V', 'W', 'X', 'Y', 'Z', '!', '@', '#', '$'],
             ['%', '^', '&', '*', '(', ')', '-', '+', '=', '~'],
             ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
             ['0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']]
        ]
        print("\nГотовые примеры:")
        for idx, mat in enumerate(examples, 1):
            print(f"{idx}:")
            for row in mat:
                print(" ".join(row))
            print()
        while True:
            try:
                num = int(input("Выберите номер примера: "))
                if 1 <= num <= len(examples):
                    return examples[num-1]
                else:
                    print(f"Номер должен быть от 1 до {len(examples)}.")
            except ValueError:
                print("Ошибка ввода. Введите целое число.")


def main():
    N = 10
    matrix = get_matrix()

    # Вывод исходной матрицы
    print("\nИсходная матрица:")
    for row in matrix:
        print(" ".join(row))

    # Замена элементов выше главной диагонали на 'a'
    for i in range(N):
        for j in range(N):
            if i < j:          # выше главной диагонали
                matrix[i][j] = 'a'

    # Вывод преобразованной матрицы
    print("\nМатрица после замены (выше главной диагонали – 'a'):")
    for row in matrix:
        print(" ".join(row))


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
