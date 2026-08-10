"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

527. Даны два текстовых файла f и g. Определить совпадают ли компоненты файла f с компонентами файла g. Если нет, то получить номер первой строки и позицию первого символа в этой строке, в которых файлы f и g отличаются между собой. Принять во внимание уточнение к задаче 494.
"""


import random
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
# 2. Создание одного из файлов f или g (если отсутствует или пуст)
# ------------------------------------------------------------
def create_file(filename, name):
    """Создаёт файл с текстом по выбору пользователя."""
    print(f"Файл {name}.txt не существует или пуст. Задайте его содержимое.")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод строк (пустая строка — конец)")
    print("2 — Случайная генерация строк")
    print("3 — Готовый пример")

    while True:
        choice = input("Ваш выбор (1/2/3): ").strip()
        if choice in ('1', '2', '3'):
            break
        print("Ошибка: выберите 1, 2 или 3.")

    if choice == '1':
        print(f"Введите строки для {name}.txt. Для завершения — пустая строка.")
        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
        if not lines:
            print("Не введено ни одной строки. Будет использован готовый пример.")
            lines = default_lines_for(name)
        text = "\n".join(lines)
    elif choice == '2':
        n = random.randint(3, 6)
        words_pool = ["hello", "world", "python", "file", "text",
                      "example", "difference", "compare", "test"]
        lines = []
        for _ in range(n):
            # составляем строку из случайных слов
            line_words = random.choices(words_pool, k=random.randint(2, 5))
            lines.append(' '.join(line_words))
        text = "\n".join(lines)
        print(f"Сгенерировано {n} случайных строк.")
    else:  # готовый пример
        lines = default_lines_for(name)
        text = "\n".join(lines)
        print(f"Использован готовый пример для {name}.txt.")

    create_text_file(filename, text)
    print(f"Данные записаны в '{filename}'.\n")


def default_lines_for(name):
    """Возвращает список строк по умолчанию для файла f или g."""
    if name == 'f':
        return ["Первая строка.", "Вторая строка.", "Третья строка."]
    else:  # g
        # По умолчанию сделаем различие во второй строке на 9-й позиции
        return ["Первая строка.", "Вторая строка.", "Третья строка."]


def ensure_files_exist():
    """Проверяет существование файлов f.txt и g.txt и создаёт их при необходимости."""
    for name in ('f', 'g'):
        filename = f"{name}.txt"
        if not os.path.exists(filename) or not read_file(filename).strip():
            create_file(filename, name)


# ------------------------------------------------------------
# 3. Сравнение файлов (задача 527)
# ------------------------------------------------------------
def compare_files(file_f, file_g):
    """
    Сравнивает два текстовых файла построчно и посимвольно.
    Возвращает кортеж:
        (True, None, None) – если файлы полностью совпадают;
        (False, строка, позиция) – если есть различия.
        Строка и позиция указываются с 1.
    Если один файл является началом другого (префиксом), возвращается
    номер строки min+1 и позиция 1.
    """
    lines_f = read_file(file_f).splitlines()
    lines_g = read_file(file_g).splitlines()
    min_lines = min(len(lines_f), len(lines_g))

    for i in range(min_lines):
        line_f = lines_f[i]
        line_g = lines_g[i]
        if line_f != line_g:
            # Ищем первый различающийся символ
            min_len = min(len(line_f), len(line_g))
            for j in range(min_len):
                if line_f[j] != line_g[j]:
                    return False, i + 1, j + 1
            # Если строки разной длины и короткая является началом длинной
            return False, i + 1, min_len + 1

    if len(lines_f) == len(lines_g):
        return True, None, None

    # Один файл является началом другого (префикс)
    return False, min_lines + 1, 1


# ------------------------------------------------------------
# 4. Основная программа
# ------------------------------------------------------------
def main():
    print("Задача 527: Сравнение текстовых файлов f и g")
    ensure_files_exist()

    file_f = "f.txt"
    file_g = "g.txt"

    # Выводим содержимое для наглядности
    print("Содержимое f.txt:")
    print(read_file(file_f))
    print("\nСодержимое g.txt:")
    print(read_file(file_g))

    # Сравниваем
    equal, row, col = compare_files(file_f, file_g)

    print("\nРезультат сравнения:")
    if equal:
        print("✅ Файлы полностью совпадают.")
    else:
        print(f"❌ Файлы различаются.")
        print(f"   Первое различие: строка {row}, позиция {col}.")

        # Показываем строки для справки
        lines_f = read_file(file_f).splitlines()
        lines_g = read_file(file_g).splitlines()
        line_f = lines_f[row - 1] if row <= len(lines_f) else "<конец файла f>"
        line_g = lines_g[row - 1] if row <= len(lines_g) else "<конец файла g>"
        print(f"   Строка в f: {line_f}")
        print(f"   Строка в g: {line_g}")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")