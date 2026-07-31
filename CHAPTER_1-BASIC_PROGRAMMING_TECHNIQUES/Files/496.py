"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

496. Дан символьный файл f. Записать в файл g с сохранением порядка следования те символы файла f:
а) которым в этом файле предшествует буква а;
б) вслед за которым в этом файле идет буква а.
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
    print("2 — Случайная генерация текста (с буквами 'a')")
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
        # Генерируем случайный текст, содержащий буквы (особенно 'a')
        length = random.randint(15, 40)
        chars = string.ascii_letters + string.digits + ' \n'
        text = ''.join(random.choice(chars) for _ in range(length))
        # Увеличим вероятность появления 'a' для наглядности
        text = text.replace('a', 'a', random.randint(3, 8))
        print("Сгенерирован случайный текст с несколькими 'a'.")
    else:  # готовый пример
        text = "xabacadefag"
        print("Готовый пример: 'xabacadefag'.")

    create_text_file(filename, text)
    print(f"Содержимое записано в '{filename}'.")


def ensure_file_exists(filename, name):
    """Проверяет, существует ли файл и не пуст ли он; если нет – создаёт."""
    if not os.path.exists(filename) or not read_file(filename).strip():
        create_file_f(filename)


# ------------------------------------------------------------
# 3. Процедуры для пунктов а) и б)
# ------------------------------------------------------------
def extract_after_a(source, destination):
    """
    а) Записывает в destination все символы из source,
    которым предшествует буква 'a' (т.е. следующие сразу за 'a').
    """
    content = read_file(source)
    result = []
    for i in range(1, len(content)):
        if content[i - 1] == 'a':
            result.append(content[i])
    create_text_file(destination, ''.join(result))
    print(f"Пункт а) выполнен: {len(result)} символов записаны в '{destination}'.")


def extract_before_a(source, destination):
    """
    б) Записывает в destination все символы из source,
    вслед за которыми идёт буква 'a' (т.е. непосредственно перед 'a').
    """
    content = read_file(source)
    result = []
    for i in range(len(content) - 1):
        if content[i + 1] == 'a':
            result.append(content[i])
    create_text_file(destination, ''.join(result))
    print(f"Пункт б) выполнен: {len(result)} символов записаны в '{destination}'.")


# ------------------------------------------------------------
# 4. Основная программа
# ------------------------------------------------------------
def main():
    print("Задача 496: Символы, граничащие с буквой 'a'")
    file_f = "f.txt"
    file_g_a = "g_a.txt"
    file_g_b = "g_b.txt"

    # Убеждаемся, что файл f существует
    ensure_file_exists(file_f, 'f')

    # Выводим исходный текст
    print("\nИсходное содержимое f.txt:")
    print(read_file(file_f))

    # Выполняем оба пункта
    extract_after_a(file_f, file_g_a)
    extract_before_a(file_f, file_g_b)

    # Выводим результаты
    print("\nРезультаты:")
    print(f"g_a.txt (после 'a'): {read_file(file_g_a)}")
    print(f"g_b.txt (перед 'a'): {read_file(file_g_b)}")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")