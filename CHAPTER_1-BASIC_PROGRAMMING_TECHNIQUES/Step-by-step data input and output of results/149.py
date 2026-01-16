"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
6. Пошаговый ввод данных и вывод результатов *)

149. Вычислить значения функции y = 4 * x * x * x - 2 * x * x + 5 для значений x, изменяющихся от –3 до 1, с шагом 0.1.
"""


def main():
    print("Вычисление значений функции y = 4x³ - 2x² + 5")
    print("для x от -3 до 1 с шагом 0.1")
    print("=" * 70)
    
    # Параметры
    start = -3.0
    end = 1.0
    step = 0.1
    
    # Вычисляем количество точек (с учетом погрешности округления)
    num_points = int(round((end - start) / step)) + 1
    
    print(f"Начало: {start}, конец: {end}, шаг: {step}")
    print(f"Количество точек: {num_points}")
    print("=" * 70)
    
    # Переменные для статистики
    min_y = float('inf')
    max_y = float('-inf')
    min_x = 0
    max_x = 0
    sum_y = 0
    
    # Таблица значений (с разбиением на колонки)
    print("\nТаблица значений функции:")
    print("-" * 60)
    print(f"{'x':>8} | {'y':>12} | {'y (округл.)':>12} | {'Знак':>8}")
    print("-" * 60)
    
    # Используем целочисленный счетчик для избежания ошибок округления
    for i in range(num_points):
        x = start + i * step
        y = 4 * x**3 - 2 * x**2 + 5
        
        # Обновляем статистику
        if y < min_y:
            min_y = y
            min_x = x
        if y > max_y:
            max_y = y
            max_x = x
        sum_y += y
        
        # Определяем знак функции
        sign = "+" if y > 0 else ("-" if y < 0 else "0")
        
        # Выводим строку таблицы (каждую 3-ю точку для краткости)
        if i % 3 == 0 or i == num_points - 1:
            print(f"{x:8.2f} | {y:12.6f} | {y:12.3f} | {sign:>8}")
    
    print("-" * 60)
    
    # Подробная таблица в несколько колонок
    print("\nПодробная таблица (все точки в 4 колонки):")
    print("=" * 80)
    
    # Разбиваем на 4 колонки
    cols = 4
    rows = (num_points + cols - 1) // cols
    
    for row in range(rows):
        line = ""
        for col in range(cols):
            idx = row + col * rows
            if idx < num_points:
                x = start + idx * step
                y = 4 * x**3 - 2 * x**2 + 5
                line += f"x={x:5.1f} y={y:7.2f} | "
            else:
                line += " " * 20 + " | "
        print(line.rstrip(" | "))
    
    # Анализ функции
    print("\n" + "=" * 70)
    print("Анализ функции y = 4x³ - 2x² + 5 на отрезке [-3, 1]:")
    print("-" * 70)
    
    # Находим производную: y' = 12x² - 4x
    print("\n1. Производная функции: y' = 12x² - 4x")
    print("   Критические точки: y' = 0 => 12x² - 4x = 0")
    print("                      4x(3x - 1) = 0")
    print("                      x₁ = 0, x₂ = 1/3 ≈ 0.3333")
    
    # Вычисляем значения в критических точках
    print("\n2. Значения в критических точках и на границах:")
    
    points_to_check = [-3.0, 0.0, 1/3, 1.0]
    for x in points_to_check:
        y = 4 * x**3 - 2 * x**2 + 5
        print(f"   x = {x:6.3f}: y = {y:8.3f}")
    
    # Корни уравнения (приближенно)
    print("\n3. Поиск корней уравнения 4x³ - 2x² + 5 = 0")
    print("   (функция не имеет действительных корней на данном отрезке)")
    
    # Проверяем наличие корней методом перебора знаков
    prev_x = start
    prev_y = 4 * prev_x**3 - 2 * prev_x**2 + 5
    roots_found = []
    
    for i in range(1, num_points):
        x = start + i * step
        y = 4 * x**3 - 2 * x**2 + 5
        
        if prev_y == 0:
            roots_found.append(prev_x)
        elif y == 0:
            roots_found.append(x)
        elif prev_y * y < 0:  # Знак меняется
            # Приближенный корень методом деления пополам
            root_approx = (prev_x + x) / 2
            roots_found.append(root_approx)
        
        prev_x, prev_y = x, y
    
    if roots_found:
        print(f"   Найдены корни: {roots_found}")
    else:
        print("   Корней нет (функция не меняет знак на отрезке)")
    
    # Статистика по вычисленным значениям
    print("\n" + "=" * 70)
    print("Статистика по вычисленным точкам:")
    print("-" * 70)
    
    avg_y = sum_y / num_points
    
    print(f"Минимальное значение: y({min_x:.2f}) = {min_y:.6f}")
    print(f"Максимальное значение: y({max_x:.2f}) = {max_y:.6f}")
    print(f"Среднее значение: {avg_y:.6f}")
    print(f"Размах значений: {max_y - min_y:.6f}")
    
    # Количество положительных, отрицательных и нулевых значений
    positive_count = 0
    negative_count = 0
    zero_count = 0
    
    for i in range(num_points):
        x = start + i * step
        y = 4 * x**3 - 2 * x**2 + 5
        if y > 0:
            positive_count += 1
        elif y < 0:
            negative_count += 1
        else:
            zero_count += 1
    
    print(f"\nПоложительных значений: {positive_count}")
    print(f"Отрицательных значений: {negative_count}")
    print(f"Нулевых значений: {zero_count}")
    
    # Текстовый график
    print("\n" + "=" * 70)
    print("Текстовый график функции (масштаб по вертикали условный):")
    print("-" * 70)
    
    # Определяем масштаб для графика
    y_min = min_y
    y_max = max_y
    y_range = y_max - y_min
    
    if y_range == 0:
        y_range = 1
    
    # Рисуем график для каждой 5-й точки
    print(f"{'x':>6} {'y':>8} ", "График")
    print("-" * 50)
    
    for i in range(0, num_points, 5):
        x = start + i * step
        y = 4 * x**3 - 2 * x**2 + 5
        
        # Масштабируем для отображения в 40 символах
        scaled_y = int(40 * (y - y_min) / y_range)
        bar = "█" * scaled_y
        
        print(f"{x:6.2f} {y:8.3f} {bar}")

if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
