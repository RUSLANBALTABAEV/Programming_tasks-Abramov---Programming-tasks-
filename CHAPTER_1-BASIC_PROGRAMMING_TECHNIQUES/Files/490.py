"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

490. Дан файл f , компоненты которого являются целыми числами. Число компонент файла делится на 100. Записать в файл g наибольшее значение первых ста компонент файла f , затем – следующих ста компонент и т. д. 
"""


import random
import os


# ------------------------------------------------------------
# 1. Процедуры работы с файлами
# ------------------------------------------------------------
def read_numbers_from_file(filename):
    """Читает целые числа из файла и возвращает список."""
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
    """Записывает список целых чисел в файл (каждое с новой строки)."""
    with open(filename, 'w', encoding='utf-8') as f:
        for num in numbers:
            f.write(f"{num}\n")


# ------------------------------------------------------------
# 2. Создание исходного файла f (если отсутствует или не удовлетворяет условию)
# ------------------------------------------------------------
def is_valid_file(numbers):
    """Проверяет, что количество чисел кратно 100 и больше нуля."""
    return len(numbers) > 0 and len(numbers) % 100 == 0


def create_file_f(filename):
    """Создаёт файл f с целыми числами, количество которых делится на 100."""
    print("Файл f не существует, пуст или количество чисел не кратно 100.")
    print("Выберите способ задания содержимого:")
    print("1 — Ручной ввод чисел (количество должно быть кратно 100)")
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
                n = int(input("Сколько чисел записать в файл (должно делиться на 100): "))
                if n <= 0 or n % 100 != 0:
                    print("Число должно быть положительным и кратным 100.")
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
        blocks = random.randint(2, 4)   # от 2 до 4 блоков по 100 чисел
        total = blocks * 100
        numbers = [random.randint(-1000, 1000) for _ in range(total)]
        print(f"Сгенерировано {total} случайных чисел ({blocks} блоков по 100).")
    else:  # готовый пример
        # 200 чисел: первые 100 – от 1 до 100, вторые 100 – от -100 до -1
        numbers = list(range(1, 101)) + list(range(-1, -101, -1))
        print("Готовый пример: 200 чисел (положительные и отрицательные).")

    write_numbers_to_file(filename, numbers)
    print(f"Числа записаны в '{filename}'.")


# ------------------------------------------------------------
# 3. Процедура извлечения максимумов по сотням
# ------------------------------------------------------------
def extract_max_per_hundred(src_filename, dest_filename):
    """
    Читает src_filename, находит максимум в каждой группе из 100 чисел
    и записывает эти максимумы в dest_filename.
    """
    data = read_numbers_from_file(src_filename)
    if data is None:
        print(f"Ошибка: файл '{src_filename}' не найден.")
        return
    if not data:
        print("Исходный файл пуст.")
        return
    if len(data) % 100 != 0:
        print("Предупреждение: количество чисел не кратно 100. "
              "Обработано будет только полное число сотен.")
        data = data[:len(data) // 100 * 100]

    max_values = []
    for i in range(0, len(data), 100):
        block = data[i:i+100]
        max_values.append(max(block))

    write_numbers_to_file(dest_filename, max_values)
    print(f"Обработано {len(data)} чисел, найдено {len(max_values)} максимумов.")


# ------------------------------------------------------------
# 4. Основная программа
# ------------------------------------------------------------
def main():
    print("Задача 490: Максимумы в блоках по 100 чисел")
    src = "f.txt"
    dest = "g.txt"

    # Проверка исходного файла
    numbers = read_numbers_from_file(src)
    if numbers is None or not is_valid_file(numbers):
        create_file_f(src)
        numbers = read_numbers_from_file(src)

    # Если файл всё равно пуст или некратен 100 после создания – выходим
    if not numbers or len(numbers) % 100 != 0:
        print("Не удалось получить корректный файл. Завершение работы.")
        return

    print(f"\nФайл '{src}' содержит {len(numbers)} чисел.")
    extract_max_per_hundred(src, dest)

    # Вывод результата для проверки
    result = read_numbers_from_file(dest)
    if result is not None:
        print(f"Максимумы, записанные в '{dest}': {result}")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")