"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

509. Сведения об автомобиле состоят из его марки, номера и фамилии владельца. Дан файл f, содержащий сведения о нескольких автомобилях. Найти:
а) фамилии владельцев и номера автомобилей данной марки;
б) количество автомобилей каждой марки.
"""


import random
import os
from collections import Counter


# ------------------------------------------------------------
# 1. Процедуры работы с файлами (как в задаче 508)
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
    """Создаёт файл f со сведениями об автомобилях."""
    print("Файл f не существует или пуст. Задайте данные об автомобилях.")
    print("Формат строки: Марка Номер Фамилия_владельца")
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
                print("  Ошибка: нужно три поля (Марка, Номер, Фамилия).")
                continue
            # Проверка: номер обычно состоит из букв и цифр, фамилия из букв
            if not (parts[0].isalpha() and parts[2].isalpha()):
                print("  Предупреждение: марка и фамилия должны содержать только буквы.")
            lines.append(line)
        if not lines:
            print("Не введено ни одной строки. Будет использован готовый пример.")
            text = ("Toyota A123BC Иванов\nToyota B456CD Петров\nBMW C789DE Сидоров\n"
                    "Toyota D012EF Смирнов\nMercedes E345FG Кузнецов\n"
                    "BMW F678GH Попов\nLada G901HI Морозов\nBMW H234IJ Новиков\n"
                    "Toyota I567KL Федоров")
        else:
            text = "\n".join(lines)
    elif choice == '2':
        brands = ["Toyota", "BMW", "Lada", "Mercedes", "Honda", "Ford", "Nissan", "Kia"]
        owners = ["Иванов", "Петров", "Сидоров", "Смирнов", "Кузнецов", "Попов",
                  "Васильев", "Михайлов", "Новиков", "Федоров", "Морозов", "Соколов"]
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        digits = '0123456789'
        n = random.randint(8, 15)  # количество записей
        lines = []
        for _ in range(n):
            brand = random.choice(brands)
            # Номер формата: буква, три цифры, две буквы (упрощённо)
            number = (random.choice(letters) +
                      ''.join(random.choices(digits, k=3)) +
                      ''.join(random.choices(letters, k=2)))
            owner = random.choice(owners)
            lines.append(f"{brand} {number} {owner}")
        text = "\n".join(lines)
        print(f"Сгенерировано {n} записей об автомобилях.")
    else:  # готовый пример
        text = ("Toyota A123BC Иванов\nToyota B456CD Петров\nBMW C789DE Сидоров\n"
                "Toyota D012EF Смирнов\nMercedes E345FG Кузнецов\n"
                "BMW F678GH Попов\nLada G901HI Морозов\nBMW H234IJ Новиков\n"
                "Toyota I567KL Федоров")
        print("Использован готовый пример (9 автомобилей).")

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
            # Простейшая проверка: марка и фамилия – буквы, номер – не менее 3 символов
            if parts[0].isalpha() and parts[2].isalpha() and len(parts[1]) >= 4:
                has_valid = True
                break
    if not has_valid:
        print("Файл не содержит корректных записей об автомобилях.")
        create_file_f(filename)


# ------------------------------------------------------------
# 3. Чтение автомобилей из файла
# ------------------------------------------------------------
def read_cars(filename):
    """Возвращает список словарей с ключами brand, number, owner."""
    cars = []
    for line in read_file(filename).strip().splitlines():
        parts = line.split()
        if len(parts) == 3:
            cars.append({
                'brand': parts[0],
                'number': parts[1],
                'owner': parts[2]
            })
    return cars


# ------------------------------------------------------------
# 4. Решения пунктов а) и б)
# ------------------------------------------------------------
def solve_a(cars):
    """Вывод фамилий и номеров автомобилей заданной марки."""
    target = input("Введите марку автомобиля для поиска: ").strip()
    found = [c for c in cars if c['brand'].lower() == target.lower()]
    print(f"\nа) Автомобили марки '{target}':")
    if found:
        for c in found:
            print(f"   Владелец: {c['owner']}, Номер: {c['number']}")
    else:
        print("   Таких автомобилей не найдено.")


def solve_b(cars):
    """Подсчёт количества автомобилей каждой марки."""
    counter = Counter(c['brand'] for c in cars)
    print("\nб) Количество автомобилей каждой марки:")
    for brand, count in sorted(counter.items()):
        print(f"   {brand}: {count}")


# ------------------------------------------------------------
# 5. Основная программа
# ------------------------------------------------------------
def main():
    print("Задача 509: Сведения об автомобилях")
    file_f = "f.txt"

    ensure_file_exists(file_f)
    cars = read_cars(file_f)

    if not cars:
        print("Нет данных для обработки.")
        return

    print(f"\nВсего записей: {len(cars)}")
    print("Примеры записей:")
    for c in cars[:5]:
        print(f"   {c['brand']} {c['number']} {c['owner']}")
    if len(cars) > 5:
        print("   ...")

    solve_a(cars)
    solve_b(cars)


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")