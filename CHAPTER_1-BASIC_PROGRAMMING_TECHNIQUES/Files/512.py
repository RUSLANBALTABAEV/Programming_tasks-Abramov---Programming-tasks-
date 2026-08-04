"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

512. Дан файл f1, который содержит номера телефонов сотрудников учреждения: указывается фамилия, его инициалы и номер телефона. Найти телефон сотрудника по его фамилии и инициалам.
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
# 2. Создание исходного файла f1 (если отсутствует или пуст)
# ------------------------------------------------------------
def create_file_f1(filename):
    """Создаёт файл f1 с данными о сотрудниках и их телефонах."""
    print("Файл f1 не существует или пуст. Задайте данные о сотрудниках.")
    print("Формат строки: Фамилия И.О. Номер_телефона")
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
                print("  Ошибка: нужно минимум три поля (фамилия, инициалы, телефон).")
                continue
            # Проверим, что последнее поле похоже на телефон (содержит цифры и дефисы)
            phone = parts[-1]
            if not any(ch.isdigit() for ch in phone):
                print("  Предупреждение: телефон должен содержать цифры.")
            lines.append(line)
        if not lines:
            print("Не введено ни одной строки. Будет использован готовый пример.")
            text = ("Иванов И.И. 123-45-67\n"
                    "Петров П.П. 890-12-34\n"
                    "Сидоров С.С. 567-89-01\n"
                    "Кузнецов К.К. 234-56-78\n"
                    "Смирнов А.Б. 901-23-45")
        else:
            text = "\n".join(lines)
    elif choice == '2':
        surnames = ["Иванов", "Петров", "Сидоров", "Кузнецов", "Смирнов",
                    "Попов", "Васильев", "Михайлов", "Новиков", "Федоров"]
        # генерируем инициалы случайно
        letters = "АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЭЮЯ"
        n = random.randint(5, 12)  # количество записей
        lines = []
        for _ in range(n):
            surname = random.choice(surnames)
            # инициалы: два случайных символа с точками
            initials = random.choice(letters) + '.' + random.choice(letters) + '.'
            # телефон в формате XXX-XX-XX
            phone = f"{random.randint(100,999)}-{random.randint(10,99)}-{random.randint(10,99)}"
            lines.append(f"{surname} {initials} {phone}")
        text = "\n".join(lines)
        print(f"Сгенерировано {n} записей о сотрудниках.")
    else:  # готовый пример
        text = ("Иванов И.И. 123-45-67\n"
                "Петров П.П. 890-12-34\n"
                "Сидоров С.С. 567-89-01\n"
                "Кузнецов К.К. 234-56-78\n"
                "Смирнов А.Б. 901-23-45")
        print("Использован готовый пример (5 сотрудников).")

    create_text_file(filename, text)
    print(f"Данные записаны в '{filename}'.")


def ensure_file_exists(filename):
    """Проверяет, существует ли файл и содержит ли данные. Если нет – создаёт."""
    if not os.path.exists(filename):
        create_file_f1(filename)
        return
    content = read_file(filename).strip()
    if not content:
        create_file_f1(filename)
        return
    # Проверим наличие хотя бы одной корректной записи
    lines = content.splitlines()
    has_valid = False
    for line in lines:
        parts = line.split()
        if len(parts) >= 3:
            # Проверим, что последнее поле содержит цифры (признак телефона)
            if any(ch.isdigit() for ch in parts[-1]):
                has_valid = True
                break
    if not has_valid:
        print("Файл не содержит корректных записей о сотрудниках.")
        create_file_f1(filename)


# ------------------------------------------------------------
# 3. Чтение данных о сотрудниках из файла
# ------------------------------------------------------------
def normalize_initials(initials):
    """Приводит инициалы к каноническому виду для сравнения: заглавные буквы без точек и пробелов."""
    return initials.replace(' ', '').replace('.', '').upper()


def read_phonebook(filename):
    """
    Возвращает список словарей с ключами:
        surname, initials, normalized_initials, phone
    """
    employees = []
    for line in read_file(filename).strip().splitlines():
        parts = line.split()
        if len(parts) >= 3:
            surname = parts[0]
            phone = parts[-1]
            initials = ' '.join(parts[1:-1])
            normalized = normalize_initials(initials)
            employees.append({
                'surname': surname,
                'initials': initials,
                'normalized_initials': normalized,
                'phone': phone
            })
    return employees


# ------------------------------------------------------------
# 4. Поиск телефона сотрудника
# ------------------------------------------------------------
def find_phone(employees, surname, initials):
    """
    Возвращает номер телефона, если найден сотрудник с указанной
    фамилией и инициалами, иначе None.
    """
    target = normalize_initials(initials)
    for emp in employees:
        if emp['surname'].lower() == surname.lower() and emp['normalized_initials'] == target:
            return emp['phone']
    return None


# ------------------------------------------------------------
# 5. Основная программа
# ------------------------------------------------------------
def main():
    print("Задача 512: Телефонный справочник")
    file_f1 = "f1.txt"

    ensure_file_exists(file_f1)
    employees = read_phonebook(file_f1)

    if not employees:
        print("Нет данных для обработки.")
        return

    print(f"\nВсего записей: {len(employees)}")
    print("Примеры записей:")
    for emp in employees[:5]:
        print(f"   {emp['surname']} {emp['initials']} – {emp['phone']}")
    if len(employees) > 5:
        print("   ...")

    # Запрос фамилии и инициалов
    surname = input("\nВведите фамилию: ").strip()
    initials = input("Введите инициалы (например, И.И. или ИИ): ").strip()

    phone = find_phone(employees, surname, initials)
    if phone:
        print(f"Телефон: {phone}")
    else:
        print("Сотрудник с такими данными не найден.")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")