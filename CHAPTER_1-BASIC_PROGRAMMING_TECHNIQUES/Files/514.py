"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

514. Дан файл f, содержащий сведения о веществах: указывается название вещества, его удельный вес и проводимость (проводника, полупроводник, изолятор).
а) Найти удельные веса и названия всех полупроводников.
б) Выбрать данные о проводниках и упорядочить их по убыванию удельных весов.
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
    """Создаёт файл f со сведениями о веществах."""
    print("Файл f не существует или пуст. Задайте данные о веществах.")
    print("Формат строки: Название Удельный_вес Проводимость")
    print("Проводимость: проводник, полупроводник, изолятор")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод (пустая строка — конец)")
    print("2 — Случайная генерация")
    print("3 — Готовый пример")

    while True:
        choice = input("Ваш выбор (1/2/3): ").strip()
        if choice in ('1', '2', '3'):
            break
        print("Ошибка: выберите 1, 2 или 3.")

    valid_conductivity = {'проводник', 'полупроводник', 'изолятор'}

    if choice == '1':
        print("Вводите по одной строке. Для завершения — пустая строка.")
        lines = []
        while True:
            line = input().strip()
            if line == "":
                break
            parts = line.split()
            if len(parts) != 3:
                print("  Ошибка: нужно три поля (название, удельный вес, проводимость).")
                continue
            try:
                weight = float(parts[1])
                if weight <= 0:
                    print("  Ошибка: удельный вес должен быть положительным.")
                    continue
            except ValueError:
                print("  Ошибка: удельный вес должен быть числом.")
                continue
            if parts[2] not in valid_conductivity:
                print(f"  Ошибка: проводимость должна быть одной из {valid_conductivity}.")
                continue
            lines.append(line)
        if not lines:
            print("Не введено ни одной строки. Будет использован готовый пример.")
            text = ("Кремний 2.33 полупроводник\nГерманий 5.32 полупроводник\n"
                    "Арсенид_галлия 5.32 полупроводник\nМедь 8.96 проводник\n"
                    "Алюминий 2.71 проводник\nСеребро 10.49 проводник\n"
                    "Железо 7.87 проводник\nСтекло 2.50 изолятор\n"
                    "Резина 1.20 изолятор\nПарафин 0.90 изолятор")
        else:
            text = "\n".join(lines)
    elif choice == '2':
        substances_pool = [
            ("Кремний", 2.33, "полупроводник"),
            ("Германий", 5.32, "полупроводник"),
            ("Арсенид_галлия", 5.32, "полупроводник"),
            ("Медь", 8.96, "проводник"),
            ("Алюминий", 2.71, "проводник"),
            ("Серебро", 10.49, "проводник"),
            ("Железо", 7.87, "проводник"),
            ("Стекло", 2.50, "изолятор"),
            ("Резина", 1.20, "изолятор"),
            ("Парафин", 0.90, "изолятор"),
            ("Графит", 2.25, "полупроводник"),
            ("Золото", 19.32, "проводник"),
            ("Фарфор", 2.30, "изолятор")
        ]
        n = random.randint(6, 12)
        lines = []
        for _ in range(n):
            name, weight, conductivity = random.choice(substances_pool)
            lines.append(f"{name} {weight} {conductivity}")
        text = "\n".join(lines)
        print(f"Сгенерировано {n} записей о веществах.")
    else:  # готовый пример
        text = ("Кремний 2.33 полупроводник\nГерманий 5.32 полупроводник\n"
                "Арсенид_галлия 5.32 полупроводник\nМедь 8.96 проводник\n"
                "Алюминий 2.71 проводник\nСеребро 10.49 проводник\n"
                "Железо 7.87 проводник\nСтекло 2.50 изолятор\n"
                "Резина 1.20 изолятор\nПарафин 0.90 изолятор")
        print("Использован готовый пример (10 веществ).")

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
    # Проверим наличие хотя бы одной корректной записи
    lines = content.splitlines()
    has_valid = False
    for line in lines:
        parts = line.split()
        if len(parts) == 3:
            try:
                float(parts[1])
                if parts[2] in {'проводник', 'полупроводник', 'изолятор'}:
                    has_valid = True
                    break
            except ValueError:
                pass
    if not has_valid:
        print("Файл не содержит корректных записей о веществах.")
        create_file_f(filename)


# ------------------------------------------------------------
# 3. Чтение веществ из файла
# ------------------------------------------------------------
def read_substances(filename):
    """Возвращает список словарей с ключами name, weight, conductivity."""
    substances = []
    for line in read_file(filename).strip().splitlines():
        parts = line.split()
        if len(parts) == 3:
            try:
                weight = float(parts[1])
                conductivity = parts[2]
                if weight > 0 and conductivity in {'проводник', 'полупроводник', 'изолятор'}:
                    substances.append({
                        'name': parts[0],
                        'weight': weight,
                        'conductivity': conductivity
                    })
            except ValueError:
                pass
    return substances


# ------------------------------------------------------------
# 4. Решения пунктов а) и б)
# ------------------------------------------------------------
def solve_a(substances):
    """Вывод полупроводников: название и удельный вес."""
    semiconductors = [s for s in substances if s['conductivity'] == 'полупроводник']
    print("\nа) Полупроводники (название и удельный вес):")
    if semiconductors:
        for s in semiconductors:
            print(f"   {s['name']}: {s['weight']} г/см³")
    else:
        print("   Полупроводников не найдено.")


def solve_b(substances):
    """Вывод проводников, упорядоченных по убыванию удельного веса."""
    conductors = [s for s in substances if s['conductivity'] == 'проводник']
    sorted_conductors = sorted(conductors, key=lambda x: x['weight'], reverse=True)
    print("\nб) Проводники (по убыванию удельного веса):")
    if sorted_conductors:
        for s in sorted_conductors:
            print(f"   {s['name']}: {s['weight']} г/см³")
    else:
        print("   Проводников не найдено.")


# ------------------------------------------------------------
# 5. Основная программа
# ------------------------------------------------------------
def main():
    print("Задача 514: Сведения о веществах")
    file_f = "f.txt"

    ensure_file_exists(file_f)
    substances = read_substances(file_f)

    if not substances:
        print("Нет данных для обработки.")
        return

    print(f"\nВсего записей: {len(substances)}")
    print("Примеры записей:")
    for s in substances[:5]:
        print(f"   {s['name']}: вес {s['weight']}, проводимость: {s['conductivity']}")
    if len(substances) > 5:
        print("   ...")

    solve_a(substances)
    solve_b(substances)


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")