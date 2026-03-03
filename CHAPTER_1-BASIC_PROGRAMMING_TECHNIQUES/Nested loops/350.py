"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
10. Вложенные циклы

350. Даны натуральные числа k,n действительные числа a1, ... ,akn. Получить:
а) последовательность a1 +...+ ak * ak+1 + ... ,ak(n-1)+1 +...+akn;
а) последовательность max(a1, ... ,ak), max(ak+1, ... ,a2k), ... ,max(ak(n - 1) + 1, ..., akn);
в) min(a1, ... , ak) + min(ak+1, ... ,a2k) + ... + min(ak(n-1)+1, ... ,akn);
г) max(a1 +...+ ak,ak+1 +...+ a2k, ak(n-1)+1 +...+ akn);
д) min(max(a1, ... , ak), max(ak+1, ... , a2k), ... , max(ak(n-1)+1, ... ,akn))
"""


import random

def get_input():
    """Выбор способа ввода k, n и массива a."""
    print("Выберите способ ввода:")
    print("1 - Ручной ввод")
    print("2 - Случайная генерация")
    print("3 - Готовый пример")
    choice = input("Ваш выбор (1/2/3): ").strip()
    while choice not in ('1', '2', '3'):
        choice = input("Некорректно. Выберите 1, 2 или 3: ")

    if choice == '1':
        try:
            k = int(input("Введите натуральное число k: "))
            n = int(input("Введите натуральное число n: "))
            if k <= 0 or n <= 0:
                print("k и n должны быть положительными.")
                return None
            total = k * n
            print(f"Введите {total} действительных чисел a1...a{total} через пробел:")
            line = input().strip()
            tokens = line.split()
            if len(tokens) != total:
                print(f"Ожидалось {total} чисел, получено {len(tokens)}.")
                return None
            a = [float(t) for t in tokens]
            return k, n, a
        except ValueError:
            print("Ошибка ввода.")
            return None

    elif choice == '2':
        k = random.randint(2, 5)
        n = random.randint(2, 5)
        total = k * n
        a = [random.uniform(-10, 10) for _ in range(total)]
        print(f"Сгенерировано: k = {k}, n = {n}")
        print("a =", a)
        return k, n, a

    else:  # choice == '3'
        examples = [
            (2, 3, [1, 2, 3, 4, 5, 6]),
            (3, 2, [10, 20, 30, 40, 50, 60]),
            (2, 4, [5, 1, 8, 3, 7, 2, 4, 6]),
            (1, 5, [1.5, 2.5, 3.5, 4.5, 5.5]),
            (4, 2, [0, -1, -2, -3, -4, -5, -6, -7])
        ]
        print("Готовые примеры (k, n, a):")
        for idx, (k_val, n_val, a_val) in enumerate(examples, 1):
            print(f"{idx}: k = {k_val}, n = {n_val}, a = {a_val}")
        try:
            idx = int(input("Выберите номер примера: "))
            if 1 <= idx <= len(examples):
                k, n, a = examples[idx-1]
                return k, n, a
            else:
                print("Неверный номер.")
                return None
        except ValueError:
            print("Ошибка ввода.")
            return None

def main():
    data = get_input()
    if data is None:
        return
    k, n, a = data
    total = k * n
    print("\n" + "="*60)
    print(f"k = {k}, n = {n}, всего элементов = {total}")
    print("a =", a)
    print("="*60)

    # Разбиение на блоки длины k
    blocks = []
    for i in range(n):
        start = i * k
        end = start + k
        blocks.append(a[start:end])

    # a) суммы по блокам
    sums = [sum(block) for block in blocks]
    print("\nа) Суммы по блокам:", sums)

    # б) максимумы по блокам
    maxs = [max(block) for block in blocks]
    print("б) Максимумы по блокам:", maxs)

    # в) сумма минимумов по блокам
    mins = [min(block) for block in blocks]
    sum_mins = sum(mins)
    print("в) Сумма минимумов по блокам:", sum_mins)

    # г) максимум из сумм
    max_sum = max(sums)
    print("г) Максимум из сумм:", max_sum)

    # д) минимум из максимумов
    min_max = min(maxs)
    print("д) Минимум из максимумов:", min_max)

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
