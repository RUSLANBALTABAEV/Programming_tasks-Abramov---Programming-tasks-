"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

498. Дан символьный файл f. Найти самое длинное слово (см. предыдущую задачу) среди слов, вторая буква которых есть е; если таких слов с наибольшей длиной несколько, то найти последнее. Если таких слов нет вообще, то сообщить об этом. Решить эту задачу:
а) полагая, что слова состоят не более чем из 10 символов;
б) без ограничения на число символов в слове.
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
    print("2 — Случайная генерация текста (со словами, где вторая буква 'e')")
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
        # Генерируем случайные слова, некоторые со второй буквой 'e'
        word_count = random.randint(5, 12)
        words = []
        for _ in range(word_count):
            length = random.randint(1, 8)  # могут быть и однобуквенные, но нам нужны >=2
            if length >= 2 and random.random() < 0.6:
                # делаем вторую букву 'e'
                first = random.choice(string.ascii_letters)
                rest = ''.join(random.choice(string.ascii_letters) for _ in range(length - 1))
                word = first + 'e' + rest[1:]  # заменяем вторую букву на 'e'
            else:
                word = ''.join(random.choice(string.ascii_letters) for _ in range(length))
            words.append(word)
        text = ' '.join(words)
        print("Сгенерирован случайный текст со словами.")
    else:  # готовый пример
        text = "next eel text meet test"
        print("Готовый пример: 'next eel text meet test'.")

    create_text_file(filename, text)
    print(f"Содержимое записано в '{filename}'.")


def ensure_file_exists(filename, name):
    """Проверяет, существует ли файл и не пуст ли он; если нет – создаёт."""
    if not os.path.exists(filename) or not read_file(filename).strip():
        create_file_f(filename)


# ------------------------------------------------------------
# 3. Поиск самого длинного слова (со второй буквой 'e')
# ------------------------------------------------------------
def find_longest_word(text, max_len=None):
    """
    Возвращает самое длинное слово со второй буквой 'e'.
    Если несколько, возвращает последнее (по порядку в тексте).
    Если max_len не None, игнорируются слова длиннее max_len.
    """
    words = text.split()
    best_word = None
    best_len = -1

    # Ищем с учётом требования «последнее» — перебираем в прямом порядке,
    # но запоминаем, если длина >= текущей (тогда последнее останется).
    for w in words:
        if len(w) < 2 or w[1] != 'e':
            continue
        if max_len is not None and len(w) > max_len:
            continue
        if len(w) >= best_len:
            best_len = len(w)
            best_word = w
    return best_word, best_len


# ------------------------------------------------------------
# 4. Вывод результата для обоих подпунктов
# ------------------------------------------------------------
def main():
    print("Задача 498: Поиск самого длинного слова со второй буквой 'e'")
    file_f = "f.txt"

    # Убеждаемся, что файл f существует и не пуст
    ensure_file_exists(file_f, 'f')

    # Читаем содержимое
    text = read_file(file_f)
    print("\nИсходный текст:")
    print(text)

    # Пункт а) с ограничением длины <= 10
    print("\nа) С ограничением длины слов (не более 10 символов):")
    word_a, len_a = find_longest_word(text, max_len=10)
    if word_a:
        print(f"   Самое длинное слово: '{word_a}' (длина {len_a})")
    else:
        print("   Подходящих слов не найдено.")

    # Пункт б) без ограничения длины
    print("\nб) Без ограничения длины слов:")
    word_b, len_b = find_longest_word(text)
    if word_b:
        print(f"   Самое длинное слово: '{word_b}' (длина {len_b})")
    else:
        print("   Подходящих слов не найдено.")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")