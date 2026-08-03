"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

505. Условие предыдущей задачи сохраняется. Требуется получить в файле g коэффициенты всех различных прямых файла f.
"""


import random
import math
import os


# ------------------------------------------------------------
# 1. Процедуры работы с файлами (общие)
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
# 2. Создание исходного файла f (если отсутствует или содержит менее трёх прямых)
# ------------------------------------------------------------
def create_file_f(filename):
    """Создаёт файл f с коэффициентами прямых (не менее трёх)."""
    print("Файл f не существует, пуст или содержит менее трёх корректных прямых.")
    print("Требуются прямые с целыми коэффициентами a, b, c (a и b не равны нулю одновременно).")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод (вводите строки вида 'a b c', пустая строка — конец)")
    print("2 — Случайная генерация (7 прямых, включая совпадающие)")
    print("3 — Готовый пример (7 прямых)")

    while True:
        choice = input("Ваш выбор (1/2/3): ").strip()
        if choice in ('1', '2', '3'):
            break
        print("Ошибка: выберите 1, 2 или 3.")

    if choice == '1':
        print("Вводите по одной прямой на строку. Для завершения введите пустую строку.")
        lines = []
        while True:
            line = input().strip()
            if line == "":
                break
            parts = line.split()
            if len(parts) != 3:
                print("  Ошибка: нужно ровно три целых числа. Попробуйте снова.")
                continue
            try:
                a, b, c = map(int, parts)
            except ValueError:
                print("  Ошибка: введите целые числа.")
                continue
            if a == 0 and b == 0:
                print("  Ошибка: a и b не могут быть нулями одновременно.")
                continue
            lines.append(f"{a} {b} {c}")
        if len(lines) < 3:
            print("Предупреждение: введено менее трёх прямых. Будут добавлены дополнительные.")
            while len(lines) < 3:
                a = random.randint(-3, 3)
                b = random.randint(-3, 3)
                if a == 0 and b == 0:
                    b = 1
                c = random.randint(-5, 5)
                lines.append(f"{a} {b} {c}")
        text = "\n".join(lines)
    elif choice == '2':
        # Набор прямых: первая базовая, а затем дубликаты и параллельные варианты
        base = (1, 1, 1)
        variants = [
            (2, 2, 2),   # совпадает с первой (пропорциональна)
            (1, 1, -5),  # параллельна, но другая
            (1, 2, 3),   # пересекает
            (2, 4, 6),   # совпадает с предыдущей
            (2, 1, 0),   # пересекает
            (3, 6, 0)    # пересекает, но параллельна (1,2,3)
        ]
        lines_list = [base] + variants
        text = "\n".join(f"{a} {b} {c}" for a, b, c in lines_list)
        print("Сгенерированы 7 прямых с целыми коэффициентами.")
    else:  # готовый пример
        lines_list = [
            (1, 1, 1),
            (2, 2, 2),
            (1, 1, -5),
            (1, 2, 3),
            (2, 4, 6),
            (2, 1, 0),
            (3, 6, 0)
        ]
        text = "\n".join(f"{a} {b} {c}" for a, b, c in lines_list)
        print("Использован готовый пример (7 прямых).")

    create_text_file(filename, text)
    print(f"Содержимое записано в '{filename}'.")


def ensure_file_exists(filename):
    """Проверяет, существует ли файл и содержит ли он не менее трёх корректных прямых.
       Если нет – создаёт его."""
    if not os.path.exists(filename):
        create_file_f(filename)
        return
    raw = read_file(filename).strip()
    if not raw:
        create_file_f(filename)
        return
    lines = raw.splitlines()
    valid = 0
    for line in lines:
        parts = line.strip().split()
        if len(parts) == 3:
            try:
                a, b, c = map(int, parts)
                if not (a == 0 and b == 0):
                    valid += 1
            except ValueError:
                pass
    if valid < 3:
        print(f"Файл '{filename}' содержит только {valid} корректные прямые. Нужно не менее трёх.")
        create_file_f(filename)


# ------------------------------------------------------------
# 3. Нормализация прямой (для выявления дубликатов)
# ------------------------------------------------------------
def normalize_line(line):
    """Приводит коэффициенты к каноническому виду:
       сокращает на НОД и делает первый ненулевой коэффициент положительным."""
    a, b, c = line
    g = math.gcd(abs(a), math.gcd(abs(b), abs(c)))
    if g != 0:
        a //= g
        b //= g
        c //= g
    if a < 0 or (a == 0 and b < 0):
        a, b, c = -a, -b, -c
    return (a, b, c)


# ------------------------------------------------------------
# 4. Основная программа
# ------------------------------------------------------------
def main():
    print("Задача 505: Получить коэффициенты всех различных прямых")
    file_f = "f.txt"
    file_g = "g.txt"

    # Проверяем и, если нужно, создаём файл f
    ensure_file_exists(file_f)

    # Читаем прямые из файла
    raw = read_file(file_f).strip().splitlines()
    all_lines = []
    for line in raw:
        parts = line.split()
        if len(parts) == 3:
            a, b, c = map(int, parts)
            if not (a == 0 and b == 0):
                all_lines.append((a, b, c))

    print(f"Всего прямых в исходном файле: {len(all_lines)}")

    # Отбираем уникальные (различные) прямые
    unique_map = {}
    for line in all_lines:
        norm = normalize_line(line)
        if norm not in unique_map:
            unique_map[norm] = line  # можно сохранить любой из совпадающих, здесь – исходный
    distinct_lines = list(unique_map.keys())  # или unique_map.values() – без разницы

    # Записываем результат в файл g
    create_text_file(file_g,
                     "\n".join(f"{a} {b} {c}" for a, b, c in distinct_lines))
    print(f"Различных прямых: {len(distinct_lines)} → записаны в '{file_g}'.")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")