"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
12. Использование процедур 

В задачах этого параграфа будем для краткости говорить просто о процедурах, подразумевая, что решающий задачи сам выберет подходящее средство программирования – подпрограмму, функцию и 
т. д. Этот выбор должен быть сделан с учётом как характера задач, так и особенностей используемого языка программирования.

464. Составить процедуру «сжатия» исходной последовательности символов: каждая подпоследовательность, состоящая из нескольких вхождений одного и того же символа, заменяется на текст x(k), где x - символ, k - строка, являющаяся записью числа вхождений символа x в исходную последовательность. 
"""


import random
import string


def compress_sequence(s):
    """
    Процедура сжатия последовательности символов.
    Возвращает строку, в которой каждая группа повторяющихся символов
    заменена на x(k), где x – символ, k – количество его повторений.
    """
    if not s:
        return ""
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(f"{s[i - 1]}({count})")
            count = 1
    result.append(f"{s[-1]}({count})")
    return "".join(result)


def get_sequence():
    """Выбор способа ввода последовательности символов."""
    print("Задача 464: Сжатие последовательности символов")
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
            s = input("Введите строку символов: ")
            if s == "":
                print("Строка не должна быть пустой (или нажмите Ctrl+C для выхода).")
                continue
            return s

    elif choice == '2':
        # Генерируем строку длиной 10-30 из случайных символов (буквы, цифры, знаки)
        length = random.randint(10, 30)
        pool = string.ascii_letters + string.digits + string.punctuation
        # Для реалистичности создаём участки с повторениями
        s = []
        while len(s) < length:
            ch = random.choice(pool)
            repeat = random.randint(1, 5)
            s.extend([ch] * repeat)
        s = "".join(s[:length])
        print(f"Сгенерирована строка: '{s}'")
        return s

    else:  # готовые примеры
        examples = [
            "aaaabbbccdaaaaa",
            "111112223334444",
            "!!!!!!!@@@@@@@###$$$",
            "AaaBBbbCCcc",
            "   ++++---===="
        ]
        print("Готовые примеры:")
        for idx, ex in enumerate(examples, 1):
            print(f"{idx}: '{ex}'")
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
    s = get_sequence()
    compressed = compress_sequence(s)
    print("\nИсходная строка:     ", s)
    print("Результат сжатия:    ", compressed)


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
