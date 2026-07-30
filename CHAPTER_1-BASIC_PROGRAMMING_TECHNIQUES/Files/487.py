"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

487. Дан файл f , компоненты которого являются целыми числами. Получить файл g , образованный из файла f исключением повторных вхождений одного и того же числа.
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
    """Записывает список целых чисел в файл (через пробел)."""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(' '.join(str(x) for x in numbers))


# ------------------------------------------------------------
# 2. Создание исходного файла f (если он отсутствует или пуст)
# ------------------------------------------------------------
def create_file_f(filename):
    """Создаёт файл f с целыми числами (возможно, повторяющимися)."""
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
        # Генерируем числа с повторениями: выбираем из небольшого пула
        pool = [random.randint(-10, 10) for _ in range(random.randint(3, 6))]
        numbers = [random.choice(pool) for _ in range(n)]
        print(f"Сгенерирована последовательность из {n} чисел (с возможными повторениями).")
    else:  # готовый пример
        numbers = [1, 2, 2, 3, 4, 4, 4, 5, 1, 3, 2]
        print("Готовый пример: ", numbers)

    write_numbers_to_file(filename, numbers)
    print(f"Числа записаны в '{filename}'.")


# ------------------------------------------------------------
# 3. Процедура удаления повторных вхождений
# ------------------------------------------------------------
def remove_duplicates(src_filename, dest_filename):
    """
    Читает файл src_filename и записывает в dest_filename все числа,
    исключая повторные вхождения, с сохранением порядка первого появления.
    """
    numbers = read_numbers_from_file(src_filename)
    if numbers is None:
        print(f"Ошибка: файл '{src_filename}' не найден.")
        return
    if not numbers:
        print("Исходный файл пуст. Будет создан пустой выходной файл.")
        write_numbers_to_file(dest_filename, [])
        return

    seen = set()
    unique_numbers = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            unique_numbers.append(num)

    write_numbers_to_file(dest_filename, unique_numbers)
    print(f"Удалены повторения. Записано {len(unique_numbers)} уникальных чисел в '{dest_filename}'.")


# ------------------------------------------------------------
# 4. Основная программа
# ------------------------------------------------------------
def main():
    print("Задача 487: Исключение повторных вхождений чисел")
    src = "f.txt"
    dest = "g.txt"

    # Проверяем, существует ли f и не пуст ли он
    numbers = read_numbers_from_file(src)
    if numbers is None or len(numbers) == 0:
        create_file_f(src)
    else:
        print(f"Файл '{src}' уже существует и содержит числа.")

    # Выводим исходные числа
    numbers = read_numbers_from_file(src)
    print(f"\nИсходные числа из файла '{src}': {numbers}")

    # Выполняем удаление дубликатов
    remove_duplicates(src, dest)

    # Выводим результат
    result = read_numbers_from_file(dest)
    if result is not None:
        print(f"Числа в файле '{dest}': {result}")
    else:
        print("Файл g не создан из-за ошибки.")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")