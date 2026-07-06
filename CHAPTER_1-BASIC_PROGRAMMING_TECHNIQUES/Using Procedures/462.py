"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
12. Использование процедур 

В задачах этого параграфа будем для краткости говорить просто о процедурах, подразумевая, что решающий задачи сам выберет подходящее средство программирования – подпрограмму, функцию и 
т. д. Этот выбор должен быть сделан с учётом как характера задач, так и особенностей используемого языка программирования.

462. Составить процедуру, результатом работы которой является истинное значение, если символ, заданный при обращении к процедуре, – буква, и ложное значение в противном случае. 
"""


import random
import string


def is_letter(symbol):
    """
    Процедура проверяет, является ли заданный символ буквой.
    Возвращает True, если символ — буква (любого алфавита, включая кириллицу),
    и False в противном случае.
    """
    if not isinstance(symbol, str) or len(symbol) != 1:
        return False
    return symbol.isalpha()


def get_symbol():
    """Выбор способа ввода символа."""
    print("Задача 462: Проверка, является ли символ буквой")
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
            s = input("Введите один символ: ")
            if len(s) != 1:
                print("Нужно ввести ровно один символ.")
                continue
            return s

    elif choice == '2':
        # Случайный выбор из букв, цифр и знаков пунктуации
        pool = string.ascii_letters + string.digits + string.punctuation + ' '
        s = random.choice(pool)
        print(f"Сгенерирован символ: '{s}' (код {ord(s)})")
        return s

    else:  # готовые примеры
        examples = ['A', 'z', 'Я', '1', '?', ' ', 'AB']
        print("Готовые примеры:", [repr(c) for c in examples])
        while True:
            try:
                num = int(input("Выберите номер примера (1-7): "))
                if 1 <= num <= len(examples):
                    return examples[num - 1]
                else:
                    print(f"Номер от 1 до {len(examples)}.")
            except ValueError:
                print("Введите целое число.")


def main():
    symbol = get_symbol()
    result = is_letter(symbol)
    print(f"\nСимвол: '{symbol}'")
    print(f"Является ли буквой? {result}")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
