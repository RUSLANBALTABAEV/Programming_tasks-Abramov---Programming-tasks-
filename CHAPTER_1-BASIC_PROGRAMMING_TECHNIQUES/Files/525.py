"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

525. Даны текстовый файл, строка s. Получить все строки файла f, содержащие в качестве фрагмента строку s.
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
    """Создаёт файл f с текстовыми строками."""
    print("Файл f не существует или пуст. Задайте содержимое файла.")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод строк (пустая строка — конец)")
    print("2 — Случайная генерация строк")
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
            text = ("Python — это мощный язык программирования.\n"
                    "Сегодня отличная погода для программирования.\n"
                    "Java также является популярным языком.\n"
                    "Мы пишем программы на Python.\n"
                    "Этот файл содержит несколько строк для проверки.\n"
                    "Завершающая строка.")
        else:
            text = "\n".join(lines)
    elif choice == '2':
        n = random.randint(4, 8)  # количество строк
        words = ["Python", "Java", "C++", "programming", "language",
                 "file", "string", "example", "random", "text"]
        lines = []
        for _ in range(n):
            # строка из нескольких случайных слов
            line = ' '.join(random.choices(words, k=random.randint(2, 5)))
            lines.append(line)
        text = "\n".join(lines)
        print(f"Сгенерировано {n} случайных строк.")
    else:  # готовый пример
        text = ("Python — это мощный язык программирования.\n"
                "Сегодня отличная погода для программирования.\n"
                "Java также является популярным языком.\n"
                "Мы пишем программы на Python.\n"
                "Этот файл содержит несколько строк для проверки.\n"
                "Завершающая строка.")
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
# 3. Поиск строк, содержащих заданную подстроку
# ------------------------------------------------------------
def filter_lines_by_substring(source, substring):
    """
    Возвращает список строк из файла source, которые содержат substring.
    """
    lines = read_file(source).splitlines()
    return [line for line in lines if substring in line]


# ------------------------------------------------------------
# 4. Основная программа
# ------------------------------------------------------------
def main():
    print("Задача 525: Получить строки, содержащие фрагмент s")
    file_f = "f.txt"
    file_g = "g.txt"

    ensure_file_exists(file_f)

    # Запрашиваем строку s у пользователя
    s = input("Введите строку для поиска (фрагмент): ").strip()
    if not s:
        print("Строка поиска пуста – вывод всех строк файла.")

    # Фильтруем строки
    matching_lines = filter_lines_by_substring(file_f, s)

    # Записываем результат в g
    if matching_lines:
        create_text_file(file_g, "\n".join(matching_lines))
    else:
        create_text_file(file_g, "")

    print(f"\nНайдено {len(matching_lines)} строк, содержащих '{s}'.")
    if matching_lines:
        print("Они записаны в g.txt:")
        for line in matching_lines:
            print(f"  {line}")
    else:
        print("Файл g.txt пуст.")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")