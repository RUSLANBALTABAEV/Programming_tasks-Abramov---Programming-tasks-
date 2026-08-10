"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

522. Дан текстовый файл f. Получить самую длинную строку файла. Если в файле имеется несколько строк с наибольшей длиной, то получить одну из них.
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
    print("2 — Случайная генерация строк разной длины")
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
            text = ("Короткая строка.\n"
                    "Это строка немного длиннее, чем предыдущая.\n"
                    "А это самая длинная строка в этом файле, она должна быть найдена.\n"
                    "Снова короткая строка.\n"
                    "Ещё одна длинная строка, но мы выведем первую при равенстве длин.\n"
                    "Конец.")
        else:
            text = "\n".join(lines)
    elif choice == '2':
        n = random.randint(5, 12)  # количество строк
        lines = []
        for _ in range(n):
            length = random.randint(10, 100)  # длина строки от 10 до 100 символов
            # Генерируем случайную строку из букв, цифр и пробелов
            chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 '
            line = ''.join(random.choice(chars) for _ in range(length))
            lines.append(line)
        text = "\n".join(lines)
        print(f"Сгенерировано {n} строк случайной длины.")
    else:  # готовый пример
        text = ("Короткая строка.\n"
                "Это строка немного длиннее, чем предыдущая.\n"
                "А это самая длинная строка в этом файле, она должна быть найдена.\n"
                "Снова короткая строка.\n"
                "Ещё одна длинная строка, но мы выведем первую при равенстве длин.\n"
                "Конец.")
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
# 3. Поиск самой длинной строки
# ------------------------------------------------------------
def find_longest_line(filename):
    """
    Читает файл filename и возвращает первую строку с максимальной длиной,
    а также её длину.
    Если файл пуст, возвращает (None, 0).
    """
    content = read_file(filename)
    if not content:
        return None, 0

    lines = content.splitlines()
    max_len = -1
    longest_line = ""

    for line in lines:
        current_len = len(line)
        if current_len > max_len:
            max_len = current_len
            longest_line = line

    return longest_line, max_len


# ------------------------------------------------------------
# 4. Основная программа
# ------------------------------------------------------------
def main():
    print("Задача 522: Получить самую длинную строку файла")
    file_f = "f.txt"

    ensure_file_exists(file_f)

    print("\nИсходное содержимое f.txt:")
    print(read_file(file_f))

    longest_line, max_len = find_longest_line(file_f)

    print("\nСамая длинная строка:")
    if longest_line is not None:
        print(f"Длина: {max_len} символов")
        print(f"Строка: '{longest_line}'")
    else:
        print("Файл пуст.")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")