"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

526. Дан текстовый файл f. Исключить пробелы, стоящие в концах его строк. Результат поместить в файл f1.
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
    """Создаёт файл f с текстовыми строками, в некоторых строках добавлены концевые пробелы."""
    print("Файл f не существует или пуст. Задайте содержимое файла.")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод строк (пустая строка — конец)")
    print("2 — Случайная генерация строк с пробелами в конце")
    print("3 — Готовый пример")

    while True:
        choice = input("Ваш выбор (1/2/3): ").strip()
        if choice in ('1', '2', '3'):
            break
        print("Ошибка: выберите 1, 2 или 3.")

    if choice == '1':
        print("Вводите строки. Для завершения — пустая строка.")
        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
        if not lines:
            print("Не введено ни одной строки. Будет использован готовый пример.")
            text = ("Первая строка с пробелами в конце.      \n"
                    "Вторая строка без пробелов в конце.\n"
                    "Строка с пробелами в конце.      \n"
                    "Ещё одна строка с пробелами в конце.      \n"
                    "Строка без завершающих пробелов.")
        else:
            text = "\n".join(lines)
    elif choice == '2':
        n = random.randint(4, 8)  # количество строк
        lines = []
        for _ in range(n):
            length = random.randint(10, 40)
            chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 '
            line = ''.join(random.choice(chars) for _ in range(length))
            # в 50% случаев добавим пробелы в конце
            if random.random() < 0.5:
                line += ' ' * random.randint(1, 5)
            lines.append(line)
        text = "\n".join(lines)
        print(f"Сгенерировано {n} случайных строк.")
    else:  # готовый пример
        text = ("Первая строка с пробелами в конце.      \n"
                "Вторая строка без пробелов в конце.\n"
                "Строка с пробелами в конце.      \n"
                "Ещё одна строка с пробелами в конце.      \n"
                "Строка без завершающих пробелов.")
        print("Использован готовый пример.")

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


# ------------------------------------------------------------
# 3. Удаление концевых пробелов в строках
# ------------------------------------------------------------
def remove_trailing_spaces(source, destination):
    """
    Читает файл source, удаляет пробельные символы с концов строк
    и записывает результат в destination.
    """
    lines = read_file(source).splitlines()
    # Удаляем пробелы справа у каждой строки
    cleaned_lines = [line.rstrip() for line in lines]
    create_text_file(destination, "\n".join(cleaned_lines))
    print(f"Концевые пробелы удалены. Результат записан в '{destination}'.")


# ------------------------------------------------------------
# 4. Основная программа
# ------------------------------------------------------------
def main():
    print("Задача 526: Исключение пробелов в концах строк")
    file_f = "f.txt"
    file_f1 = "f1.txt"

    ensure_file_exists(file_f)

    print("\nИсходное содержимое f.txt (пробелы в конце видны как '<<<'):")
    for line in read_file(file_f).splitlines():
        if line != line.rstrip():
            print(f"'{line}' <<<")
        else:
            print(f"'{line}'")

    remove_trailing_spaces(file_f, file_f1)

    print("\nСодержимое f1.txt (после удаления концевых пробелов):")
    for line in read_file(file_f1).splitlines():
        print(f"'{line}'")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")