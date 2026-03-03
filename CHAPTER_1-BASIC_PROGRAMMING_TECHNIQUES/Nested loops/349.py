"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
10. Вложенные циклы

349. Даны целые числа a1, ... ,an. Для каждого из чисел, входящих в последовательность a1, ... ,an, выяснить, сколько раз оно входит в эту последовательность. Результат представить в виде ряда строк, первая из которых есть a1-k, где k-число вхождений a1 в последовательность a1, ... ,an. Вторая строка будет иметь вид ai-m, где ai-первый порядку член последовательности, отличный от a1 а m - число вхождений этого члена в последовательность.
"""


import random
from collections import Counter, OrderedDict

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
            a = [int(t) for t in tokens]
            return a
        except ValueError:
            print("Ошибка ввода.")
            return None

    elif choice == '2':
        n = random.randint(3, 15)
        a = [random.randint(-5, 10) for _ in range(n)]
        print(f"Сгенерирована последовательность из {n} чисел:")
        print(a)
        return a

    else:  # choice == '3'
        examples = [
            [1, 2, 3, 4, 5],
            [1, 1, 2, 2, 3, 3],
            [5, 5, 5, 5],
            [1, 2, 1, 2, 1, 3, 4, 5, 5],
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

def main():
    a = get_sequence()
    if a is None:
        return

    print("\n" + "="*60)
    print("Последовательность:", a)
    print("="*60)

    # Подсчёт частот с сохранением порядка первого появления
    # Используем OrderedDict для отслеживания порядка
    freq = OrderedDict()
    for x in a:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1

    print("\nРезультат (число - количество вхождений):")
    for num, count in freq.items():
        print(f"{num} - {count}")

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
