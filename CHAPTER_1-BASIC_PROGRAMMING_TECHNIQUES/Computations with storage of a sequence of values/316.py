"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
9. Вычисления с хранением последовательности значений

316. Даны натуральное число n, символы s1,… , sn. Будем рассматривать слова, образованные символами, входящими в последовательность s1, …, sn (см. задачу 269), считая при этом, что количество символов в каждом слове не превосходит 15. 
а) Найти какое-нибудь слово, оканчивающееся буквой д (если таких слов нет, то сообщить об этом).
б) Найти какое-нибудь слово, начинающееся буквой а и оканчивающееся буквой я (если таких слов нет, то сообщить об этом).
в) Удалить из s1,…, sn все слова с нечетными порядковыми номерами и перевернуть все слова с четными номерами. Например, если n = 21 и данная последовательность символов представляет собой последовательность во_что_бы_то_ни_стало, то должна получиться последовательность отч_от_олатс.
г) Удалить из s1,… , sn все слова, в которых встречается не более двух различных букв.
д) Удалить из s1, …, sn все слова, оканчивающиеся группой букв кая или кое.
"""


import random

def get_words_from_sequence(seq):
    """Разбивает строку на слова по пробелам, игнорируя лишние пробелы."""
    return [word for word in seq.split(' ') if word != '']

def main():
    print("Задача 316. Обработка слов в последовательности символов.")
    print("Слова разделяются пробелами. Длина каждого слова не превосходит 15.")
    
    # Выбор способа ввода
    print("\nВыберите способ задания последовательности:")
    print("1. Ввести символы вручную")
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
        n = int(input("Введите количество символов n: "))
        chars = []
        for i in range(n):
            char = input(f"Введите символ s{i+1}: ")
            if len(char) > 0:
                chars.append(char[0])
            else:
                chars.append(' ')
        sequence = ''.join(chars)
    else:
        # Готовые примеры
        examples = [
            "vo cto bi to ni stalo",  # пример из условия (используем пробелы)
            "a b c d e f g",           # простой набор
            "hello world python code",  # английские слова
            "как кое так как",          # русские слова с окончаниями
            "a bc def ghi jkl mno",     # разная длина
            "один два три четыре пять"  # русские числа
        ]
        print("Выберите пример:")
        for i, ex in enumerate(examples, 1):
            print(f"{i}. {ex}")
        while True:
            try:
                ex_choice = int(input("Номер примера (1-{}): ".format(len(examples))))
                if 1 <= ex_choice <= len(examples):
                    sequence = examples[ex_choice-1]
                    break
                else:
                    print(f"Ошибка: введите число от 1 до {len(examples)}.")
            except ValueError:
                print("Ошибка: введите целое число.")
    
    print(f"\nИсходная последовательность: '{sequence}'")
    words = get_words_from_sequence(sequence)
    print(f"Список слов: {words}")
    print(f"Количество слов: {len(words)}")
    
    # Проверка на пустоту
    if not words:
        print("В последовательности нет слов. Дальнейшие действия невозможны.")
        return
    
    # а) Найти слово, оканчивающееся на 'd'
    found_a = None
    for w in words:
        if w.endswith('d'):
            found_a = w
            break
    if found_a:
        print(f"\nа) Слово, оканчивающееся на 'd': '{found_a}'")
    else:
        print("\nа) Слов, оканчивающихся на 'd', не найдено.")
    
    # б) Найти слово, начинающееся на 'a' и оканчивающееся на 'g'
    found_b = None
    for w in words:
        if w.startswith('a') and w.endswith('g'):
            found_b = w
            break
    if found_b:
        print(f"б) Слово, начинающееся на 'a' и оканчивающееся на 'g': '{found_b}'")
    else:
        print("б) Слов, начинающихся на 'a' и оканчивающихся на 'g', не найдено.")
    
    # в) Удалить слова с нечетными номерами, перевернуть слова с четными
    new_words_v = []
    for i, w in enumerate(words, start=1):
        if i % 2 == 0:  # четный номер
            new_words_v.append(w[::-1])  # переворачиваем
        # нечетные просто пропускаем (удаляем)
    result_v = ' '.join(new_words_v)
    print(f"в) После удаления нечетных и переворота четных: '{result_v}'")
    
    # г) Удалить слова, в которых не более двух различных букв
    def distinct_letters(word):
        # Множество букв (только alphabetic)
        return set(ch for ch in word if ch.isalpha())
    
    new_words_g = []
    for w in words:
        if len(distinct_letters(w)) > 2:
            new_words_g.append(w)
    result_g = ' '.join(new_words_g)
    print(f"г) После удаления слов с ≤2 различными буквами: '{result_g}'")
    
    # д) Удалить слова, оканчивающиеся на "как" или "кое"
    endings = ("как", "кое")
    new_words_d = []
    for w in words:
        if not (w.endswith(endings[0]) or w.endswith(endings[1])):
            new_words_d.append(w)
    result_d = ' '.join(new_words_d)
    print(f"д) После удаления слов, оканчивающихся на 'как' или 'кое': '{result_d}'")

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
