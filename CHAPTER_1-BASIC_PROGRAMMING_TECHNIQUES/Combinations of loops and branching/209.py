"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
7. Сочетания цикла и разветвления

209. Даны натуральное число n, действительное число x. Среди чисел  
e^(cos(x²)) * sin(x^(3k)) (k = 1, ..., n) найти ближайшее к какому-нибудь целому.
"""

import math

def find_closest_to_integer(n, x):
    """
    Находит среди чисел f(k) = e^(cos(x²)) * sin(x^(3k)) (k=1..n)
    значение, ближайшее к целому числу.
    
    Возвращает:
    - индекс k
    - значение функции f(k)
    - ближайшее целое число
    - расстояние до ближайшего целого
    - список всех значений (для подробного вывода)
    """
    # Константный множитель (не зависит от k)
    const_factor = math.exp(math.cos(x**2))
    
    values = []
    min_distance = float('inf')
    closest_k = None
    closest_value = None
    closest_integer = None
    
    for k in range(1, n + 1):
        # Вычисляем значение функции
        sin_arg = x**(3 * k)  # x^(3k)
        sin_val = math.sin(sin_arg)
        value = const_factor * sin_val
        
        # Находим ближайшее целое и расстояние до него
        nearest_int = round(value)
        distance = abs(value - nearest_int)
        
        values.append({
            'k': k,
            'value': value,
            'nearest_int': nearest_int,
            'distance': distance
        })
        
        # Обновляем минимальное расстояние
        if distance < min_distance:
            min_distance = distance
            closest_k = k
            closest_value = value
            closest_integer = nearest_int
    
    return closest_k, closest_value, closest_integer, min_distance, values


def find_closest_detailed(n, x):
    """
    Подробная версия с пошаговым выводом.
    """
    steps = []
    steps.append(f"1. Входные данные: n = {n}, x = {x}")
    
    # Вычисляем константный множитель
    x_squared = x**2
    cos_x_squared = math.cos(x_squared)
    exp_cos = math.exp(cos_x_squared)
    steps.append(f"2. Вычисляем константный множитель:")
    steps.append(f"   x² = {x:.4f}² = {x_squared:.4f}")
    steps.append(f"   cos(x²) = cos({x_squared:.4f}) = {cos_x_squared:.4f}")
    steps.append(f"   e^(cos(x²)) = e^({cos_x_squared:.4f}) = {exp_cos:.4f}")
    
    steps.append(f"3. Вычисляем значения для k = 1..{n}:")
    steps.append(f"   Формула: f(k) = {exp_cos:.4f} * sin(x^(3k))")
    
    values = []
    min_distance = float('inf')
    closest_info = None
    
    for k in range(1, n + 1):
        # Вычисляем x^(3k)
        exponent = 3 * k
        x_power = x**exponent
        sin_val = math.sin(x_power)
        value = exp_cos * sin_val
        
        # Находим ближайшее целое
        nearest_int = round(value)
        distance = abs(value - nearest_int)
        
        values.append({
            'k': k,
            'x^(3k)': x_power,
            'sin(x^(3k))': sin_val,
            'value': value,
            'nearest_int': nearest_int,
            'distance': distance
        })
        
        # Обновляем минимальное расстояние
        if distance < min_distance:
            min_distance = distance
            closest_info = values[-1]
    
    # Форматируем таблицу
    steps.append(f"   {'k':<4} | {'x^(3k)':<12} | {'sin(x^(3k))':<12} | {'f(k)':<12} | {'Ближайшее целое':<16} | {'Расстояние':<10}")
    steps.append("-" * 85)
    
    for v in values:
        steps.append(f"   {v['k']:<4} | {v['x^(3k)']:<12.6f} | {v['sin(x^(3k))']:<12.6f} | "
                    f"{v['value']:<12.6f} | {v['nearest_int']:<16} | {v['distance']:<10.6f}")
    
    steps.append(f"\n4. Наименьшее расстояние до целого: {min_distance:.6f}")
    if closest_info:
        steps.append(f"   Достигается при k = {closest_info['k']}:")
        steps.append(f"   f({closest_info['k']}) = {closest_info['value']:.6f}")
        steps.append(f"   Ближайшее целое: {closest_info['nearest_int']}")
        steps.append(f"   Расстояние: {closest_info['distance']:.6f}")
    
    detailed_explanation = "\n".join(steps)
    return closest_info, detailed_explanation


def main():
    """
    Основная функция программы с выбором режима работы.
    """
    print("Программа поиска значения, ближайшего к целому числу")
    print("=" * 70)
    print("Среди чисел f(k) = e^(cos(x²)) * sin(x^(3k)) (k=1..n)")
    print("находим то, которое ближе всего к целому числу.")
    print("=" * 70)
    
    choice = input("Выберите режим:\n1 - Использовать примеры\n2 - Ввести свои данные\nВведите 1 или 2: ")
    
    if choice == '1':
        # Примеры для демонстрации
        examples = [
            ("Пример 1 (малые значения)", 5, 0.5),
            ("Пример 2 (средние значения)", 8, 1.2),
            ("Пример 3 (интересный случай)", 6, 0.8),
            ("Пример 4 (большой n)", 10, 0.3),
        ]
        
        for title, n, x in examples:
            print(f"\n{title}:")
            print(f"n = {n}, x = {x}")
            
            closest_k, closest_value, closest_int, min_dist, all_values = find_closest_to_integer(n, x)
            
            print(f"Результат:")
            print(f"  Наименьшее расстояние до целого: {min_dist:.6f}")
            print(f"  Достигается при k = {closest_k}:")
            print(f"  f({closest_k}) = {closest_value:.6f}")
            print(f"  Ближайшее целое: {closest_int}")
            
            # Для первого примера предлагаем показать детали
            if title == "Пример 1 (малые значения)":
                detailed_choice = input("\nПоказать подробное решение для этого примера? (да/нет): ")
                if detailed_choice.lower() in ['да', 'д', 'yes', 'y']:
                    closest_info, explanation = find_closest_detailed(n, x)
                    print("\nПодробное решение:")
                    print(explanation)
            
            print("-" * 50)
    
    elif choice == '2':
        # Ввод данных от пользователя
        try:
            n = int(input("\nВведите натуральное число n: "))
            if n <= 0:
                print("Ошибка: n должно быть натуральным числом!")
                return
            
            x = float(input("Введите действительное число x: "))
            
            print(f"\nВведены данные: n = {n}, x = {x}")
            
            # Вычисление результата
            closest_k, closest_value, closest_int, min_dist, all_values = find_closest_to_integer(n, x)
            
            print(f"\nРезультат:")
            print(f"Наименьшее расстояние до целого: {min_dist:.6f}")
            print(f"Достигается при k = {closest_k}:")
            print(f"f({closest_k}) = {closest_value:.6f}")
            print(f"Ближайшее целое: {closest_int}")
            
            # Предложение показать подробное решение
            detailed_choice = input("\nПоказать подробное решение? (да/нет): ")
            if detailed_choice.lower() in ['да', 'д', 'yes', 'y']:
                closest_info, explanation = find_closest_detailed(n, x)
                print("\nПодробное решение:")
                print(explanation)
        
        except ValueError:
            print("Ошибка ввода! Убедитесь, что вводите числа в правильном формате.")
            return
    
    else:
        print("Неверный выбор. Программа завершена.")
        return
    
    # Математическое пояснение
    print("\n" + "=" * 70)
    print("МАТЕМАТИЧЕСКОЕ ПОЯСНЕНИЕ:")
    print("=" * 70)
    print("Функция f(k) = e^(cos(x²)) * sin(x^(3k)) обладает интересными свойствами:")
    print("1. e^(cos(x²)) - постоянный множитель (не зависит от k)")
    print("2. sin(x^(3k)) - осциллирующая часть, которая зависит от k")
    print("3. При росте k аргумент синуса x^(3k) растет очень быстро")
    print("4. Значения синуса лежат в диапазоне [-1, 1]")
    print("5. Таким образом, f(k) ∈ [-e^(cos(x²)), e^(cos(x²))]")
    print("=" * 70)
    
    # Особые случаи
    print("\n" + "=" * 70)
    print("ОСОБЫЕ СЛУЧАИ:")
    print("=" * 70)
    print("1. Если x = 0, то f(k) = 0 для всех k (ближайшее к целому 0)")
    print("2. Если x = π^(1/3), то x^3 = π, и sin(π^k) = 0 для всех k")
    print("3. Если e^(cos(x²)) = 1, то f(k) = sin(x^(3k))")
    print("4. Если sin(x^(3k)) = ±1, то f(k) = ±e^(cos(x²))")
    print("=" * 70)


if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
