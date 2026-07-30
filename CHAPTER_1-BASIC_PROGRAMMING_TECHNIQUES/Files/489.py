"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

489. Дан файл f, компоненты которого являются целыми числами. Никакая из компонент файла f не равна нулю. Числа в файле идут в следующем порядке: десять положительных, десять отрицательных, десять положительных, десять отрицательных и т. д. Переписать компоненты файла f в файл g так, чтобы в файле g числа шли в следующем порядке:
а) пять положительных, пять отрицательных, пять положительных, пять отрицательных и т. д.;
б) двадцать положительных, двадцать отрицательных, двадцать положительных, двадцать отрицательных и т. д. (предполагается, что число компонент файла f делится на 40).
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
# 2. Проверка и создание исходного файла f
# ------------------------------------------------------------
def is_valid_file(numbers):
    """Проверяет, что числа ненулевые и имеют нужную структуру (блоки по 10)."""
    if not numbers or any(x == 0 for x in numbers):
        return False
    # Проверим, что идут блоки по 10: сначала все положительные в десятках, потом отрицательные...
    # Для простоты проверим только что количество положительных и отрицательных одинаково
    # и кратно 10. (Полную проверку структуры можно добавить при необходимости.)
    pos = [x for x in numbers if x > 0]
    neg = [x for x in numbers if x < 0]
    if len(pos) != len(neg):
        return False
    if len(pos) % 10 != 0:
        return False
    # Проверим, действительно ли они идут группами по 10
    i = 0
    n = len(numbers)
    while i < n:
        # Группа из 10 чисел одного знака
        sign = 1 if numbers[i] > 0 else -1
        for j in range(i, i + 10):
            if numbers[j] * sign <= 0:
                return False
        i += 10
    return True


def create_file_f(filename):
    """Создаёт файл f с корректными числами по выбору пользователя."""
    print("Файл f не существует, пуст или не удовлетворяет условиям.")
    print("Условия: числа ненулевые, идут блоками по 10 (10+, 10–, 10+, 10–...),")
    print("количество чисел делится на 40.")
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
                n = int(input("Введите общее количество чисел (должно делиться на 40): "))
                if n <= 0 or n % 40 != 0:
                    print("Число должно быть положительным и кратным 40.")
                    continue
                print(f"Введите {n} ненулевых целых чисел через пробел (блоками по 10):")
                numbers = list(map(int, input().split()))
                if len(numbers) != n:
                    print(f"Ожидалось {n} чисел, получено {len(numbers)}.")
                    continue
                if not is_valid_file(numbers):
                    print("Числа не соответствуют требуемой структуре.")
                    continue
                break
            except ValueError:
                print("Ошибка ввода. Введите целые числа.")
    elif choice == '2':
        # Генерируем 80 чисел (2 блока по 40 => 4 группы по 10+, 10–)
        numbers = []
        for _ in range(2):
            # 20 положительных подряд (две группы по 10)
            for __ in range(2):
                numbers.extend([random.randint(1, 20) for _ in range(10)])
            # 20 отрицательных подряд (две группы по 10)
            for __ in range(2):
                numbers.extend([random.randint(-20, -1) for _ in range(10)])
        print(f"Сгенерировано {len(numbers)} чисел (блоки по 10).")
    else:  # готовый пример
        numbers = [
            1,2,3,4,5,6,7,8,9,10,
            -1,-2,-3,-4,-5,-6,-7,-8,-9,-10,
            11,12,13,14,15,16,17,18,19,20,
            -11,-12,-13,-14,-15,-16,-17,-18,-19,-20
        ] * 2  # удвоим, чтобы получить 80 чисел
        print("Готовый пример (80 чисел).")

    write_numbers_to_file(filename, numbers)
    print(f"Числа записаны в '{filename}'.")


# ------------------------------------------------------------
# 3. Процедуры перезаписи
# ------------------------------------------------------------
def solve_a(numbers):
    """Преобразование: 5+,5–,5+,5–... вместо 10+,10–..."""
    pos = [x for x in numbers if x > 0]
    neg = [x for x in numbers if x < 0]
    result = []
    # Исходные группы по 10; делим каждую десятку пополам и чередуем с другой
    for i in range(0, len(pos), 10):
        # Берём первые 5 положительных из текущей десятки
        result.extend(pos[i:i+5])
        # Берём первые 5 отрицательных из соответствующей десятки
        result.extend(neg[i:i+5])
        # Оставшиеся 5 положительных
        result.extend(pos[i+5:i+10])
        # Оставшиеся 5 отрицательных
        result.extend(neg[i+5:i+10])
    return result


def solve_b(numbers):
    """Преобразование: 20+,20–,20+,20–... (объединяем по две десятки)"""
    pos = [x for x in numbers if x > 0]
    neg = [x for x in numbers if x < 0]
    result = []
    for i in range(0, len(pos), 20):
        result.extend(pos[i:i+20])
        result.extend(neg[i:i+20])
    return result


# ------------------------------------------------------------
# 4. Основная программа
# ------------------------------------------------------------
def main():
    print("Задача 489: Перегруппировка чисел (10+/10– → 5+/5– и 20+/20–)")
    src = "f.txt"
    dest_a = "g_a.txt"
    dest_b = "g_b.txt"

    # Проверка исходного файла
    numbers = read_numbers_from_file(src)
    if numbers is None or not is_valid_file(numbers):
        create_file_f(src)
        numbers = read_numbers_from_file(src)

    print(f"\nИсходные числа (первые 40): {numbers[:40]} ...")

    # Вариант а)
    result_a = solve_a(numbers)
    write_numbers_to_file(dest_a, result_a)
    print(f"а) Результат (первые 20): {result_a[:20]} ...")

    # Вариант б)
    result_b = solve_b(numbers)
    write_numbers_to_file(dest_b, result_b)
    print(f"б) Результат (первые 20): {result_b[:20]} ...")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")