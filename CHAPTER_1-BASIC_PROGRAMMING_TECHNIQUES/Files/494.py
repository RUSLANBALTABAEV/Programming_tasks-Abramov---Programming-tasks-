"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

494. Даны символьные файлы f и g. Определить, совпадают ли компоненты файла f с компонентами файла g. Если нет, то получить 
номер первой компоненты, в которой файлы f и g отличаются между собой. В случае, когда один из файлов имеет n компонент (n≥0) и повторяет начало другого (более длинного) файла, ответом должно быть число n+1.
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
            'f': "Hello ab world!\nabcdefgh\nab ab ab",
            'g': "Hello ab world!\nabcdefgh\nab ab ab"  # по умолчанию одинаковые, можно изменить
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
# 3. Сравнение файлов (по компонентам)
# ------------------------------------------------------------
def compare_files(file_f, file_g):
    """
    Сравнивает два символьных файла покомпонентно (посимвольно).
    Возвращает номер первой отличающейся компоненты (начиная с 1),
    либо 0, если файлы полностью совпадают,
    либо n+1, где n — длина более короткого файла, если он является началом другого.
    """
    content_f = read_file(file_f)
    content_g = read_file(file_g)

    len_f = len(content_f)
    len_g = len(content_g)
    min_len = min(len_f, len_g)

    for i in range(min_len):
        if content_f[i] != content_g[i]:
            return i + 1   # номер с 1

    if len_f == len_g:
        return 0           # полностью совпадают

    # Один файл является началом другого
    return min_len + 1


# ------------------------------------------------------------
# 4. Основная программа
# ------------------------------------------------------------
def main():
    print("Задача 494: Сравнение символьных файлов f и g")
    file_f = "f.txt"
    file_g = "g.txt"

    # Убеждаемся, что файлы существуют
    ensure_file_exists(file_f, 'f')
    ensure_file_exists(file_g, 'g')

    # Выводим содержимое файлов
    print("Содержимое f.txt:")
    print(read_file(file_f))
    print("\nСодержимое g.txt:")
    print(read_file(file_g))

    # Сравниваем
    result = compare_files(file_f, file_g)
    print("\nРезультат сравнения:")
    if result == 0:
        print("Файлы полностью совпадают.")
    else:
        print(f"Файлы отличаются, первая различающаяся позиция: {result}")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")