"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

486. Даны символьные файлы f и g . Записать в файл h сначала компоненты файла f , затем – компоненты файла g с сохранением порядка.
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
# 2. Создание исходных файлов f и g (если они отсутствуют)
# ------------------------------------------------------------
def create_file(filename, name):
    """Создаёт один файл (f или g) с текстом по выбору пользователя."""
    print(f"Содержимое файла {name}.txt не найдено или пусто.")
    print("Выберите способ задания текста:")
    print("1 — Ручной ввод")
    print("2 — Случайная генерация")
    print("3 — Готовый пример")

    while True:
        choice = input("Ваш выбор (1/2/3): ").strip()
        if choice in ('1', '2', '3'):
            break
        print("Ошибка: выберите 1, 2 или 3.")

    if choice == '1':
        print(f"Введите текст для {name}.txt (для окончания — пустая строка):")
        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
        text = "\n".join(lines)
    elif choice == '2':
        length = random.randint(30, 80)
        chars = string.ascii_letters + string.digits + string.punctuation + ' \n'
        text = ''.join(random.choice(chars) for _ in range(length))
        print(f"Сгенерирован случайный текст для {name}.txt.")
    else:
        # готовые примеры
        examples = {
            'f': "Hello from f!\nLine 2 of f.",
            'g': "Greetings from g.\nSecond line of g."
        }
        text = examples.get(name, "Some default text.")
        print(f"Использован готовый пример для {name}.txt.")

    create_text_file(filename, text)
    print(f"Файл '{filename}' создан.\n")


def ensure_file_exists(filename, name):
    """Проверяет, существует ли файл и не пуст ли он; если нет – вызывает создание."""
    if not os.path.exists(filename) or not read_file(filename).strip():
        create_file(filename, name)


# ------------------------------------------------------------
# 3. Объединение файлов
# ------------------------------------------------------------
def concatenate_files(src1, src2, dest):
    """Записывает в dest содержимое src1, а затем src2."""
    content1 = read_file(src1)
    content2 = read_file(src2)
    create_text_file(dest, content1 + content2)
    print(f"Файлы '{src1}' и '{src2}' объединены в '{dest}'.")


# ------------------------------------------------------------
# 4. Основная программа
# ------------------------------------------------------------
def main():
    print("Задача 486: Объединение файлов f и g в файл h")
    file_f = "f.txt"
    file_g = "g.txt"
    file_h = "h.txt"

    # Убедимся, что f и g существуют
    ensure_file_exists(file_f, 'f')
    ensure_file_exists(file_g, 'g')

    # Покажем исходные содержимые
    print("Содержимое f.txt:")
    print(read_file(file_f))
    print("\nСодержимое g.txt:")
    print(read_file(file_g))

    # Выполняем конкатенацию
    concatenate_files(file_f, file_g, file_h)

    # Результат
    print("\nСодержимое h.txt (результат):")
    print(read_file(file_h))


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
