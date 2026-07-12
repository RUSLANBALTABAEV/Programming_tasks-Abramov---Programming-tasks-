"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
12. Использование процедур 

В задачах этого параграфа будем для краткости говорить просто о процедурах, подразумевая, что решающий задачи сам выберет подходящее средство программирования – подпрограмму, функцию и 
т. д. Этот выбор должен быть сделан с учётом как характера задач, так и особенностей используемого языка программирования.

469. Выравнивание строки заключается в том, что между ее отдельными словами (см. задачу 269) дополнительно вносятся пробелы так, чтобы длина строки стала равной заданной длине (предполагается, что требуемая длина не меньше исходной), а последнее слово строки сдвинулось к ее правому краю. Составить процедуру выравнивания заданной строки текста. 
"""


import random
import string


def align_string(text, target_length):
    """
    Процедура выравнивания строки.
    Распределяет пробелы между словами так, чтобы:
    – длина итоговой строки была равна target_length (>= исходной длины текста),
    – последнее слово оказалось у правого края.
    """
    if target_length < len(text):
        return text  # если заданная длина меньше исходной, возвращаем без изменений

    words = text.split()
    if not words:
        return ' ' * target_length

    total_chars = sum(len(w) for w in words)
    spaces_to_distribute = target_length - total_chars

    if len(words) == 1:
        # единственное слово прижимаем к правому краю
        return ' ' * spaces_to_distribute + words[0]

    gaps = len(words) - 1
    base_spaces = spaces_to_distribute // gaps
    extra_spaces = spaces_to_distribute % gaps

    result_parts = []
    for i in range(gaps):
        result_parts.append(words[i])
        spaces = base_spaces + (1 if i < extra_spaces else 0)
        result_parts.append(' ' * spaces)
    result_parts.append(words[-1])

    return ''.join(result_parts)


def get_data():
    """Выбор способа ввода строки и требуемой длины."""
    print("Задача 469: Выравнивание строки до заданной длины")
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
        while True:
            text = input("Введите исходную строку: ")
            if not text:
                print("Строка не должна быть пустой.")
                continue
            try:
                length = int(input("Введите требуемую длину (не меньше исходной): "))
                if length < len(text):
                    print(f"Длина должна быть >= {len(text)}.")
                    continue
                return text, length
            except ValueError:
                print("Ошибка: введите целое число.")

    elif choice == '2':
        # Генерируем случайную строку из нескольких слов
        num_words = random.randint(2, 6)
        words = []
        for _ in range(num_words):
            word_len = random.randint(2, 8)
            word = ''.join(random.choice(string.ascii_letters) for _ in range(word_len))
            words.append(word)
        text = ' '.join(words)
        # Требуемая длина: исходная + случайный добавок от 0 до 20
        extra = random.randint(0, 20)
        target = len(text) + extra
        print(f"Сгенерирована строка: '{text}' (длина {len(text)})")
        print(f"Требуемая длина: {target}")
        return text, target

    else:  # готовые примеры
        examples = [
            ("Hello world", 20),
            ("I  am   fine", 25),
            ("Python", 15),
            ("a b c", 10),
            ("one two three", 30)
        ]
        print("Готовые примеры:")
        for idx, (t, l) in enumerate(examples, 1):
            print(f"{idx}: строка = '{t}' (длина {len(t)}), требуемая длина={l}")
        while True:
            try:
                num = int(input("Выберите номер примера (1-5): "))
                if 1 <= num <= len(examples):
                    return examples[num - 1]
                else:
                    print(f"Номер от 1 до {len(examples)}.")
            except ValueError:
                print("Введите целое число.")


def main():
    text, target = get_data()
    aligned = align_string(text, target)

    print("\nИсходная строка:    ", f"'{text}' (длина {len(text)})")
    print("Требуемая длина:    ", target)
    print("Выровненная строка: ", f"'{aligned}' (длина {len(aligned)})")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
