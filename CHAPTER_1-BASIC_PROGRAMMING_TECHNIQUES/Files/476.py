"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

476. Дан символьный файл *) f. Получить копию файла в файле g.
*) Файл, компоненты которого являются символами, называется символьным файлом.
"""


import random
import string


# ------------------------------------------------------------
# 1. Процедуры работы с файлами
# ------------------------------------------------------------
def create_text_file(filename, text):
    """Создаёт (или перезаписывает) текстовый файл с указанным содержимым."""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)


def copy_file(source, destination):
    """Копирует содержимое символьного файла source в файл destination."""
    with open(source, 'r', encoding='utf-8') as src:
        content = src.read()
    with open(destination, 'w', encoding='utf-8') as dst:
        dst.write(content)


def read_file(filename):
    """Читает и возвращает содержимое текстового файла."""
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()


# ------------------------------------------------------------
# 2. Ввод содержимого исходного файла f
# ------------------------------------------------------------
def get_file_content():
    """Выбор способа ввода содержимого для файла f."""
    print("Задача 476: Копирование символьного файла f в файл g")
    print("Выберите способ задания содержимого файла f:")
    print("1 — Ручной ввод (введите строку)")
    print("2 — Случайная генерация текста")
    print("3 — Готовый пример")

    while True:
        choice = input("Ваш выбор (1/2/3): ").strip()
        if choice in ('1', '2', '3'):
            break
        print("Ошибка: выберите 1, 2 или 3.")

    if choice == '1':
        print("Введите текст (можно несколько строк). Для окончания введите пустую строку:")
        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
        text = "\n".join(lines)
        return text

    elif choice == '2':
        # Генерируем случайный текст: буквы, цифры, знаки препинания, пробелы, переводы строк
        length = random.randint(50, 200)
        pool = string.ascii_letters + string.digits + string.punctuation + ' \n'
        text = ''.join(random.choice(pool) for _ in range(length))
        print("Сгенерирован случайный текст для файла f.")
        return text

    else:  # готовые примеры
        examples = [
            "Hello, world!\nThis is a sample text.\nCopy me to another file.",
            "А роза упала на лапу Азора.\nСимвольный файл может содержать русские буквы.\n1234567890\n!@#$%^&*()",
            "One line text without newlines."
        ]
        print("Готовые примеры текста:")
        for idx, txt in enumerate(examples, 1):
            print(f"{idx}: {repr(txt[:60])}...")
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
# 3. Основная программа
# ------------------------------------------------------------
def main():
    # Создаём файл f с выбранным содержимым
    text = get_file_content()
    create_text_file("f.txt", text)

    # Копируем f в g
    copy_file("f.txt", "g.txt")
    print("\nФайл f.txt скопирован в g.txt.")

    # Выводим содержимое для проверки
    print("\nСодержимое f.txt:")
    print(read_file("f.txt"))
    print("\nСодержимое g.txt (копия):")
    print(read_file("g.txt"))


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
