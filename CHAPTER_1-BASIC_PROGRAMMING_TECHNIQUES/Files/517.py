"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

517. Дан файл f, содержащий сведения об игрушках: указывается название игрушки (например, кукла, кубики, мяч, конструктор и т. д.), ее стоимость в копейках и возрастные границы детей, для которых игрушка предназначена (например, для детей от двух до пяти лет). Получить следующие сведения:
а) названия игрушек, цена которых не превышает 4 руб. и которые подходят детям 5 лет;
б) цену самого дорогого конструктора, оформленную по образцу … руб. …коп.;
в) названия наиболее дорогих игрушек (цена которых отличается от цены самой дорогой игрушки не более чем на 1 руб.);
г) названия игрушек, которые подходят как детям 4 лет, так и детям 10 лет;
д) цены всех кубиков, оформленные по образцу, указанному в б);
е) можно ли подобрать игрушку, любую, кроме мяча, подходящую ребенку 3 лет, и дополнительно мяч так, чтобы суммарная стоимость игрушек не превосходила 5 руб.?;
ж) имеется ли мяч ценой 2 руб. 50 коп., предназначенный детям от 3 до 8 лет?; если нет, занести сведения об этой игрушке в файл f.
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
    """Создаёт файл f со сведениями об игрушках."""
    print("Файл f не существует или пуст. Задайте данные об игрушках.")
    print("Формат строки: Название Цена_в_копейках Нижний_возраст Верхний_возраст")
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
            if len(parts) != 4:
                print("  Ошибка: нужно четыре поля (название, цена, возраст_от, возраст_до).")
                continue
            try:
                price = int(parts[1])
                age_low = int(parts[2])
                age_high = int(parts[3])
                if price <= 0 or age_low < 0 or age_high < age_low:
                    print("  Ошибка: цена должна быть положительной, возраст корректным.")
                    continue
            except ValueError:
                print("  Ошибка: цена и возраст должны быть целыми числами.")
                continue
            lines.append(line)
        if not lines:
            print("Не введено ни одной строки. Будет использован готовый пример.")
            text = ("Кукла 350 3 7\nМяч 250 3 8\nКубики 120 1 5\n"
                    "Конструктор 450 5 12\nКубики 180 2 6\nМяч 150 1 4\n"
                    "Пазл 300 4 12\nКонструктор 400 6 12")
        else:
            text = "\n".join(lines)
    elif choice == '2':
        names = ["Кукла", "Мяч", "Кубики", "Конструктор", "Пазл", "Машинка",
                 "Пирамидка", "Лото", "Домино", "Робот"]
        n = random.randint(6, 12)
        lines = []
        for _ in range(n):
            name = random.choice(names)
            price = random.randint(50, 2000)  # копейки, до 20 руб
            age_low = random.randint(0, 8)
            age_high = random.randint(age_low, 12)
            lines.append(f"{name} {price} {age_low} {age_high}")
        text = "\n".join(lines)
        print(f"Сгенерировано {n} записей об игрушках.")
    else:  # готовый пример
        text = ("Кукла 350 3 7\nМяч 250 3 8\nКубики 120 1 5\n"
                "Конструктор 450 5 12\nКубики 180 2 6\nМяч 150 1 4\n"
                "Пазл 300 4 12\nКонструктор 400 6 12")
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
        if len(parts) == 4:
            try:
                price = int(parts[1])
                age_low = int(parts[2])
                age_high = int(parts[3])
                if price > 0 and age_low >= 0 and age_high >= age_low:
                    has_valid = True
                    break
            except ValueError:
                pass
    if not has_valid:
        print("Файл не содержит корректных записей об игрушках.")
        create_file_f(filename)


# ------------------------------------------------------------
# 3. Чтение данных об игрушках
# ------------------------------------------------------------
def read_toys(filename):
    """Возвращает список словарей с ключами name, price, age_low, age_high."""
    toys = []
    for line in read_file(filename).strip().splitlines():
        parts = line.split()
        if len(parts) == 4:
            try:
                name = parts[0]
                price = int(parts[1])
                age_low = int(parts[2])
                age_high = int(parts[3])
                if price > 0 and age_low >= 0 and age_high >= age_low:
                    toys.append({
                        'name': name,
                        'price': price,
                        'age_low': age_low,
                        'age_high': age_high
                    })
            except ValueError:
                pass
    return toys


# ------------------------------------------------------------
# 4. Вспомогательные функции
# ------------------------------------------------------------
def format_price(kop):
    """Форматирует цену в копейках в вид 'X руб. Y коп.'"""
    return f"{kop // 100} руб. {kop % 100} коп."


def is_in_age(toy, age):
    """Проверяет, подходит ли игрушка ребёнку заданного возраста."""
    return toy['age_low'] <= age <= toy['age_high']


