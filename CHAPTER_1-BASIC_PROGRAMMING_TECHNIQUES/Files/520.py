"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

520. Дан текстовый файл f. Получить все его строки, содержащие более 60 символов.
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
                    "Эта строка имеет длину более 60 символов, поэтому она точно будет включена в результат.\n"
                    "Ещё одна длинная строка, которая превышает порог в шестьдесят символов.\n"
                    "Коротко.\n"
                    "Очень длинная строка, содержащая много слов, чтобы её длина превышала заданный порог в 60 символов.")
        else:
            text = "\n".join(lines)
    elif choice == '2':
        n = random.randint(5, 12)  # количество строк
        lines = []
        for _ in range(n):
            length = random.randint(10, 120)  # длина строки от 10 до 120 символов
            line = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz         ') for _ in range(length))
            lines.append(line.strip())
        text = "\n".join(lines)
        print(f"Сгенерировано {n} строк случайной длины.")
    else:  # готовый пример
        text = ("Короткая строка.\n"
                "Эта строка имеет длину более 60 символов, поэтому она точно будет включена в результат.\n"
                "Ещё одна длинная строка, которая превышает порог в шестьдесят символов.\n"
                "Коротко.\n"
                "Очень длинная строка, содержащая много слов, чтобы её длина превышала заданный порог в 60 символов.")
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
# 3. Фильтрация строк длиной более 60 символов
# ------------------------------------------------------------
def get_long_lines(source, destination, threshold=60):
    """
    Читает файл source, отбирает строки длиной > threshold
    и записывает их в destination.
    """
    lines = read_file(source).splitlines()
    long_lines = [line + '\n' for line in lines if len(line) > threshold]

    if long_lines:
        create_text_file(destination, ''.join(long_lines))
    else:
        create_text_file(destination, "")

    print(f"Найдено {len(long_lines)} строк длиннее {threshold} символов. "
          f"Результат записан в '{destination}'.")


# ------------------------------------------------------------
# 4. Основная программа
# ------------------------------------------------------------
def main():
    print("Задача 520: Получить строки длиной более 60 символов")
    file_f = "f.txt"
    file_g = "g.txt"

    ensure_file_exists(file_f)

    print("\nИсходное содержимое f.txt:")
    print(read_file(file_f))

    get_long_lines(file_f, file_g)

    print("\nСодержимое g.txt (строки > 60 символов):")
    content_g = read_file(file_g)
    if content_g.strip():
        print(content_g)
    else:
        print("(пусто – нет строк длиннее 60 символов)")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")