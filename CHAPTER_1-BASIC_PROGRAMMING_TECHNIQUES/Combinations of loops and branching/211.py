"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
7. Сочетания цикла и разветвления

211. Пусть
      x1 = 0.3; x2 = -0.3; xi = sin(xi-2), i = 3, 4, ...
Среди x1, … , x100 найти ближайшее к какому–нибудь целому.
"""


"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
7. Сочетания цикла и разветвления

211. Пусть
x₁ = 0.3; x₂ = -0.3; xᵢ = sin(xᵢ₋₂), i = 3, 4, ...
Среди x₁, ..., x₁₀₀ найти ближайшее к какому-нибудь целому.
"""


import math

def generate_sequence():
    """
    Генерирует последовательность из 100 элементов по правилу:
    x₁ = 0.3, x₂ = -0.3, xᵢ = sin(xᵢ₋₂) для i ≥ 3.
    Возвращает список из 100 элементов.
    """
    n = 100
    x = [0.0] * n
    x[0] = 0.3      # x₁
    x[1] = -0.3     # x₂
    
    for i in range(2, n):
        x[i] = math.sin(x[i-2])
    
    return x


def find_closest_to_integer(sequence):
    """
    Находит в последовательности элемент, ближайший к целому числу.
    Возвращает:
    - индекс элемента (в 1-индексации)
    - значение элемента
    - ближайшее целое число
    - расстояние до ближайшего целого
    - список всех расстояний (для детального анализа)
    """
    n = len(sequence)
    min_distance = float('inf')
    closest_index = None
    closest_value = None
    closest_integer = None
    
    distances = []
    
    for i in range(n):
        value = sequence[i]
        nearest_int = round(value)
        distance = abs(value - nearest_int)
        
        distances.append({
            'index': i+1,  # 1-индексация
            'value': value,
            'nearest_int': nearest_int,
            'distance': distance
        })
        
        if distance < min_distance:
            min_distance = distance
            closest_index = i+1
            closest_value = value
            closest_integer = nearest_int
    
    return closest_index, closest_value, closest_integer, min_distance, distances


def analyze_sequence_detailed():
    """
    Подробный анализ последовательности.
    Возвращает детальное описание.
    """
    x = generate_sequence()
    
    steps = []
    steps.append("1. Генерация последовательности:")
    steps.append("   x₁ = 0.3")
    steps.append("   x₂ = -0.3")
    steps.append("   xᵢ = sin(xᵢ₋₂) для i ≥ 3")
    steps.append("")
    steps.append("2. Первые 10 элементов последовательности:")
    steps.append("   i     xᵢ           sin(xᵢ₋₂)      Ближайшее целое   Расстояние")
    steps.append("   --------------------------------------------------------------")
    
    for i in range(10):
        value = x[i]
        nearest_int = round(value)
        distance = abs(value - nearest_int)
        
        if i < 2:
            formula = "начальное"
        else:
            formula = f"sin({x[i-2]:.6f})"
        
        steps.append(f"   {i+1:2}   {value:12.9f}   {formula:<15} {nearest_int:4}           {distance:12.9f}")
    
    steps.append("")
    steps.append("3. Поиск элемента, ближайшего к целому:")
    
    closest_index, closest_value, closest_integer, min_distance, distances = find_closest_to_integer(x)
    
    steps.append(f"   Всего элементов: {len(x)}")
    steps.append(f"   Минимальное расстояние до целого: {min_distance:.9f}")
    steps.append(f"   Достигается при i = {closest_index}:")
    steps.append(f"   x{closest_index} = {closest_value:.9f}")
    steps.append(f"   Ближайшее целое: {closest_integer}")
    
    # Находим несколько ближайших элементов
    sorted_distances = sorted(distances, key=lambda d: d['distance'])
    
    steps.append("")
    steps.append("4. Топ-5 элементов, ближайших к целым числам:")
    steps.append("   i     xᵢ           Ближайшее целое   Расстояние")
    steps.append("   ------------------------------------------------")
    
    for i in range(min(5, len(sorted_distances))):
        d = sorted_distances[i]
        steps.append(f"   {d['index']:2}   {d['value']:12.9f}   {d['nearest_int']:4}           {d['distance']:12.9f}")
    
    # Анализ поведения последовательности
    steps.append("")
    steps.append("5. Анализ поведения последовательности:")
    steps.append("   - Все элементы стремятся к 0 (по модулю убывают)")
    steps.append("   - Ближайшее целое для всех элементов - 0")
    steps.append("   - Поэтому элемент с минимальным расстоянием - это элемент с минимальным модулем")
    
    # Находим элемент с минимальным модулем
    min_abs_index = min(range(len(x)), key=lambda i: abs(x[i]))
    steps.append(f"   - Элемент с минимальным модулем: x{min_abs_index+1} = {x[min_abs_index]:.9f}")
    steps.append(f"     |x{min_abs_index+1}| = {abs(x[min_abs_index]):.9f}")
    
    detailed_explanation = "\n".join(steps)
    return detailed_explanation, x, distances


