"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

518. Даны натуральное k, символьный файл f и текстовый файл f1 *). Файл f содержит 30 слов (см. задачу 497), каждое из которых будем называть ключевым. Сформировать файл g, который содержит строки файла f1, циклически сдвинутые так, чтобы каждое ключевое слово, входящее в строку, начиналось с k-й позиции. Строки, не содержащие ключевых слов, в файл g не включаются. Строки, которые содержат n ключевых слов, записываются в файл g n раз. 
*) Текстовым называется файл, компоненты которого являются строками. Будем предполагать, что строки имеют произвольную длину, не превосходящую некоторого оговоренного числа символов, например 255.
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
# 2. Создание файлов f (ключевые слова) и f1 (текстовые строки)
# ------------------------------------------------------------
def create_files():
    """Создаёт оба входных файла f и f1 по выбору пользователя."""
    print("Необходимы файлы f.txt (30 ключевых слов) и f1.txt (текстовые строки).")
    print("Выберите способ ввода данных:")
    print("1 — Ручной ввод")
    print("2 — Случайная генерация")
    print("3 — Готовый пример")

    while True:
        choice = input("Ваш выбор (1/2/3): ").strip()
        if choice in ('1', '2', '3'):
            break
        print("Ошибка: выберите 1, 2 или 3.")

    if choice == '1':
        # Ручной ввод ключевых слов
        print("\nВведите 30 ключевых слов через пробел (строка должна содержать ровно 30 слов):")
        while True:
            keys_input = input().strip()
            keys_list = keys_input.split()
            if len(keys_list) != 30:
                print(f"  Ошибка: нужно ровно 30 слов, а введено {len(keys_list)}. Повторите.")
                continue
            break
        text_f = ' '.join(keys_list)

        # Ручной ввод строк f1
        print("Введите строки текстового файла f1. Для завершения введите пустую строку.")
        lines_f1 = []
        while True:
            line = input()
            if line == "":
                break
            lines_f1.append(line)
        if not lines_f1:
            lines_f1 = ["word5 and word15 are here.", "No keywords."]
            print("  Использованы строки по умолчанию.")
        text_f1 = "\n".join(lines_f1)

    elif choice == '2':
        # Случайная генерация
        word_pool = [f"word{i}" for i in range(1, 31)]
        random.shuffle(word_pool)
        text_f = ' '.join(word_pool)  # 30 слов

        num_lines = random.randint(3, 6)
        lines_f1 = []
        for _ in range(num_lines):
            words_in_line = random.randint(1, 5)
            # составляем строку из случайных ключевых слов и произвольных слов
            line_words = []
            for _ in range(words_in_line):
                if random.random() < 0.7:
                    line_words.append(random.choice(word_pool))
                else:
                    line_words.append(f"extra_{random.randint(100,999)}")
            # добавляем обычные слова вокруг
            lines_f1.append(' '.join(line_words))
        text_f1 = "\n".join(lines_f1)
        print("Сгенерированы случайные ключевые слова и строки.")
    else:  # готовый пример
        text_f = ' '.join([f"word{i}" for i in range(1, 31)])
        text_f1 = ("word5 and word15 are here.\n"
                   "This line has only word20.\n"
                   "word25 word25 and word30.\n"
                   "No keywords here, so ignore me.\n"
                   "word10 at the end of this line word10.")
        print("Использован готовый пример.")

    create_text_file("f.txt", text_f)
    create_text_file("f1.txt", text_f1)
    print("Файлы f.txt и f1.txt созданы.\n")


def ensure_files_exist():
    """Проверяет существование и корректность файлов f и f1. Если что-то не так – создаёт заново."""
    if not os.path.exists("f.txt") or not os.path.exists("f1.txt"):
        create_files()
        return

    # Проверка содержимого f (должен содержать ровно 30 слов)
    f_content = read_file("f.txt").strip()
    f_words = f_content.split()
    if len(f_words) != 30:
        print("Файл f.txt должен содержать ровно 30 ключевых слов.")
        create_files()
        return

    # Проверка содержимого f1 (должен содержать хотя бы одну строку)
    f1_content = read_file("f1.txt").strip()
    if not f1_content:
        print("Файл f1.txt пуст.")
        create_files()
        return


# ------------------------------------------------------------
# 3. Логика задачи 518
# ------------------------------------------------------------
def find_keyword_positions(line, keywords):
    """Возвращает список всех позиций и соответствующих ключевых слов в строке."""
    matches = []
    for kw in keywords:
        start = 0
        while True:
            pos = line.find(kw, start)
            if pos == -1:
                break
            matches.append((pos, kw))
            start = pos + 1
    matches.sort()  # для предсказуемого порядка
    return matches


def cyclic_shift(line, pos, k):
    """
    Циклически сдвигает строку так, чтобы символ, находящийся
    на позиции pos (0-индексация), оказался на позиции k-1.
    """
    if not line:
        return line
    target = k - 1
    shift = (pos - target) % len(line)
    return line[shift:] + line[:shift]


def process_files(k):
    """Формирует файл g согласно условию задачи."""
    # Читаем ключевые слова из f
    f_words = read_file("f.txt").split()
    keywords = f_words[:30]

    # Читаем строки из f1
    f1_content = read_file("f1.txt").strip()
    if not f1_content:
        print("Файл f1.txt пуст.")
        return
    lines_f1 = f1_content.splitlines()

    with open("g.txt", 'w', encoding='utf-8') as g:
        count = 0
        for line in lines_f1:
            matches = find_keyword_positions(line, keywords)
            if not matches:
                continue
            for pos, kw in matches:
                shifted = cyclic_shift(line, pos, k)
                g.write(shifted + '\n')
                count += 1
    print(f"Сформирован файл g.txt, записано строк: {count}")


# ------------------------------------------------------------
# 4. Основная программа
# ------------------------------------------------------------
def main():
    print("Задача 518: Циклический сдвиг строк по ключевым словам")
    ensure_files_exist()

    try:
        k = int(input("Введите натуральное число k (позиция для ключевого слова): "))
        if k < 1:
            print("k должно быть > 0.")
            return
    except ValueError:
        print("Ошибка: введите целое число.")
        return

    process_files(k)

    print("\nСодержимое g.txt:")
    print(read_file("g.txt"))


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")