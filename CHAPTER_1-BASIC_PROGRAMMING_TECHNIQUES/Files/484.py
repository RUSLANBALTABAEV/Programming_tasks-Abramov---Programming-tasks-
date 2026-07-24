"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

484. Дан файл f , компоненты которого являются целыми числами. Записать в файл g все четные числа файла f , а в файл h – все нечетные. Порядок следования чисел сохраняется. 
"""


import random
import os


# ------------------------------------------------------------
# 1. Процедуры работы с файлами
# ------------------------------------------------------------
def read_numbers_from_file(filename):
    """Читает целые числа из файла (разделённые пробелами) и возвращает список."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            if not content:
                return []
            return [int(x) for x in content.split()]
    except FileNotFoundError:
        return None
    except ValueError:
        print(f"Ошибка: файл '{filename}' содержит некорректные данные.")
        return None


def write_numbers_to_file(filename, numbers):
    """Записывает список целых чисел в файл (каждое число на новой строке)."""
    with open(filename, 'w', encoding='utf-8') as f:
        for num in numbers:
            f.write(f"{num}\n")


# ------------------------------------------------------------
# 2. Создание исходного файла f (если он отсутствует или требуется пересоздать)
# ------------------------------------------------------------
def create_file_f(filename):
    """Создаёт файл f с целыми числами одним из трёх способов."""
    print("Файл f не существует или пуст. Задайте его содержимое.")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод чисел")
    print("2 — Случайная генерация")
    print("3 — Готовый пример")

    while True:
        choice = input("Ваш выбор (1/2/3): ").strip()
        if choice in ('1', '2', '3'):
            break
        print("Ошибка: выберите 1, 2 или 3.")

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
                break
            except ValueError:
                print("Ошибка ввода. Введите целые числа.")
    elif choice == '2':
        n = random.randint(8, 15)
        numbers = [random.randint(-20, 20) for _ in range(n)]
        print(f"Сгенерировано {n} случайных чисел.")
    else:  # готовый пример
        numbers = [4, -7, 0, 13, 2, -5, 8, 11, -3, 6]
        print("Готовый пример: ", numbers)

    write_numbers_to_file(filename, numbers)
    print(f"Числа записаны в '{filename}'.")


# ------------------------------------------------------------
# 3. Основная программа
# ------------------------------------------------------------
def main():
    print("Задача 484: Разделение чётных и нечётных чисел по файлам")
    src = "f.txt"
    dst_even = "g.txt"
    dst_odd = "h.txt"

    # Проверка существования и наполнения файла f
    numbers = read_numbers_from_file(src)
    if numbers is None or len(numbers) == 0:
        create_file_f(src)
        numbers = read_numbers_from_file(src)

    print(f"\nИсходные числа из файла '{src}': {numbers}")

    # Разделяем с сохранением порядка
    even_numbers = [x for x in numbers if x % 2 == 0]
    odd_numbers = [x for x in numbers if x % 2 != 0]

    # Записываем в файлы g и h
    write_numbers_to_file(dst_even, even_numbers)
    write_numbers_to_file(dst_odd, odd_numbers)

    print(f"\nРезультаты:")
    print(f"Чётные числа ({len(even_numbers)}): {even_numbers} → '{dst_even}'")
    print(f"Нечётные числа ({len(odd_numbers)}): {odd_numbers} → '{dst_odd}'")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
