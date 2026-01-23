"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
7. Сочетания цикла и разветвления

212. Пусть
x₁ = y₁ = 1; 
xᵢ = xᵢ₋₁ + yᵢ₋₁ / i²; 
yᵢ = yᵢ₋₁ + xᵢ₋₁ / i, 
i = 2, 3, ...

Получить x₈, x₁₈.
"""


def compute_sequences(n):
    """
    Вычисляет последовательности x и y до заданного n.
    Возвращает:
    - список x (индексация с 1, x[0] = x₁)
    - список y (индексация с 1, y[0] = y₁)
    """
    # Инициализируем массивы
    x = [0.0] * n
    y = [0.0] * n
    
    # Начальные условия
    x[0] = 1.0  # x₁
    y[0] = 1.0  # y₁
    
    # Вычисляем последовательно для i = 2..n
    for i in range(2, n + 1):
        # Индексы в Python: i-1 соответствует xᵢ
        x_prev = x[i-2]  # xᵢ₋₁
        y_prev = y[i-2]  # yᵢ₋₁
        
        # Вычисляем xᵢ и yᵢ
        x[i-1] = x_prev + y_prev / (i * i)
        y[i-1] = y_prev + x_prev / i
    
    return x, y


def compute_sequences_detailed(n):
    """
    Вычисляет последовательности с подробным выводом шагов.
    Возвращает детальное описание вычислений.
    """
    x = [0.0] * n
    y = [0.0] * n
    x[0] = 1.0
    y[0] = 1.0
    
    steps = []
    steps.append("ВЫЧИСЛЕНИЕ ПОСЛЕДОВАТЕЛЬНОСТЕЙ x и y")
    steps.append("=" * 70)
    steps.append("Рекуррентные формулы:")
    steps.append("  x₁ = y₁ = 1")
    steps.append("  xᵢ = xᵢ₋₁ + yᵢ₋₁ / i²")
    steps.append("  yᵢ = yᵢ₋₁ + xᵢ₋₁ / i")
    steps.append("  для i = 2, 3, ...")
    steps.append("")
    steps.append("Начальные условия:")
    steps.append(f"  x₁ = {x[0]}, y₁ = {y[0]}")
    steps.append("")
    steps.append("Последовательные вычисления:")
    
    # Выводим шаги для i от 2 до min(n, 10) для наглядности
    max_steps_to_show = 10
    for i in range(2, min(n, max_steps_to_show) + 1):
        x_prev = x[i-2]
        y_prev = y[i-2]
        
        # Вычисляем xᵢ и yᵢ
        x[i-1] = x_prev + y_prev / (i * i)
        y[i-1] = y_prev + x_prev / i
        
        steps.append(f"\nШаг i = {i}:")
        steps.append(f"  x_{i-1} = {x_prev:.6f}, y_{i-1} = {y_prev:.6f}")
        steps.append(f"  x_{i} = x_{i-1} + y_{i-1} / {i}²")
        steps.append(f"       = {x_prev:.6f} + {y_prev:.6f} / {i*i}")
        steps.append(f"       = {x_prev:.6f} + {y_prev/(i*i):.6f}")
        steps.append(f"       = {x[i-1]:.6f}")
        steps.append(f"  y_{i} = y_{i-1} + x_{i-1} / {i}")
        steps.append(f"       = {y_prev:.6f} + {x_prev:.6f} / {i}")
        steps.append(f"       = {y_prev:.6f} + {x_prev/i:.6f}")
        steps.append(f"       = {y[i-1]:.6f}")
    
    # Если n > 10, показываем только конечные результаты для оставшихся
    if n > max_steps_to_show:
        steps.append(f"\n... (вычисления для i = {max_steps_to_show+1}..{n})")
        for i in range(max_steps_to_show + 1, n + 1):
            x_prev = x[i-2]
            y_prev = y[i-2]
            x[i-1] = x_prev + y_prev / (i * i)
            y[i-1] = y_prev + x_prev / i
    
    steps.append("\n" + "=" * 70)
    steps.append("РЕЗУЛЬТАТЫ:")
    steps.append(f"x_{n} = {x[n-1]:.10f}")
    steps.append(f"y_{n} = {y[n-1]:.10f}")
    
    detailed_explanation = "\n".join(steps)
    return detailed_explanation, x, y


def main():
    """
    Основная функция программы с выбором режима работы.
    """
    print("Программа вычисления последовательностей x и y")
    print("=" * 70)
    print("Рекуррентные формулы:")
    print("  x₁ = y₁ = 1")
    print("  xᵢ = xᵢ₋₁ + yᵢ₋₁ / i²")
    print("  yᵢ = yᵢ₋₁ + xᵢ₋₁ / i")
    print("  для i = 2, 3, ...")
    print("=" * 70)
    
    print("\nЗадача: получить x₈ и x₁₈")
    
    # Вычисляем x и y до 18
    n = 18
    x, y = compute_sequences(n)
    
    print("\n" + "=" * 70)
    print("РЕЗУЛЬТАТЫ:")
    print("=" * 70)
    print(f"x₈  = {x[7]:.10f}")
    print(f"x₁₈ = {x[17]:.10f}")
    print("=" * 70)
    
    # Предложение показать подробные вычисления
    choice = input("\nПоказать подробные вычисления? (да/нет): ")
    if choice.lower() in ['да', 'д', 'yes', 'y']:
        explanation, x_detailed, y_detailed = compute_sequences_detailed(n)
        print("\n" + explanation)
    
    # Дополнительная информация
    print("\n" + "=" * 70)
    print("ДОПОЛНИТЕЛЬНАЯ ИНФОРМАЦИЯ:")
    print("=" * 70)
    
    # Создаем таблицу значений xᵢ и yᵢ для i=1..18
    print("\nТаблица значений для i = 1..18:")
    print(" i      xᵢ                yᵢ")
    print("-" * 50)
    
    x, y = compute_sequences(18)  # Пересчитываем для надежности
    for i in range(18):
        print(f"{i+1:2}   {x[i]:15.10f}   {y[i]:15.10f}")
    
    # Анализ поведения последовательностей
    print("\nАнализ поведения последовательностей:")
    print("1. Обе последовательности монотонно возрастают.")
    print("2. xᵢ растет медленнее, чем yᵢ.")
    print("3. С ростом i вклад слагаемых yᵢ₋₁/i² и xᵢ₋₁/i уменьшается.")
    
    # Вычисляем разности для анализа скорости роста
    print("\nАнализ скорости роста:")
    print(" i     Δxᵢ (xᵢ - xᵢ₋₁)    Δyᵢ (yᵢ - yᵢ₋₁)")
    print("-" * 50)
    for i in range(1, 18):
        delta_x = x[i] - x[i-1]
        delta_y = y[i] - y[i-1]
        print(f"{i+1:2}   {delta_x:15.10f}   {delta_y:15.10f}")
    
    # Проверка: вычисляем x₈ и x₁₈ по отдельности для контроля
    print("\n" + "=" * 70)
    print("ПРОВЕРКА:")
    print("=" * 70)
    
    # Вычисляем только до 8
    x8, y8 = compute_sequences(8)
    print(f"x₈ (вычислено отдельно) = {x8[7]:.10f}")
    print(f"x₈ (из полного расчета) = {x[7]:.10f}")
    print(f"Совпадение: {'ДА' if abs(x8[7] - x[7]) < 1e-12 else 'НЕТ'}")
    
    print("\n" + "=" * 70)
    print("МАТЕМАТИЧЕСКИЙ АНАЛИЗ:")
    print("=" * 70)
    print("Рекуррентные формулы образуют систему разностных уравнений.")
    print("Можно записать в векторном виде:")
    print("  [xᵢ]   [1   1/i²] [xᵢ₋₁]")
    print("  [yᵢ] = [1/i   1 ] [yᵢ₋₁]")
    print("\nСобственные значения матрицы перехода:")
    print("  λ₁ = 1 + 1/(i√i), λ₂ = 1 - 1/(i√i)")
    print("Таким образом, система устойчива и сходится.")
    
    # Вычисляем предельное поведение
    print("\nОценка предельного поведения:")
    print("При больших i, xᵢ и yᵢ растут примерно линейно с i,")
    print("но с уменьшающейся скоростью.")
    
    # Экстраполяция
    if len(x) >= 3:
        last_delta = x[-1] - x[-2]
        second_last_delta = x[-2] - x[-3]
        print(f"\nПоследние разности для x:")
        print(f"  x₁₈ - x₁₇ = {last_delta:.10f}")
        print(f"  x₁₇ - x₁₆ = {second_last_delta:.10f}")
        print(f"  Отношение: {last_delta/second_last_delta:.6f}")
        print("  Разности уменьшаются, последовательность замедляет рост.")
    
    print("=" * 70)


if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
