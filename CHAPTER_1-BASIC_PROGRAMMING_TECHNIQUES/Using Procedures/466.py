"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
12. Использование процедур 

В задачах этого параграфа будем для краткости говорить просто о процедурах, подразумевая, что решающий задачи сам выберет подходящее средство программирования – подпрограмму, функцию и 
т. д. Этот выбор должен быть сделан с учётом как характера задач, так и особенностей используемого языка программирования.

466. Составить процедуру, заменяющую в исходной строке Составить процедуру, заменяющую в исходной строке выполняться, начиная с заданной позиции строки. 
"""


import random
import string


def swap_zeros_ones_from_pos(s, pos):
    """
    Процедура заменяет все '0' на '1' и все '1' на '0' в строке s,
    начиная с позиции pos (позиции нумеруются с 1).
    Символы, не являющиеся '0' или '1', остаются без изменений.
    Если pos выходит за границы строки, возвращается исходная строка.
    """
    index = pos - 1                     # переводим в 0‑based индекс
    if index < 0 or index >= len(s):
        return s

    chars = list(s)
    for i in range(index, len(chars)):
        if chars[i] == '0':
            chars[i] = '1'
        elif chars[i] == '1':
            chars[i] = '0'
    return "".join(chars)


def get_data():
    """Выбор способа ввода строки и стартовой позиции."""
    print("Задача 466: Замена 0↔1 с заданной позиции")
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
            s = input("Введите исходную строку (содержащую 0 и 1): ")
            try:
                pos = int(input("Введите позицию, с которой начать замену (с 1): "))
                if pos < 1:
                    print("Позиция должна быть >= 1.")
                    continue
                return s, pos
            except ValueError:
                print("Ошибка ввода позиции.")

    elif choice == '2':
        length = random.randint(10, 25)
        s = ''.join(random.choice('01') for _ in range(length))
        pos = random.randint(1, length + 2)  # иногда за границей
        print(f"Сгенерирована строка: '{s}'")
        print(f"Стартовая позиция: {pos}")
        return s, pos

    else:  # готовые примеры
        examples = [
            ("01001 1010 010", 3),
            ("111000111", 5),
            ("0000", 1),
            ("101010", 7),    # позиция за границей
            ("abc01def10", 4)
        ]
        print("Готовые примеры:")
        for idx, (st, p) in enumerate(examples, 1):
            print(f"{idx}: строка='{st}', позиция={p}")
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
    s, pos = get_data()
    result = swap_zeros_ones_from_pos(s, pos)

    print("\nИсходная строка:    ", s)
    print(f"Замена с позиции {pos}: ", result)


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
