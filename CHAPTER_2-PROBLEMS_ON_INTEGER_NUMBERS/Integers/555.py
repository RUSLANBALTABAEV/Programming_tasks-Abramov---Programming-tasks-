"""
ГЛАВА 2
ЗАДАЧИ ПО ТЕМАМ
15. Целые числа.

555. Треугольником Паскаля называется числовой треугольник 
                         1
                        1 1
                       1 2 1
                      1 3 3 1
                     1 4 6 4 1
                    ...........
в котором по краям стоят единицы, а каждое число внутри равно сумме двух стоящих над ним в ближайшей строке сверху.
Дано натуральное n. Получить первые n строк треугольника Паскаля.
"""


import random


def get_n():
    """Выбор способа ввода натурального числа n."""
    print("Задача 555: Треугольник Паскаля")
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
                n = int(input("Введите натуральное число n (>=1): "))
                if n < 1:
                    print("n должно быть >= 1.")
                    continue
                return n
            except ValueError:
                print("Ошибка ввода. Повторите.")

    elif choice == '2':
        # Случайное n от 1 до 12, чтобы треугольник не был слишком большим
        n = random.randint(1, 12)
        print(f"\nСгенерировано n = {n}")
        return n

    else:  # готовые примеры
        examples = [1, 5, 7, 10]
        print("\nГотовые примеры n:")
        for idx, val in enumerate(examples, 1):
            print(f"{idx}: n = {val}")
        while True:
            try:
                num = int(input("Выберите номер примера: "))
                if 1 <= num <= len(examples):
                    return examples[num - 1]
                else:
                    print(f"Номер должен быть от 1 до {len(examples)}.")
            except ValueError:
                print("Ошибка ввода. Введите целое число.")


def generate_pascals_triangle(n):
    """
    Генерирует первые n строк треугольника Паскаля.
    Возвращает список строк, где каждая строка – список целых чисел.
    """
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle


def print_triangle(triangle):
    """
    Выводит треугольник Паскаля с центрированием.
    """
    if not triangle:
        return
    # Определяем ширину самого длинного элемента (последнее число последней строки)
    max_num_width = len(str(triangle[-1][len(triangle[-1])//2])) if triangle[-1] else 1
    # Ширина последней строки (сумма ширин чисел и пробелов)
    last_row_str = ' '.join(str(x).rjust(max_num_width) for x in triangle[-1])
    max_width = len(last_row_str)

    for i, row in enumerate(triangle):
        row_str = ' '.join(str(x).rjust(max_num_width) for x in row)
        print(f"Строка {i+1:2d}: {row_str.center(max_width)}")


def main():
    n = get_n()
    print(f"\nИсходные данные: n = {n}")
    print("Первые строки треугольника Паскаля:")
    print("-" * 50)

    triangle = generate_pascals_triangle(n)
    print_triangle(triangle)

    print("-" * 50)
    print("По краям стоят единицы; внутри – сумма двух чисел сверху.")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")