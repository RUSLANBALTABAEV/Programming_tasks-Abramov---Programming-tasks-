"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
7. Сочетания цикла и разветвления

206. Дано натуральное число n. Найти наибольшее среди чисел 
k*e^sin^2(k+1) (k = 1, ..., n), а также сумму всех этих чисел.
"""

import math

def compute_sequence(n):
    """
    Вычисляет последовательность значений k * exp(sin²(k+1)) для k = 1..n
    Возвращает наибольшее значение и сумму всех значений.
    """
    max_value = float('-inf')  # начальное значение для максимума
    total_sum = 0.0
    
    for k in range(1, n + 1):
        # Вычисляем значение: k * e^(sin²(k+1))
        value = k * math.exp(math.sin(k + 1) ** 2)
        
        # Обновляем максимум
        if value > max_value:
            max_value = value
        
        # Добавляем к сумме
        total_sum += value
    
    return max_value, total_sum


def compute_sequence_detailed(n):
    """
    Вычисляет последовательность с сохранением всех значений и дополнительной информацией.
    Возвращает список значений, максимальное значение с индексом и сумму.
    """
    values = []
    for k in range(1, n + 1):
        value = k * math.exp(math.sin(k + 1) ** 2)
        values.append((k, value))
    
    # Находим максимум и сумму
    max_value = max(values, key=lambda x: x[1])
    total_sum = sum(v for _, v in values)
    
    return values, max_value, total_sum


def main():
    """
    Основная функция программы с выбором режима работы:
    1. Использовать пример из кода
    2. Ввести свое значение n
    """
    print("Программа вычисления последовательности k * e^(sin²(k+1))")
    print("=" * 70)
    print("Для каждого натурального k от 1 до n вычисляется значение:")
    print("f(k) = k * e^(sin²(k+1))")
    print("=" * 70)
    
    choice = input("Выберите режим:\n1 - Использовать пример из кода (n=10)\n2 - Ввести свое значение n\nВведите 1 или 2: ")
    
    if choice == '1':
        # Используем пример из кода
        n = 10
        print(f"\nИспользуется значение n = {n}")
    elif choice == '2':
        # Ввод данных от пользователя
        try:
            n = int(input("\nВведите натуральное число n: "))
            if n <= 0:
                print("Ошибка: n должно быть натуральным числом!")
                return
        except ValueError:
            print("Ошибка ввода! Убедитесь, что вводите целое число.")
            return
    else:
        print("Неверный выбор. Программа завершена.")
        return
    
    # Вычисление результатов
    max_val, total_sum = compute_sequence(n)
    
    # Вывод основных результатов
    print("\n" + "=" * 70)
    print("ОСНОВНЫЕ РЕЗУЛЬТАТЫ:")
    print(f"Для n = {n}:")
    print(f"Наибольшее значение в последовательности: {max_val:.6f}")
    print(f"Сумма всех значений последовательности: {total_sum:.6f}")
    print("=" * 70)
    
    # Предложение показать подробную таблицу
    table_choice = input("\nПоказать подробную таблицу значений? (да/нет): ")
    if table_choice.lower() in ['да', 'д', 'yes', 'y']:
        # Получаем детализированные данные
        values, max_value, total_sum_detailed = compute_sequence_detailed(n)
        
        print("\n" + "=" * 70)
        print("ПОДРОБНАЯ ТАБЛИЦА ЗНАЧЕНИЙ:")
        print("=" * 70)
        print(f"{'k':^5} | {'sin(k+1)':^12} | {'sin²(k+1)':^12} | {'e^(sin²(k+1))':^15} | {'k * e^(sin²(k+1))':^20}")
        print("-" * 70)
        
        for k, value in values:
            sin_val = math.sin(k + 1)
            sin_squared = sin_val ** 2
            exp_val = math.exp(sin_squared)
            
            print(f"{k:^5} | {sin_val:^12.6f} | {sin_squared:^12.6f} | {exp_val:^15.6f} | {value:^20.6f}")
        
        print("=" * 70)
        
        # Информация о максимальном значении
        print(f"\nМаксимальное значение достигается при k = {max_value[0]}:")
        print(f"f({max_value[0]}) = {max_value[1]:.6f}")
    
    # Математическое пояснение
    print("\n" + "=" * 70)
    print("МАТЕМАТИЧЕСКОЕ ПОЯСНЕНИЕ:")
    print("=" * 70)
    print("Последовательность определяется функцией:")
    print("f(k) = k * exp(sin²(k+1))")
    print("\nгде:")
    print("- exp(x) = e^x - экспоненциальная функция")
    print("- sin²(x) = (sin(x))² - квадрат синуса")
    print("- k - натуральное число от 1 до n")
    print("\nСвойства функции:")
    print("1. Значение sin²(k+1) всегда в диапазоне [0, 1]")
    print("2. exp(sin²(k+1)) в диапазоне [1, e] ≈ [1, 2.71828]")
    print("3. Таким образом, f(k) ∈ [k, k*e]")
    print("=" * 70)
    
    # Дополнительная статистика
    print("\n" + "=" * 70)
    print("ДОПОЛНИТЕЛЬНАЯ СТАТИСТИКА:")
    print("=" * 70)
    
    # Вычисляем среднее значение
    average = total_sum / n if n > 0 else 0
    print(f"Среднее значение: {average:.6f}")
    
    # Минимальное значение (вычисляем заново для полноты)
    values_detailed, _, _ = compute_sequence_detailed(n)
    min_value = min(values_detailed, key=lambda x: x[1])
    print(f"Минимальное значение: {min_value[1]:.6f} (при k = {min_value[0]})")
    
    # Отношение максимального к минимальному
    if min_value[1] != 0:
        ratio = max_val / min_value[1]
        print(f"Отношение максимального к минимальному: {ratio:.6f}")
    
    print("=" * 70)


if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
