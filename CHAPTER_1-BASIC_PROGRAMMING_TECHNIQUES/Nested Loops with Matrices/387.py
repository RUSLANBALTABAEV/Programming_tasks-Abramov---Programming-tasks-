"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
11. Вложенные циклы в матричных задачах

387. Даны натуральное число n, действительная квадратная матрица порядка n, действительные a1,...,an+5. Элементы последовательности a1,...,an+5 домножить на 10, если наибольший элемент матрицы (в предположении, что такой элемент единственный) находится на главной диагонали, и на 0.5 в противном случае.
"""


import random

def get_input():
    """Выбор способа ввода n, матрицы и последовательности a."""
    print("=== Задача 387: Изменение последовательности в зависимости от положения максимума матрицы ===")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод")
    print("2 — Случайная генерация")
    print("3 — Готовые примеры")

    choice = input("Ваш выбор (1/2/3): ").strip()
    while choice not in ('1', '2', '3'):
        choice = input("Выберите 1, 2 или 3: ").strip()

    if choice == '1':
        try:
            n = int(input("Введите порядок матрицы n (натуральное): "))
            if n <= 0:
                print("n должно быть положительным.")
                return None
            print(f"Введите матрицу {n}x{n} построчно (действительные числа):")
            matrix = []
            for i in range(n):
                row = list(map(float, input(f"Строка {i+1}: ").split()))
                if len(row) != n:
                    print(f"Ошибка: в строке должно быть {n} чисел.")
                    return None
                matrix.append(row)

            print(f"Введите {n+5} действительных чисел a1...a{n+5} через пробел:")
            a_line = input().strip()
            a = list(map(float, a_line.split()))
            if len(a) != n+5:
                print(f"Ошибка: ожидалось {n+5} чисел, получено {len(a)}.")
                return None
            return n, matrix, a
        except ValueError:
            print("Ошибка ввода.")
            return None

    elif choice == '2':
        n = random.randint(2, 6)
        matrix = [[random.uniform(-10, 10) for _ in range(n)] for _ in range(n)]
        a = [random.uniform(-5, 5) for _ in range(n+5)]
        print(f"\nСгенерировано: n = {n}")
        print("Матрица:")
        for row in matrix:
            print(" ".join(f"{x:8.4f}" for x in row))
        print("Последовательность a:", [round(x, 4) for x in a])
        return n, matrix, a

    else:
        examples = [
            (3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1,2,3,4,5,6,7,8]),  # n=3, n+5=8, максимум 9 на диагонали? 9 на (3,3) да
            (2, [[-1, 0], [0, 2]], [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5]),  # n=2, n+5=7, максимум 2 на диагонали (2,2)
            (3, [[10, 1, 2], [3, 4, 5], [6, 7, 8]], [1,1,1,1,1,1,1,1]),  # максимум 10 на (1,1) диагональ
            (2, [[1, 10], [2, 3]], [10,20,30,40,50,60,70]),  # максимум 10 вне диагонали (1,2)
            (3, [[0,0,0],[0,0,0],[0,0,5]], [0]*8)  # максимум 5 на диагонали (3,3)
        ]
        print("\nГотовые примеры:")
        for idx, (n_val, mat, a_val) in enumerate(examples, 1):
            print(f"{idx}: n={n_val}, первая строка матрицы: {mat[0][:3]}, первые элементы a: {a_val[:3]}...")
        try:
            num = int(input("Выберите номер примера: "))
            if 1 <= num <= len(examples):
                n, matrix, a = examples[num-1]
                return n, matrix, a
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
    n, matrix, a = data

    # Поиск максимального элемента матрицы
    max_val = float('-inf')
    max_pos = (-1, -1)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] > max_val:
                max_val = matrix[i][j]
                max_pos = (i, j)

    # Проверка на уникальность (предупреждение)
    count_max = sum(1 for i in range(n) for j in range(n) if matrix[i][j] == max_val)
    if count_max > 1:
        print(f"\nВнимание: найдено {count_max} элементов со значением {max_val}. Используется первый (строка {max_pos[0]+1}, столбец {max_pos[1]+1}).")

    # Определяем коэффициент
    if max_pos[0] == max_pos[1]:
        factor = 10.0
        reason = "на главной диагонали"
    else:
        factor = 0.5
        reason = "не на главной диагонали"

    # Преобразуем последовательность
    a_new = [x * factor for x in a]

    print("\n" + "="*60)
    print("РЕЗУЛЬТАТ")
    print("="*60)
    print(f"Максимальный элемент матрицы: {max_val:.6f}")
    print(f"Позиция: строка {max_pos[0]+1}, столбец {max_pos[1]+1} ({reason})")
    print(f"Коэффициент умножения: {factor}")
    print("\nИсходная последовательность a:")
    print(" ".join(f"{x:.6f}" for x in a))
    print("\nПреобразованная последовательность:")
    print(" ".join(f"{x:.6f}" for x in a_new))
    print("="*60)

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
