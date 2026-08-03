"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

507. Сведения об ученике состоят из его имени и фамилии и названия класса (года обучения и буквы), в котором он учится. Дан файл f, содержащий сведения об учениках школы. 
а) Выяснить, имеются ли в школе однофамильцы.
б) Выяснить, имеются ли однофамильцы в каких-либо параллельных классах.
в) Выяснить, имеются ли однофамильцы в каком-нибудь классе.
г) Ответить на вопросы а) – в), но в отношении учеников, у которых совпадают и имя, и фамилия.
д) Выяснить, в каких классах насчитывается более 35 учащихся.
е) Выяснить, насколько человек в восьмых классах больше, чем в десятых.
ж) Собрать в файле g сведения об учениках 9-х и 10-х классов, поместив вначале сведения об учениках класса 9а, затем 9б и т. д., затем 10а, 10б и т. д.
з) Получить список учеников данного класса по следующим образцам: 
фамилия _ имя
фамилия _ и.
и. _ фамилия
"""


import random
import os
from collections import defaultdict


# ------------------------------------------------------------
# 1. Процедуры работы с файлами (как в задаче 506)
# ------------------------------------------------------------
def create_text_file(filename, text):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)


def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()


# ------------------------------------------------------------
# 2. Создание исходного файла f (если отсутствует или пуст)
# ------------------------------------------------------------
def create_file_f(filename):
    print("Файл f не существует или пуст. Задайте данные об учениках.")
    print("Формат строки: Фамилия Имя Класс (например, Иванов Иван 9а)")
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
                print("  Ошибка: нужно три поля (Фамилия, Имя, Класс).")
                continue
            # Проверяем класс (например, 9а)
            cls = parts[2]
            if not (cls[:-1].isdigit() and cls[-1].isalpha()):
                print("  Ошибка: класс должен быть вида 9а.")
                continue
            lines.append(line)
        if not lines:
            print("Не введено ни одной строки. Будет использован готовый пример.")
            text = ("Иванов Иван 9а\nПетров Петр 9а\nСидоров Алексей 9а\n"
                    "Иванов Василий 9а\nПетров Сергей 9б\nСмирнов Дмитрий 9б\n"
                    "Смирнов Олег 10а\nИванов Николай 10а\nКузнецов Антон 10а\n"
                    "Смирнов Илья 10б\nСмирнов Павел 10б\nДмитриев Виктор 10б\n"
                    "Иванов Алексей 8а\nСидоров Михаил 8а\nПетров Игорь 8б\n"
                    "Смирнов Станислав 8б\nИванов Иван 11а")
        else:
            text = "\n".join(lines)
    elif choice == '2':
        # Случайная генерация: фамилии из списка, имена, классы
        surnames = ["Иванов", "Петров", "Сидоров", "Смирнов", "Кузнецов",
                    "Попов", "Васильев", "Михайлов", "Новиков", "Федоров"]
        names = ["Иван", "Петр", "Алексей", "Сергей", "Дмитрий", "Олег",
                 "Николай", "Павел", "Виктор", "Михаил", "Илья", "Андрей"]
        grades = [1,2,3,4,5,6,7,8,9,10,11]
        letters = ['а','б','в','г']
        count = random.randint(20, 40)  # от 20 до 40 учеников
        students = []
        for _ in range(count):
            surname = random.choice(surnames)
            name = random.choice(names)
            grade = random.choice(grades)
            letter = random.choice(letters)
            students.append(f"{surname} {name} {grade}{letter}")
        text = "\n".join(students)
        print(f"Сгенерировано {count} записей об учениках.")
    else:  # готовый пример
        text = ("Иванов Иван 9а\nПетров Петр 9а\nСидоров Алексей 9а\n"
                "Иванов Василий 9а\nПетров Сергей 9б\nСмирнов Дмитрий 9б\n"
                "Смирнов Олег 10а\nИванов Николай 10а\nКузнецов Антон 10а\n"
                "Смирнов Илья 10б\nСмирнов Павел 10б\nДмитриев Виктор 10б\n"
                "Иванов Алексей 8а\nСидоров Михаил 8а\nПетров Игорь 8б\n"
                "Смирнов Станислав 8б\nИванов Иван 11а")
        print("Использован готовый пример (17 учеников).")

    create_text_file(filename, text)
    print(f"Данные записаны в '{filename}'.")


def ensure_file_exists(filename):
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
            cls = parts[2]
            if cls[:-1].isdigit() and cls[-1].isalpha():
                has_valid = True
                break
    if not has_valid:
        print("Файл не содержит корректных записей об учениках.")
        create_file_f(filename)


# ------------------------------------------------------------
# 3. Чтение учеников из файла
# ------------------------------------------------------------
def read_students(filename):
    students = []
    for line in read_file(filename).strip().splitlines():
        parts = line.split()
        if len(parts) == 3:
            surname, name, cls = parts
            try:
                grade = int(cls[:-1])
                letter = cls[-1]
                students.append((surname, name, grade, letter))
            except ValueError:
                pass
    return students


# ------------------------------------------------------------
# 4. Решения задач а) – з)
# ------------------------------------------------------------
def task_a(students):
    surname_groups = defaultdict(list)
    for surname, name, _, _ in students:
        surname_groups[surname].append(name)
    duplicates = {s: n for s, n in surname_groups.items() if len(n) > 1}
    return len(duplicates) > 0, duplicates

def task_b(students):
    surname_parallels = defaultdict(set)
    for surname, _, grade, _ in students:
        surname_parallels[surname].add(grade)
    in_parallel = {s: sorted(list(g)) for s, g in surname_parallels.items() if len(g) > 1}
    return len(in_parallel) > 0, in_parallel

def task_c(students):
    class_groups = defaultdict(list)
    for surname, _, grade, letter in students:
        class_groups[(grade, letter)].append(surname)
    result = {}
    for (grade, letter), surnames in class_groups.items():
        surname_count = defaultdict(int)
        for s in surnames:
            surname_count[s] += 1
        duplicates_in_class = {s: c for s, c in surname_count.items() if c > 1}
        if duplicates_in_class:
            result[f"{grade}{letter}"] = duplicates_in_class
    return len(result) > 0, result

def task_d(students):
    name_groups = defaultdict(list)
    for surname, name, grade, letter in students:
        name_groups[(surname, name)].append((grade, letter))
    full_duplicates_all = {k: v for k, v in name_groups.items() if len(v) > 1}
    has_any = len(full_duplicates_all) > 0
    full_duplicates_parallel = {}
    for (surname, name), classes in full_duplicates_all.items():
        grades = {g for g, _ in classes}
        if len(grades) > 1:
            full_duplicates_parallel[(surname, name)] = sorted(list(grades))
    full_duplicates_single_class = {}
    for (surname, name), classes in full_duplicates_all.items():
        if len(classes) > 1:
            class_counts = defaultdict(int)
            for gr, lt in classes:
                class_counts[(gr, lt)] += 1
            for (gr, lt), count in class_counts.items():
                if count > 1:
                    full_duplicates_single_class[f"{surname} {name}"] = f"{gr}{lt}"
    return has_any, full_duplicates_all, full_duplicates_parallel, full_duplicates_single_class

def task_e(students):
    class_counts = defaultdict(int)
    for _, _, grade, letter in students:
        class_counts[(grade, letter)] += 1
    return [f"{g}{l}" for (g, l), count in class_counts.items() if count > 35]

def task_f(students):
    eighth = sum(1 for _, _, g, _ in students if g == 8)
    tenth = sum(1 for _, _, g, _ in students if g == 10)
    return eighth - tenth, eighth, tenth

def task_g(students, filename):
    filtered = [s for s in students if s[2] in (9, 10)]
    filtered.sort(key=lambda x: (x[2], x[3]))
    lines = [f"{surname} {name} {grade}{letter}" for surname, name, grade, letter in filtered]
    create_text_file(filename, "\n".join(lines))
    return filtered

def task_h(students):
    target = input("\nВведите название класса для списка (например, 9а): ").strip()
    if len(target) < 2:
        print("Некорректный ввод.")
        return
    try:
        g = int(target[:-1])
        l = target[-1]
    except ValueError:
        print("Некорректный формат класса.")
        return
    class_students = [(s, n) for s, n, gr, lt in students if gr == g and lt == l]
    if not class_students:
        print(f"Учеников в классе {target} не найдено.")
        return
    print(f"\nСписок класса {target}:")
    print("1) фамилия _ имя")
    for s, n in class_students:
        print(f"   {s} _ {n}")
    print("\n2) фамилия _ и.")
    for s, n in class_students:
        print(f"   {s} _ {n[0]}.")
    print("\n3) и. _ фамилия")
    for s, n in class_students:
        print(f"   {n[0]}. _ {s}")


# ------------------------------------------------------------
# 5. Основная программа
# ------------------------------------------------------------
def main():
    print("Задача 507: Сведения об учениках")
    file_f = "f.txt"
    file_g = "g.txt"

    ensure_file_exists(file_f)
    students = read_students(file_f)
    if not students:
        print("Нет данных для обработки.")
        return

    print(f"Всего записей об учениках: {len(students)}\n")

    # а)
    has_a, dup_a = task_a(students)
    print(f"а) Однофамильцы в школе: {'ДА' if has_a else 'НЕТ'}")
    if has_a:
        print("   Фамилии с повторами:", ", ".join(f"{s} ({len(n)})" for s, n in dup_a.items()))

    # б)
    has_b, dup_b = task_b(students)
    print(f"\nб) Однофамильцы в параллельных классах: {'ДА' if has_b else 'НЕТ'}")
    if has_b:
        print("   Фамилии в разных параллелях:", ", ".join(f"{s} в {g}" for s, g in dup_b.items()))

    # в)
    has_c, dup_c = task_c(students)
    print(f"\nв) Однофамильцы в одном классе: {'ДА' if has_c else 'НЕТ'}")
    if has_c:
        for cls, dup_map in dup_c.items():
            print(f"   Класс {cls}:", ", ".join(f"{s} ({c})" for s, c in dup_map.items()))

    # г)
    has_d, all_d, parallel_d, class_d = task_d(students)
    print(f"\nг) Полные тёзки:")
    print(f"   По школе: {'ДА' if has_d else 'НЕТ'}")
    if has_d:
        print("     Тёзки:", ", ".join(f"{s} {n}" for (s,n) in all_d))
        print(f"   В параллелях: {'ДА' if parallel_d else 'НЕТ'}")
        if parallel_d:
            for (s,n), g_list in parallel_d.items():
                print(f"     {s} {n} в параллелях {g_list}")
        print(f"   В одном классе: {'ДА' if class_d else 'НЕТ'}")
        if class_d:
            for name, cls in class_d.items():
                print(f"     {name} в {cls}")

    # д)
    large_classes = task_e(students)
    print(f"\nд) Классы с >35 учащимися: {large_classes if large_classes else 'отсутствуют'}")

    # е)
    diff, e_cnt, t_cnt = task_f(students)
    print(f"\nе) В 8-х классах: {e_cnt}, в 10-х: {t_cnt}. "
          f"Разница: {'+' if diff > 0 else ''}{diff} человек.")

    # ж)
    task_g(students, file_g)
    print(f"\nж) Сведения о 9-х и 10-х классах записаны в '{file_g}'.")

    # з)
    task_h(students)


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")