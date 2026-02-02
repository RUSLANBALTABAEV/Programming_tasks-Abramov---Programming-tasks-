"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
9. Вычисления с хранением последовательности значений

298. Даны целые числа a1,…, a25, b1,…, b25. Преобразовать последовательность b1, …, b25 по правилу: если ai <= 0, то bi увеличить в 10 раз, иначе bi заменить нулем (i = 1, ..., 25).
"""


import random

def main():
    print("Программа для преобразования последовательности b в зависимости от значений a.")
    print("Условие: если a_i ≤ 0, то b_i увеличить в 10 раз, иначе заменить b_i на 0.")
    
    # Выбор способа ввода данных
    print("\nВыберите способ задания последовательностей:")
    print("1. Ввести числа вручную")
    print("2. Использовать случайные числа от -10 до 10")
    print("3. Использовать готовый набор 1: a - смешанные, b - от 1 до 25")
    print("4. Использовать готовый набор 2: a - все положительные")
    print("5. Использовать готовый набор 3: a - все отрицательные")
    
    while True:
        try:
            choice = int(input("\nВаш выбор (1-5): "))
            if 1 <= choice <= 5:
                break
            else:
                print("Ошибка: выберите число от 1 до 5.")
        except ValueError:
            print("Ошибка: введите целое число от 1 до 5.")
    
    n = 25  # количество элементов по условию
    
    # Инициализация последовательностей в зависимости от выбора
    if choice == 1:
        # Ручной ввод
        print(f"\nВведите {n} целых чисел для последовательности a:")
        a = []
        for i in range(n):
            while True:
                try:
                    value = int(input(f"a_{i+1}: "))
                    a.append(value)
                    break
                except ValueError:
                    print("Ошибка: введите целое число.")
        
        print(f"\nВведите {n} целых чисел для последовательности b:")
        b = []
        for i in range(n):
            while True:
                try:
                    value = int(input(f"b_{i+1}: "))
                    b.append(value)
                    break
                except ValueError:
                    print("Ошибка: введите целое число.")
    
    elif choice == 2:
        # Случайные числа от -10 до 10
        random.seed()
        a = [random.randint(-10, 10) for _ in range(n)]
        b = [random.randint(-10, 10) for _ in range(n)]
        print(f"\nИспользуются наборы из {n} случайных чисел от -10 до 10")
    
    elif choice == 3:
        # Готовый набор 1: a - смешанные, b - от 1 до 25
        a = [5, -3, 0, 8, -1, 4, -6, 2, -7, 9, 0, -2, 6, -4, 3, -8, 1, -5, 7, -9, 0, 10, -10, 11, -11]
        b = list(range(1, n+1))
        print("\nИспользуется готовый набор 1: a - смешанные, b - от 1 до 25")
    
    elif choice == 4:
        # Готовый набор 2: a - все положительные
        a = [random.randint(1, 10) for _ in range(n)]
        b = [random.randint(-10, 10) for _ in range(n)]
        print("\nИспользуется готовый набор 2: a - все положительные, b - случайные")
    
    elif choice == 5:
        # Готовый набор 3: a - все отрицательные
        a = [random.randint(-10, -1) for _ in range(n)]
        b = [random.randint(-10, 10) for _ in range(n)]
        print("\nИспользуется готовый набор 3: a - все отрицательные, b - случайные")
    
    # Создаем копию b для отображения изменений
    b_original = b.copy()
    
    # Преобразуем последовательность b по правилу
    for i in range(n):
        if a[i] <= 0:
            b[i] = b[i] * 10
        else:
            b[i] = 0
    
    # Выводим результаты
    print("\nРезультаты преобразования:")
    print("i   |    a_i   |  b_i (исходное) |  b_i (новое) | Преобразование")
    print("-" * 70)
    
    # Выводим первые 15 и последние 10 элементов для компактности
    for i in range(15):
        condition = "a ≤ 0" if a[i] <= 0 else "a > 0"
        transform = "×10" if a[i] <= 0 else "→0"
        print(f"{i+1:2}  | {a[i]:7}   | {b_original[i]:13}   | {b[i]:11}   | {condition} → {transform}")
    
    print("...")
    
    for i in range(n-10, n):
        condition = "a ≤ 0" if a[i] <= 0 else "a > 0"
        transform = "×10" if a[i] <= 0 else "→0"
        print(f"{i+1:2}  | {a[i]:7}   | {b_original[i]:13}   | {b[i]:11}   | {condition} → {transform}")
    
    # Статистика
    print("\n" + "="*70)
    print("Статистика:")
    
    # Подсчет условий
    count_a_le_zero = sum(1 for x in a if x <= 0)
    count_a_gt_zero = sum(1 for x in a if x > 0)
    
    print(f"Количество элементов a_i ≤ 0: {count_a_le_zero}")
    print(f"Количество элементов a_i > 0: {count_a_gt_zero}")
    
    # Изменения в b
    count_b_multiplied = sum(1 for i in range(n) if a[i] <= 0)
    count_b_zeroed = sum(1 for i in range(n) if a[i] > 0)
    
    print(f"\nКоличество элементов b_i, увеличенных в 10 раз: {count_b_multiplied}")
    print(f"Количество элементов b_i, замененных на 0: {count_b_zeroed}")
    
    # Суммы и средние
    print(f"\nСумма исходных b_i: {sum(b_original)}")
    print(f"Сумма новых b_i: {sum(b)}")
    
    if count_b_multiplied > 0:
        avg_multiplied = sum(b[i] for i in range(n) if a[i] <= 0) / count_b_multiplied
        print(f"Среднее значение увеличенных b_i: {avg_multiplied:.2f}")
    
    # Дополнительная информация
    print("\nДополнительная информация о последовательности a:")
    print(f"Минимальное a_i: {min(a)}")
    print(f"Максимальное a_i: {max(a)}")
    print(f"Среднее a_i: {sum(a)/n:.2f}")
    print(f"Количество нулей в a: {sum(1 for x in a if x == 0)}")

if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
