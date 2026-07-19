"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

480. Дан файл, компоненты которого являются целыми числами. Получить в файле g все компоненты файла f: 
а) являющиеся четными числами;
б) делящиеся на 3 и не делящиеся на 7;
в) являющиеся точными квадратами.
"""


import random
import math


# ------------------------------------------------------------
# 1. Процедуры работы с файлами
# ------------------------------------------------------------
def create_file_with_numbers(filename, numbers):
    """Записывает список целых чисел в файл (через пробел)."""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(' '.join(str(x) for x in numbers))


def read_numbers_from_file(filename):
    """Читает целые числа из файла и возвращает список."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            return [int(x) for x in content.split()]
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден.")
        return None
    except ValueError:
        print(f"Ошибка: файл '{filename}' содержит некорректные данные.")
        return None


# ------------------------------------------------------------
# 2. Условия фильтрации
# ------------------------------------------------------------
def is_even(x):
    return x % 2 == 0


def is_divisible_by_3_not_7(x):
    return x % 3 == 0 and x % 7 != 0


def is_perfect_square(x):
    if x < 0:
        return False
    root = math.isqrt(x)
    return root * root == x


# ------------------------------------------------------------
# 3. Ввод данных (создание файла f)
# ------------------------------------------------------------
def get_file():
    """Выбор способа задания чисел в файле f."""
    print("Задача 480: Фильтрация чисел из файла f в файлы g_a, g_b, g_c")
    print("Выберите способ задания чисел:")
    print("1 — Ручной ввод")
    print("2 — Случайная генерация")
    print("3 — Готовые примеры")

    while True:
        choice = input("Ваш выбор (1/2/3): ").strip()
        if choice in ('1', '2', '3'):
            break
        print("Ошибка: выберите 1, 2 или 3.")

    filename = "f.txt"

    if choice == '1':
        while True:
            try:
                n = int(input("Сколько чисел записать в файл? "))
                if n <= 0:
                    print("Количество должно быть положительным.")
                    continue
                print(f"Введите {n} целых чисел через пробел:")
                numbers = list(map(int, input().split()))
                if len(numbers) != n:
                    print(f"Ожидалось {n} чисел, получено {len(numbers)}.")
                    continue
                create_file_with_numbers(filename, numbers)
                print(f"Числа записаны в '{filename}'.")
                return filename
            except ValueError:
                print("Ошибка ввода. Введите целые числа.")

    elif choice == '2':
        n = random.randint(10, 25)
        # Генерируем смесь чисел, чтобы все три условия потенциально выполнялись
        numbers = [random.randint(-20, 30) for _ in range(n)]
        create_file_with_numbers(filename, numbers)
        print(f"Случайно сгенерировано {n} чисел и записано в '{filename}'.")
        return filename

    else:  # Готовые примеры
        example_numbers = [
            -4, 0, 1, 2, 3, 4, 6, 7, 9, 12, 14, 16, 21, 25, 28, 36, 49, 64, 81, 100
        ]
        create_file_with_numbers(filename, example_numbers)
        print(f"Готовый пример записан в '{filename}': {example_numbers}")
        return filename


# ------------------------------------------------------------
# 4. Основная программа
# ------------------------------------------------------------
def main():
    filename = get_file()
    numbers = read_numbers_from_file(filename)

    if not numbers:
        return

    print(f"\nЧисла из файла ({len(numbers)}): {numbers}")

    # Фильтрация
    even_nums = [x for x in numbers if is_even(x)]
    div3_not7_nums = [x for x in numbers if is_divisible_by_3_not_7(x)]
    squares_nums = [x for x in numbers if is_perfect_square(x)]

    # Запись в отдельные файлы
    create_file_with_numbers("g_a.txt", even_nums)
    create_file_with_numbers("g_b.txt", div3_not7_nums)
    create_file_with_numbers("g_c.txt", squares_nums)

    # Вывод результатов
    print("\nРезультаты:")
    print(f"а) Чётные числа           ({len(even_nums)} шт.): {even_nums}   → записаны в g_a.txt")
    print(f"б) Делятся на 3, не на 7  ({len(div3_not7_nums)} шт.): {div3_not7_nums}   → записаны в g_b.txt")
    print(f"в) Точные квадраты        ({len(squares_nums)} шт.): {squares_nums}   → записаны в g_c.txt")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
