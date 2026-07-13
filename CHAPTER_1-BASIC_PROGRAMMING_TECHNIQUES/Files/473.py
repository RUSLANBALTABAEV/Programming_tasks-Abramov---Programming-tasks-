"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

473. Дан файл f, компоненты которого являются целыми числами. Найти:
а) количество четных чисел среди компонент;
б) количество удвоенных нечетных чисел среди компонент;
в) количество квадратов нечетных чисел среди компонент. 
"""


import random
import math


def create_file_with_numbers(filename, numbers):
    """Записывает последовательность целых чисел в файл (через пробел)."""
    with open(filename, 'w') as f:
        f.write(' '.join(str(x) for x in numbers))


def read_numbers_from_file(filename):
    """Читает целые числа из файла, разделённые пробельными символами."""
    try:
        with open(filename, 'r') as f:
            content = f.read()
            return [int(x) for x in content.split()]
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден.")
        return None
    except ValueError:
        print("Ошибка: файл содержит некорректные данные (не целые числа).")
        return None


def get_file():
    """Выбор способа ввода данных и создание/использование файла f.txt."""
    filename = "f.txt"
    print("Задача 473: Анализ целочисленных компонент файла")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод чисел")
    print("2 — Случайная генерация файла")
    print("3 — Готовый пример")

    while True:
        choice = input("Ваш выбор (1/2/3): ").strip()
        if choice in ('1', '2', '3'):
            break
        print("Ошибка: выберите 1, 2 или 3.")

    if choice == '1':
        while True:
            try:
                n = int(input("Сколько целых чисел записать в файл? "))
                if n <= 0:
                    print("Количество должно быть положительным.")
                    continue
                print(f"Введите {n} целых чисел через пробел:")
                data = list(map(int, input().split()))
                if len(data) != n:
                    print(f"Ожидалось {n} чисел, получено {len(data)}.")
                    continue
                create_file_with_numbers(filename, data)
                print(f"Числа записаны в файл '{filename}'.")
                return filename
            except ValueError:
                print("Ошибка ввода. Повторите.")

    elif choice == '2':
        n = random.randint(10, 20)
        # Генерируем целые числа от -30 до 30, чтобы было разнообразие
        numbers = [random.randint(-30, 30) for _ in range(n)]
        create_file_with_numbers(filename, numbers)
        print(f"Случайно сгенерировано {n} чисел и записано в '{filename}'.")
        return filename

    else:
        # Готовый пример: набор чисел, содержащий все нужные категории
        example_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 25, 49, -3, -6, -9]
        create_file_with_numbers(filename, example_numbers)
        print(f"Готовый пример записан в '{filename}': {example_numbers}")
        return filename


def main():
    filename = get_file()
    data = read_numbers_from_file(filename)

    if not data:
        return

    print(f"\nКомпоненты файла ({len(data)}): {data}\n")

    # а) Количество чётных чисел
    count_even = sum(1 for num in data if num % 2 == 0)

    # б) Количество удвоенных нечётных чисел (числа, которые делятся на 2, но не на 4)
    # Такие числа дают остаток 2 при делении на 4 (например, 2, 6, 10, -2, -6 ...)
    count_doubled_odd = sum(1 for num in data if num % 4 == 2)

    # в) Количество квадратов нечётных чисел (числа, являющиеся полными квадратами, чей корень нечётен)
    count_squares_odd = 0
    for num in data:
        if num >= 0:   # квадраты неотрицательны
            root = math.isqrt(num)
            if root * root == num and root % 2 == 1:
                count_squares_odd += 1

    print("Результаты:")
    print(f"а) Количество чётных чисел:                 {count_even}")
    print(f"б) Количество удвоенных нечётных чисел:     {count_doubled_odd}")
    print(f"в) Количество квадратов нечётных чисел:     {count_squares_odd}")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
