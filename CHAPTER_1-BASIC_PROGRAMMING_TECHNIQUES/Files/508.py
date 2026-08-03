"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

508. Дан файл f, содержание те же самые сведения об учениках школы, что и в предыдущей задаче, и дополнительно отметки, полученные учениками в последней четверти.
а) Выяснить, сколько учеников школы не имеют отметок ниже четырех.
б) Собрать в файле g сведения о лучших учениках школы, т. е. об учениках, не имеющих отметок ниже четырех и по сумме баллов, не уступающих другим ученикам своего и параллельных классов.
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
# 2. Создание исходного файла f (если отсутствует или пуст)
# ------------------------------------------------------------
def create_file_f(filename):
    """Создаёт файл f с данными об учениках и их отметками."""
    print("Файл f не существует или пуст. Задайте данные об учениках и их отметках.")
    print("Формат строки: Фамилия Имя Класс Оценка1 Оценка2 ... (оценки через пробел)")
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
            if len(parts) < 4:
                print("  Ошибка: нужны как минимум фамилия, имя, класс и одна оценка.")
                continue
            cls = parts[2]
            if not (cls[:-1].isdigit() and cls[-1].isalpha()):
                print("  Ошибка: класс должен быть вида 9а.")
                continue
            try:
                grades = list(map(int, parts[3:]))
                for g in grades:
                    if not 1 <= g <= 5:
                        raise ValueError
            except ValueError:
                print("  Ошибка: оценки должны быть целыми числами от 1 до 5.")
                continue
            lines.append(line)
        if not lines:
            print("Не введено ни одной строки. Будет использован готовый пример.")
            text = ("Иванов Иван 9а 5 4 5 4 5\n"
                    "Петров Петр 9б 5 5 5 5 5\n"
                    "Сидоров Сидор 9а 3 4 5 4 5\n"
                    "Смирнов Илья 9в 5 5 4 4 5\n"
                    "Кузнецов Антон 10а 5 4 4 4 5\n"
                    "Дмитриев Виктор 10б 5 5 5 5 5\n"
                    "Васильев Николай 10а 4 4 4 4 5\n"
                    "Федоров Федор 11а 5 5 5 5 4")
        else:
            text = "\n".join(lines)
    elif choice == '2':
        surnames = ["Иванов", "Петров", "Сидоров", "Смирнов", "Кузнецов",
                    "Попов", "Васильев", "Михайлов", "Новиков", "Федоров"]
        names = ["Иван", "Петр", "Алексей", "Сергей", "Дмитрий", "Олег",
                 "Николай", "Павел", "Виктор", "Михаил", "Илья", "Андрей"]
        grades_pool = [1,2,3,4,5]
        num_students = random.randint(15, 30)
        lines = []
        for _ in range(num_students):
            surname = random.choice(surnames)
            name = random.choice(names)
            grade_num = random.randint(1, 11)
            letter = random.choice(['а','б','в','г'])
            cls = f"{grade_num}{letter}"
            # случайное количество оценок от 3 до 6
            num_grades = random.randint(3, 6)
            marks = [random.choice(grades_pool) for _ in range(num_grades)]
            lines.append(f"{surname} {name} {cls} " + " ".join(map(str, marks)))
        text = "\n".join(lines)
        print(f"Сгенерировано {num_students} записей об учениках.")
    else:  # готовый пример
        text = ("Иванов Иван 9а 5 4 5 4 5\n"
                "Петров Петр 9б 5 5 5 5 5\n"
                "Сидоров Сидор 9а 3 4 5 4 5\n"
                "Смирнов Илья 9в 5 5 4 4 5\n"
                "Кузнецов Антон 10а 5 4 4 4 5\n"
                "Дмитриев Виктор 10б 5 5 5 5 5\n"
                "Васильев Николай 10а 4 4 4 4 5\n"
                "Федоров Федор 11а 5 5 5 5 4")
        print("Использован готовый пример (8 учеников).")

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
        if len(parts) >= 4:
            cls = parts[2]
            if cls[:-1].isdigit() and cls[-1].isalpha():
                try:
                    int(parts[3])
                    has_valid = True
                    break
                except ValueError:
                    pass
    if not has_valid:
        print("Файл не содержит корректных записей об учениках с оценками.")
        create_file_f(filename)


# ------------------------------------------------------------
# 3. Чтение учеников из файла
# ------------------------------------------------------------
def read_students(filename):
    students = []
    for line in read_file(filename).strip().splitlines():
        parts = line.split()
        if len(parts) >= 4:
            surname = parts[0]
            name = parts[1]
            cls = parts[2]
            try:
                grade_num = int(cls[:-1])
                grades = list(map(int, parts[3:]))
                students.append({
                    'surname': surname,
                    'name': name,
                    'class': cls,
                    'grade_num': grade_num,
                    'grades': grades,
                    'total': sum(grades)
                })
            except ValueError:
                pass
    return students


# ------------------------------------------------------------
# 4. Решения подзадач а) и б)
# ------------------------------------------------------------
def solve_a(students):
    """Подсчёт учеников без отметок ниже 4."""
    count = sum(1 for s in students if s['grades'] and all(g >= 4 for g in s['grades']))
    print(f"\nа) Учеников без отметок ниже четырёх: {count}")
    return count


def solve_b(students, dest_filename):
    """
    Лучшие ученики: без отметок ниже 4 и с максимальной суммой в своей параллели.
    Результат записывается в dest_filename.
    """
    # отбираем тех, у кого все оценки ≥ 4
    excellent = [s for s in students if s['grades'] and all(g >= 4 for g in s['grades'])]

    if not excellent:
        print("б) Нет учеников без троек и двоек.")
        create_text_file(dest_filename, "")
        return []

    # группируем по параллелям
    by_parallel = defaultdict(list)
    for s in excellent:
        by_parallel[s['grade_num']].append(s)

    best = []
    for grade_num, group in by_parallel.items():
        max_sum = max(s['total'] for s in group)
        best.extend([s for s in group if s['total'] == max_sum])

    # запись в файл g
    lines = [f"{s['surname']} {s['name']} {s['class']} {' '.join(map(str, s['grades']))}" for s in best]
    create_text_file(dest_filename, "\n".join(lines))
    print(f"б) Лучшие ученики записаны в '{dest_filename}'.")
    return best


# ------------------------------------------------------------
# 5. Основная программа
# ------------------------------------------------------------
def main():
    print("Задача 508: Успеваемость учеников (отметки)")
    file_f = "f.txt"
    file_g = "g.txt"

    ensure_file_exists(file_f)
    students = read_students(file_f)

    if not students:
        print("Нет данных для обработки.")
        return

    print(f"\nВсего записей об учениках: {len(students)}")
    print("Первые 5 строк для проверки:")
    for s in students[:5]:
        print(f"  {s['surname']} {s['name']} {s['class']}: {s['grades']} (сумма {s['total']})")
    if len(students) > 5:
        print("  ...")

    solve_a(students)
    best = solve_b(students, file_g)

    if best:
        print("\nЛучшие ученики по параллелям:")
        current_parallel = None
        for s in best:
            if s['grade_num'] != current_parallel:
                current_parallel = s['grade_num']
                print(f"  Параллель {current_parallel}:")
            print(f"    {s['surname']} {s['name']} ({s['class']}) – сумма {s['total']}")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")