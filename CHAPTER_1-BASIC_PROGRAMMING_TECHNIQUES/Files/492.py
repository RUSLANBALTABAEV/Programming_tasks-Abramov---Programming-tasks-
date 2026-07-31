"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

492. Дан символьный файл f . Добавить в его конец символы e, n, d (если это необходимо, использовать дополнительный файл g).
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


def append_via_temp(source, temp, suffix):
    """Добавляет строку suffix в конец файла source, используя временный файл temp."""
    content = read_file(source)
    new_content = content + suffix
    create_text_file(temp, new_content)
    # Копируем обратно из temp в source
    create_text_file(source, read_file(temp))


# ------------------------------------------------------------
# 2. Создание исходного файла f (если отсутствует или пуст)
# ------------------------------------------------------------
def create_file_f(filename):
    """Создаёт файл f с текстовым содержимым по выбору пользователя."""
    print("Файл f не существует или пуст. Задайте его содержимое.")
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
        length = random.randint(5, 20)
        text = ''.join(random.choice(string.ascii_letters) for _ in range(length))
        print("Сгенерирован случайный текст.")
    else:  # готовый пример
        text = "Hello"
        print(f"Готовый пример: {repr(text)}")

    create_text_file(filename, text)
    print(f"Содержимое записано в '{filename}'.")


# ------------------------------------------------------------
# 3. Основная программа
# ------------------------------------------------------------
def main():
    print("Задача 492: Добавление символов 'e', 'n', 'd' в конец файла")
    src = "f.txt"
    temp = "g.txt"

    # Если файл f не существует или пуст — создаём его
    if not os.path.exists(src) or not read_file(src).strip():
        create_file_f(src)

    print("\nИсходное содержимое f.txt:")
    print(read_file(src))

    # Добавляем "end" в конец через вспомогательный файл g
    append_via_temp(src, temp, "end")

    print("\nСодержимое f.txt после добавления:")
    print(read_file(src))
    print("(символы 'e', 'n', 'd' дописаны в конец)")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")