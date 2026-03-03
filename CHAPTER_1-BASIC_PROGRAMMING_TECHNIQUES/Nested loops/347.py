"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
10. Вложенные циклы

347. Даны целые числа a1, ... ,a30. Пусть M – наибольшее, а m - наименьшее из a1, ... ,a30. Получить в порядке возрастания все целые из интервала (m, M), которые не входят в последовательность a1, ... ,a30.
"""


import random

def get_sequence():
    """Выбор способа ввода 30 целых чисел."""
    print("Выберите способ ввода:")
    print("1 - Ручной ввод")
    print("2 - Случайная генерация")
    print("3 - Готовый пример")
    choice = input("Ваш выбор (1/2/3): ").strip()
    while choice not in ('1', '2', '3'):
        choice = input("Некорректно. Выберите 1, 2 или 3: ")

    if choice == '1':
        try:
            print("Введите 30 целых чисел a1...a30 через пробел:")
            line = input().strip()
            tokens = line.split()
            if len(tokens) != 30:
                print("Ожидалось 30 чисел.")
                return None
            a = []
            for t in tokens:
                a.append(int(t))
            return a
        except ValueError:
            print("Ошибка ввода.")
            return None

    elif choice == '2':
        a = [random.randint(-50, 50) for _ in range(30)]
        print("Сгенерированы числа:")
        print(a)
        return a

    else:  # choice == '3'
        examples = [
            [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],
            [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
            [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300],
            [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],
            [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15]
        ]
        print("Готовые примеры:")
        for idx, ex in enumerate(examples, 1):
            print(f"{idx}: {ex[:5]}... (всего 30)")
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

def find_missing_in_interval(a):
    """Возвращает отсортированный список целых чисел из (min(a), max(a)), отсутствующих в a."""
    if not a:
        return []
    m = min(a)
    M = max(a)
    # Множество для быстрой проверки
    present = set(a)
    missing = []
    for x in range(m+1, M):  # range до M-1 включительно
        if x not in present:
            missing.append(x)
    return missing

def main():
    a = get_sequence()
    if a is None:
        return
    print("\n" + "="*60)
    print("Последовательность a =", a)
    m = min(a)
    M = max(a)
    print(f"Минимум m = {m}, максимум M = {M}")
    print("="*60)

    missing = find_missing_in_interval(a)
    if missing:
        print("\nЦелые числа из интервала (m, M), не входящие в последовательность:")
        print(missing)
    else:
        print("\nВсе целые числа из интервала (m, M) присутствуют в последовательности.")

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
