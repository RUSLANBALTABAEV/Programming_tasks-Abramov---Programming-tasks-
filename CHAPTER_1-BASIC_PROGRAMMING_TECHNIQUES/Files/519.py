"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

519. Даны текстовый файл f, содержащий программу на языке Паскаль. Проверить эту программу на несоответствие числа открывающих и закрывающих круглых скобок. Считать, что каждый оператор программы
а) занимает не более одной строки файла f;
б) может занимать произвольное число строк файла f.
"""


import random
import os


# ------------------------------------------------------------
# 1. Общие процедуры работы с файлами
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
    """Создаёт файл f с программой на Паскале."""
    print("Файл f не существует или пуст. Задайте текст программы на Паскале.")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод (пустая строка — конец)")
    print("2 — Случайная генерация (программа с возможными ошибками скобок)")
    print("3 — Готовый пример")

    while True:
        choice = input("Ваш выбор (1/2/3): ").strip()
        if choice in ('1', '2', '3'):
            break
        print("Ошибка: выберите 1, 2 или 3.")

    if choice == '1':
        print("Вводите строки программы. Для завершения — пустая строка.")
        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
        if not lines:
            print("Не введено ни одной строки. Будет использован готовый пример.")
            text = ("program test;\nbegin\n    writeln('Hello');\n"
                    "    if (a > b) then\n        begin\n"
                    "            a := a + 1;\n            b := b + 2);  // Ошибка\n"
                    "        end;\n    writeln('Done');\nend.")
        else:
            text = "\n".join(lines)
    elif choice == '2':
        # Случайно генерируем строки, похожие на код, иногда нарушая баланс скобок
        statements = ["a := b + c;", "if (x > 0) then", "begin", "end;",
                      "writeln('ok');", "for i := 1 to n do", "a := (b + c) * d;"]
        num_lines = random.randint(5, 10)
        lines = []
        open_cnt = 0
        for _ in range(num_lines):
            stmt = random.choice(statements)
            # Вставим лишнюю скобку с вероятностью 30%
            if random.random() < 0.3:
                if random.random() < 0.5:
                    stmt = stmt.replace('(', '((')
                else:
                    stmt = stmt.replace(')', '))')
            lines.append(stmt)
        text = "\n".join(lines)
        print("Сгенерирована случайная программа (возможно, с ошибками скобок).")
    else:  # готовый пример
        text = ("program test;\nbegin\n    writeln('Hello');\n"
                "    if (a > b) then\n        begin\n"
                "            a := a + 1;\n            b := b + 2);  // Ошибка\n"
                "        end;\n    writeln('Done');\nend.")
        print("Использован готовый пример программы.")

    create_text_file(filename, text)
    print(f"Текст программы записан в '{filename}'.")


def ensure_file_exists(filename):
    """Проверяет, существует ли файл и содержит ли данные. Если нет – создаёт."""
    if not os.path.exists(filename):
        create_file_f(filename)
        return
    content = read_file(filename).strip()
    if not content:
        create_file_f(filename)


# ------------------------------------------------------------
# 3. Проверка баланса скобок
# ------------------------------------------------------------
def count_parentheses(text):
    """Возвращает количество открывающих и закрывающих круглых скобок в тексте."""
    return text.count('('), text.count(')')


def check_balance_a(filename):
    """
    а) Проверка построчно: каждый оператор – не более одной строки.
    Выводит сообщения об ошибках в конкретных строках.
    """
    print("--- а) Проверка построчно (оператор на одной строке) ---")
    content = read_file(filename)
    if not content:
        print("   Файл пуст.")
        return

    lines = content.splitlines()
    has_error = False
    for i, line in enumerate(lines, start=1):
        open_cnt, close_cnt = count_parentheses(line)
        if open_cnt != close_cnt:
            print(f"   ❌ Ошибка в строке {i}: {open_cnt} откр., {close_cnt} закр.")
            print(f"      {line}")
            has_error = True

    if not has_error:
        print("   ✅ Во всех строках количество скобок совпадает.")


def check_balance_b(filename):
    """
    б) Проверка по всему файлу: оператор может занимать несколько строк.
    Выводит общий итог.
    """
    print("\n--- б) Проверка по всему файлу (оператор может быть на нескольких строках) ---")
    content = read_file(filename)
    if not content:
        print("   Файл пуст.")
        return

    open_cnt, close_cnt = count_parentheses(content)
    if open_cnt == close_cnt:
        print(f"   ✅ Общий баланс соблюдён: {open_cnt} откр. и {close_cnt} закр. скобок.")
    else:
        print(f"   ❌ Общий баланс нарушен: {open_cnt} откр., {close_cnt} закр.")


# ------------------------------------------------------------
# 4. Основная программа
# ------------------------------------------------------------
def main():
    print("Задача 519: Проверка баланса круглых скобок в программе Паскаль")
    file_f = "f.txt"

    ensure_file_exists(file_f)

    print("\nСодержимое файла f.txt:")
    print(read_file(file_f))
    print("-" * 50)

    check_balance_a(file_f)
    check_balance_b(file_f)


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")