"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
10. Вложенные циклы

340 . Даны целые числа m,a1, ... ,a20. Найти три натуральных числа i,j,k, каждое из которых не превосходит двадцати, такие, что ai + aj + ak = m. Если таких чисел нет, то сообщить об этом.
"""


import random

def get_input():
    """Выбор способа ввода m и массива a."""
    print("Выберите способ ввода:")
    print("1 - Ручной ввод")
    print("2 - Случайная генерация")
    print("3 - Готовый пример")
    choice = input("Ваш выбор (1/2/3): ").strip()
    while choice not in ('1', '2', '3'):
        choice = input("Некорректно. Выберите 1, 2 или 3: ")

    if choice == '1':
        try:
            m = int(input("Введите целое число m: "))
            print("Введите 20 целых чисел a1...a20 через пробел:")
            line = input().strip()
            tokens = line.split()
            if len(tokens) != 20:
                print("Ожидалось 20 чисел.")
                return None
            a = []
            for t in tokens:
                a.append(int(t))
            return m, a
        except ValueError:
            print("Ошибка ввода.")
            return None

    elif choice == '2':
        a = [random.randint(-100, 100) for _ in range(20)]
        m = random.randint(-300, 300)
        print(f"Сгенерировано: m = {m}")
        print("a =", a)
        return m, a

    else:  # choice == '3'
        examples = [
            (10, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]),
            (50, [10,20,30,40,50,60,70,80,90,100, -10, -20, -30, -40, -50, 0, 5, 15, 25, 35]),
            (0, [1,2,3,4,5,6,7,8,9,10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]),
            (100, [100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
            (42, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
        ]
        print("Готовые примеры (m, a):")
        for idx, (m_val, a_val) in enumerate(examples, 1):
            print(f"{idx}: m = {m_val}, a = {a_val[:5]}... (всего 20)")
        try:
            idx = int(input("Выберите номер примера: "))
            if 1 <= idx <= len(examples):
                m, a = examples[idx-1]
                return m, a
            else:
                print("Неверный номер.")
                return None
        except ValueError:
            print("Ошибка ввода.")
            return None

def find_triple(m, a):
    """Поиск трёх индексов i,j,k (от 1 до 20) таких, что a[i-1]+a[j-1]+a[k-1] == m."""
    n = len(a)  # должно быть 20
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if a[i] + a[j] + a[k] == m:
                    return (i+1, j+1, k+1)  # индексы с 1
    return None

def main():
    data = get_input()
    if data is None:
        return
    m, a = data
    print("\n" + "="*60)
    print(f"m = {m}")
    print("a =", a)
    print("="*60)

    result = find_triple(m, a)
    if result:
        i, j, k = result
        print(f"\nНайдены индексы: i={i}, j={j}, k={k}")
        print(f"a[{i}] + a[{j}] + a[{k}] = {a[i-1]} + {a[j-1]} + {a[k-1]} = {m}")
    else:
        print("\nНет тройки индексов, дающих сумму m.")

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
