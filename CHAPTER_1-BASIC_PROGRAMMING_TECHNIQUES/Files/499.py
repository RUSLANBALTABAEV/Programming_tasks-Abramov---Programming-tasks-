"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

499. Дан символьный файл f. Считая, что количество символов в слове (см. задачу 497) не превосходит двадцати:
а) определить, сколько в файле f имеется слов, состоящих из одного, двух, трех и т. д. символов;
б) получить гистограмму (столбчатую диаграмму) длин всех слов файла f;
в) определить количество слов в файле f.
"""


import random
import string
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
    """Создаёт файл f с текстовым содержимым по выбору пользователя."""
    print("Файл f не существует или пуст. Задайте его содержимое.")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод текста")
    print("2 — Случайная генерация текста (слова длиной до 20)")
    print("3 — Готовый пример")

    while True:
        choice = input("Ваш выбор (1/2/3): ").strip()
        if choice in ('1', '2', '3'):
            break
        print("Ошибка: выберите 1, 2 или 3.")

    if choice == '1':
        print("Введите текст (для окончания — пустая строка):")
        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
        text = "\n".join(lines)
    elif choice == '2':
        # Генерируем случайные слова длиной от 1 до 20 символов
        word_count = random.randint(10, 20)
        words = []
        for _ in range(word_count):
            word_len = random.randint(1, 20)
            word = ''.join(random.choices(string.ascii_letters, k=word_len))
            words.append(word)
        text = ' '.join(words)   # один пробел между словами
        print("Сгенерирован случайный текст со словами длиной до 20.")
    else:  # готовый пример
        text = "This is an example text with words of various lengths"
        print("Готовый пример: 'This is an example text with words of various lengths'.")

    create_text_file(filename, text)
    print(f"Содержимое записано в '{filename}'.")


def ensure_file_exists(filename, name):
    """Проверяет, существует ли файл и не пуст ли он; если нет – создаёт."""
    if not os.path.exists(filename) or not read_file(filename).strip():
        create_file_f(filename)


# ------------------------------------------------------------
# 3. Анализ длин слов и вывод результатов
# ------------------------------------------------------------
def analyze_file(filename):
    """
    Читает файл filename, разбивает на слова и выводит:
    в) общее количество слов;
    а) распределение слов по длинам (1..20);
    б) текстовую гистограмму длин.
    """
    text = read_file(filename)
    words = text.split()

    # в) Общее количество слов
    total = len(words)
    print(f"в) Общее количество слов в файле: {total}")

    # а) Подсчёт длин (максимум 20, как в условии)
    MAX_LEN = 20
    length_counts = [0] * (MAX_LEN + 1)
    for w in words:
        length = len(w)
        if length <= MAX_LEN:
            length_counts[length] += 1

    print("\nа) Количество слов каждой длины:")
    for l in range(1, MAX_LEN + 1):
        if length_counts[l] > 0:
            print(f"  длина {l:2}: {length_counts[l]} слов(а)")

    # б) Текстовая гистограмма
    print("\nб) Гистограмма длин слов (символ '#' – одно слово):")
    for l in range(1, MAX_LEN + 1):
        cnt = length_counts[l]
        if cnt > 0:
            print(f"  {l:2} | {'#' * cnt} ({cnt})")


# ------------------------------------------------------------
# 4. Основная программа
# ------------------------------------------------------------
def main():
    print("Задача 499: Анализ длин слов в файле")
    file_f = "f.txt"

    # Убеждаемся, что файл f существует и не пуст
    ensure_file_exists(file_f, 'f')

    # Выводим исходное содержимое
    print("\nИсходное содержимое f.txt:")
    print(read_file(file_f))
    print()

    # Выполняем анализ
    analyze_file(file_f)


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")