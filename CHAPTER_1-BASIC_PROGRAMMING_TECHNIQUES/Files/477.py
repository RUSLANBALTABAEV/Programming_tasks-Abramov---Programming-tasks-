"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

477. Даны символьные файлы f1 и f2. Переписать с сохранением порядка следования компоненты файла f1 в файл f2, а компоненты файла f2 - в файл f1. Использовать вспомогательный файл h.
"""


import random
import string


# ------------------------------------------------------------
# Процедуры работы с файлами
# ------------------------------------------------------------
def create_text_file(filename, text):
    """Создаёт (или перезаписывает) текстовый файл."""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)


def read_file(filename):
    """Читает и возвращает содержимое текстового файла."""
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()


def copy_file(source, destination):
    """Копирует содержимое source в destination."""
    content = read_file(source)
    create_text_file(destination, content)


def swap_files(f1, f2, h):
    """Обменивает содержимое файлов f1 и f2 через вспомогательный файл h."""
    copy_file(f1, h)     # f1 -> h
    copy_file(f2, f1)    # f2 -> f1
    copy_file(h, f2)     # h -> f2


# ------------------------------------------------------------
# Ввод данных (содержимого файлов f1 и f2)
# ------------------------------------------------------------
def get_file_contents():
    """Выбор способа задания содержимого файлов f1 и f2."""
    print("Задача 477: Обмен содержимым файлов f1 и f2")
    print("Выберите способ задания текста:")
    print("1 — Ручной ввод для f1 и f2")
    print("2 — Случайная генерация")
    print("3 — Готовые примеры")

    while True:
        choice = input("Ваш выбор (1/2/3): ").strip()
        if choice in ('1', '2', '3'):
            break
        print("Ошибка: выберите 1, 2 или 3.")

    if choice == '1':
        print("Введите текст для файла f1 (для окончания — пустая строка):")
        lines1 = []
        while True:
            line = input()
            if line == "":
                break
            lines1.append(line)
        text1 = "\n".join(lines1)

        print("Введите текст для файла f2 (для окончания — пустая строка):")
        lines2 = []
        while True:
            line = input()
            if line == "":
                break
            lines2.append(line)
        text2 = "\n".join(lines2)
        return text1, text2

    elif choice == '2':
        length1 = random.randint(30, 100)
        length2 = random.randint(30, 100)
        pool = string.ascii_letters + string.digits + string.punctuation + ' \n'
        text1 = ''.join(random.choice(pool) for _ in range(length1))
        text2 = ''.join(random.choice(pool) for _ in range(length2))
        print("Сгенерированы случайные тексты для f1 и f2.")
        return text1, text2

    else:
        examples = [
            ("Содержимое файла f1.\nПервая строка.\nВторая строка.",
             "А это файл f2.\nСовсем другой текст!"),
            ("Hello, world!\nCopy me.",
             "Привет, мир!\nСкопируй меня."),
            ("Одна строка в f1",
             "И одна строка в f2")
        ]
        print("Готовые примеры:")
        for idx, (t1, t2) in enumerate(examples, 1):
            print(f"{idx}: f1 = {repr(t1[:40])}... f2 = {repr(t2[:40])}...")
        while True:
            try:
                num = int(input("Выберите номер примера: "))
                if 1 <= num <= len(examples):
                    return examples[num - 1]
                else:
                    print(f"Номер от 1 до {len(examples)}.")
            except ValueError:
                print("Введите целое число.")


# ------------------------------------------------------------
# Основная программа
# ------------------------------------------------------------
def main():
    text1, text2 = get_file_contents()

    # Создаём исходные файлы
    create_text_file("f1.txt", text1)
    create_text_file("f2.txt", text2)

    print("\nСодержимое файлов ДО обмена:")
    print("f1.txt:\n" + read_file("f1.txt"))
    print("f2.txt:\n" + read_file("f2.txt"))

    # Выполняем обмен
    swap_files("f1.txt", "f2.txt", "h.txt")

    print("\nСодержимое файлов ПОСЛЕ обмена:")
    print("f1.txt:\n" + read_file("f1.txt"))
    print("f2.txt:\n" + read_file("f2.txt"))
    print("\nОбмен завершён. Вспомогательный файл h.txt использован для временного хранения.")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
