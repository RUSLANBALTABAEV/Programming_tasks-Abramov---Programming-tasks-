"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
7. Сочетания цикла и разветвления

208. Даны натуральное число n, целые числа a₁, ..., aₙ. Найти:
a) наименьшее из четных чисел, входящих в последовательность a₁-1, a₁, a₂, ..., aₙ;
"""

def find_min_even_in_sequence(n, a):
    """
    Находит наименьшее четное число в последовательности a₁-1, a₁, a₂, ..., aₙ.
    n: натуральное число (количество элементов)
    a: список целых чисел [a₁, a₂, ..., aₙ]
    Возвращает наименьшее четное число или None, если четных чисел нет.
    """
    # Формируем последовательность: a₁-1, a₁, a₂, ..., aₙ
    sequence = [a[0] - 1] + a
    
    # Находим все четные числа в последовательности
    even_numbers = [x for x in sequence if x % 2 == 0]
    
    # Возвращаем минимальное четное число, если такие есть
    if even_numbers:
        return min(even_numbers)
    else:
        return None


def find_min_even_detailed(n, a):
    """
    Находит наименьшее четное число с подробным выводом каждого шага.
    Возвращает результат и детальное описание.
    """
    steps = []
    steps.append(f"1. Исходная последовательность: a = {a}")
    
    # Формируем последовательность
    a1_minus_1 = a[0] - 1
    sequence = [a1_minus_1] + a
    steps.append(f"2. Формируем последовательность: a₁-1, a₁, a₂, ..., aₙ")
    steps.append(f"   a₁-1 = {a[0]} - 1 = {a1_minus_1}")
    steps.append(f"   Полная последовательность: {sequence}")
    
    # Находим четные числа
    even_numbers = [x for x in sequence if x % 2 == 0]
    steps.append(f"3. Четные числа в последовательности: {even_numbers}")
    
    if even_numbers:
        min_even = min(even_numbers)
        steps.append(f"4. Наименьшее четное число: {min_even}")
        detailed_explanation = "\n".join(steps)
        return min_even, detailed_explanation
    else:
        steps.append("4. Четных чисел в последовательности нет!")
        detailed_explanation = "\n".join(steps)
        return None, detailed_explanation


def main():
    """
    Основная функция программы с выбором режима работы:
    1. Использовать примеры
    2. Ввести свои данные
    """
    print("Программа поиска наименьшего четного числа в последовательности")
    print("=" * 60)
    print("Находит наименьшее четное число в последовательности:")
    print("a₁-1, a₁, a₂, ..., aₙ")
    print("=" * 60)
    
    choice = input("Выберите режим:\n1 - Использовать примеры\n2 - Ввести свои данные\nВведите 1 или 2: ")
    
    if choice == '1':
        # Используем примеры
        examples = [
            ("Пример 1", 5, [3, 5, 7, 2, 8]),
            ("Пример 2 (все нечетные)", 4, [1, 3, 5, 7]),
            ("Пример 3 (все четные)", 3, [2, 4, 6]),
            ("Пример 4 (с отрицательными числами)", 6, [-1, 0, 3, -2, 5, 4]),
            ("Пример 5 (большой пример)", 8, [10, 15, 20, 25, 30, 35, 40, 45]),
        ]
        
        for title, n, a in examples:
            print(f"\n{title}:")
            print(f"n = {n}, a = {a}")
            
            result = find_min_even_in_sequence(n, a)
            if result is not None:
                print(f"Наименьшее четное число: {result}")
            else:
                print("Четных чисел в последовательности нет!")
            
            # Для первого примера предлагаем показать детали
            if title == "Пример 1":
                detailed_choice = input("\nПоказать подробное решение для этого примера? (да/нет): ")
                if detailed_choice.lower() in ['да', 'д', 'yes', 'y']:
                    result_detailed, explanation = find_min_even_detailed(n, a)
                    print("\nПодробное решение:")
                    print(explanation)
            
            print("-" * 40)
    
    elif choice == '2':
        # Ввод данных от пользователя
        try:
            n = int(input("\nВведите натуральное число n: "))
            if n <= 0:
                print("Ошибка: n должно быть натуральным числом!")
                return
            
            a = []
            for i in range(n):
                value = int(input(f"Введите a_{i+1}: "))
                a.append(value)
            
            print(f"\nВведена последовательность: a = {a}")
            
            # Вычисление результата
            result = find_min_even_in_sequence(n, a)
            
            if result is not None:
                print(f"Наименьшее четное число: {result}")
            else:
                print("Четных чисел в последовательности нет!")
            
            # Предложение показать подробное решение
            detailed_choice = input("\nПоказать подробное решение? (да/нет): ")
            if detailed_choice.lower() in ['да', 'д', 'yes', 'y']:
                result_detailed, explanation = find_min_even_detailed(n, a)
                print("\nПодробное решение:")
                print(explanation)
        
        except ValueError:
            print("Ошибка ввода! Убедитесь, что вводите целые числа.")
            return
    
    else:
        print("Неверный выбор. Программа завершена.")
        return
    
    # Пояснение алгоритма
    print("\n" + "=" * 60)
    print("ПОЯСНЕНИЕ АЛГОРИТМА:")
    print("=" * 60)
    print("1. Формируем последовательность, добавляя элемент a₁-1 в начало")
    print("2. Находим все четные числа в полученной последовательности")
    print("3. Среди найденных четных чисел ищем минимальное значение")
    print("4. Если четных чисел нет, возвращаем None")
    print("=" * 60)
    
    # Проверка работы на дополнительных примерах
    interactive_choice = input("\nПротестировать дополнительные примеры? (да/нет): ")
    if interactive_choice.lower() in ['да', 'д', 'yes', 'y']:
        print("\n" + "=" * 60)
        print("ТЕСТИРОВАНИЕ ДОПОЛНИТЕЛЬНЫХ ПРИМЕРОВ:")
        print("=" * 60)
        
        test_cases = [
            (3, [1, 2, 3], "a₁-1=0, есть четные: 0, 2 → min=0"),
            (2, [0, 1], "a₁-1=-1, есть четные: 0 → min=0"),
            (3, [-1, -2, -3], "a₁-1=-2, есть четные: -2 → min=-2"),
            (1, [5], "a₁-1=4, есть четные: 4 → min=4"),
            (2, [3, 3], "a₁-1=2, есть четные: 2 → min=2"),
        ]
        
        for n_test, a_test, description in test_cases:
            result = find_min_even_in_sequence(n_test, a_test)
            if result is not None:
                print(f"n={n_test}, a={a_test}: {result} ({description})")
            else:
                print(f"n={n_test}, a={a_test}: четных чисел нет ({description})")
        
        print("=" * 60)


if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
