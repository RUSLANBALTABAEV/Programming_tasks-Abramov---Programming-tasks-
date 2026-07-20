"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

482. Дан символьный файл f . Получить файл g , образованный из файла f заменой всех его прописных (больших) букв одноименными строчными (малыми). 
"""


import random
import string
import os


# ------------------------------------------------------------
# 1. Процедуры работы с файлами
# ------------------------------------------------------------
def create_text_file(filename, text):
    """Создаёт (или перезаписывает) текстовый файл."""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)


def read_file(filename):
    """Читает и возвращает содержимое текстового файла."""
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()


# ------------------------------------------------------------
# 2. Процедура преобразования: замена прописных букв строчными
# ------------------------------------------------------------
def convert_to_lowercase(source, destination):
    """Читает файл source, заменяет большие буквы на маленькие,
       результат записывает в destination."""
    content = read_file(source)
    converted = content.lower()
    create_text_file(destination, converted)
    print(f"Файл '{source}' обработан. Результат записан в '{destination}'.")


# ------------------------------------------------------------
# 3. Ввод данных (содержимого файла f)
# ------------------------------------------------------------
def get_file_content(filename):
    """
    Если файл f не существует или пуст, предлагает пользователю
    выбрать способ задания его содержимого.
    """
    if os.path.exists(filename):
        existing = read_file(filename)
        if existing.strip():
            print(f"Файл '{filename}' уже существует и содержит текст.")
            return  # используем существующий

    print("Файл f не найден или пуст. Задайте его содержимое.")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод текста")
    print("2 — Случайная генерация текста")
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
        length = random.randint(30, 100)
        chars = string.ascii_letters + string.digits + string.punctuation + ' \n'
        text = ''.join(random.choice(chars) for _ in range(length))
        print("Сгенерирован случайный текст.")
    else:  # готовый пример
        text = "HELLO World! This Is A Test String. 12345."
        print(f"Готовый пример: {repr(text)}")

    create_text_file(filename, text)
    print(f"Содержимое записано в '{filename}'.")


# ------------------------------------------------------------
# 4. Основная программа
# ------------------------------------------------------------
def main():
    src = "f.txt"
    dest = "g.txt"

    print("Задача 482: Замена прописных букв на строчные")
    get_file_content(src)

    print("\nСодержимое исходного файла f.txt:")
    print(read_file(src))

    convert_to_lowercase(src, dest)

    print("\nСодержимое файла g.txt (результат):")
    print(read_file(dest))


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
