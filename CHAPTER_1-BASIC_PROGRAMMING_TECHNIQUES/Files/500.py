"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

500. Дан символьный файл f. Предполагается, что длина одного слова (см. задачу 497) не превосходит десяти и что число слов делится на 100. Подготовить файл для печати слов в две колонки по пятьдесят строк на странице.
Слова должны быть размещены в файле f1 в следующем порядке: 1-е слово, 51-е слово, 2-е слово, 52-е слово, …, 50-е слово, 100-е слово, затем (следующая страница) 101-е слово, 151-е слово, …, 150-е слово, 200-е слово и т. д.
"""


import random
import string
import os


# ------------------------------------------------------------
# 1. Процедуры работы с файлами (как в задаче 497)
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
    """
    Создаёт файл f со словами, количество которых кратно 100.
    Предоставляет выбор способа ввода: ручной, случайный или готовый пример.
    """
    print("Файл f не существует или пуст. Задайте его содержимое.")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод текста (слова длиной не более 10 символов)")
    print("2 — Случайная генерация (200 слов, длина ≤ 10)")
    print("3 — Готовый пример (200 слов word_1 … word_200)")

    while True:
        choice = input("Ваш выбор (1/2/3): ").strip()
        if choice in ('1', '2', '3'):
            break
        print("Ошибка: выберите 1, 2 или 3.")

    if choice == '1':
        print("Введите текст. Количество слов должно быть кратно 100, длина каждого слова ≤ 10.")
        print("Для окончания ввода нажмите Enter (пустая строка).")
        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
        text = "\n".join(lines)
        # Проверяем, что количество слов кратно 100
        words = text.split()
        if len(words) % 100 != 0:
            print(f"Предупреждение: количество слов ({len(words)}) не кратно 100. "
                  f"Будет обрезано до {len(words) // 100 * 100} слов.")
            words = words[:len(words) // 100 * 100]
            text = ' '.join(words)
    elif choice == '2':
        # Генерируем 200 случайных слов с длиной от 1 до 10
        word_count = 200  # для наглядности 2 страницы по 100 слов
        words = []
        for _ in range(word_count):
            word_len = random.randint(1, 10)
            word = ''.join(random.choice(string.ascii_letters) for _ in range(word_len))
            words.append(word)
        text = ' '.join(words)
        print("Сгенерировано 200 случайных слов.")
    else:  # готовый пример
        # Классический пример: word_1, word_2, ..., word_200
        words = [f"word_{i}" for i in range(1, 201)]
        text = ' '.join(words)
        print("Использован готовый пример (200 слов).")

    create_text_file(filename, text)
    print(f"Содержимое записано в '{filename}'.")


def ensure_file_exists(filename, name):
    """Проверяет, существует ли файл и не пуст ли он; если нет – создаёт."""
    if not os.path.exists(filename) or not read_file(filename).strip():
        create_file_f(filename)


# ------------------------------------------------------------
# 3. Процедура подготовки файла для печати в две колонки
# ------------------------------------------------------------
def prepare_print_file(source, destination):
    """
    Читает файл source, переставляет слова в порядке:
    1-е, 51-е, 2-е, 52-е, …, 50-е, 100-е (и т. д. для последующих страниц),
    и записывает результат в destination в виде строк по два слова.
    """
    text = read_file(source)
    words = text.split()
    total = len(words)

    if total % 100 != 0:
        print(f"Предупреждение: количество слов ({total}) не кратно 100. "
              f"Будет обрезано до {total // 100 * 100} слов.")
        words = words[:total // 100 * 100]
        total = len(words)

    if total == 0:
        print("Слишком мало слов для формирования страниц. Файл не создан.")
        return

    output_lines = []
    for page in range(total // 100):
        offset = page * 100
        for row in range(50):
            word1 = words[offset + row]
            word2 = words[offset + 50 + row]
            output_lines.append(f"{word1:<10}{word2:<10}")
        if page < total // 100 - 1:
            output_lines.append("")   # разделитель страниц

    create_text_file(destination, "\n".join(output_lines))
    print(f"Файл '{destination}' подготовлен для печати в две колонки.")


# ------------------------------------------------------------
# 4. Основная программа
# ------------------------------------------------------------
def main():
    print("Задача 500: Подготовка файла для печати в две колонки")
    file_f = "f.txt"
    file_f1 = "f1.txt"

    # Убеждаемся, что файл f существует и не пуст
    ensure_file_exists(file_f, 'f')

    # Выводим информацию об исходном файле
    raw = read_file(file_f)
    words = raw.split()
    print(f"\nИсходный файл '{file_f}' содержит {len(words)} слов(а).")
    print("Первые 10 слов:", words[:10])

    # Выполняем подготовку для печати
    prepare_print_file(file_f, file_f1)

    # Выводим первые несколько строк результата для проверки
    print("\nПервые 5 строк файла f1.txt:")
    with open(file_f1, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            if i >= 5:
                break
            print(f"  {line.rstrip()}")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")