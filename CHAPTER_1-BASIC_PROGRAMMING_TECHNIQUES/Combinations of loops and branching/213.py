"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
7. Сочетания цикла и разветвления

213. Пусть
aᵢ = (i-1)/(i+1) + sin((i-1)³/(i+1)), i = 1, 2, ...
Дано натуральное n. Среди a₁, ..., aₙ найти все положительные числа,
среди положительных a₁, ..., aₙ выбрать наименьшее число.
"""


import math

def compute_sequence(n):
    """
    Вычисляет последовательность aᵢ для i = 1..n.
    aᵢ = (i-1)/(i+1) + sin((i-1)³/(i+1))
    Возвращает список значений.
    """
    a = []
    for i in range(1, n + 1):
        numerator = i - 1
        denominator = i + 1
        
        if denominator == 0:  # Для i=1, denominator=2, так что это не произойдет
            continue
        
        first_term = numerator / denominator
        second_term = math.sin((numerator ** 3) / denominator)
        a_i = first_term + second_term
        a.append(a_i)
    
    return a


def analyze_sequence(n, a):
    """
    Анализирует последовательность:
    1. Находит все положительные числа
    2. Среди положительных находит наименьшее
    Возвращает:
    - список положительных чисел с индексами
    - наименьшее положительное число с его индексом
    - статистику
    """
    # Находим все положительные числа (aᵢ > 0)
    positive_items = []
    for i, value in enumerate(a):
        if value > 0:
            positive_items.append({
                'index': i + 1,  # 1-индексация
                'value': value
            })
    
    # Находим наименьшее среди положительных
    if positive_items:
        min_positive = min(positive_items, key=lambda x: x['value'])
        return positive_items, min_positive
    else:
        return positive_items, None


def analyze_sequence_detailed(n, a):
    """
    Подробный анализ последовательности с пошаговым выводом.
    """
    steps = []
    steps.append("ПОДРОБНЫЙ АНАЛИЗ ПОСЛЕДОВАТЕЛЬНОСТИ")
    steps.append("=" * 70)
    steps.append(f"Формула: aᵢ = (i-1)/(i+1) + sin((i-1)³/(i+1))")
    steps.append(f"Количество элементов: n = {n}")
    steps.append("")
    
    # Таблица вычислений
    steps.append("Вычисление значений:")
    steps.append(" i    (i-1)/(i+1)   (i-1)³/(i+1)   sin((i-1)³/(i+1))   aᵢ")
    steps.append("-" * 70)
    
    for i in range(1, n + 1):
        numerator = i - 1
        denominator = i + 1
        first_term = numerator / denominator
        cube_term = (numerator ** 3) / denominator
        sin_term = math.sin(cube_term)
        a_i = first_term + sin_term
        
        steps.append(f"{i:2}   {first_term:12.6f}   {cube_term:12.6f}   {sin_term:17.6f}   {a_i:12.6f}")
    
    # Поиск положительных чисел
    steps.append("\nПоиск положительных чисел (aᵢ > 0):")
    positive_count = 0
    for i in range(n):
        if a[i] > 0:
            positive_count += 1
            steps.append(f"  a_{i+1} = {a[i]:.6f} > 0")
    
    if positive_count == 0:
        steps.append("  Положительных чисел не найдено.")
    else:
        steps.append(f"  Всего положительных чисел: {positive_count}")
    
    # Нахождение наименьшего положительного
    steps.append("\nПоиск наименьшего положительного числа:")
    positive_items = []
    for i in range(n):
        if a[i] > 0:
            positive_items.append((i+1, a[i]))
    
    if positive_items:
        # Находим наименьшее по значению
        min_index, min_value = min(positive_items, key=lambda x: x[1])
        steps.append(f"  Наименьшее положительное число: a_{min_index} = {min_value:.6f}")
        
        # Проверяем, есть ли еще элементы с таким же значением (редко, но возможно)
        same_value_items = [(idx, val) for idx, val in positive_items if abs(val - min_value) < 1e-10]
        if len(same_value_items) > 1:
            steps.append("  Примечание: есть несколько элементов с таким же значением:")
            for idx, val in same_value_items:
                steps.append(f"    a_{idx} = {val:.6f}")
    else:
        steps.append("  Положительных чисел нет, наименьшее не определено.")
    
    steps.append("=" * 70)
    
    detailed_explanation = "\n".join(steps)
    return detailed_explanation, positive_items


def main():
    """
    Основная функция программы с выбором режима работы.
    """
    print("Программа анализа последовательности aᵢ")
    print("=" * 70)
    print("Формула: aᵢ = (i-1)/(i+1) + sin((i-1)³/(i+1))")
    print("Задача: найти все положительные числа и наименьшее среди них.")
    print("=" * 70)
    
    choice = input("Выберите режим:\n1 - Использовать примеры\n2 - Ввести свое n\nВведите 1 или 2: ")
    
    if choice == '1':
        # Примеры для демонстрации
        examples = [
            ("Пример 1 (n=5)", 5),
            ("Пример 2 (n=10)", 10),
            ("Пример 3 (n=15)", 15),
            ("Пример 4 (n=20)", 20),
            ("Пример 5 (малое n, n=3)", 3),
        ]
        
        for title, n in examples:
            print(f"\n{title}:")
            print("-" * 50)
            
            # Вычисляем последовательность
            a = compute_sequence(n)
            positive_items, min_positive = analyze_sequence(n, a)
            
            # Выводим результаты
            print(f"n = {n}")
            print(f"Последовательность: {[f'{val:.4f}' for val in a]}")
            
            if positive_items:
                print(f"\nПоложительные числа (всего {len(positive_items)}):")
                for item in positive_items:
                    print(f"  a_{item['index']} = {item['value']:.6f}")
                
                print(f"\nНаименьшее положительное число:")
                print(f"  a_{min_positive['index']} = {min_positive['value']:.6f}")
            else:
                print("\nПоложительных чисел не найдено.")
            
            # Для первого примера предлагаем показать детали
            if title == "Пример 1 (n=5)":
                detailed_choice = input("\nПоказать подробный анализ для этого примера? (да/нет): ")
                if detailed_choice.lower() in ['да', 'д', 'yes', 'y']:
                    explanation, _ = analyze_sequence_detailed(n, a)
                    print("\n" + explanation)
            
            print("-" * 50)
    
    elif choice == '2':
        # Ввод данных от пользователя
        try:
            n = int(input("\nВведите натуральное число n: "))
            if n <= 0:
                print("Ошибка: n должно быть натуральным числом!")
                return
            
            # Вычисляем последовательность
            a = compute_sequence(n)
            positive_items, min_positive = analyze_sequence(n, a)
            
            # Выводим результаты
            print(f"\nРезультаты для n = {n}:")
            print("=" * 50)
            
            # Можно вывести не всю последовательность, если n большое
            if n <= 20:
                print(f"Последовательность: {[f'{val:.4f}' for val in a]}")
            else:
                print(f"Первые 10 элементов: {[f'{val:.4f}' for val in a[:10]]}")
                print(f"Последние 10 элементов: {[f'{val:.4f}' for val in a[-10:]]}")
            
            if positive_items:
                print(f"\nПоложительные числа (всего {len(positive_items)}):")
                # Если положительных много, покажем только первые 10
                if len(positive_items) > 10:
                    print("  (показаны первые 10)")
                    for item in positive_items[:10]:
                        print(f"  a_{item['index']} = {item['value']:.6f}")
                    print(f"  ... и еще {len(positive_items) - 10} положительных чисел")
                else:
                    for item in positive_items:
                        print(f"  a_{item['index']} = {item['value']:.6f}")
                
                print(f"\nНаименьшее положительное число:")
                print(f"  a_{min_positive['index']} = {min_positive['value']:.6f}")
            else:
                print("\nПоложительных чисел не найдено.")
            
            print("=" * 50)
            
            # Предложение показать подробный анализ
            if n <= 30:  # Ограничим, чтобы не выводить огромные таблицы
                detailed_choice = input("\nПоказать подробный анализ? (да/нет): ")
                if detailed_choice.lower() in ['да', 'д', 'yes', 'y']:
                    explanation, _ = analyze_sequence_detailed(n, a)
                    print("\n" + explanation)
            else:
                print("\nПримечание: подробный анализ доступен только для n ≤ 30.")
                quick_detail = input("Показать краткий анализ первых 10 элементов? (да/нет): ")
                if quick_detail.lower() in ['да', 'д', 'yes', 'y']:
                    # Покажем краткую таблицу для первых 10 элементов
                    print("\nКраткий анализ первых 10 элементов:")
                    print(" i    aᵢ")
                    print("-" * 20)
                    for i in range(min(10, n)):
                        print(f"{i+1:2}   {a[i]:.6f}")
        
        except ValueError:
            print("Ошибка ввода! Убедитесь, что вводите целое число.")
            return
    
    else:
        print("Неверный выбор. Программа завершена.")
        return
    
    # Математический анализ
    print("\n" + "=" * 70)
    print("МАТЕМАТИЧЕСКИЙ АНАЛИЗ:")
    print("=" * 70)
    
    print("1. Асимптотическое поведение при i → ∞:")
    print("   (i-1)/(i+1) → 1")
    print("   (i-1)³/(i+1) ≈ i² → ∞")
    print("   sin((i-1)³/(i+1)) осциллирует между -1 и 1")
    print("   Таким образом, aᵢ ∈ [0, 2] при больших i")
    print()
    print("2. Поведение при малых i:")
    print("   i=1: a₁ = 0/2 + sin(0/2) = 0")
    print("   i=2: a₂ = 1/3 + sin(1/3) ≈ 0.3333 + 0.3272 = 0.6605")
    print("   i=3: a₃ = 2/4 + sin(8/4) = 0.5 + sin(2) ≈ 0.5 + 0.9093 = 1.4093")
    print()
    print("3. Особые точки:")
    print("   sin((i-1)³/(i+1)) = 0 при (i-1)³/(i+1) = kπ, k ∈ ℤ")
    print("   В этих точках aᵢ = (i-1)/(i+1) ≥ 0")
    print()
    print("4. Положительность:")
    print("   Поскольку (i-1)/(i+1) ≥ 0 для всех i ≥ 1,")
    print("   отрицательные значения возможны только если sin(...) < -(i-1)/(i+1)")
    print("   Это может произойти при некоторых i.")
    print("=" * 70)
    
    # Дополнительное исследование
    print("\n" + "=" * 70)
    print("ДОПОЛНИТЕЛЬНОЕ ИССЛЕДОВАНИЕ:")
    print("=" * 70)
    
    # Исследуем, всегда ли есть положительные числа
    print("Для разных n исследуем наличие положительных чисел:")
    test_n_values = [1, 2, 3, 5, 10, 20, 50]
    print(" n   Положительных   Наименьшее положительное")
    print("-" * 50)
    
    for test_n in test_n_values:
        test_a = compute_sequence(test_n)
        test_positive, test_min = analyze_sequence(test_n, test_a)
        if test_positive:
            pos_count = len(test_positive)
            min_val = test_min['value']
            print(f"{test_n:2}   {pos_count:12}   a_{test_min['index']} = {min_val:.6f}")
        else:
            print(f"{test_n:2}   {'0':12}   не определено")
    
    print("\nВывод: При n≥2 всегда есть положительные числа,")
    print("поскольку a₂ > 0, а a₁ = 0 (не положительное).")
    print("Наименьшее положительное обычно достигается при малых i.")
    print("=" * 70)


if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