def main():
    """
    Основная функция программы с выбором режима работы.
    """
    print("Программа поиска элемента, ближайшего к целому числу")
    print("=" * 70)
    print("Дана последовательность:")
    print("x₁ = 0.3, x₂ = -0.3, xᵢ = sin(xᵢ₋₂) для i ≥ 3")
    print("Среди x₁, ..., x₁₀₀ найти ближайшее к целому числу.")
    print("=" * 70)
    
    choice = input("Выберите режим:\n1 - Полный анализ\n2 - Только результат\nВведите 1 или 2: ")
    
    if choice == '1':
        print("\n" + "=" * 70)
        print("ПОЛНЫЙ АНАЛИЗ ПОСЛЕДОВАТЕЛЬНОСТИ")
        print("=" * 70)
        
        explanation, sequence, distances = analyze_sequence_detailed()
        print(explanation)
        
        # Дополнительная информация
        print("\n" + "=" * 70)
        print("ДОПОЛНИТЕЛЬНАЯ ИНФОРМАЦИЯ:")
        print("=" * 70)
        
        # Статистика по расстояниям
        all_distances = [d['distance'] for d in distances]
        avg_distance = sum(all_distances) / len(all_distances)
        max_distance = max(all_distances)
        
        print(f"Среднее расстояние до ближайшего целого: {avg_distance:.9f}")
        print(f"Максимальное расстояние до ближайшего целого: {max_distance:.9f}")
        
        # Подсчет, сколько элементов ближе к 0, чем к другим целым
        zero_count = sum(1 for d in distances if d['nearest_int'] == 0)
        print(f"Количество элементов, ближайших к 0: {zero_count} из 100")
        
        # Поведение последовательности
        print("\nПоведение последовательности:")
        print("Поскольку |sin(x)| ≤ |x| для всех x, и строго меньше для x ≠ 0,")
        print("последовательность по модулю монотонно убывает к 0.")
        print("Таким образом, элементы с большими индексами ближе к 0.")
        
        # График сходимости (текстовый)
        print("\nСходимость последовательности к 0:")
        print("Индекс  |xᵢ|        log10(|xᵢ|)")
        print("--------------------------------")
        indices_to_show = [1, 2, 3, 4, 5, 10, 20, 30, 50, 70, 100]
        for i in indices_to_show:
            if i <= len(sequence):
                value = sequence[i-1]
                abs_value = abs(value)
                if abs_value > 0:
                    log_value = math.log10(abs_value)
                    print(f"{i:6}  {abs_value:.2e}  {log_value:8.3f}")
                else:
                    print(f"{i:6}  0.00e+00   -inf")
        
        print("=" * 70)
    
    elif choice == '2':
        print("\n" + "=" * 70)
        print("КРАТКИЙ РЕЗУЛЬТАТ")
        print("=" * 70)
        
        # Генерируем последовательность и находим ближайший элемент
        sequence = generate_sequence()
        closest_index, closest_value, closest_integer, min_distance, distances = find_closest_to_integer(sequence)
        
        print(f"Элемент, ближайший к целому числу:")
        print(f"  Индекс: x{closest_index}")
        print(f"  Значение: {closest_value:.9f}")
        print(f"  Ближайшее целое: {closest_integer}")
        print(f"  Расстояние: {min_distance:.9f}")
        
        # Несколько ближайших элементов
        sorted_distances = sorted(distances, key=lambda d: d['distance'])
        
        print("\nТоп-5 ближайших к целым числам:")
        print("  i    xᵢ          Ближ. целое  Расстояние")
        print("  -----------------------------------------")
        for i in range(min(5, len(sorted_distances))):
            d = sorted_distances[i]
            print(f"  {d['index']:2}  {d['value']:10.7f}  {d['nearest_int']:4}       {d['distance']:10.7f}")
        
        print("=" * 70)
        
        # Математическое объяснение
        print("\nПОЯСНЕНИЕ:")
        print("Последовательность определена рекуррентно:")
        print("x₁ = 0.3, x₂ = -0.3, xᵢ = sin(xᵢ₋₂) для i ≥ 3")
        print("Поскольку |sin(x)| < |x| для всех x ≠ 0,")
        print("последовательность по модулю строго убывает и стремится к 0.")
        print("Поэтому элементы с большими индексами ближе к 0,")
        print("а ближайшее целое для всех элементов - это 0.")
        print("=" * 70)
    
    else:
        print("Неверный выбор. Программа завершена.")
        return
    
    # Интерактивный режим для просмотра конкретных элементов
    print("\n" + "=" * 70)
    view_choice = input("Показать значение конкретного элемента? (да/нет): ")
    if view_choice.lower() in ['да', 'д', 'yes', 'y']:
        sequence = generate_sequence()
        while True:
            try:
                index = int(input(f"\nВведите индекс элемента (1-100, 0 для выхода): "))
                if index == 0:
                    break
                if 1 <= index <= 100:
                    value = sequence[index-1]
                    nearest_int = round(value)
                    distance = abs(value - nearest_int)
                    print(f"x{index} = {value:.10f}")
                    print(f"Ближайшее целое: {nearest_int}")
                    print(f"Расстояние: {distance:.10f}")
                    print(f"|x{index}| = {abs(value):.10f}")
                else:
                    print("Индекс должен быть от 1 до 100.")
            except ValueError:
                print("Ошибка: введите целое число.")
    
    print("\n" + "=" * 70)
    print("ЗАКЛЮЧЕНИЕ:")
    print("=" * 70)
    print("В данной последовательности все элементы стремятся к 0.")
    print("Поскольку 0 - целое число, то чем ближе элемент к 0,")
    print("тем ближе он к целому числу. Поэтому элемент с наибольшим")
    print("индексом (x₁₀₀) будет ближе всего к целому числу.")
    print("=" * 70)


if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
