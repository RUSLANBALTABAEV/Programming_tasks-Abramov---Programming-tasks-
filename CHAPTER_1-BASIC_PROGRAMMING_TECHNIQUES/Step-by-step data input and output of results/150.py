"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
6. Пошаговый ввод данных и вывод результатов *)

150. Дано натуральное число n. Вычислить значения функции y = (x * x - 3 * x + 2) / sqrt(2 * x * x * x - 1) для x = 1, 1.1, 1.2, ..., 1 + 0.1 * n.
"""


import math

def main():
    print("Вычисление значений функции y = (x² - 3x + 2) / √(2x³ - 1)")
    print("для x = 1, 1.1, 1.2, ..., 1 + 0.1n")
    print("=" * 70)
    
    # Ввод натурального числа n
    n = int(input("Введите натуральное число n: "))
    
    if n <= 0:
        print("Ошибка: n должно быть натуральным числом (больше 0)!")
        return
    
    # Параметры
    start = 1.0
    step = 0.1
    end = start + n * step
    
    # Вычисляем количество точек (включая начальную)
    num_points = n + 1
    
    print(f"\nДиапазон x: от {start} до {end} с шагом {step}")
    print(f"Количество точек: {num_points}")
    print("=" * 70)
    
    # Проверка области определения функции
    print("\nАнализ области определения функции:")
    print("Знаменатель: √(2x³ - 1) определен при 2x³ - 1 > 0")
    print("Решаем неравенство: 2x³ - 1 > 0 => x³ > 1/2 => x > (1/2)^(1/3) ≈ 0.7937")
    print(f"Так как x начинается с 1, функция определена для всех точек.")
    print("-" * 70)
    
    # Таблица значений (первые 15 и последние 15 точек)
    print("\nТаблица значений функции (первые 15 точек):")
    print("-" * 70)
    print(f"{'x':>8} | {'y':>15} | {'Числитель':>15} | {'Знаменатель':>15}")
    print("-" * 70)
    
    results = []
    undefined_points = []
    
    for i in range(num_points):
        x = start + i * step
        numerator = x**2 - 3*x + 2
        denominator_inside = 2*x**3 - 1
        
        # Проверка области определения
        if denominator_inside <= 0:
            y = float('nan')  # Не число
            undefined_points.append((x, denominator_inside))
        else:
            denominator = math.sqrt(denominator_inside)
            y = numerator / denominator
        
        results.append((x, y, numerator, denominator_inside))
        
        # Выводим первые 15 точек
        if i < 15:
            if denominator_inside <= 0:
                print(f"{x:8.2f} | {'не определена':^15} | {numerator:15.6f} | {denominator_inside:15.6f}")
            else:
                print(f"{x:8.2f} | {y:15.6f} | {numerator:15.6f} | {denominator_inside:15.6f}")
    
    # Выводим последние 15 точек, если точек больше 30
    if num_points > 30:
        print("...")
        print(f"\nПоследние 15 точек:")
        print("-" * 70)
        print(f"{'x':>8} | {'y':>15} | {'Числитель':>15} | {'Знаменатель':>15}")
        print("-" * 70)
        
        for i in range(max(0, num_points - 15), num_points):
            x, y, numerator, denominator_inside = results[i]
            if denominator_inside <= 0:
                print(f"{x:8.2f} | {'не определена':^15} | {numerator:15.6f} | {denominator_inside:15.6f}")
            else:
                print(f"{x:8.2f} | {y:15.6f} | {numerator:15.6f} | {denominator_inside:15.6f}")
    
    print("-" * 70)
    
    # Подробная таблица в несколько колонок (если точек не слишком много)
    if num_points <= 50:
        print("\nПолная таблица значений (в 3 колонки):")
        print("=" * 70)
        
        cols = 3
        rows = (num_points + cols - 1) // cols
        
        print(f"{'x':>8} {'y':>12} | {'x':>8} {'y':>12} | {'x':>8} {'y':>12}")
        print("-" * 70)
        
        for row in range(rows):
            line = ""
            for col in range(cols):
                idx = row + col * rows
                if idx < num_points:
                    x, y, _, _ = results[idx]
                    if math.isnan(y):
                        y_str = "не опр."
                    else:
                        y_str = f"{y:12.6f}"
                    line += f"{x:8.2f} {y_str} | "
                else:
                    line += " " * 22 + "| "
            print(line.rstrip("| "))
    
    # Анализ функции
    print("\n" + "=" * 70)
    print("Анализ функции:")
    print("-" * 70)
    
    # Статистика по определенным значениям
    defined_values = [y for _, y, _, denom in results if not math.isnan(y)]
    
    if defined_values:
        min_y = min(defined_values)
        max_y = max(defined_values)
        avg_y = sum(defined_values) / len(defined_values)
        
        # Находим x, соответствующие min и max
        min_x = None
        max_x = None
        for x, y, _, _ in results:
            if not math.isnan(y):
                if y == min_y:
                    min_x = x
                if y == max_y:
                    max_x = x
        
        print(f"Минимальное значение: y({min_x:.2f}) = {min_y:.6f}")
        print(f"Максимальное значение: y({max_x:.2f}) = {max_y:.6f}")
        print(f"Среднее значение: {avg_y:.6f}")
        print(f"Количество определенных точек: {len(defined_values)} из {num_points}")
    else:
        print("Нет определенных значений функции на данном интервале.")
    
    if undefined_points:
        print(f"\nТочки, в которых функция не определена:")
        for x, denom in undefined_points[:5]:  # Покажем первые 5
            print(f"  x = {x:.2f}: 2x³-1 = {denom:.6f} <= 0")
        if len(undefined_points) > 5:
            print(f"  ... и еще {len(undefined_points) - 5} точек")
    
    # Поведение функции при больших x
    print("\nПоведение функции при больших x:")
    print("При x → ∞:")
    print("  Числитель: x² - 3x + 2 ~ x²")
    print("  Знаменатель: √(2x³ - 1) ~ √(2) * x^(3/2)")
    print("  y ~ x² / (√2 * x^(3/2)) = (1/√2) * x^(1/2)")
    print("  Функция растет как √x, т.е. неограниченно возрастает.")
    
    # Проверка на наличие нулей функции
    print("\nНули функции (y = 0):")
    print("y = 0, когда числитель равен 0: x² - 3x + 2 = 0")
    print("Решаем квадратное уравнение: x₁ = 1, x₂ = 2")
    
    zeros_in_range = []
    for x, y, numerator, _ in results:
        if abs(numerator) < 1e-10:  # Практически ноль
            zeros_in_range.append(x)
    
    if zeros_in_range:
        print(f"  В заданном диапазоне нули при x: {', '.join([f'{x:.2f}' for x in zeros_in_range])}")
    else:
        print("  В заданном диапазоне нет нулей функции (кроме возможной погрешности)")
    
    # Текстовый график
    print("\n" + "=" * 70)
    print("Текстовый график функции (только для определенных значений):")
    print("-" * 70)
    
    if defined_values:
        # Находим диапазон значений y для масштабирования
        y_min = min(defined_values)
        y_max = max(defined_values)
        y_range = y_max - y_min
        
        if y_range == 0:
            y_range = 1
        
        # Выводим график для каждых 10-х точек (чтобы не перегружать)
        print(f"{'x':>6} {'y':>10} ", "График (масштабированный)")
        print("-" * 60)
        
        for i in range(0, num_points, max(1, num_points // 30)):  # Не более 30 строк
            x, y, _, denom = results[i]
            if not math.isnan(y):
                # Масштабируем для отображения в 40 символах
                scaled_y = int(40 * (y - y_min) / y_range)
                bar = "█" * scaled_y
                print(f"{x:6.2f} {y:10.4f} {bar}")
            else:
                print(f"{x:6.2f} {'не опр.':>10}")

if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
