"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

521. Дан текстовый файл f. Переписать в файл g все компоненты файла f с заменой в них символа 0 на символ 1 и наоборот. 
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
    """Создаёт файл f с текстом, содержащим символы 0 и 1."""
    print("Файл f не существует или пуст. Задайте его содержимое.")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод строк (пустая строка — конец)")
    print("2 — Случайная генерация строк с 0 и 1")
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
            text = ("01010\n111000\nHello World!\n1010 0101\nPython 0 and 1\n000\n111")
        else:
            text = "\n".join(lines)
    elif choice == '2':
        n = random.randint(5, 12)  # количество строк
        lines = []
        for _ in range(n):
            length = random.randint(1, 60)
            # строка из случайных символов, среди которых часто встречаются 0 и 1
            chars = random.choices('01' + 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ' * 2, k=length)
            line = ''.join(chars)
            lines.append(line)
        text = "\n".join(lines)
        print(f"Сгенерировано {n} случайных строк.")
    else:  # готовый пример
        text = ("01010\n111000\nHello World!\n1010 0101\nPython 0 and 1\n000\n111")
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
# 3. Замена 0 ↔ 1 в файле
# ------------------------------------------------------------
def swap_zeros_ones(source, destination):
    """
    Читает файл source, заменяет все символы '0' на '1' и '1' на '0',
    результат записывает в файл destination.
    """
    text = read_file(source)
    # Таблица перевода: '0' → '1', '1' → '0'
    trans_table = str.maketrans('01', '10')
    transformed = text.translate(trans_table)
    create_text_file(destination, transformed)
    print(f"Замена выполнена. Результат записан в '{destination}'.")


# ------------------------------------------------------------
# 4. Основная программа
# ------------------------------------------------------------
def main():
    print("Задача 521: Замена символов 0 и 1 в текстовом файле")
    file_f = "f.txt"
    file_g = "g.txt"

    ensure_file_exists(file_f)

    print("\nИсходное содержимое f.txt:")
    print(read_file(file_f))

    swap_zeros_ones(file_f, file_g)

    print("\nСодержимое g.txt (после замены 0↔1):")
    print(read_file(file_g))


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")