"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
12. Использование процедур 

В задачах этого параграфа будем для краткости говорить просто о процедурах, подразумевая, что решающий задачи сам выберет подходящее средство программирования – подпрограмму, функцию и 
т. д. Этот выбор должен быть сделан с учётом как характера задач, так и особенностей используемого языка программирования.

467. Составить процедуру, в результате обращения к которой из первой заданной строки удаляется каждый символ, принадлежащий и второй заданной строке.
"""


import random
import string


def remove_common_characters(s1, s2):
    """
    Процедура удаляет из s1 все символы, которые есть в s2.
    """
    chars_to_remove = set(s2)
    return "".join(ch for ch in s1 if ch not in chars_to_remove)


def get_strings():
    """Выбор способа ввода двух строк."""
    print("Задача 467: Удаление из первой строки символов, общих со второй")
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
        s1 = input("Введите первую строку: ")
        s2 = input("Введите вторую строку (символы для удаления): ")
        return s1, s2

    elif choice == '2':
        # Генерируем случайные строки
        length1 = random.randint(10, 30)
        length2 = random.randint(3, 8)
        pool = string.ascii_letters + string.digits + string.punctuation + ' '
        s1 = ''.join(random.choice(pool) for _ in range(length1))
        s2 = ''.join(random.choice(pool) for _ in range(length2))
        print(f"Сгенерирована первая строка: '{s1}'")
        print(f"Сгенерирована вторая строка: '{s2}'")
        return s1, s2

    else:  # готовые примеры
        examples = [
            ("Hello, World!", "ol"),
            ("Programming", "aeiou"),
            ("1234567890", "13579"),
            ("aabbccddee", "abc"),
            ("Some text with spaces", " ")
        ]
        print("Готовые примеры:")
        for idx, (st1, st2) in enumerate(examples, 1):
            print(f"{idx}: s1='{st1}', s2='{st2}'")
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
    s1, s2 = get_strings()
    result = remove_common_characters(s1, s2)

    print("\nПервая строка:    ", s1)
    print("Вторая строка:    ", s2)
    print("Результат:        ", result)


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
