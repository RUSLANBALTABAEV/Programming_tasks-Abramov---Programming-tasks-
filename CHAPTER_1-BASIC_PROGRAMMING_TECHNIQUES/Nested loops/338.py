"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
10. Вложенные циклы

338.Даны натуральное число n , целые числа a1,... , a25, b1, ..., bn.
Среди a1, ... , a25 нет повторяющихся чисел, нет их и среди b1, ..., bn.
а) Построить пересечение последовательностей a1, ... ,a25 и b1, ... ,bn (т.е. получить в каком-нибудь порядке все числа, принадлежащие последовательности a1, ..., a25 и последовательности b1,... , bn одновременно)+.
б) Построить объединение данных последовательностей.
в) Получить все члены последовательности b1, ... , bn, которые не входят в последовательность a1, ... , a25.
г) Верно ли, что все члены последовательности a1, ... , a25 входят в последовательность b1, ..., bn?
д) Верно ли, что все члены последовательности b1, ... , bn входят в последовательность a1, ... , a25?
е) Верно ли, что все члены последовательности a1, ... , a25 входят в последовательность b1, ..., bn и при этом a1 встречается в последовательности b1, ... , bn не позднее, чем a2, a2 - не позднее, чем a3, и т.д.?
"""


import random

def get_sequences():
    """Выбор способа ввода n, a и b."""
    print("Выберите способ ввода:")
    print("1 - Ручной ввод")
    print("2 - Случайная генерация")
    print("3 - Готовый пример")
    choice = input("Ваш выбор (1/2/3): ").strip()
    while choice not in ('1', '2', '3'):
        choice = input("Некорректно. Выберите 1, 2 или 3: ")

    if choice == '1':
        try:
            n = int(input("Введите натуральное число n: "))
            if n <= 0:
                print("n должно быть положительным.")
                return None
            print("Введите 25 целых чисел a1...a25 (без повторов):")
            a_list = []
            while len(a_list) < 25:
                line = input().strip()
                nums = line.split()
                for token in nums:
                    if len(a_list) >= 25:
                        break
                    try:
                        val = int(token)
                        if val in a_list:
                            print(f"Ошибка: число {val} уже введено. Повторы не допускаются.")
                            return None
                        a_list.append(val)
                    except ValueError:
                        print("Ошибка: введите целое число.")
                        return None
            print("Введите n целых чисел b1...bn (без повторов):")
            b_list = []
            while len(b_list) < n:
                line = input().strip()
                nums = line.split()
                for token in nums:
                    if len(b_list) >= n:
                        break
                    try:
                        val = int(token)
                        if val in b_list:
                            print(f"Ошибка: число {val} уже введено. Повторы не допускаются.")
                            return None
                        b_list.append(val)
                    except ValueError:
                        print("Ошибка: введите целое число.")
                        return None
            return n, a_list, b_list
        except ValueError:
            print("Ошибка ввода.")
            return None

    elif choice == '2':
        n = random.randint(5, 30)  # случайное n
        # Генерируем a: 25 уникальных чисел
        a_set = set()
        while len(a_set) < 25:
            a_set.add(random.randint(-100, 100))
        a_list = list(a_set)
        random.shuffle(a_list)
        # Генерируем b: n уникальных чисел
        b_set = set()
        while len(b_set) < n:
            b_set.add(random.randint(-100, 100))
        b_list = list(b_set)
        random.shuffle(b_list)
        print(f"Сгенерировано: n = {n}")
        print("a:", a_list)
        print("b:", b_list)
        return n, a_list, b_list

    else:  # choice == '3'
        examples = [
            (5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],
             [10, 20, 30, 40, 50]),
            (8, [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49],
             [2, 4, 6, 8, 10, 12, 14, 16]),
            (10, [ -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
             [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
        ]
        print("Готовые примеры:")
        for idx, (n_val, a_val, b_val) in enumerate(examples, 1):
            print(f"{idx}: n = {n_val}, a = {a_val[:5]}... (всего {len(a_val)}), b = {b_val}")
        try:
            idx = int(input("Выберите номер примера: "))
            if 1 <= idx <= len(examples):
                n, a, b = examples[idx-1]
                return n, a, b
            else:
                print("Неверный номер.")
                return None
        except ValueError:
            print("Ошибка ввода.")
            return None

def main():
    data = get_sequences()
    if data is None:
        return
    n, a, b = data
    print("\n" + "="*60)
    print("Исходные данные:")
    print(f"n = {n}")
    print("a =", a)
    print("b =", b)
    print("="*60)

    # Для удобства используем множества
    set_a = set(a)
    set_b = set(b)

    # а) Пересечение
    intersection = set_a & set_b
    print("\nа) Пересечение:", sorted(intersection) if intersection else "пусто")

    # б) Объединение
    union = set_a | set_b
    print("б) Объединение:", sorted(union))

    # в) Разность (b \ a)
    diff = set_b - set_a
    print("в) Элементы b, не входящие в a:", sorted(diff) if diff else "пусто")

    # г) Все ли a входят в b?
    all_a_in_b = set_a.issubset(set_b)
    print("г) Все члены a входят в b?", "Да" if all_a_in_b else "Нет")

    # д) Все ли b входят в a?
    all_b_in_a = set_b.issubset(set_a)
    print("д) Все члены b входят в a?", "Да" if all_b_in_a else "Нет")

    # е) Проверка упорядоченного вхождения a в b
    if all_a_in_b:
        # Найдём индексы вхождений элементов a в b (по порядку b)
        # Создадим словарь: элемент -> индекс в b
        index_in_b = {val: i for i, val in enumerate(b)}
        # Проверим, что для всех i от 0 до 23 (т.е. a[0]..a[24]) индексы возрастают
        ordered = True
        prev_idx = -1
        for elem in a:
            idx = index_in_b[elem]  # гарантировано есть, так как все a входят в b
            if idx < prev_idx:
                ordered = False
                break
            prev_idx = idx
        print("е) Сохранение порядка a в b?", "Да" if ordered else "Нет")
    else:
        print("е) Не все a входят в b, поэтому условие не выполнено.")

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
