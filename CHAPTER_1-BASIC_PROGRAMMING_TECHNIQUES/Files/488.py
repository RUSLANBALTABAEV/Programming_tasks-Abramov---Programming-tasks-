"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

488. Дан файл f , компоненты которого являются целыми числами. Никакая из компонент файла не равна нулю. Файл f содержит столько же отрицательных чисел, сколько и положительных.
Используя вспомогательный файл h , переписать компоненты файла f в файл g так, чтобы в файле g:
а) не было двух соседних чисел с одним знаком;
б) сначала шли положительные, потом отрицательные числа;
в) числа шли в следующем порядке: два положительных, два отрицательных, два положительных, два отрицательных и т. д.
(предполагается, что число компонент в файле f делится на 4).
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
# 2. Создание исходного файла f (если отсутствует или не удовлетворяет условиям)
# ------------------------------------------------------------
def is_valid_file(numbers):
    """Проверяет, что ни одно число не ноль, и количество положительных равно отрицательным."""
    if not numbers:
        return False
    if any(x == 0 for x in numbers):
        return False
    pos = sum(1 for x in numbers if x > 0)
    neg = sum(1 for x in numbers if x < 0)
    return pos == neg


def create_file_f(filename):
    """Создаёт файл f с корректными числами по выбору пользователя."""
    print("Файл f не существует, пуст или не удовлетворяет условиям.")
    print("Условия: числа ненулевые, поровну положительных и отрицательных.")
    print("Выберите способ задания:")
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
                n = int(input("Сколько чисел записать (чётное количество, n >= 2): "))
                if n <= 1 or n % 2 != 0:
                    print("Нужно чётное количество чисел.")
                    continue
                print(f"Введите {n} ненулевых целых чисел через пробел:")
                numbers = list(map(int, input().split()))
                if len(numbers) != n:
                    print(f"Ожидалось {n} чисел, получено {len(numbers)}.")
                    continue
                if not is_valid_file(numbers):
                    print("Числа должны быть ненулевыми, с равным количеством положительных и отрицательных.")
                    continue
                break
            except ValueError:
                print("Ошибка ввода. Введите целые числа.")
    elif choice == '2':
        # Генерируем чётное количество чисел, поровну + и -, без нулей
        half = random.randint(2, 5)  # количество положительных
        pos_numbers = [random.randint(1, 20) for _ in range(half)]
        neg_numbers = [random.randint(-20, -1) for _ in range(half)]
        numbers = pos_numbers + neg_numbers
        random.shuffle(numbers)
        print(f"Сгенерирована последовательность из {len(numbers)} чисел.")
    else:  # готовый пример
        numbers = [5, -2, 3, -7, 8, -1, 4, -6]
        print("Готовый пример: ", numbers)

    write_numbers_to_file(filename, numbers)
    print(f"Числа записаны в '{filename}'.")


# ------------------------------------------------------------
# 3. Процедуры преобразований (с использованием h)
# ------------------------------------------------------------
def solve_a(numbers):
    """Чередование знаков: + - + - ..."""
    pos = [x for x in numbers if x > 0]
    neg = [x for x in numbers if x < 0]
    result = []
    for i in range(len(pos)):
        result.append(pos[i])
        result.append(neg[i])
    return result


def solve_b(numbers):
    """Сначала все положительные, затем все отрицательные."""
    pos = [x for x in numbers if x > 0]
    neg = [x for x in numbers if x < 0]
    return pos + neg


def solve_c(numbers):
    """Блоками: два положительных, два отрицательных, два положительных, ..."""
    pos = [x for x in numbers if x > 0]
    neg = [x for x in numbers if x < 0]
    result = []
    for i in range(0, len(pos), 2):
        result.extend(pos[i:i+2])
        result.extend(neg[i:i+2])
    return result


def process_variant(src, h_file, dest, transform_func):
    """Читает src, применяет transform_func, записывает в h, затем копирует в dest."""
    numbers = read_numbers_from_file(src)
    if not numbers:
        print("Исходный файл пуст.")
        return
    transformed = transform_func(numbers)
    write_numbers_to_file(h_file, transformed)
    # Копирование h -> dest
    temp = read_numbers_from_file(h_file)
    write_numbers_to_file(dest, temp)


# ------------------------------------------------------------
# 4. Основная программа
# ------------------------------------------------------------
def main():
    print("Задача 488: Преобразование файла с использованием вспомогательного h")
    src = "f.txt"
    h_file = "h.txt"

    # Проверка исходного файла
    numbers = read_numbers_from_file(src)
    if numbers is None or not is_valid_file(numbers):
        create_file_f(src)
        numbers = read_numbers_from_file(src)

    print(f"\nИсходные числа: {numbers}")

    # Вариант а)
    dest_a = "g_a.txt"
    process_variant(src, h_file, dest_a, solve_a)
    print(f"а) Чередование знаков: {read_numbers_from_file(dest_a)}")

    # Вариант б)
    dest_b = "g_b.txt"
    process_variant(src, h_file, dest_b, solve_b)
    print(f"б) Сначала положительные, затем отрицательные: {read_numbers_from_file(dest_b)}")

    # Вариант в)
    dest_c = "g_c.txt"
    if len(numbers) % 4 != 0:
        print("Предупреждение: количество чисел не делится на 4, вариант в) может работать некорректно.")
    process_variant(src, h_file, dest_c, solve_c)
    print(f"в) Блоки по два числа: {read_numbers_from_file(dest_c)}")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")