# ------------------------------------------------------------
# 5. Решения пунктов задания
# ------------------------------------------------------------
def task_a(toys):
    """а) Игрушки ≤ 400 коп, подходящие 5-летним."""
    result = [t for t in toys if t['price'] <= 400 and is_in_age(t, 5)]
    print("\nа) Игрушки не дороже 4 руб., подходящие детям 5 лет:")
    if result:
        for t in result:
            print(f"   {t['name']} ({format_price(t['price'])})")
    else:
        print("   Таких игрушек нет.")


def task_b(toys):
    """б) Цена самого дорогого конструктора."""
    constructors = [t for t in toys if t['name'].lower() == 'конструктор']
    if constructors:
        max_price = max(t['price'] for t in constructors)
        print(f"\nб) Самый дорогой конструктор стоит {format_price(max_price)}")
    else:
        print("\nб) Конструкторы не найдены.")


def task_c(toys):
    """в) Самые дорогие игрушки (отличаются от максимума не более чем на 1 руб.)."""
    if not toys:
        return
    max_price = max(t['price'] for t in toys)
    result = [t for t in toys if t['price'] >= max_price - 100]  # 1 руб = 100 коп
    print(f"\nв) Игрушки, цена которых отличается от максимальной ({format_price(max_price)}) не более чем на 1 руб.:")
    for t in result:
        print(f"   {t['name']} – {format_price(t['price'])}")


def task_d(toys):
    """г) Игрушки, подходящие одновременно и 4-летним, и 10-летним."""
    result = [t for t in toys if t['age_low'] <= 4 and t['age_high'] >= 10]
    print("\nг) Игрушки, подходящие детям и 4, и 10 лет:")
    if result:
        for t in result:
            print(f"   {t['name']} (от {t['age_low']} до {t['age_high']} лет)")
    else:
        print("   Таких игрушек нет.")


def task_d_price(toys):
    """д) Цены всех кубиков в формате руб./коп."""
    cubes = [t for t in toys if t['name'].lower() == 'кубики']
    print("\nд) Цены всех кубиков:")
    if cubes:
        for t in cubes:
            print(f"   {format_price(t['price'])}")
    else:
        print("   Кубики не найдены.")


def task_e(toys):
    """е) Можно ли подобрать пару: не мяч (для 3 лет) + мяч ≤ 5 руб."""
    balls = [t for t in toys if t['name'].lower() == 'мяч']
    if not balls:
        print("\nе) Мячей в файле нет – условие невыполнимо.")
        return
    min_ball = min(t['price'] for t in balls)

    others_3 = [t for t in toys if t['name'].lower() != 'мяч' and is_in_age(t, 3)]
    if not others_3:
        print("\nе) Нет игрушек, кроме мяча, подходящих 3-летним.")
        return
    min_other = min(t['price'] for t in others_3)

    total = min_ball + min_other
    print(f"\nе) Самый дешёвый мяч: {format_price(min_ball)}")
    print(f"   Самая дешёвая подходящая игрушка (не мяч): {format_price(min_other)}")
    print(f"   Сумма: {format_price(total)}")
    if total <= 500:
        print("   Ответ: ДА, можно подобрать пару не дороже 5 руб.")
    else:
        print("   Ответ: НЕТ, стоимость пары превышает 5 руб.")


def task_f(toys, filename):
    """ж) Проверка наличия мяча 2 руб. 50 коп. (3-8 лет), добавление при отсутствии."""
    target = {'name': 'Мяч', 'price': 250, 'age_low': 3, 'age_high': 8}
    found = any(t['name'].lower() == target['name'].lower() and
                t['price'] == target['price'] and
                t['age_low'] == target['age_low'] and
                t['age_high'] == target['age_high'] for t in toys)

    print(f"\nж) Мяч за {format_price(target['price'])} для детей {target['age_low']}-{target['age_high']} лет:")
    if found:
        print("   Такой мяч имеется в файле.")
    else:
        print("   Мяч отсутствует. Добавляю запись в файл.")
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(f"\n{target['name']} {target['price']} {target['age_low']} {target['age_high']}")
        print("   Запись добавлена.")


# ------------------------------------------------------------
# 6. Основная программа
# ------------------------------------------------------------
def main():
    print("Задача 517: Сведения об игрушках")
    file_f = "f.txt"

    ensure_file_exists(file_f)
    toys = read_toys(file_f)

    if not toys:
        print("Нет данных для обработки.")
        return

    print(f"\nВсего записей: {len(toys)}")
    print("Примеры записей:")
    for t in toys[:5]:
        print(f"   {t['name']} – {format_price(t['price'])}, возраст {t['age_low']}-{t['age_high']}")
    if len(toys) > 5:
        print("   ...")

    task_a(toys)
    task_b(toys)
    task_c(toys)
    task_d(toys)
    task_d_price(toys)
    task_e(toys)
    task_f(toys, file_f)


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")