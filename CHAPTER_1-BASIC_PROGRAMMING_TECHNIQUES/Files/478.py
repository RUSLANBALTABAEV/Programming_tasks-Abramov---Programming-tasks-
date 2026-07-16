"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

478. Даны файлы f1, f2, f3, f4, f5, компоненты которых являются действительными числами. Организовать обмен компонентами между файлами в соответствии со следующей схемой: 
              
                 f1 f2 f3 f4 f5
                 |  |  |  |  |
                 f3 f4 f6 f2 f1
т. е. компоненты файла f1 переписываются в файл f3, компоненты файла f2 - в f4 и т. д. Разрешается использовать только один вспомогательный файл h.
"""


import random
import os


# ------------------------------------------------------------
# 1. Процедуры работы с файлами
# ------------------------------------------------------------
def write_numbers_to_file(filename, numbers):
    """Записывает список действительных чисел в файл (через пробел)."""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(' '.join(str(x) for x in numbers))


def read_numbers_from_file(filename):
    """Читает действительные числа из файла и возвращает список."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            return [float(x) for x in content.split()]
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")
        return None
    except ValueError:
        print(f"Файл '{filename}' содержит некорректные данные.")
        return None


def copy_file(source, destination):
    """Копирует содержимое source в destination."""
    with open(source, 'r', encoding='utf-8') as src:
        content = src.read()
    with open(destination, 'w', encoding='utf-8') as dst:
        dst.write(content)


# ------------------------------------------------------------
# 2. Процедура обмена по схеме с использованием файла h
# ------------------------------------------------------------
def swap_files():
    """
    Выполняет обмен согласно схеме:
    f1 -> f3, f2 -> f4, f3 -> f5, f4 -> f2, f5 -> f1.
    Используется только один вспомогательный файл h.txt.
    """
    # Цикл 1 -> 3 -> 5 -> 1
    copy_file("f1.txt", "h.txt")      # сохраняем f1 во временный
    copy_file("f5.txt", "f1.txt")     # f5 → f1
    copy_file("f3.txt", "f5.txt")     # f3 → f5
    copy_file("h.txt", "f3.txt")      # h (старый f1) → f3

    # Цикл 2 -> 4 -> 2
    copy_file("f2.txt", "h.txt")      # сохраняем f2 во временный
    copy_file("f4.txt", "f2.txt")     # f4 → f2
    copy_file("h.txt", "f4.txt")      # h (старый f2) → f4

    print("Обмен завершён.")


# ------------------------------------------------------------
# 3. Ввод данных (создание файлов f1...f5)
# ------------------------------------------------------------
def create_initial_files():
    """Выбор способа задания содержимого файлов f1...f5."""
    print("Задача 478: Обмен компонентами между пятью файлами")
    print("Выберите способ задания чисел в файлах f1..f5:")
    print("1 — Ручной ввод для каждого файла")
    print("2 — Случайная генерация чисел")
    print("3 — Готовые примеры")

    while True:
        choice = input("Ваш выбор (1/2/3): ").strip()
        if choice in ('1', '2', '3'):
            break
        print("Ошибка: выберите 1, 2 или 3.")

    filenames = ["f1.txt", "f2.txt", "f3.txt", "f4.txt", "f5.txt"]

    if choice == '1':
        print("Для каждого файла введите действительные числа через пробел.")
        for name in filenames:
            while True:
                try:
                    data = list(map(float, input(f"{name}: ").split()))
                    if not data:
                        print("Нужно хотя бы одно число.")
                        continue
                    write_numbers_to_file(name, data)
                    break
                except ValueError:
                    print("Ошибка ввода. Введите числа.")

    elif choice == '2':
        # Случайная генерация: от 1 до 5 чисел в каждом файле
        for name in filenames:
            count = random.randint(1, 5)
            numbers = [round(random.uniform(-20, 20), 4) for _ in range(count)]
            write_numbers_to_file(name, numbers)
        print("Случайные числа записаны в файлы f1..f5.")

    else:  # Готовые примеры
        examples = {
            "f1.txt": [1.1],
            "f2.txt": [2.2, 2.22],
            "f3.txt": [3.3],
            "f4.txt": [4.4],
            "f5.txt": [5.5, 5.55]
        }
        for name, nums in examples.items():
            write_numbers_to_file(name, nums)
        print("Готовый пример записан в файлы.")


# ------------------------------------------------------------
# 4. Основная программа
# ------------------------------------------------------------
def main():
    # Создаём исходные файлы
    create_initial_files()

    # Выводим содержимое ДО обмена
    print("\nСодержимое файлов ДО обмена:")
    for name in ["f1.txt", "f2.txt", "f3.txt", "f4.txt", "f5.txt"]:
        nums = read_numbers_from_file(name)
        print(f"{name}: {nums}")

    # Выполняем обмен
    swap_files()

    # Выводим содержимое ПОСЛЕ обмена
    print("\nСодержимое файлов ПОСЛЕ обмена:")
    for name in ["f1.txt", "f2.txt", "f3.txt", "f4.txt", "f5.txt"]:
        nums = read_numbers_from_file(name)
        print(f"{name}: {nums}")

    print("\nСхема обмена: f1→f3, f2→f4, f3→f5, f4→f2, f5→f1.")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
