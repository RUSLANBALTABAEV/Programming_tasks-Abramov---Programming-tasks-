"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

523. Дан текстовый файл f. Записать в перевернутом виде строки файла f в файл g. Порядок строк в файле g должен 
а) совпадать с порядком исходных строк в файле f;
б) быть обратным по отношению к порядку строк исходного файла.
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
# 2. Создание исходного файла f (если отсутствует или пуст)
# ------------------------------------------------------------
def create_file_f(filename):
    """Создаёт файл f с текстовыми строками."""
    print("Файл f не существует или пуст. Задайте содержимое файла.")
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
        print("Вводите строки. Для завершения — пустая строка.")
        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
        if not lines:
            print("Не введено ни одной строки. Будет использован готовый пример.")
            text = ("Hello World!\nPython is awesome.\nЭто третья строка.\nКонец файла.")
        else:
            text = "\n".join(lines)
    elif choice == '2':
        n = random.randint(4, 8)  # количество строк
        lines = []
        for _ in range(n):
            length = random.randint(5, 30)
            # генерируем случайную строку из букв, цифр и пробелов
            chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 '
            line = ''.join(random.choice(chars) for _ in range(length))
            lines.append(line)
        text = "\n".join(lines)
        print(f"Сгенерировано {n} случайных строк.")
    else:  # готовый пример
        text = "Hello World!\nPython is awesome.\nЭто третья строка.\nКонец файла."
        print("Использован готовый пример.")

    create_text_file(filename, text)
    print(f"Данные записаны в '{filename}'.")


def ensure_file_exists(filename):
    """Проверяет, существует ли файл и содержит ли данные. Если нет – создаёт."""
    if not os.path.exists(filename):
        create_file_f(filename)
        return
    content = read_file(filename).strip()
    if not content:
        create_file_f(filename)


# ------------------------------------------------------------
# 3. Обработка файла: переворот строк
# ------------------------------------------------------------
def reverse_lines_order_preserved(source, destination):
    """
    а) Переворачивает каждую строку, сохраняя порядок строк.
    """
    lines = read_file(source).splitlines()
    reversed_lines = [line[::-1] for line in lines]
    create_text_file(destination, "\n".join(reversed_lines))
    print(f"а) Записано в '{destination}' с сохранением порядка строк.")


def reverse_lines_order_reversed(source, destination):
    """
    б) Переворачивает каждую строку и записывает строки в обратном порядке.
    """
    lines = read_file(source).splitlines()
    reversed_lines = [line[::-1] for line in reversed(lines)]
    create_text_file(destination, "\n".join(reversed_lines))
    print(f"б) Записано в '{destination}' с обратным порядком строк.")


# ------------------------------------------------------------
# 4. Основная программа
# ------------------------------------------------------------
def main():
    print("Задача 523: Запись перевёрнутых строк в файл g")
    file_f = "f.txt"
    file_a = "g_a.txt"
    file_b = "g_b.txt"

    ensure_file_exists(file_f)

    print("\nИсходное содержимое f.txt:")
    print(read_file(file_f))

    reverse_lines_order_preserved(file_f, file_a)
    reverse_lines_order_reversed(file_f, file_b)

    print("\nРезультат а) (g_a.txt):")
    print(read_file(file_a))

    print("\nРезультат б) (g_b.txt):")
    print(read_file(file_b))


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")