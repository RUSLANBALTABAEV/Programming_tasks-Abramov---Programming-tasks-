"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

485. Дан символьный файл f . Записать в файл g компоненты файла f в обратном порядке.
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
# 2. Создание исходного файла f (если он отсутствует)
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
        length = random.randint(30, 100)
        chars = string.ascii_letters + string.digits + string.punctuation + ' \n'
        text = ''.join(random.choice(chars) for _ in range(length))
        print("Сгенерирован случайный текст.")
    else:  # готовый пример
        text = "Hello World! 12345"
        print(f"Готовый пример: {repr(text)}")

    create_text_file(filename, text)
    print(f"Содержимое записано в '{filename}'.")


# ------------------------------------------------------------
# 3. Основная программа
# ------------------------------------------------------------
def main():
    print("Задача 485: Запись компонент файла f в обратном порядке в файл g")
    src = "f.txt"
    dest = "g.txt"

    # Если файл f не существует или пуст — создаём его
    if not os.path.exists(src) or not read_file(src).strip():
        create_file_f(src)

    # Читаем исходный текст и переворачиваем
    original_text = read_file(src)
    reversed_text = original_text[::-1]

    # Записываем в файл g
    create_text_file(dest, reversed_text)

    # Выводим результат для проверки
    print("\nИсходный файл f.txt:")
    print(original_text)
    print("\nФайл g.txt (перевёрнутый):")
    print(reversed_text)


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
