"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

491. Из условия предыдущей задачи удаляется предположение о том, что число компонент файла f делится на 100. Если в последней группе окажется менее ста компонент, то последняя компонента файла g должна быть равна наибольшей из компонент файла f , образующих последнюю (неполную) группу.
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
# 2. Создание исходного файла f (если отсутствует или пуст)
# ------------------------------------------------------------
def create_file_f(filename):
    """Создаёт файл f с целыми числами (любое количество > 0)."""
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
        # Генерируем случайное количество чисел (от 50 до 250)
        count = random.randint(50, 250)
        numbers = [random.randint(-1000, 1000) for _ in range(count)]
        print(f"Сгенерировано {count} случайных чисел.")
    else:  # готовый пример
        # 250 чисел: две полные сотни и 50 чисел в неполной группе
        numbers = list(range(1, 101)) + list(range(-1, -101, -1)) + list(range(50))
        print("Готовый пример: 250 чисел (две полные сотни и 50 чисел).")

    write_numbers_to_file(filename, numbers)
    print(f"Числа записаны в '{filename}'.")


# ------------------------------------------------------------
# 3. Процедура извлечения максимумов по сотням (включая неполную группу)
# ------------------------------------------------------------
def extract_max_per_hundred(src_filename, dest_filename):
    """
    Читает src_filename, находит максимум в каждой группе из 100 чисел
    (последняя группа может содержать менее 100 чисел) и записывает
    эти максимумы в dest_filename.
    """
    data = read_numbers_from_file(src_filename)
    if data is None:
        print(f"Ошибка: файл '{src_filename}' не найден.")
        return
    if not data:
        print("Исходный файл пуст.")
        return

    max_values = []
    total = len(data)

    for i in range(0, total, 100):
        block = data[i:i+100]          # срез автоматически учитывает неполный конец
        max_values.append(max(block))

    write_numbers_to_file(dest_filename, max_values)
    print(f"Обработано {total} чисел, найдено {len(max_values)} максимумов.")


# ------------------------------------------------------------
# 4. Основная программа
# ------------------------------------------------------------
def main():
    print("Задача 491: Максимумы в блоках по 100 чисел (с учётом неполной последней группы)")
    src = "f.txt"
    dest = "g.txt"

    # Проверка исходного файла
    numbers = read_numbers_from_file(src)
    if numbers is None or len(numbers) == 0:
        create_file_f(src)
        numbers = read_numbers_from_file(src)

    if not numbers:
        print("Файл пуст. Завершение работы.")
        return

    print(f"\nФайл '{src}' содержит {len(numbers)} чисел.")
    extract_max_per_hundred(src, dest)

    # Вывод результата для проверки
    result = read_numbers_from_file(dest)
    if result is not None:
        print(f"Максимумы, записанные в '{dest}': {result}")
        print(f"Количество максимумов: {len(result)} "
              f"(последняя группа {'полная' if len(numbers) % 100 == 0 else 'неполная'}).")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")