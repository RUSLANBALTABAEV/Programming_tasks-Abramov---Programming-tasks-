"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

510. Дан файл f, содержащий различные даты. Каждая дата - это число, месяц и год. Найти:
а) год с наименьшим номером;
б) все весенние даты;
в) самую позднюю дату.
"""


import random
import os


# ------------------------------------------------------------
# 1. Процедуры работы с файлами
# ------------------------------------------------------------
def create_text_file(filename, text):
    """Создаёт (или перезаписывает) текстовый файл с указанным содержимым."""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)


def read_file(filename):
    """Читает и возвращает содержимое текстового файла."""
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()


# ------------------------------------------------------------
# 2. Создание исходного файла f (если отсутствует или пуст)
# ------------------------------------------------------------
def create_file_f(filename):
    """Создаёт файл f с датами (день месяц год)."""
    print("Файл f не существует или пуст. Задайте даты.")
    print("Формат строки: день месяц год (целые числа через пробел).")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод (пустая строка — конец)")
    print("2 — Случайная генерация")
    print("3 — Готовый пример")

    while True:
        choice = input("Ваш выбор (1/2/3): ").strip()
        if choice in ('1', '2', '3'):
            break
        print("Ошибка: выберите 1, 2 или 3.")

    if choice == '1':
        print("Вводите по одной строке. Для завершения — пустая строка.")
        lines = []
        while True:
            line = input().strip()
            if line == "":
                break
            parts = line.split()
            if len(parts) != 3:
                print("  Ошибка: нужно три целых числа (день, месяц, год).")
                continue
            try:
                day, month, year = map(int, parts)
                if not (1 <= day <= 31 and 1 <= month <= 12):
                    print("  Ошибка: некорректная дата.")
                    continue
            except ValueError:
                print("  Ошибка: введите целые числа.")
                continue
            lines.append(line)
        if not lines:
            print("Не введено ни одной строки. Будет использован готовый пример.")
            text = ("15 3 2023\n20 11 2022\n10 5 2024\n1 1 2021\n"
                    "30 4 2023\n28 2 2023\n15 7 2024\n31 12 2022")
        else:
            text = "\n".join(lines)
    elif choice == '2':
        n = random.randint(5, 12)  # количество дат
        lines = []
        for _ in range(n):
            year = random.randint(2000, 2025)
            month = random.randint(1, 12)
            # простейшая проверка на максимальное число дней в месяце
            if month == 2:
                max_day = 29 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 28
            elif month in (4, 6, 9, 11):
                max_day = 30
            else:
                max_day = 31
            day = random.randint(1, max_day)
            lines.append(f"{day} {month} {year}")
        text = "\n".join(lines)
        print(f"Сгенерировано {n} случайных дат.")
    else:  # готовый пример
        text = ("15 3 2023\n20 11 2022\n10 5 2024\n1 1 2021\n"
                "30 4 2023\n28 2 2023\n15 7 2024\n31 12 2022")
        print("Использован готовый пример (8 дат).")

    create_text_file(filename, text)
    print(f"Данные записаны в '{filename}'.")


def ensure_file_exists(filename):
    """Проверяет, существует ли файл и содержит ли данные. Если нет – создаёт."""
    if not os.path.exists(filename):
        create_file_f(filename)
        return
    content = read_file(filename).strip()
    if not content:
        create_file_f(filename)
        return
    # Проверим, есть ли хотя бы одна корректная строка
    lines = content.splitlines()
    has_valid = False
    for line in lines:
        parts = line.split()
        if len(parts) == 3:
            try:
                day, month, year = map(int, parts)
                if 1 <= day <= 31 and 1 <= month <= 12:
                    has_valid = True
                    break
            except ValueError:
                pass
    if not has_valid:
        print("Файл не содержит корректных дат.")
        create_file_f(filename)


# ------------------------------------------------------------
# 3. Чтение дат из файла
# ------------------------------------------------------------
def read_dates(filename):
    """Возвращает список кортежей (день, месяц, год)."""
    dates = []
    for line in read_file(filename).strip().splitlines():
        parts = line.split()
        if len(parts) == 3:
            try:
                day, month, year = map(int, parts)
                if 1 <= day <= 31 and 1 <= month <= 12:
                    dates.append((day, month, year))
            except ValueError:
                pass
    return dates


# ------------------------------------------------------------
# 4. Решения пунктов а), б), в)
# ------------------------------------------------------------
def solve_a(dates):
    """Год с наименьшим номером."""
    if not dates:
        return None
    return min(date[2] for date in dates)


def solve_b(dates):
    """Все весенние даты (март, апрель, май)."""
    return [date for date in dates if 3 <= date[1] <= 5]


def solve_c(dates):
    """Самая поздняя дата (сравнение по году, месяцу, дню)."""
    if not dates:
        return None
    return max(dates, key=lambda d: (d[2], d[1], d[0]))


# ------------------------------------------------------------
# 5. Основная программа
# ------------------------------------------------------------
def main():
    print("Задача 510: Обработка дат")
    file_f = "f.txt"

    ensure_file_exists(file_f)
    dates = read_dates(file_f)

    if not dates:
        print("Нет данных для обработки.")
        return

    print(f"\nВсего дат: {len(dates)}")
    print("Примеры записей:")
    for d in dates[:5]:
        print(f"   {d[0]:02d}.{d[1]:02d}.{d[2]}")
    if len(dates) > 5:
        print("   ...")

    # а)
    earliest = solve_a(dates)
    print(f"\nа) Год с наименьшим номером: {earliest}" if earliest else "\nа) Дат нет.")

    # б)
    spring = solve_b(dates)
    print("\nб) Весенние даты:")
    if spring:
        for d in spring:
            print(f"   {d[0]:02d}.{d[1]:02d}.{d[2]}")
    else:
        print("   Отсутствуют.")

    # в)
    latest = solve_c(dates)
    if latest:
        print(f"\nв) Самая поздняя дата: {latest[0]:02d}.{latest[1]:02d}.{latest[2]}")
    else:
        print("\nв) Нет данных.")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")