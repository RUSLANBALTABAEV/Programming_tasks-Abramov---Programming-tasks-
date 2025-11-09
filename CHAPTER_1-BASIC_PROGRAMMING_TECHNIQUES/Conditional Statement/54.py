"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
2. Разветвления
54. Даны действительные числа x1, x2, x3, y1, y2, y3. Принадлежит
ли начало координат треугольнику с вершинами (x1, y1), (x2, y2), (x3, y3)?
"""


def calculate_triangle_area(x1, y1, x2, y2, x3, y3):
    """
    Вычисляет площадь треугольника по координатам вершин.
    
    Формула: S = |0.5 * ((x₂-x₁)(y₃-y₁) - (x₃-x₁)(y₂-y₁))|
    
    Args:
        x1, y1: Координаты первой вершины
        x2, y2: Координаты второй вершины
        x3, y3: Координаты третьей вершины
    
    Returns:
        float: Площадь треугольника
    """
    area = abs(0.5 * ((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)))
    return area


def point_in_triangle(px, py, x1, y1, x2, y2, x3, y3):
    """
    Проверяет, находится ли точка P(px, py) внутри или на границе
    треугольника ABC с вершинами A(x1, y1), B(x2, y2), C(x3, y3).
    
    Метод: Сумма площадей треугольников PAB, PBC, PCA должна равняться
    площади треугольника ABC.
    
    Args:
        px, py: Координаты проверяемой точки
        x1, y1: Координаты вершины A
        x2, y2: Координаты вершины B
        x3, y3: Координаты вершины C
    
    Returns:
        tuple: (is_inside, area_abc, area_pab, area_pbc, area_pca, sum_areas)
    """
    # Площадь исходного треугольника ABC
    area_abc = calculate_triangle_area(x1, y1, x2, y2, x3, y3)
    
    # Проверка на вырожденный треугольник
    if area_abc == 0:
        return None, area_abc, 0, 0, 0, 0
    
    # Площади треугольников, образованных точкой P и сторонами ABC
    area_pab = calculate_triangle_area(px, py, x1, y1, x2, y2)
    area_pbc = calculate_triangle_area(px, py, x2, y2, x3, y3)
    area_pca = calculate_triangle_area(px, py, x3, y3, x1, y1)
    
    # Сумма площадей
    sum_areas = area_pab + area_pbc + area_pca
    
    # Точка внутри или на границе, если сумма площадей равна площади ABC
    # Используем малую погрешность для сравнения вещественных чисел
    epsilon = 1e-9
    is_inside = abs(sum_areas - area_abc) < epsilon
    
    return is_inside, area_abc, area_pab, area_pbc, area_pca, sum_areas


def main():
    """Основная функция программы."""
    print("Проверка принадлежности начала координат треугольнику")
    print("=" * 75)
    
    try:
        # Ввод координат вершин треугольника
        print("Введите координаты вершин треугольника:")
        print("Вершина A (x₁, y₁):")
        x1 = float(input("  x₁ = "))
        y1 = float(input("  y₁ = "))
        
        print("Вершина B (x₂, y₂):")
        x2 = float(input("  x₂ = "))
        y2 = float(input("  y₂ = "))
        
        print("Вершина C (x₃, y₃):")
        x3 = float(input("  x₃ = "))
        y3 = float(input("  y₃ = "))
        
        print("=" * 75)
        
        # Выводим данные
        print("Вершины треугольника:")
        print(f"  A = ({x1}, {y1})")
        print(f"  B = ({x2}, {y2})")
        print(f"  C = ({x3}, {y3})")
        print()
        print("Проверяемая точка:")
        print("  O = (0, 0) - начало координат")
        print("-" * 75)
        
        # Проверяем принадлежность начала координат треугольнику
        px, py = 0, 0  # Начало координат
        result = point_in_triangle(px, py, x1, y1, x2, y2, x3, y3)
        is_inside, area_abc, area_oab, area_obc, area_oca, sum_areas = result
        
        if is_inside is None:
            print("⚠ ОШИБКА: Вырожденный треугольник!")
            print("  Все три вершины лежат на одной прямой")
            print("  (площадь треугольника равна нулю)")
            return
        
        # Выводим площади
        print("Метод проверки: сравнение площадей")
        print()
        print(f"Площадь треугольника ABC: S(ABC) = {area_abc:.6f}")
        print()
        print("Площади треугольников, образованных точкой O:")
        print(f"  S(OAB) = {area_oab:.6f}")
        print(f"  S(OBC) = {area_obc:.6f}")
        print(f"  S(OCA) = {area_oca:.6f}")
        print(f"  Сумма = {sum_areas:.6f}")
        print("-" * 75)
        
        # Проверяем равенство площадей
        difference = abs(sum_areas - area_abc)
        print(f"Разность: |Сумма - S(ABC)| = {difference:.10f}")
        print()
        
        if is_inside:
            print("✓ Начало координат O(0, 0) ПРИНАДЛЕЖИТ треугольнику ABC")
            print("  (сумма площадей равна площади треугольника)")
            print()
            
            # Дополнительная информация о расположении точки
            epsilon = 1e-9
            if (area_oab < epsilon or area_obc < epsilon or area_oca < epsilon):
                print("  Примечание: точка O лежит на границе треугольника")
                if area_oab < epsilon:
                    print("    (на стороне AB или её продолжении)")
                if area_obc < epsilon:
                    print("    (на стороне BC или её продолжении)")
                if area_oca < epsilon:
                    print("    (на стороне CA или её продолжении)")
            else:
                print("  Точка O находится внутри треугольника")
        else:
            print("✗ Начало координат O(0, 0) НЕ ПРИНАДЛЕЖИТ треугольнику ABC")
            print("  (сумма площадей не равна площади треугольника)")
            print()
            print(f"  Сумма площадей ({sum_areas:.6f}) ≠ "
                  f"Площадь ABC ({area_abc:.6f})")
        
        print("=" * 75)
        
    except ValueError:
        print("Ошибка: необходимо вводить числа!")


if __name__ == "__main__":
    main()

input("\nНажмите Enter, чтобы завершить программу.")
