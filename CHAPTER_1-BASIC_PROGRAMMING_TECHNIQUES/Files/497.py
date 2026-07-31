"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

497. Дан символьный файл f. Группы символов, разделенные пробелами (одним или несколькими) и не содержащие пробелов внутри себя, будем, как и прежде (см. задачу 269), называть словами.
Удалить из файла все однобуквенные слова и лишние пробелы. 
Результат записать в файл g.
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
    print("2 — Случайная генерация текста (с короткими словами)")
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
        # Генерируем случайный текст с короткими (1–5 букв) словами
        word_count = random.randint(8, 15)
        words = []
        for _ in range(word_count):
            word_len = random.randint(1, 5)
            word = ''.join(random.choice(string.ascii_letters) for _ in range(word_len))
            words.append(word)
        text = '   '.join(words)  # добавим множественные пробелы
        print("Сгенерирован случайный текст с короткими словами.")
    else:  # готовый пример
        text = "Hello   a world  i   from  Python  b  and   a  task"
        print("Готовый пример: 'Hello   a world  i   from  Python  b  and   a  task'.")

    create_text_file(filename, text)
    print(f"Содержимое записано в '{filename}'.")


def ensure_file_exists(filename, name):
    """Проверяет, существует ли файл и не пуст ли он; если нет – создаёт."""
    if not os.path.exists(filename) or not read_file(filename).strip():
        create_file_f(filename)


# ------------------------------------------------------------
# 3. Процедура очистки текста
# ------------------------------------------------------------
def clean_text_file(source, destination):
    """
    Читает файл source, удаляет из него все однобуквенные слова
    и лишние пробелы, результат записывает в destination.
    """
    raw_text = read_file(source)
    # Разбиваем на слова (убираем все пробелы, в том числе множественные)
    words = raw_text.split()
    # Оставляем только слова длиннее одного символа
    filtered_words = [w for w in words if len(w) > 1]
    # Собираем обратно с одиночными пробелами
    cleaned_text = ' '.join(filtered_words)
    create_text_file(destination, cleaned_text)
    print(f"Очищенный текст записан в '{destination}'.")


# ------------------------------------------------------------
# 4. Основная программа
# ------------------------------------------------------------
def main():
    print("Задача 497: Удаление однобуквенных слов и лишних пробелов")
    file_f = "f.txt"
    file_g = "g.txt"

    # Убеждаемся, что файл f существует и не пуст
    ensure_file_exists(file_f, 'f')

    # Выводим исходное содержимое
    print("\nИсходное содержимое f.txt:")
    print(read_file(file_f))

    # Выполняем очистку
    clean_text_file(file_f, file_g)

    # Выводим результат
    print("\nРезультат в g.txt:")
    print(read_file(file_g))


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")