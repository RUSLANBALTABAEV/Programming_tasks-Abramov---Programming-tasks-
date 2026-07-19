"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

479. Дан символьный файл f. В файле f не менее двух компонент. Определить, являются ли два первых символа файла цифрами. Если да, то установить, является ли число, образованное этими цифрами, четным.
"""


import random
import string


# ------------------------------------------------------------
# 1. Процедуры работы с файлом
# ------------------------------------------------------------
def create_text_file(filename, text):
    """Создаёт (или перезаписывает) текстовый файл с указанным содержимым."""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)


def read_first_two_chars(filename):
    """Читает первые два символа из файла и возвращает их (или меньше, если файл короче)."""
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read(2)


# ------------------------------------------------------------
# 2. Анализ первых двух символов
# ------------------------------------------------------------
def analyze_file(filename):
    """
    Проверяет, являются ли два первых символа файла цифрами,
    и если да, то является ли образованное ими число чётным.
    """
    chars = read_first_two_chars(filename)
    if len(chars) < 2:
        print("Ошибка: файл содержит менее двух символов.")
        return

    print(f"Первые два символа: '{chars[0]}' и '{chars[1]}'")

    if chars[0].isdigit() and chars[1].isdigit():
        print("Оба символа являются цифрами.")
        number = int(chars[0] + chars[1])
        if number % 2 == 0:
            print(f"Число {number} — чётное.")
        else:
            print(f"Число {number} — нечётное.")
    else:
        print("Не оба символа являются цифрами (или вовсе не цифры).")


# ------------------------------------------------------------
# 3. Ввод данных (создание файла f)
# ------------------------------------------------------------
def get_file_content():
    """Выбор способа задания содержимого файла f."""
    print("Задача 479: Анализ первых двух символов файла")
    print("Выберите способ задания содержимого файла f:")
    print("1 — Ручной ввод")
    print("2 — Случайная генерация")
    print("3 — Готовые примеры")

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
        if len(text) < 2:
            print("Текст должен содержать хотя бы два символа. Добавлены пробелы.")
            text = text.ljust(2, ' ')
        return text

    elif choice == '2':
        # Генерируем случайный текст длиной от 2 до 50 символов
        length = random.randint(2, 50)
        # Иногда делаем первые два символа цифрами (с вероятностью 0.5)
        if random.random() < 0.5:
            # Первые два символа — случайные цифры
            prefix = ''.join(random.choice(string.digits) for _ in range(2))
            suffix_length = max(0, length - 2)
            suffix = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation + ' ') for _ in range(suffix_length))
            text = prefix + suffix
        else:
            # Просто случайные символы (первые два могут быть любыми)
            text = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation + ' ') for _ in range(length))
        print("Сгенерирован случайный текст для файла f.")
        return text

    else:  # готовые примеры
        examples = [
            "24abc",                   # цифры, чётное
            "37xyz",                   # цифры, нечётное
            "a1b2c",                   # не цифры
            "00",                      # цифры, чётное (ноль)
            "99"                       # цифры, нечётное
        ]
        print("Готовые примеры:")
        for idx, txt in enumerate(examples, 1):
            print(f"{idx}: {repr(txt)}")
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
# 4. Основная программа
# ------------------------------------------------------------
def main():
    text = get_file_content()
    create_text_file("f.txt", text)
    print("\nСодержимое файла f.txt:")
    with open("f.txt", 'r', encoding='utf-8') as f:
        print(f.read())

    print()
    analyze_file("f.txt")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
