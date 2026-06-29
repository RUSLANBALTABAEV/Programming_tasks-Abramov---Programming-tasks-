"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
12. Использование процедур 

В задачах этого параграфа будем для краткости говорить просто о процедурах, подразумевая, что решающий задачи сам выберет подходящее средство программирования – подпрограмму, функцию и 
т. д. Этот выбор должен быть сделан с учётом как характера задач, так и особенностей используемого языка программирования.

453. Даны натуральные числа k, l, m, символы s1, ... , s30. Вывести данные cимволы в следующем виде:

(Определить процедуру, обращение к которой дает вывод символа t
после n пробелов.)
"""


import random
import string


# ------------------------------------------------------------
# Процедура вывода символа после n пробелов
# ------------------------------------------------------------
def print_symbol_after_spaces(t, n):
    """Выводит символ t после n пробелов (без перевода строки)."""
    print(' ' * n + t, end='')


# ------------------------------------------------------------
# Ввод данных (три способа)
# ------------------------------------------------------------
def get_data():
    """Выбор способа ввода k, l, m и 30 символов."""
    print("Задача 453: Форматированный вывод символов")
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
            try:
                print("Введите три натуральных числа k, l, m через пробел:")
                k, l, m = map(int, input().split())
                if k <= 0 or l <= 0 or m <= 0:
                    print("Числа должны быть натуральными (>= 1).")
                    continue
                print("Введите 30 символов через пробел (или слитно, например: a b c ...):")
                symbols_input = input().split()
                if len(symbols_input) != 30:
                    # Возможно, пользователь ввёл слитно строку из 30 символов без пробелов
                    if len(symbols_input) == 1 and len(symbols_input[0]) == 30:
                        symbols = list(symbols_input[0])
                    else:
                        print("Нужно ровно 30 символов.")
                        continue
                else:
                    symbols = symbols_input
                return k, l, m, symbols
            except ValueError:
                print("Ошибка ввода.")

    elif choice == '2':
        k = random.randint(2, 5)
        l = random.randint(2, 5)
        m = random.randint(2, 5)
        # Генерируем 30 случайных символов (буквы и цифры)
        symbols = [random.choice(string.ascii_letters + string.digits) for _ in range(30)]
        print(f"Сгенерированы: k = {k}, l = {l}, m = {m}")
        print(f"Символы: {' '.join(symbols)}")
        return k, l, m, symbols

    else:  # готовые примеры
        examples = [
            (4, 3, 5, list("abcdefghijklmnopqrstuvwxyz1234")),  # ровно 30 символов
            (2, 2, 2, ['A']*30),
            (1, 5, 3, list("1234567890abcdefghij1234567890"))
        ]
        print("Готовые примеры:")
        for idx, (kv, lv, mv, syms) in enumerate(examples, 1):
            print(f"{idx}: k = {kv}, l = {lv}, m = {mv}, символы = {' '.join(syms[:5])}...")
        while True:
            try:
                num = int(input("Выберите номер примера: "))
                if 1 <= num <= len(examples):
                    return examples[num - 1]
                else:
                    print(f"Номер от 1 до {len(examples)}.")
            except ValueError:
                print("Введите целое число.")


# ------------------------------------------------------------
# Основная программа
# ------------------------------------------------------------
def main():
    k, l, m, symbols = get_data()
    # Индексы нужных символов (нумерация с 1)
    s1 = symbols[0]
    s2 = symbols[1]
    s15 = symbols[14]
    s16 = symbols[15]
    s17 = symbols[16]
    s30 = symbols[29]

    print("\nРезультат:")
    # Первая строка
    print_symbol_after_spaces(s1, k)
    print_symbol_after_spaces(s16, l)
    print_symbol_after_spaces('*', m)
    print()

    # Вторая строка
    print_symbol_after_spaces(s2, k)
    print_symbol_after_spaces(s17, l)
    print_symbol_after_spaces('*', m)
    print()

    # Третья строка
    print_symbol_after_spaces(s15, k)
    print_symbol_after_spaces(s30, l)
    print_symbol_after_spaces('*', m)
    print()


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
