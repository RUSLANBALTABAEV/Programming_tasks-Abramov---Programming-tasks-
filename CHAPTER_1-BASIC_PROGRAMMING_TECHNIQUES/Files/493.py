"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

493. Дан символьный файл f.
а) Подсчитать число вхождений в файл сочетаний ab.
б) Определить, входит ли в файл сочетание abcdefgh.
в) Подсчитать число вхождений в файл каждой из букв a, b, c, d, e, f и вывести результат в виде таблицы
                          a - Na b - Nb c - Nc
                          d - Nd e - Ne f - Nf
где Na, Nb, Nc, Nd, Ne, Nf - числа вхождений соответствующих букв.
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
        # Генерируем случайный текст, содержащий буквы a-f и сочетания "ab"
        length = random.randint(30, 150)
        chars = string.ascii_letters + string.digits + ' \n'
        text = ''.join(random.choice(chars) for _ in range(length))
        # Добавим несколько сочетаний "ab" для проверки
        text = text.replace('ab', 'ab', random.randint(2, 5))
        # Иногда вставим "abcdefgh"
        if random.random() < 0.5:
            text += " abcdefgh"
        print("Сгенерирован случайный текст.")
    else:  # готовый пример
        text = (
            "Hello ab world!\n"
            "abcdefgh is a sequence.\n"
            "ab ab ab\n"
            "a b c d e f and some text.\n"
            "Final line with a and b."
        )
        print("Готовый пример выбран.")

    create_text_file(filename, text)
    print(f"Содержимое записано в '{filename}'.")


# ------------------------------------------------------------
# 3. Анализ файла (пункты а, б, в)
# ------------------------------------------------------------
def analyze_file(filename):
    """
    Выполняет анализ символьного файла:
    а) подсчитывает число вхождений 'ab';
    б) проверяет наличие 'abcdefgh';
    в) подсчитывает вхождения букв a–f и выводит таблицу.
    """
    content = read_file(filename)

    # а) Подсчитать число вхождений 'ab'
    count_ab = content.count('ab')

    # б) Проверить наличие 'abcdefgh'
    has_abcdefgh = 'abcdefgh' in content

    # в) Подсчитать вхождения каждой буквы
    target_letters = 'abcdef'
    letter_counts = {ch: 0 for ch in target_letters}
    for ch in content:
        if ch in letter_counts:
            letter_counts[ch] += 1

    # Вывод результатов
    print("=" * 40)
    print(f"а) Число вхождений сочетания 'ab': {count_ab}")
    print(f"б) Сочетание 'abcdefgh' входит в файл? {'Да' if has_abcdefgh else 'Нет'}")
    print("\nв) Таблица вхождений букв a–f:")
    print(f"a – {letter_counts['a']}   b – {letter_counts['b']}   c – {letter_counts['c']}")
    print(f"d – {letter_counts['d']}   e – {letter_counts['e']}   f – {letter_counts['f']}")
    print("=" * 40)


# ------------------------------------------------------------
# 4. Основная программа
# ------------------------------------------------------------
def main():
    print("Задача 493: Анализ символьного файла")
    filename = "f.txt"

    # Проверка существования и непустоты файла
    if not os.path.exists(filename) or not read_file(filename).strip():
        create_file_f(filename)

    print("\nИсходное содержимое f.txt:")
    print(read_file(filename))
    print()

    analyze_file(filename)


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")