"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

524. Дан текстовый файл f. Переписать компоненты файла f в файл g, вставляя в начало каждой строки по одному пробелу. Порядок компонент должен быть сохранен.
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
            text = "Первая строка файла.\nВторая строка файла.\nТретья строка.\nКонец."
        else:
            text = "\n".join(lines)
    elif choice == '2':
        n = random.randint(4, 8)  # количество строк
        lines = []
        for _ in range(n):
            length = random.randint(10, 40)
            chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 '
            line = ''.join(random.choice(chars) for _ in range(length))
            lines.append(line)
        text = "\n".join(lines)
        print(f"Сгенерировано {n} случайных строк.")
    else:  # готовый пример
        text = "Первая строка файла.\nВторая строка файла.\nТретья строка.\nКонец."
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
# 3. Добавление пробела в начало каждой строки
# ------------------------------------------------------------
def prepend_space_to_lines(source, destination):
    """
    Читает файл source, добавляет один пробел в начало каждой строки
    и записывает результат в destination. Порядок строк сохраняется.
    """
    lines = read_file(source).splitlines()
    # Добавляем пробел в начало каждой строки, сохраняя переносы строк
    modified_lines = [' ' + line for line in lines]
    create_text_file(destination, "\n".join(modified_lines))
    print(f"Строки с начальным пробелом записаны в '{destination}'.")


# ------------------------------------------------------------
# 4. Основная программа
# ------------------------------------------------------------
def main():
    print("Задача 524: Добавление пробела в начало каждой строки")
    file_f = "f.txt"
    file_g = "g.txt"

    ensure_file_exists(file_f)

    print("\nИсходное содержимое f.txt:")
    print(read_file(file_f))

    prepend_space_to_lines(file_f, file_g)

    print("\nСодержимое g.txt (с пробелом в начале строк):")
    # Выводим явно, чтобы были видны начальные пробелы
    for line in read_file(file_g).splitlines():
        print(repr(line))


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")