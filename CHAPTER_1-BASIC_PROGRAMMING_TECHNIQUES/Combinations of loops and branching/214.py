"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
7. Сочетания цикла и разветвления

214. Пусть  
a₀ = cos²(1); a₁ = -sin²(1); aₖ = 2aₖ₋₁ - aₖ₋₂; k = 2, 3, ...
Найти сумму квадратов тех чисел a₁, ..., a₁₀₀, которые не превосходят двух.
"""

import math

def compute_sequence_recursive(n):
    """
    Вычисляет последовательность aₖ рекуррентно для k=0..n.
    Возвращает список значений a₀,...,aₙ.
    """
    a = [0.0] * (n + 1)
    a[0] = math.cos(1) ** 2
    a[1] = -math.sin(1) ** 2
    
    for k in range(2, n + 1):
        a[k] = 2 * a[k-1] - a[k-2]
    
    return a


def compute_sequence_formula(n):
    """
    Вычисляет последовательность aₖ по аналитической формуле.
    aₖ = cos²(1) - k
    Возвращает список значений a₀,...,aₙ.
    """
    c = math.cos(1) ** 2
    a = [c - k for k in range(n + 1)]
    return a


def solve_problem():
    """
    Решает задачу: находит сумму квадратов тех чисел a₁,...,a₁₀₀,
    которые не превосходят двух.
    """
    n = 100
    # Используем формулу, так как она точнее и быстрее
    a = compute_sequence_formula(n)
    
    # Выбираем элементы от 1 до 100, которые <= 2
    selected = []
    sum_squares = 0.0
    
    for k in range(1, n + 1):
        if a[k] <= 2:
            selected.append((k, a[k]))
            sum_squares += a[k] ** 2
    
    return a, selected, sum_squares


def solve_problem_detailed():
    """
    Подробное решение с выводом шагов.
    """
    n = 100
    steps = []
    
    steps.append("РЕШЕНИЕ ЗАДАЧИ 214")
    steps.append("=" * 70)
    steps.append("Дано:")
    steps.append("  a₀ = cos²(1)")
    steps.append("  a₁ = -sin²(1)")
    steps.append("  aₖ = 2aₖ₋₁ - aₖ₋₂, k = 2, 3, ...")
    steps.append("")
    steps.append("Найти сумму квадратов тех чисел a₁, ..., a₁₀₀, которые не превосходят двух.")
    steps.append("")
    
    # 1. Найдем аналитическую формулу
    steps.append("1. Найдем общую формулу для aₖ.")
    steps.append("   Рекуррентное уравнение: aₖ - 2aₖ₋₁ + aₖ₋₂ = 0")
    steps.append("   Характеристическое уравнение: r² - 2r + 1 = 0")
    steps.append("   Корень: r = 1 (кратности 2)")
    steps.append("   Общее решение: aₖ = (C₁ + C₂·k)·1ᵏ = C₁ + C₂·k")
    steps.append("")
    
    # Начальные условия
    c = math.cos(1) ** 2
    s = math.sin(1) ** 2
    steps.append("2. Используем начальные условия:")
    steps.append(f"   a₀ = C₁ = cos²(1) = {c:.6f}")
    steps.append(f"   a₁ = C₁ + C₂ = -sin²(1) = {-s:.6f}")
    steps.append(f"   C₂ = -sin²(1) - cos²(1) = -(sin²(1) + cos²(1)) = -1")
    steps.append("")
    steps.append(f"3. Итак, aₖ = cos²(1) - k = {c:.6f} - k")
    steps.append("")
    
    # 4. Анализ условия aₖ <= 2
    steps.append("4. Условие отбора: aₖ ≤ 2")
    steps.append(f"   {c:.6f} - k ≤ 2")
    steps.append(f"   -k ≤ 2 - {c:.6f}")
    steps.append(f"   k ≥ {c:.6f} - 2 ≈ {c - 2:.6f}")
    steps.append(f"   Так как k ≥ 1, и {c - 2:.6f} < 1, условие выполняется для всех k ≥ 1.")
    steps.append("   Вывод: все a₁,...,a₁₀₀ удовлетворяют условию aₖ ≤ 2.")
    steps.append("")
    
    # 5. Сумма квадратов
    steps.append("5. Вычисляем сумму квадратов S = Σ (aₖ)² для k=1..100")
    steps.append(f"   S = Σ (cos²(1) - k)² = Σ ({c:.6f} - k)²")
    steps.append("   Раскроем квадрат: (c - k)² = c² - 2c·k + k²")
    steps.append("   S = 100·c² - 2c·Σk + Σk²")
    steps.append("   Σk (k=1..100) = 100·101/2 = 5050")
    steps.append("   Σk² (k=1..100) = 100·101·201/6 = 338350")
    steps.append("")
    
    # Вычисления
    c_squared = c ** 2
    term1 = 100 * c_squared
    term2 = 2 * c * 5050
    term3 = 338350
    S = term1 - term2 + term3
    
    steps.append(f"6. Вычисления:")
    steps.append(f"   c² = ({c:.6f})² = {c_squared:.6f}")
    steps.append(f"   100·c² = 100·{c_squared:.6f} = {term1:.6f}")
    steps.append(f"   2c·5050 = 2·{c:.6f}·5050 = {term2:.6f}")
    steps.append(f"   Σk² = 338350")
    steps.append(f"   S = {term1:.6f} - {term2:.6f} + {term3} = {S:.6f}")
    steps.append("")
    
    # 7. Проверка рекуррентным вычислением
    steps.append("7. Проверка рекуррентным вычислением (первые 10 элементов):")
    a_rec = compute_sequence_recursive(10)
    a_form = compute_sequence_formula(10)
    
    steps.append("   k   По формуле      Рекуррентно     Разница")
    steps.append("   ---------------------------------------------")
    for k in range(11):
        diff = abs(a_form[k] - a_rec[k])
        steps.append(f"   {k:2}   {a_form[k]:12.6f}   {a_rec[k]:12.6f}   {diff:12.6e}")
    
    steps.append("")
    steps.append(f"8. Итоговый результат: S = {S:.10f}")
    steps.append("=" * 70)
    
    detailed_explanation = "\n".join(steps)
    return detailed_explanation, S


def main():
    """
    Основная функция программы.
    """
    print("Программа решения задачи 214")
    print("=" * 70)
    print("Последовательность определена как:")
    print("  a₀ = cos²(1), a₁ = -sin²(1), aₖ = 2aₖ₋₁ - aₖ₋₂ (k ≥ 2)")
    print("Найти сумму квадратов тех чисел a₁,...,a₁₀₀, которые ≤ 2.")
    print("=" * 70)
    
    choice = input("Выберите режим:\n1 - Краткий результат\n2 - Подробное решение\nВведите 1 или 2: ")
    
    if choice == '1':
        print("\n" + "=" * 70)
        print("КРАТКИЙ РЕЗУЛЬТАТ")
        print("=" * 70)
        
        a, selected, sum_squares = solve_problem()
        
        print(f"Всего элементов от a₁ до a₁₀₀: 100")
        print(f"Из них удовлетворяют условию aₖ ≤ 2: {len(selected)}")
        
        # Покажем несколько значений
        print("\nПервые 10 значений:")
        print(" k    aₖ")
        print("-" * 20)
        for k in range(1, 11):
            print(f"{k:2}   {a[k]:.6f}")
        
        print("\nПоследние 10 значений:")
        print(" k    aₖ")
        print("-" * 20)
        for k in range(91, 101):
            print(f"{k:3}   {a[k]:.6f}")
        
        print(f"\nСумма квадратов: {sum_squares:.10f}")
        print("=" * 70)
    
    elif choice == '2':
        print("\n" + "=" * 70)
        explanation, S = solve_problem_detailed()
        print(explanation)
        
        # Дополнительная информация
        print("\n" + "=" * 70)
        print("ДОПОЛНИТЕЛЬНАЯ ИНФОРМАЦИЯ")
        print("=" * 70)
        
        # Точные значения тригонометрических функций
        cos1 = math.cos(1)
        sin1 = math.sin(1)
        print(f"cos(1) = {cos1:.15f}")
        print(f"sin(1) = {sin1:.15f}")
        print(f"cos²(1) = {cos1**2:.15f}")
        print(f"sin²(1) = {sin1**2:.15f}")
        print(f"cos²(1) + sin²(1) = {cos1**2 + sin1**2:.15f} (должно быть 1)")
        
        # Проверка формулы
        print("\nПроверка формулы aₖ = cos²(1) - k:")
        print("Для k=0: cos²(1) - 0 =", cos1**2)
        print("Для k=1: cos²(1) - 1 =", cos1**2 - 1, "= -sin²(1) =", -sin1**2)
        
        # Вычисление суммы с помощью разных методов
        print("\nСравнение методов вычисления суммы:")
        
        # Метод 1: по формуле
        c = cos1**2
        S_formula = 100*c**2 - 2*c*5050 + 338350
        
        # Метод 2: прямым суммированием
        S_direct = 0.0
        for k in range(1, 101):
            a_k = c - k
            S_direct += a_k**2
        
        print(f"По формуле:        {S_formula:.10f}")
        print(f"Прямым суммированием: {S_direct:.10f}")
        print(f"Разница:           {abs(S_formula - S_direct):.2e}")
        
        # Анализ поведения последовательности
        print("\nАнализ последовательности:")
        print("aₖ = cos²(1) - k - линейная убывающая функция")
        print("a₁ = cos²(1) - 1 = -sin²(1) ≈ -0.708073")
        print("a₁₀₀ = cos²(1) - 100 ≈ -99.708073")
        print("Все элементы отрицательны, поэтому все ≤ 2.")
        
        # Минимальный и максимальный элементы среди a₁..a₁₀₀
        a_min = c - 100
        a_max = c - 1
        print(f"\nМинимальное значение: a₁₀₀ = {a_min:.6f}")
        print(f"Максимальное значение: a₁ = {a_max:.6f}")
        
        print("=" * 70)
    
    else:
        print("Неверный выбор. Программа завершена.")
        return
    
    # Интерактивная проверка значений
    print("\n" + "=" * 70)
    check_choice = input("Проверить значения для конкретных k? (да/нет): ")
    if check_choice.lower() in ['да', 'д', 'yes', 'y']:
        c = math.cos(1)**2
        print("\nВведите k от 1 до 100 (0 для выхода):")
        while True:
            try:
                k = int(input("k = "))
                if k == 0:
                    break
                if 1 <= k <= 100:
                    a_k = c - k
                    print(f"a_{k} = {c:.6f} - {k} = {a_k:.6f}")
                    print(f"a_{k} ≤ 2? {a_k <= 2}")
                    print(f"Квадрат: {a_k**2:.6f}")
                else:
                    print("k должно быть от 1 до 100.")
            except ValueError:
                print("Ошибка: введите целое число.")
    
    print("\n" + "=" * 70)
    print("ЗАКЛЮЧЕНИЕ:")
    print("=" * 70)
    print("Поскольку все элементы a₁,...,a₁₀₀ отрицательны,")
    print("они все удовлетворяют условию aₖ ≤ 2.")
    print("Поэтому искомая сумма квадратов - это просто сумма")
    print("квадратов всех 100 элементов последовательности.")
    print("=" * 70)


if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
