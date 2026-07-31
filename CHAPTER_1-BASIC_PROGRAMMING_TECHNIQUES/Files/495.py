"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

495. Даны символьные файлы f и g. Записать в файл h все начальные совпадающие компоненты файлов f и g.
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
# 2. Создание файлов f и g (если отсутствуют или пусты)
# ------------------------------------------------------------
def create_file(filename, name):
    """Создаёт один из файлов f или g с текстом по выбору пользователя."""
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
        length = random.randint(10, 30)
        chars = string.ascii_letters + string.digits + ' \n'
        text = ''.join(random.choice(chars) for _ in range(length))
        print(f"Сгенерирован случайный текст для {name}.txt.")
    else:
        # Готовые примеры
        examples = {
            'f': "Hello_World!",
            'g': "Hello_User!"
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
# 3. Запись общего префикса в файл h
# ------------------------------------------------------------
def write_common_prefix(file_f, file_g, file_h):
    """
    Сравнивает файлы f и g посимвольно и записывает в h все начальные
    совпадающие символы (общий префикс).
    """
    content_f = read_file(file_f)
    content_g = read_file(file_g)

    # Ищем длину общего префикса
    common_length = 0
    for ch_f, ch_g in zip(content_f, content_g):
        if ch_f == ch_g:
            common_length += 1
        else:
            break

    prefix = content_f[:common_length]
    create_text_file(file_h, prefix)
    print(f"Общий префикс длиной {common_length} записан в '{file_h}'.")


# ------------------------------------------------------------
# 4. Основная программа
# ------------------------------------------------------------
def main():
    print("Задача 495: Запись начальных совпадающих компонент файлов f и g в файл h")
    file_f = "f.txt"
    file_g = "g.txt"
    file_h = "h.txt"

    # Убеждаемся, что файлы f и g существуют и не пусты
    ensure_file_exists(file_f, 'f')
    ensure_file_exists(file_g, 'g')

    # Выводим содержимое исходных файлов
    print("Содержимое f.txt:")
    print(read_file(file_f))
    print("\nСодержимое g.txt:")
    print(read_file(file_g))

    # Записываем общий префикс в h
    write_common_prefix(file_f, file_g, file_h)

    # Выводим результат
    print("\nСодержимое h.txt (общий префикс):")
    print(read_file(file_h))


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")