"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
10. Вложенные циклы

339. Даны целые числа a1, ... ,an (в этой последовательности могут быть повторяющиеся члены).
а) Получить все числа, которые входят в последовательность по одному разу.
б) Получить числа, взятые по одному из каждой группы равных членов.
в) Найти число различных членов последовательности 
г) Выяснить, сколько чисел входит в последовательность по одному разу.
д) Выяснить, сколько чисел входит в последовательность более чем по одному разу.
е) Выяснить, имеется ли в последовательности хотя бы одна пара совпадающих чисел.
"""


import random

def get_sequence():
    """Выбор способа ввода последовательности."""
    print("Выберите способ ввода:")
    print("1 - Ручной ввод")
    print("2 - Случайная генерация")
    print("3 - Готовый пример")
    choice = input("Ваш выбор (1/2/3): ").strip()
    while choice not in ('1', '2', '3'):
        choice = input("Некорректно. Выберите 1, 2 или 3: ")

    if choice == '1':
        try:
            n = int(input("Введите количество элементов n: "))
            if n <= 0:
                print("n должно быть положительным.")
                return None
            print(f"Введите {n} целых чисел через пробел:")
            line = input().strip()
            tokens = line.split()
            if len(tokens) != n:
                print(f"Ожидалось {n} чисел, получено {len(tokens)}.")
                return None
            seq = []
            for t in tokens:
                try:
                    seq.append(int(t))
                except ValueError:
                    print(f"Ошибка: '{t}' не является целым числом.")
                    return None
            return seq
        except ValueError:
            print("Ошибка ввода.")
            return None

    elif choice == '2':
        n = random.randint(5, 20)
        seq = [random.randint(-10, 20) for _ in range(n)]
        print(f"Сгенерирована последовательность из {n} чисел:")
        print(seq)
        return seq

    else:  # choice == '3'
        examples = [
            [1, 2, 3, 4, 5],
            [1, 1, 2, 2, 3, 3, 4],
            [5, 5, 5, 5],
            [1, 2, 3, 2, 1, 4, 5, 6, 7, 8, 9, 9],
            [10, -1, 0, 3, -1, 7, 10, 10, 2]
        ]
        print("Готовые примеры:")
        for idx, ex in enumerate(examples, 1):
            print(f"{idx}: {ex}")
        try:
            idx = int(input("Выберите номер примера: "))
            if 1 <= idx <= len(examples):
                return examples[idx-1]
            else:
                print("Неверный номер.")
                return None
        except ValueError:
            print("Ошибка ввода.")
            return None

def analyze(seq):
    """Анализ последовательности."""
    from collections import Counter
    cnt = Counter(seq)

    # а) числа, входящие ровно один раз
    once = [x for x, c in cnt.items() if c == 1]

    # б) числа, взятые по одному из каждой группы (уникальные)
    unique = list(cnt.keys())

    # в) число различных членов
    num_unique = len(unique)

    # г) сколько чисел входит по одному разу
    num_once = len(once)

    # д) сколько чисел входит более чем по одному разу
    num_more = sum(1 for c in cnt.values() if c > 1)

    # е) есть ли хотя бы одна пара совпадающих
    has_duplicate = any(c > 1 for c in cnt.values())

    return once, unique, num_unique, num_once, num_more, has_duplicate

def main():
    seq = get_sequence()
    if seq is None:
        return

    print("\n" + "="*60)
    print("Последовательность:", seq)
    print("="*60)

    once, unique, num_unique, num_once, num_more, has_duplicate = analyze(seq)

    print("\nа) Числа, входящие по одному разу:", once if once else "нет")
    print("б) Уникальные числа (по одному из каждой группы):", unique)
    print("в) Количество различных членов:", num_unique)
    print("г) Сколько чисел входит по одному разу:", num_once)
    print("д) Сколько чисел входит более чем по одному разу:", num_more)
    print("е) Имеется ли хотя бы одна пара совпадающих чисел?", "Да" if has_duplicate else "Нет")

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
