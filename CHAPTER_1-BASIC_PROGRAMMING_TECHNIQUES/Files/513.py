"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

513. Дан файл f, содержащий сведения о кубиках: размер каждого кубика (длина ребра в сантиметрах), его цвет (красный, желтый, зеленый или синий) и материал (деревянный, металлический, картонный). Найти:
а) количество кубиков каждого из перечисленных цветов и их суммарный объем;
б) количество деревянных кубиков с ребром 3 см и количество металлических кубиков с ребром, большим 5 см.
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
    """Создаёт файл f со сведениями о кубиках."""
    print("Файл f не существует или пуст. Задайте данные о кубиках.")
    print("Формат строки: длина_ребра цвет материал")
    print("Цвета: красный, желтый, зеленый, синий")
    print("Материалы: деревянный, металлический, картонный")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод (пустая строка — конец)")
    print("2 — Случайная генерация")
    print("3 — Готовый пример")

    while True:
        choice = input("Ваш выбор (1/2/3): ").strip()
        if choice in ('1', '2', '3'):
            break
        print("Ошибка: выберите 1, 2 или 3.")

    valid_colors = {'красный', 'желтый', 'зеленый', 'синий'}
    valid_materials = {'деревянный', 'металлический', 'картонный'}

    if choice == '1':
        print("Вводите по одной строке. Для завершения — пустая строка.")
        lines = []
        while True:
            line = input().strip()
            if line == "":
                break
            parts = line.split()
            if len(parts) != 3:
                print("  Ошибка: нужно три поля (ребро, цвет, материал).")
                continue
            try:
                edge = float(parts[0])
                if edge <= 0:
                    print("  Ошибка: длина ребра должна быть положительной.")
                    continue
            except ValueError:
                print("  Ошибка: длина ребра должна быть числом.")
                continue
            if parts[1] not in valid_colors:
                print(f"  Ошибка: цвет должен быть одним из {valid_colors}")
                continue
            if parts[2] not in valid_materials:
                print(f"  Ошибка: материал должен быть одним из {valid_materials}")
                continue
            lines.append(line)
        if not lines:
            print("Не введено ни одной строки. Будет использован готовый пример.")
            text = ("3 красный деревянный\n5 красный металлический\n"
                    "3 синий деревянный\n4 желтый картонный\n"
                    "6 красный металлический\n3 зеленый деревянный\n"
                    "7 зеленый металлический\n3 красный картонный\n"
                    "6 синий металлический\n3 желтый деревянный\n"
                    "5 синий деревянный\n4 красный металлический\n"
                    "8 желтый металлический")
        else:
            text = "\n".join(lines)
    elif choice == '2':
        n = random.randint(8, 15)
        colors = list(valid_colors)
        materials = list(valid_materials)
        lines = []
        for _ in range(n):
            # случайная длина ребра от 1 до 10 (целые или с десятыми)
            edge = round(random.uniform(1.0, 10.0), 1)
            color = random.choice(colors)
            material = random.choice(materials)
            lines.append(f"{edge} {color} {material}")
        text = "\n".join(lines)
        print(f"Сгенерировано {n} записей о кубиках.")
    else:  # готовый пример
        text = ("3 красный деревянный\n5 красный металлический\n"
                "3 синий деревянный\n4 желтый картонный\n"
                "6 красный металлический\n3 зеленый деревянный\n"
                "7 зеленый металлический\n3 красный картонный\n"
                "6 синий металлический\n3 желтый деревянный\n"
                "5 синий деревянный\n4 красный металлический\n"
                "8 желтый металлический")
        print("Использован готовый пример (13 кубиков).")

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
                float(parts[0])
                if parts[1] in {'красный', 'желтый', 'зеленый', 'синий'} and \
                   parts[2] in {'деревянный', 'металлический', 'картонный'}:
                    has_valid = True
                    break
            except ValueError:
                pass
    if not has_valid:
        print("Файл не содержит корректных записей о кубиках.")
        create_file_f(filename)


# ------------------------------------------------------------
# 3. Чтение кубиков из файла
# ------------------------------------------------------------
def read_cubes(filename):
    """Возвращает список словарей с ключами edge, color, material."""
    cubes = []
    for line in read_file(filename).strip().splitlines():
        parts = line.split()
        if len(parts) == 3:
            try:
                edge = float(parts[0])
                color = parts[1]
                material = parts[2]
                if edge > 0 and color in {'красный', 'желтый', 'зеленый', 'синий'} \
                        and material in {'деревянный', 'металлический', 'картонный'}:
                    cubes.append({'edge': edge, 'color': color, 'material': material})
            except ValueError:
                pass
    return cubes


# ------------------------------------------------------------
# 4. Решения пунктов а) и б)
# ------------------------------------------------------------
def solve_a(cubes):
    """Количество кубиков каждого цвета и суммарный объём."""
    colors = ['красный', 'желтый', 'зеленый', 'синий']
    count = {c: 0 for c in colors}
    volume = {c: 0.0 for c in colors}
    for cube in cubes:
        c = cube['color']
        count[c] += 1
        volume[c] += cube['edge'] ** 3
    print("\nа) Кубики по цветам:")
    for c in colors:
        print(f"   {c}: {count[c]} шт., суммарный объём: {volume[c]:.2f} куб. см")


def solve_b(cubes):
    """Деревянные с ребром 3 см и металлические с ребром > 5 см."""
    wooden_3 = sum(1 for c in cubes if c['material'] == 'деревянный' and c['edge'] == 3.0)
    metal_gt5 = sum(1 for c in cubes if c['material'] == 'металлический' and c['edge'] > 5.0)
    print("\nб) Специальные кубики:")
    print(f"   Деревянных с ребром 3 см: {wooden_3}")
    print(f"   Металлических с ребром > 5 см: {metal_gt5}")


# ------------------------------------------------------------
# 5. Основная программа
# ------------------------------------------------------------
def main():
    print("Задача 513: Сведения о кубиках")
    file_f = "f.txt"

    ensure_file_exists(file_f)
    cubes = read_cubes(file_f)

    if not cubes:
        print("Нет данных для обработки.")
        return

    print(f"\nВсего записей: {len(cubes)}")
    print("Примеры записей:")
    for cube in cubes[:5]:
        print(f"   Ребро: {cube['edge']}, цвет: {cube['color']}, материал: {cube['material']}")
    if len(cubes) > 5:
        print("   ...")

    solve_a(cubes)
    solve_b(cubes)


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")