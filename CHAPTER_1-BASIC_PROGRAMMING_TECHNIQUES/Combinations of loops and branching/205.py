"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
7. Сочетания цикла и разветвления

205. Даны натуральное число n, действительные числа a1, ... , an. 
Получить max(|a1|, ..., |an|) и sqrt(a1^2 + ... + an^2).
"""

import math

def calculate_metrics(n, a):
    """
    n: натуральное число (длина последовательности)
    a: список действительных чисел [a₁, a₂, ..., aₙ]
    Возвращает два значения:
    1) max(|a₁|, ..., |aₙ|) - максимальный модуль
    2) sqrt(a₁² + ... + aₙ²) - евклидова норма
    """
    # 1) Максимальный модуль
    max_abs = max(abs(x) for x in a)
    
    # 2) Евклидова норма (корень из суммы квадратов)
    sum_of_squares = sum(x**2 for x in a)
    euclidean_norm = math.sqrt(sum_of_squares)
    
    return max_abs, euclidean_norm


def calculate_metrics_detailed(n, a):
    """
    Подробная версия с промежуточными вычислениями.
    Возвращает максимальный модуль, евклидову норму и детальное описание.
    """
    # Вычисляем модули
    abs_values = [abs(x) for x in a]
    max_abs = max(abs_values)
    
    # Вычисляем квадраты
    squares = [x**2 for x in a]
    sum_squares = sum(squares)
    euclidean_norm = math.sqrt(sum_squares)
    
    # Формируем детальное описание
    details = []
    details.append(f"1. Исходная последовательность: {a}")
    details.append(f"2. Модули элементов: {abs_values}")
    details.append(f"3. Максимальный модуль: {max_abs:.4f}")
    details.append(f"4. Квадраты элементов: {[f'{s:.4f}' for s in squares]}")
    details.append(f"5. Сумма квадратов: {sum_squares:.4f}")
    details.append(f"6. Корень из суммы квадратов: {euclidean_norm:.4f}")
    
    detailed_explanation = "\n".join(details)
    return max_abs, euclidean_norm, detailed_explanation


def main():
    """
    Основная функция программы с выбором режима работы:
    1. Использовать пример из кода
    2. Ввести свои данные
    """
    print("Программа вычисления максимального модуля и евклидовой нормы")
    print("=" * 60)
    print("Вычисляет:")
    print("  1) max(|a₁|, ..., |aₙ|) - максимальный модуль")
    print("  2) √(a₁² + ... + aₙ²) - евклидова норма (длина вектора)")
    print("=" * 60)
    
    choice = input("Выберите режим:\n1 - Использовать пример из кода\n2 - Ввести свои данные\nВведите 1 или 2: ")
    
    if choice == '1':
        # Используем пример из кода
        n = 5
        a = [1.5, -2.3, 4.7, 0.8, -3.2]
        print(f"\nИспользуется пример: n = {n}, a = {a}")
    elif choice == '2':
        # Ввод данных от пользователя
        try:
            n = int(input("\nВведите натуральное число n: "))
            if n <= 0:
                print("Ошибка: n должно быть натуральным числом!")
                return
            
            a = []
            for i in range(n):
                value = float(input(f"Введите a_{i+1}: "))
                a.append(value)
            print(f"\nВведена последовательность: a = {a}")
        except ValueError:
            print("Ошибка ввода! Убедитесь, что вводите числа в правильном формате.")
            return
    else:
        print("Неверный выбор. Программа завершена.")
        return
    
    # Вычисление результатов
    max_abs, euclidean_norm = calculate_metrics(n, a)
    
    # Вывод результатов
    print("\n" + "=" * 60)
    print("РЕЗУЛЬТАТЫ:")
    print(f"a) max(|a₁|, ..., |aₙ|) = {max_abs:.4f}")
    print(f"б) √(a₁² + ... + aₙ²) = {euclidean_norm:.4f}")
    print("=" * 60)
    
    # Предложение показать подробный расчет
    detailed_choice = input("\nПоказать подробный расчет? (да/нет): ")
    if detailed_choice.lower() in ['да', 'д', 'yes', 'y']:
        max_abs_detailed, euclidean_norm_detailed, explanation = calculate_metrics_detailed(n, a)
        print("\nПОДРОБНЫЙ РАСЧЕТ:")
        print("=" * 60)
        print(explanation)
        print("=" * 60)
    
    # Математическое пояснение
    print("\n" + "=" * 60)
    print("МАТЕМАТИЧЕСКОЕ ПОЯСНЕНИЕ:")
    print("=" * 60)
    print("1. max(|a₁|, ..., |aₙ|) - наибольшее расстояние от нуля")
    print("   среди всех элементов последовательности.")
    print()
    print("2. √(a₁² + ... + aₙ²) - евклидова норма или длина вектора")
    print("   в n-мерном пространстве. Это обобщение теоремы Пифагора")
    print("   на многомерный случай.")
    print("=" * 60)
    
    # Сравнение результатов
    print("\n" + "=" * 60)
    print("СРАВНЕНИЕ РЕЗУЛЬТАТОВ:")
    print("=" * 60)
    print(f"Максимальный модуль: {max_abs:.4f}")
    print(f"Евклидова норма: {euclidean_norm:.4f}")
    
    if euclidean_norm >= max_abs:
        print("Евклидова норма всегда больше или равна максимальному модулю,")
        print("так как учитывает вклад всех элементов.")
    else:
        print("(В теории такого не должно происходить, проверьте вычисления)")
    print("=" * 60)


if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
