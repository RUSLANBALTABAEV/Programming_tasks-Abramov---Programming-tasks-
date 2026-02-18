"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
9. Вычисления с хранением последовательности значений

312. Даны символы s1, …, sn *). Оставить последовательность s1, …, sn без изменения, если в нее не входит символ * , иначе каждый символ / , предшествующий первому вхождению символа *:
а) заменить на запятую;
б) удалить из последовательности.
*) Задачи 312 – 316 допускают строковые варианты.
"""


def main():
    print("Задача 312. Обработка последовательности символов.")
    print("Если в строке нет символа '*', она остаётся без изменений.")
    print("Иначе для каждого символа '/', находящегося до первого '*', выполняется:")
    print("  a) замена на ','")
    print("  б) удаление из последовательности")
    
    # Выбор способа ввода
    print("\nВыберите способ задания строки:")
    print("1. Ввести строку вручную")
    print("2. Использовать готовый пример")
    
    while True:
        try:
            choice = int(input("Ваш выбор (1-2): "))
            if choice in (1, 2):
                break
            else:
                print("Ошибка: введите 1 или 2.")
        except ValueError:
            print("Ошибка: введите целое число.")
    
    if choice == 1:
        s = input("Введите строку символов: ")
    else:
        examples = [
            "abc/def*ghi/jkl",
            "///**/",
            "no star here",
            "one/and/two*and/three",
            "*first",
            "last*"
        ]
        print("Выберите пример:")
        for i, ex in enumerate(examples, 1):
            print(f"{i}. {ex}")
        while True:
            try:
                ex_choice = int(input("Номер примера (1-6): "))
                if 1 <= ex_choice <= len(examples):
                    s = examples[ex_choice-1]
                    break
                else:
                    print("Ошибка: введите число от 1 до 6.")
            except ValueError:
                print("Ошибка: введите целое число.")
    
    print(f"\nИсходная строка: {s}")
    
    # Выбор варианта
    print("\nВыберите действие:")
    print("a) заменить '/' на ','")
    print("б) удалить '/'")
    variant = input("Ваш выбор (a/б): ").strip().lower()
    while variant not in ('a', 'б'):
        print("Ошибка: введите 'a' или 'б'.")
        variant = input("Ваш выбор (a/б): ").strip().lower()
    
    # Обработка
    if '*' not in s:
        result = s
        print("Символ '*' не найден. Строка без изменений.")
    else:
        first_star = s.index('*')
        # Разделим на часть до первого '*' и после
        before = s[:first_star]
        after = s[first_star:]
        if variant == 'a':
            # замена '/' на ','
            before_processed = before.replace('/', ',')
        else:  # 'б'
            # удаление '/'
            before_processed = before.replace('/', '')
        result = before_processed + after
        print(f"Первый '*' на позиции {first_star+1}.")
    
    print(f"\nРезультат: {result}")
    
    # Дополнительно покажем символы
    print("\nПосимвольно:")
    for i, ch in enumerate(result, 1):
        print(f"{i}: {ch}")

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
