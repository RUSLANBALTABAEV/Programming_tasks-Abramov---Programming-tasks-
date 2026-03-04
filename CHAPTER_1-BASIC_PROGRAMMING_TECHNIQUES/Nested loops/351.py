"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
10. Вложенные циклы

351.Даны натуральные числа a1, ... ,an. Известно, что a1, ... ,an - перестановка чисел 1, ... ,n , т.е. в последовательности a1, ... ,an встречаются все числа 1, ... ,n. Будем говорить, что натуральное m переводится данной перестановкой в натуральное k (m <= n, k <= n), если am = k. Например, число 1 переводится в a1, a1 переводится в aa1 и т.д. Рассмотрим образованную этим способом последовательность 1, a, aa1 ,... .
а) Доказать, что первый член этой последовательности, для которого имеется равный среди предыдущих, есть 1. Получить по порядку все члены последовательности 1, a,aa1 ,... предшествующие повторению числа 1.
б) Кроме той последовательности, которую требуется получить в a), получить аналогичные последовательности, начинающиеся с чисел, больших 1. При этом последовательности должны быть попарно различны, и каждая из них должна начинаться с наименьшего члена.
Например, если n = 6, a1 = 3, a2 = 2, a3 = 5, a4 = 6, a5 = 1, a6 = 4, то должны быть получены последовательности
1, 3, 5,
2
4, 6.
"""


import random

def get_permutation():
    """Выбор способа ввода перестановки a1..an."""
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
            print(f"Введите {n} целых чисел a1...an (перестановка чисел 1..{n}) через пробел:")
            line = input().strip()
            tokens = line.split()
            if len(tokens) != n:
                print(f"Ожидалось {n} чисел, получено {len(tokens)}.")
                return None
            a = [int(t) for t in tokens]
            # Проверка, что это перестановка
            if sorted(a) != list(range(1, n+1)):
                print("Ошибка: последовательность не является перестановкой чисел 1..n.")
                return None
            return n, a
        except ValueError:
            print("Ошибка ввода.")
            return None

    elif choice == '2':
        n = random.randint(3, 10)
        a = list(range(1, n+1))
        random.shuffle(a)
        print(f"Сгенерирована случайная перестановка для n = {n}:")
        print(a)
        return n, a

    else:  # choice == '3'
        examples = [
            (6, [3, 2, 5, 6, 1, 4]),  # пример из условия
            (5, [2, 3, 4, 5, 1]),    # один цикл
            (4, [1, 2, 3, 4]),        # все единичные циклы
            (3, [2, 1, 3]),            # два цикла: (1,2) и (3)
            (7, [3, 7, 4, 1, 6, 5, 2]) # случайный
        ]
        print("Готовые примеры (n, a):")
        for idx, (n_val, a_val) in enumerate(examples, 1):
            print(f"{idx}: n = {n_val}, a = {a_val}")
        try:
            idx = int(input("Выберите номер примера: "))
            if 1 <= idx <= len(examples):
                n, a = examples[idx-1]
                return n, a
            else:
                print("Неверный номер.")
                return None
        except ValueError:
            print("Ошибка ввода.")
            return None

def find_cycles(n, a):
    """Разложение перестановки на циклы. Возвращает список циклов, каждый цикл - список элементов в порядке обхода,
    начиная с наименьшего элемента в цикле."""
    visited = [False] * (n + 1)  # индексы от 1 до n
    cycles = []
    for start in range(1, n+1):
        if not visited[start]:
            # строим цикл, начиная с start
            cycle = []
            x = start
            while not visited[x]:
                visited[x] = True
                cycle.append(x)
                x = a[x-1]  # a индексируется с 0, но значения от 1 до n
            # теперь cycle содержит все элементы цикла в порядке обхода от start
            # нужно найти минимальный элемент и переупорядочить
            min_elem = min(cycle)
            # находим позицию минимального
            idx_min = cycle.index(min_elem)
            # переставляем: от min_elem до конца, затем от начала до min_elem-1
            ordered_cycle = cycle[idx_min:] + cycle[:idx_min]
            cycles.append(ordered_cycle)
    # сортируем циклы по первому элементу (наименьшему)
    cycles.sort(key=lambda c: c[0])
    return cycles

def main():
    data = get_permutation()
    if data is None:
        return
    n, a = data
    print("\n" + "="*60)
    print(f"n = {n}")
    print("Перестановка a =", a)
    print("="*60)

    cycles = find_cycles(n, a)

    print("\nа) Последовательность, начинающаяся с 1:")
    # Найдём цикл, содержащий 1
    for cycle in cycles:
        if 1 in cycle:
            print(" ".join(str(x) for x in cycle))
            break

    print("\nб) Все циклы (каждый начинается с наименьшего члена):")
    for i, cycle in enumerate(cycles, 1):
        print(f"Цикл {i}:", " ".join(str(x) for x in cycle))

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
