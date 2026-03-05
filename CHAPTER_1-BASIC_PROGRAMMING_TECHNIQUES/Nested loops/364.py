"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
10. Вложенные циклы

364. Даны символы s1,...,s50. Выяснить, верно ли, что хотя бы один символ входит в s1,...,s50 более одного раза и при этом так, что между любыми двумя его вхождениями встречается буква a или b.
"""


import random

def get_input():
    """Выбор способа ввода строки s из 50 символов."""
    print("=== Задача 364: Проверка условия о повторяющихся символах и буквах a/b ===")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод")
    print("2 — Случайная генерация")
    print("3 — Готовые примеры")

    choice = input("Ваш выбор (1/2/3): ").strip()
    while choice not in ('1', '2', '3'):
        choice = input("Выберите 1, 2 или 3: ").strip()

    if choice == '1':
        try:
            s = input("Введите строку из 50 символов: ").strip()
            if len(s) != 50:
                print("Ошибка: строка должна содержать ровно 50 символов.")
                return None
            return s
        except Exception:
            print("Ошибка ввода.")
            return None

    elif choice == '2':
        # Генерируем случайную строку из букв и цифр (можно и другие символы)
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        s = ''.join(random.choices(chars, k=50))
        print(f"\nСгенерирована строка: {s}")
        return s

    else:
        # Готовые примеры
        examples = [
            "abcde"*10,  # 50 символов, но здесь нет повторений? "abcde" повторяется, каждый символ встречается 10 раз. Проверим условие: для символа 'a' между вхождениями есть другие символы, но есть ли среди них 'a' или 'b'? Между двумя 'a' будут символы 'b','c','d','e' – есть 'b', значит условие выполняется для 'a'. Аналогично для 'b' между ними есть 'c','d','e','a' – есть 'a'? Да, 'a' встречается. Так что ответ должен быть "да". Хорошо.
            "a"*25 + "b"*25,  # все a и b, но между a (если есть подряд?) здесь a идут подряд, между соседними a нет никаких символов (промежуток пуст). Пустой промежуток не содержит a или b, значит для символа 'a' условие не выполняется (так как между некоторыми a нет букв). Для 'b' аналогично. Но есть ли другие символы? Нет. Так что ответ "нет".
            "x"*50,  # только один символ, повторяется много раз, но между x пусто, нет a/b, значит нет.
            "ab"*25,  # чередование a и b, каждый символ встречается 25 раз. Для 'a' между ними всегда есть 'b'? Да, между двумя a всегда есть b (кроме случая, если a подряд? Но здесь a и b чередуются, так что между a всегда b). Условие выполняется.
            "abcdefghijklmnopqrstuvwxyz"*2,  # 52 символа, но нам нужно 50, поэтому обрежем? Лучше сделать ровно 50. Возьмем первые 50: это алфавит два раза, но второй раз неполный. Проверим: например, символ 'a' встречается два раза, между ними много букв, есть 'b'? Да, есть. Так что да.
            "a"*10 + "c"*30 + "a"*10,  # a встречается в начале и в конце, между ними только c, нет a/b, значит для a условие не выполняется. Другие символы? c встречается много, между ними есть только c, нет a/b, тоже нет. Ответ нет.
        ]
        # Чтобы быть уверенным в длине 50, скорректируем примеры:
        examples = [
            "abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcde",  # 50? "abcde" 10 раз = 50, да.
            "aaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbb",  # 25 a и 25 b, но здесь a подряд, b подряд. Это 50.
            "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  # 50 x
            "ab"*25,  # 50
            "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",  # 26+24=50, первые 26 алфавит, потом 24 первых букв. Тут a встречается дважды? Да, a в начале и в конце? В конце после z идет a? Второй раз a есть? В строке "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx" - второй a есть на позиции 26, и между ними все буквы от b до z, есть b. Так что условие для a выполняется.
            "a"*10 + "c"*30 + "a"*10,  # 50, a по краям, c в середине.
        ]
        print("\nГотовые примеры:")
        for i, ex in enumerate(examples, 1):
            print(f"{i}. {ex[:30]}... (длина {len(ex)})")
        try:
            num = int(input("\nВыберите номер примера: "))
            if 1 <= num <= len(examples):
                s = examples[num-1]
                if len(s) != 50:
                    print(f"Предупреждение: длина примера {len(s)}, но будем использовать как есть.")
                return s
            else:
                print("Неверный номер!")
                return None
        except ValueError:
            print("Ошибка ввода.")
            return None

def check_condition(s):
    """
    Проверяет условие:
    существует символ, который встречается не менее двух раз,
    и для любых двух последовательных вхождений этого символа
    в промежутке между ними есть хотя бы одна буква 'a' или 'b'.
    """
    from collections import defaultdict
    positions = defaultdict(list)
    for idx, ch in enumerate(s):
        positions[ch].append(idx)

    for ch, pos_list in positions.items():
        if len(pos_list) < 2:
            continue  # символ встречается только один раз
        good = True
        for i in range(len(pos_list)-1):
            start = pos_list[i] + 1
            end = pos_list[i+1]  # не включая
            interval = s[start:end]
            if not ('a' in interval or 'b' in interval):
                good = False
                break
        if good:
            return True, ch
    return False, None

def main():
    s = get_input()
    if s is None:
        return
    n = len(s)
    print(f"\nСтрока (длина {n}): {s}")
    result, ch = check_condition(s)
    print("\n" + "="*50)
    print("РЕЗУЛЬТАТ ЗАДАЧИ 364")
    print("="*50)
    if result:
        print(f"Да, условие выполняется для символа '{ch}'.")
    else:
        print("Нет, ни один символ не удовлетворяет условию.")
    print("="*50)

if __name__ == "__main__":
    main()
