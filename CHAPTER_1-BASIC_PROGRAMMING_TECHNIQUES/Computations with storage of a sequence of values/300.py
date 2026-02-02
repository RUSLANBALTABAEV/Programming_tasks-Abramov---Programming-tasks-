"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
9. Вычисления с хранением последовательности значений

300. Даны натуральное число n, действительные числа a1,…, an. 
Получить b1,…, b10, где bi равно сумме тех членов последовательности a1, … an, которые принадлежат полуинтервалу (i – 1, i] (i = 1, …, 10).
Если полуинтервал не содержит членов последовательности, то соответствующее bi положить равным нулю.
"""


import math
import random

def main():
    print("Программа вычисляет суммы членов последовательности, принадлежащих заданным полуинтервалам.")
    print("Дано: натуральное n, действительные числа a_1, ..., a_n.")
    print("Надо получить b_1, ..., b_10, где b_i равно сумме тех a_k, которые лежат в (i-1, i].")
    print("Если таких a_k нет, то b_i = 0.")
    
    # Выбор способа ввода данных
    print("\nВыберите способ задания последовательности:")
    print("1. Ввести числа вручную")
    print("2. Использовать случайные числа от -5 до 15")
    print("3. Использовать готовый набор 1: числа от 0.5 до 10.5")
    print("4. Использовать готовый набор 2: целые числа от 1 до 10")
    print("5. Использовать готовый набор 3: специальный набор для демонстрации")
    
    while True:
        try:
            choice = int(input("\nВаш выбор (1-5): "))
            if 1 <= choice <= 5:
                break
            else:
                print("Ошибка: выберите число от 1 до 5.")
        except ValueError:
            print("Ошибка: введите целое число от 1 до 5.")
    
    # Ввод n
    if choice == 1:
        while True:
            try:
                n = int(input("Введите натуральное число n: "))
                if n > 0:
                    break
                else:
                    print("Ошибка: n должно быть натуральным числом (больше 0).")
            except ValueError:
                print("Ошибка: введите натуральное число.")
    else:
        n = 15  # по умолчанию для не-ручного ввода
        print(f"Используется n = {n}")
    
    # Инициализация последовательности в зависимости от выбора
    if choice == 1:
        # Ручной ввод
        print(f"\nВведите {n} действительных чисел:")
        a = []
        for i in range(n):
            while True:
                try:
                    value = float(input(f"a_{i+1}: "))
                    a.append(value)
                    break
                except ValueError:
                    print("Ошибка: введите действительное число.")
    
    elif choice == 2:
        # Случайные числа от -5 до 15
        random.seed()
        a = [random.uniform(-5, 15) for _ in range(n)]
        print(f"\nИспользуется набор из {n} случайных чисел от -5 до 15")
    
    elif choice == 3:
        # Готовый набор 1: числа от 0.5 до 10.5
        a = [0.5 + i * (10.0 / n) for i in range(n)]
        print("\nИспользуется готовый набор 1: равномерное распределение от 0.5 до 10.5")
    
    elif choice == 4:
        # Готовый набор 2: целые числа от 1 до 10
        random.seed()
        a = [float(random.randint(1, 10)) for _ in range(n)]
        print("\nИспользуется готовый набор 2: целые числа от 1 до 10")
    
    elif choice == 5:
        # Готовый набор 3: специальный набор для демонстрации
        a = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0,
             1.1, 2.5, 3.3, 4.7, 5.2, 6.9, 7.8, 8.1, 9.4, 10.0,
             10.5, -1.2, 0.0, 2.0, 2.0]
        n = len(a)
        print("\nИспользуется готовый набор 3: специальный набор для демонстрации")
    
    # Вывод исходной последовательности
    print(f"\nИсходная последовательность a (n = {n}):")
    for i in range(min(n, 20)):  # показываем первые 20 элементов
        print(f"a_{i+1:2} = {a[i]:7.3f}")
    if n > 20:
        print(f"... (еще {n-20} элементов)")
    
    # Инициализируем b (10 элементов, все нули)
    b = [0.0] * 10
    
    # Для хранения информации о распределении чисел по интервалам
    distribution = [[] for _ in range(10)]  # список списков: для каждого интервала храним числа, попавшие в него
    
    # Обрабатываем каждое число a_k
    for k in range(n):
        value = a[k]
        # Определяем, в какой интервал попадает value
        if value > 0 and value <= 10:
            # Вычисляем i = ceil(value)
            i = math.ceil(value)
            # i будет от 1 до 10
            b[i-1] += value
            distribution[i-1].append(value)
        # Иначе: value <= 0 или value > 10 - не попадает ни в один интервал
    
    # Вывод результатов
    print("\n" + "="*60)
    print("Результаты:")
    print("i | Полуинтервал | Сумма b_i | Количество чисел в интервале | Числа в интервале")
    print("-" * 80)
    
    for i in range(10):
        interval_start = i
        interval_end = i + 1
        count = len(distribution[i])
        numbers_str = ", ".join(f"{x:.3f}" for x in distribution[i][:5])  # показываем первые 5 чисел
        if count > 5:
            numbers_str += f", ... (еще {count-5})"
        print(f"{i+1:2} | ({interval_start:3}, {interval_end:3}] | {b[i]:9.3f} | {count:25} | {numbers_str}")
    
    # Дополнительная информация
    print("\n" + "="*60)
    print("Дополнительная информация:")
    
    # Подсчет чисел, попавших в интервалы
    total_in_intervals = sum(len(interval) for interval in distribution)
    total_outside = n - total_in_intervals
    
    print(f"Всего чисел в последовательности: {n}")
    print(f"Чисел, попавших в интервалы (0, 10]: {total_in_intervals}")
    print(f"Чисел вне интервалов (≤0 или >10): {total_outside}")
    
    # Сумма всех чисел в последовательности
    total_sum = sum(a)
    sum_in_intervals = sum(b)
    sum_outside = total_sum - sum_in_intervals
    
    print(f"\nСумма всех чисел в последовательности: {total_sum:.3f}")
    print(f"Сумма чисел в интервалах (0, 10]: {sum_in_intervals:.3f}")
    print(f"Сумма чисел вне интервалов: {sum_outside:.3f}")
    
    # Процент от общей суммы
    if total_sum != 0:
        percent_in = (sum_in_intervals / total_sum) * 100
        print(f"Процент от общей суммы в интервалах: {percent_in:.1f}%")
    
    # Вывод всех интервалов, где сумма ненулевая
    non_zero_indices = [i for i in range(10) if b[i] != 0]
    print(f"\nИнтервалы с ненулевой суммой: {[i+1 for i in non_zero_indices]}")
    
    # Если есть числа вне интервалов, покажем их
    if total_outside > 0:
        outside_numbers = []
        for value in a:
            if value <= 0 or value > 10:
                outside_numbers.append(value)
        
        print(f"\nЧисла вне интервалов (≤0 или >10):")
        for j, val in enumerate(outside_numbers[:10]):
            print(f"  {val:.3f}", end=", ")
            if (j+1) % 5 == 0:
                print()
        if len(outside_numbers) > 10:
            print(f"... (еще {len(outside_numbers)-10} чисел)")
        print()

if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
