"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
12. Использование процедур 

В задачах этого параграфа будем для краткости говорить просто о процедурах, подразумевая, что решающий задачи сам выберет подходящее средство программирования – подпрограмму, функцию и 
т. д. Этот выбор должен быть сделан с учётом как характера задач, так и особенностей используемого языка программирования.

468. Составить процедуру, позволяющую определить позицию первого вхождения в заданную строку какого-либо символа из второй заданной строки. Результатом работы процедуры должна быть –1, если первая строка не содержит ни одного символа, принадлежащего и второй заданной строке.
"""


import random
import string


def find_first_common_char(s1, s2):
    """
    Процедура возвращает позицию (с 1) первого символа в s1,
    который присутствует в s2. Если таких символов нет, возвращает -1.
    """
    chars_in_s2 = set(s2)
    for i, ch in enumerate(s1):
        if ch in chars_in_s2:
            return i + 1          # позиция с 1
    return -1


def get_strings():
    """Выбор способа ввода двух строк."""
    print("Задача 468: Позиция первого общего символа")
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
        s2 = input("Введите вторую строку (искомые символы): ")
        return s1, s2

    elif choice == '2':
        length1 = random.randint(10, 25)
        length2 = random.randint(3, 8)
        pool = string.ascii_letters + string.digits + string.punctuation + ' '
        s1 = ''.join(random.choice(pool) for _ in range(length1))
        s2 = ''.join(random.choice(pool) for _ in range(length2))
        print(f"Сгенерирована первая строка: '{s1}'")
        print(f"Сгенерирована вторая строка: '{s2}'")
        return s1, s2

    else:  # готовые примеры
        examples = [
            ("abcdef", "xyzc"),          # первый общий 'c' на позиции 3
            ("hello", "xyz"),            # нет общих
            ("1234567890", "13579"),      # '1' на позиции 1
            ("programming", "aeiou"),     # 'o' на позиции 3
            ("some text", " ")            # пробел на позиции 5
        ]
        print("Готовые примеры:")
        for idx, (st1, st2) in enumerate(examples, 1):
            print(f"{idx}: s1 = '{st1}', s2 = '{st2}'")
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
    pos = find_first_common_char(s1, s2)

    print("\nПервая строка:    ", s1)
    print("Вторая строка:    ", s2)
    if pos == -1:
        print("Общих символов нет. Результат: -1")
    else:
        print(f"Первый общий символ на позиции {pos} ('{s1[pos - 1]}')")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
