"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

516. Даны два файла f1 и f2. Файл f1 - это инвентарный файл, содержащий сведения о том, сколько изделий каких видов продукции хранится на складе (вид продукции задается его порядковым номером). 
Файл f2 - это вспомогательный файл, содержащий сведения о том, на сколько уменьшилось или увеличилось количество изделий по некоторым видам продукции. Вспомогательный файл может содержать 
несколько сообщений по продукции одного вида или не содержать ни одного такого сообщения. Обновить инвентарный файл на основе вспомогательного, образовав новый файл g.
"""


import random
import os
from collections import defaultdict


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
# 2. Создание исходных файлов f1 и f2 (если отсутствуют или пусты)
# ------------------------------------------------------------
def create_files():
    """Создаёт файлы f1 (инвентарь) и f2 (изменения) по выбору пользователя."""
    print("Необходимы файлы f1.txt (инвентарь) и f2.txt (изменения).")
    print("Выберите способ ввода данных:")
    print("1 — Ручной ввод")
    print("2 — Случайная генерация")
    print("3 — Готовый пример")

    while True:
        choice = input("Ваш выбор (1/2/3): ").strip()
        if choice in ('1', '2', '3'):
            break
        print("Ошибка: выберите 1, 2 или 3.")

    if choice == '1':
        # Ручной ввод инвентаря
        print("\nВвод инвентарного файла f1.")
        print("Формат строки: Номер_продукта Количество")
        print("Для завершения введите пустую строку.")
        lines_f1 = []
        while True:
            line = input().strip()
            if line == "":
                break
            parts = line.split()
            if len(parts) != 2:
                print("  Ошибка: нужно два целых числа.")
                continue
            try:
                int(parts[0])
                int(parts[1])
            except ValueError:
                print("  Ошибка: введите целые числа.")
                continue
            lines_f1.append(line)
        if not lines_f1:
            lines_f1 = ["1 100", "2 200", "3 50", "4 10", "5 15"]
            print("  Использованы данные по умолчанию.")
        text_f1 = "\n".join(lines_f1)
        create_text_file("f1.txt", text_f1)

        # Ручной ввод изменений
        print("\nВвод вспомогательного файла f2 (изменения).")
        print("Формат строки: Номер_продукта Изменение (может быть отрицательным)")
        print("Для завершения введите пустую строку.")
        lines_f2 = []
        while True:
            line = input().strip()
            if line == "":
                break
            parts = line.split()
            if len(parts) != 2:
                print("  Ошибка: нужно два целых числа.")
                continue
            try:
                int(parts[0])
                int(parts[1])
            except ValueError:
                print("  Ошибка: введите целые числа.")
                continue
            lines_f2.append(line)
        if not lines_f2:
            lines_f2 = ["1 -20", "2 50", "1 10", "3 -10", "5 -5", "4 0", "6 100"]
            print("  Использованы данные по умолчанию.")
        text_f2 = "\n".join(lines_f2)
        create_text_file("f2.txt", text_f2)

    elif choice == '2':
        # Случайная генерация
        num_products = random.randint(4, 8)
        products = list(range(1, num_products + 1))
        lines_f1 = []
        for pid in products:
            qty = random.randint(10, 200)
            lines_f1.append(f"{pid} {qty}")
        text_f1 = "\n".join(lines_f1)
        create_text_file("f1.txt", text_f1)
        print("Сгенерирован инвентарный файл f1.")

        num_changes = random.randint(3, 7)
        lines_f2 = []
        for _ in range(num_changes):
            pid = random.choice(products)
            change = random.randint(-50, 50)
            lines_f2.append(f"{pid} {change}")
        text_f2 = "\n".join(lines_f2)
        create_text_file("f2.txt", text_f2)
        print("Сгенерирован файл изменений f2.")

    else:  # готовый пример
        text_f1 = "1 100\n2 200\n3 50\n4 10\n5 15"
        create_text_file("f1.txt", text_f1)
        text_f2 = "1 -20\n2 50\n1 10\n3 -10\n5 -5\n4 0\n6 100"
        create_text_file("f2.txt", text_f2)
        print("Использован готовый пример файлов f1 и f2.")

    print("Файлы созданы.\n")


def ensure_files_exist():
    """Проверяет существование f1 и f2 и создаёт их, если нужно."""
    if not os.path.exists("f1.txt") or not os.path.exists("f2.txt"):
        create_files()
        return
    # Проверка содержимого
    content1 = read_file("f1.txt").strip()
    content2 = read_file("f2.txt").strip()
    if not content1 or not content2:
        create_files()
        return
    # Проверка на корректность записей
    valid = True
    for line in content1.splitlines():
        parts = line.split()
        if len(parts) != 2:
            valid = False
            break
        try:
            int(parts[0])
            int(parts[1])
        except ValueError:
            valid = False
            break
    if not valid:
        create_files()
        return
    valid = True
    for line in content2.splitlines():
        parts = line.split()
        if len(parts) != 2:
            valid = False
            break
        try:
            int(parts[0])
            int(parts[1])
        except ValueError:
            valid = False
            break
    if not valid:
        create_files()


# ------------------------------------------------------------
# 3. Чтение инвентаря и изменений
# ------------------------------------------------------------
def read_inventory(filename):
    """Возвращает словарь {ID: количество} из инвентарного файла."""
    inventory = {}
    for line in read_file(filename).strip().splitlines():
        parts = line.split()
        if len(parts) == 2:
            try:
                pid = int(parts[0])
                qty = int(parts[1])
                inventory[pid] = qty
            except ValueError:
                pass
    return inventory


def read_updates(filename):
    """Возвращает словарь {ID: суммарное_изменение} из файла изменений."""
    updates = defaultdict(int)
    for line in read_file(filename).strip().splitlines():
        parts = line.split()
        if len(parts) == 2:
            try:
                pid = int(parts[0])
                change = int(parts[1])
                updates[pid] += change
            except ValueError:
                pass
    return dict(updates)


# ------------------------------------------------------------
# 4. Обновление инвентаря
# ------------------------------------------------------------
def update_inventory(inventory, updates):
    """
    Применяет суммарные изменения к инвентарю.
    Возвращает обновлённый словарь {ID: количество}.
    """
    updated = inventory.copy()
    for pid, change in updates.items():
        if pid in updated:
            updated[pid] += change
        else:
            updated[pid] = change  # новый продукт на складе
    return updated


# ------------------------------------------------------------
# 5. Основная программа
# ------------------------------------------------------------
def main():
    print("Задача 516: Обновление инвентарного файла")
    ensure_files_exist()

    inventory = read_inventory("f1.txt")
    updates = read_updates("f2.txt")

    print("\nИсходный инвентарь (f1.txt):")
    for pid, qty in sorted(inventory.items()):
        print(f"   Продукт {pid}: {qty} шт.")

    print("\nИзменения (f2.txt):")
    if updates:
        for pid, change in sorted(updates.items()):
            print(f"   Продукт {pid}: {'+' if change >= 0 else ''}{change} шт.")
    else:
        print("   (нет изменений)")

    # Обновление
    new_inventory = update_inventory(inventory, updates)

    # Запись в g.txt
    lines = [f"{pid} {qty}" for pid, qty in sorted(new_inventory.items())]
    create_text_file("g.txt", "\n".join(lines))

    print("\nОбновлённый инвентарь (g.txt):")
    for pid, qty in sorted(new_inventory.items()):
        print(f"   Продукт {pid}: {qty} шт.")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")