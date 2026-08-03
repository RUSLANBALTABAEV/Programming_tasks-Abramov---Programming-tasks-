"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

504. Прямая на плоскости задается уравнением ax+by+c=0, где a и b одновременно не равны нулю. Будем рассматривать только прямые, для которых коэффициенты a, b, c–целые числа. Пусть f – файл, содержащий коэффициенты нескольких прямых (не менее трех). 
Переписать из файла f в файл g коэффициенты тех прямых, которые 
а) параллельны первой из прямых, заданной в файле f;
б) указаны в а), но дополнительно требуется, чтобы все прямые
были различны;
в) пересекают первую из прямых, заданных в файле f;
г) указаны в в), но дополнительно требуется, чтобы среди прямых не было параллельных.
"""


import random
import math
import os


# ------------------------------------------------------------
# 1. Процедуры работы с файлами (как в задаче 497)
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
    """Создаёт файл f с коэффициентами прямых (не менее трёх)."""
    print("Файл f не существует, пуст или содержит недостаточно данных.")
    print("Требуется не менее трёх прямых с целыми коэффициентами a, b, c,")
    print("где a и b не равны нулю одновременно.")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод (введите строки вида 'a b c', пустая строка — конец)")
    print("2 — Случайная генерация (7 прямых)")
    print("3 — Готовый пример (7 прямых)")

    while True:
        choice = input("Ваш выбор (1/2/3): ").strip()
        if choice in ('1', '2', '3'):
            break
        print("Ошибка: выберите 1, 2 или 3.")

    if choice == '1':
        print("Вводите по одной строке на прямую. Для завершения введите пустую строку.")
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
            # добавим случайные прямые до трёх
            while len(lines) < 3:
                a = random.randint(-3, 3)
                b = random.randint(-3, 3)
                if a == 0 and b == 0:
                    b = 1
                c = random.randint(-5, 5)
                lines.append(f"{a} {b} {c}")
        text = "\n".join(lines)
    elif choice == '2':
        # Генерируем 7 случайных прямых, где первая выделена, есть параллельные и пересекающие
        first = (1, 1, 1)
        variants = [
            (2, 2, 2),  # совпадает с первой
            (1, 1, -5),  # параллельна
            (1, 2, 3),   # пересекает
            (2, 4, 6),   # пересекает, совпадает с предыдущей
            (2, 1, 0),   # пересекает
            (3, 6, 0)    # пересекает, но параллельна (1,2,3) и (2,4,6)
        ]
        lines_list = [first] + variants
        text = "\n".join(f"{a} {b} {c}" for a, b, c in lines_list)
        print("Сгенерированы 7 прямых с целыми коэффициентами.")
    else:  # готовый пример (такой же набор)
        first = (1, 1, 1)
        variants = [
            (2, 2, 2), (1, 1, -5), (1, 2, 3),
            (2, 4, 6), (2, 1, 0), (3, 6, 0)
        ]
        lines_list = [first] + variants
        text = "\n".join(f"{a} {b} {c}" for a, b, c in lines_list)
        print("Использован готовый пример (7 прямых).")

    create_text_file(filename, text)
    print(f"Содержимое записано в '{filename}'.")


def ensure_file_exists(filename):
    """Проверяет, существует ли файл, содержит ли он не менее трёх корректных прямых.
       Если нет – создаёт его."""
    if not os.path.exists(filename):
        create_file_f(filename)
        return
    raw = read_file(filename).strip()
    if not raw:
        create_file_f(filename)
        return
    lines = raw.splitlines()
    valid_lines = 0
    for line in lines:
        parts = line.strip().split()
        if len(parts) == 3:
            try:
                a, b, c = map(int, parts)
                if not (a == 0 and b == 0):
                    valid_lines += 1
            except ValueError:
                pass
    if valid_lines < 3:
        print(f"Файл '{filename}' содержит только {valid_lines} корректные прямые. Требуется не менее трёх.")
        create_file_f(filename)


# ------------------------------------------------------------
# 3. Геометрические процедуры
# ------------------------------------------------------------
def are_parallel(l1, l2):
    """Проверяет, параллельны ли две прямые (включая совпадающие)."""
    a1, b1, _ = l1
    a2, b2, _ = l2
    return a1 * b2 - b1 * a2 == 0


def normalize_line(line):
    """Приводит коэффициенты к каноническому виду (для удаления дубликатов)."""
    a, b, c = line
    g = math.gcd(abs(a), math.gcd(abs(b), abs(c)))
    if g != 0:
        a //= g
        b //= g
        c //= g
    # Делаем первый ненулевой коэффициент положительным
    if a < 0 or (a == 0 and b < 0):
        a, b, c = -a, -b, -c
    return (a, b, c)


# ------------------------------------------------------------
# 4. Основная программа
# ------------------------------------------------------------
def main():
    print("Задача 504: Обработка прямых на плоскости")
    file_f = "f.txt"

    # Убеждаемся, что файл f существует и содержит >=3 корректных прямых
    ensure_file_exists(file_f)

    # Читаем прямые
    raw = read_file(file_f).strip().splitlines()
    all_lines = []
    for line in raw:
        parts = line.split()
        if len(parts) == 3:
            a, b, c = map(int, parts)
            if not (a == 0 and b == 0):
                all_lines.append((a, b, c))

    if len(all_lines) < 3:
        print("Ошибка: недостаточно прямых (требуется минимум 3).")
        return

    first = all_lines[0]
    print(f"Первая прямая: {first}")

    # а) параллельные первой
    parallel_a = [l for l in all_lines[1:] if are_parallel(first, l)]
    create_text_file("g_a.txt", "\n".join(f"{a} {b} {c}" for a, b, c in parallel_a))
    print(f"а) Параллельных: {len(parallel_a)} → g_a.txt")

    # б) параллельные и различные (убираем совпадающие)
    unique_map = {}
    for l in parallel_a:
        norm = normalize_line(l)
        if norm not in unique_map:
            unique_map[norm] = l
    distinct_b = list(unique_map.values())
    create_text_file("g_b.txt", "\n".join(f"{a} {b} {c}" for a, b, c in distinct_b))
    print(f"б) Различных параллельных: {len(distinct_b)} → g_b.txt")

    # в) пересекающие первую
    intersect_c = [l for l in all_lines[1:] if not are_parallel(first, l)]
    create_text_file("g_c.txt", "\n".join(f"{a} {b} {c}" for a, b, c in intersect_c))
    print(f"в) Пересекающих: {len(intersect_c)} → g_c.txt")

    # г) пересекающие первую и не параллельные друг другу
    result_d = []
    for l in intersect_c:
        if not any(are_parallel(l, chosen) for chosen in result_d):
            result_d.append(l)
    create_text_file("g_d.txt", "\n".join(f"{a} {b} {c}" for a, b, c in result_d))
    print(f"г) Пересекающих без взаимной параллельности: {len(result_d)} → g_d.txt")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")