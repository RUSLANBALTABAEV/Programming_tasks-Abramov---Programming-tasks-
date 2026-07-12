"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
12. Использование процедур 

В задачах этого параграфа будем для краткости говорить просто о процедурах, подразумевая, что решающий задачи сам выберет подходящее средство программирования – подпрограмму, функцию и 
т. д. Этот выбор должен быть сделан с учётом как характера задач, так и особенностей используемого языка программирования.

470. При выводе текстов на экран или печатающее устройство часто используются табуляционные остановки – выделенные позиции строки. Например, при печати таблиц полезно зафиксировать положение столбцов таблицы. Если в исходном тексте встречается символ табуляции tab (например, символ с кодом 9), это означает, что текст, следующий за символом tab, должен печататься со следующей табуляционной остановки, а до нее следует выдавать пробелы. Составить процедуру печати текста с указанной интерпретацией символа tab (предположить фиксированный набор табуляционных остановок).
"""


import random
import string


def print_with_tabs(text, tab_width = 8):
    """
    Процедура вывода текста с заменой символов табуляции '\t' пробелами
    до следующей табуляционной остановки. Остановки располагаются через
    каждые tab_width позиций.
    """
    result = []
    col = 0  # текущая позиция в строке

    for ch in text:
        if ch == '\t':
            # вычисляем позицию следующей табуляционной остановки
            next_stop = ((col // tab_width) + 1) * tab_width
            spaces = next_stop - col
            result.append(' ' * spaces)
            col = next_stop
        elif ch == '\n':
            result.append(ch)
            col = 0
        else:
            result.append(ch)
            col += 1

    print(''.join(result))


def get_text():
    """Выбор способа ввода текста, содержащего символы табуляции."""
    print("Задача 470: Печать текста с интерпретацией табуляции")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод")
    print("2 — Случайная генерация")
    print("3 — Готовые примеры")

    while True:
        choice = input("Ваш выбор (1/2/3): ").strip()
        if choice in ('1', '2', '3'):
            break
        print("Ошибка: выберите 1, 2 или 3.")

    if choice == '1':
        print("Введите текст (для табуляции используйте \\t, для новой строки \\n):")
        raw = input()
        # преобразуем escape-последовательности в реальные символы
        text = raw.replace('\\t', '\t').replace('\\n', '\n')
        try:
            w = int(input("Ширина табуляции (по умолчанию 8): ") or 8)
        except ValueError:
            w = 8
        return text, w

    elif choice == '2':
        # Генерируем случайную таблицу с несколькими столбцами
        cols = random.randint(2, 4)
        rows = random.randint(2, 5)
        lines = []
        for _ in range(rows):
            cells = []
            for _ in range(cols):
                word_len = random.randint(3, 8)
                word = ''.join(random.choice(string.ascii_letters) for _ in range(word_len))
                cells.append(word)
            lines.append('\t'.join(cells))
        text = '\n'.join(lines)
        w = random.choice([4, 8])
        print(f"Сгенерирован текст (ширина табуляции {w}):")
        print(repr(text))
        return text, w

    else:  # готовые примеры
        examples = [
            ("Name\tAge\tCity\nAlice\t25\tNew York\nBob\t30\tLos Angeles", 8),
            ("a\tb\tc\t\n1\t2\t3\t\nx\ty\tz\t", 4),
            ("One\tTwo\nThree\tFour", 10)
        ]
        print("Готовые примеры:")
        for idx, (t, w) in enumerate(examples, 1):
            print(f"{idx}: ширина = {w}, текст = {repr(t)}")
        while True:
            try:
                num = int(input("Выберите номер примера: "))
                if 1 <= num <= len(examples):
                    return examples[num - 1]
                else:
                    print(f"Номер от 1 до {len(examples)}.")
            except ValueError:
                print("Введите целое число.")


def main():
    text, tab_width = get_text()
    print("\nИсходный текст (repr):", repr(text))
    print("Результат с интерпретацией табуляции:")
    print_with_tabs(text, tab_width)


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
