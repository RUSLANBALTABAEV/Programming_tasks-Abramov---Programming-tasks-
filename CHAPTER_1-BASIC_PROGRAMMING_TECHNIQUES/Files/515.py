"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

515. Дан файл f, содержащий сведения об экспортируемых товарах: указывается наименование товара, страна, импортирующая товар, и объем поставляемой партии в штуках. Найти страны, в которые экспортируется данный товар, и общий объем его экспорта.
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
    """Создаёт файл f со сведениями об экспорте товаров."""
    print("Файл f не существует или пуст. Задайте данные об экспорте.")
    print("Формат строки: Наименование_товара Страна Количество")
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
            if len(parts) < 3:
                print("  Ошибка: нужно минимум три поля (товар, страна, количество).")
                continue
            try:
                quantity = int(parts[-1])
                if quantity <= 0:
                    print("  Ошибка: количество должно быть положительным целым числом.")
                    continue
            except ValueError:
                print("  Ошибка: последнее поле должно быть целым числом (количество).")
                continue
            lines.append(line)
        if not lines:
            print("Не введено ни одной строки. Будет использован готовый пример.")
            text = ("Яблоки Соединенные Штаты 150\nЯблоки Германия 200\n"
                    "Бананы Великобритания 120\nЯблоки Канада 50\n"
                    "Апельсины Франция 300\nЯблоки Соединенные Штаты 75\n"
                    "Бананы Австралия 90\nАпельсины Германия 250")
        else:
            text = "\n".join(lines)
    elif choice == '2':
        goods = ["Яблоки", "Бананы", "Апельсины", "Груши", "Виноград",
                 "Мандарины", "Томаты", "Огурцы"]
        countries = ["Россия", "Соединенные Штаты", "Германия", "Франция",
                     "Великобритания", "Канада", "Австралия", "Италия"]
        n = random.randint(6, 12)
        lines = []
        for _ in range(n):
            goods_name = random.choice(goods)
            country = random.choice(countries)
            quantity = random.randint(10, 500)
            lines.append(f"{goods_name} {country} {quantity}")
        text = "\n".join(lines)
        print(f"Сгенерировано {n} записей об экспорте.")
    else:  # готовый пример
        text = ("Яблоки Соединенные Штаты 150\nЯблоки Германия 200\n"
                "Бананы Великобритания 120\nЯблоки Канада 50\n"
                "Апельсины Франция 300\nЯблоки Соединенные Штаты 75\n"
                "Бананы Австралия 90\nАпельсины Германия 250")
        print("Использован готовый пример (8 записей).")

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
        if len(parts) >= 3:
            try:
                int(parts[-1])
                has_valid = True
                break
            except ValueError:
                pass
    if not has_valid:
        print("Файл не содержит корректных записей об экспорте.")
        create_file_f(filename)


# ------------------------------------------------------------
# 3. Чтение записей экспорта из файла
# ------------------------------------------------------------
def read_exports(filename):
    """
    Возвращает список словарей с ключами:
        product, country, quantity
    """
    records = []
    for line in read_file(filename).strip().splitlines():
        parts = line.split()
        if len(parts) >= 3:
            try:
                quantity = int(parts[-1])
                product = parts[0]
                country = ' '.join(parts[1:-1])
                if quantity > 0:
                    records.append({
                        'product': product,
                        'country': country,
                        'quantity': quantity
                    })
            except ValueError:
                pass
    return records


# ------------------------------------------------------------
# 4. Поиск экспорта по товару
# ------------------------------------------------------------
def find_export_by_product(records, target_product):
    """
    Возвращает кортеж (список стран, общий объём).
    """
    filtered = [r for r in records if r['product'].lower() == target_product.lower()]
    if not filtered:
        return [], 0
    # Уникальные страны в порядке появления
    unique_countries = list(dict.fromkeys(r['country'] for r in filtered))
    total_volume = sum(r['quantity'] for r in filtered)
    return unique_countries, total_volume


# ------------------------------------------------------------
# 5. Основная программа
# ------------------------------------------------------------
def main():
    print("Задача 515: Экспорт товаров")
    file_f = "f.txt"

    ensure_file_exists(file_f)
    records = read_exports(file_f)

    if not records:
        print("Нет данных для обработки.")
        return

    print(f"\nВсего записей: {len(records)}")
    print("Примеры записей:")
    for r in records[:5]:
        print(f"   {r['product']} -> {r['country']} : {r['quantity']} шт.")
    if len(records) > 5:
        print("   ...")

    target = input("\nВведите наименование товара: ").strip()
    countries, total = find_export_by_product(records, target)

    print(f"\nТовар: '{target}'")
    if countries:
        print(f"Страны-импортёры: {', '.join(countries)}")
        print(f"Общий объём экспорта: {total} шт.")
    else:
        print("Информация о данном товаре не найдена.")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")