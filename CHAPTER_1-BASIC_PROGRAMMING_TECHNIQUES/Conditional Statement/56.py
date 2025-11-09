"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
2. Разветвления
56. Даны действительные положительные числа a, b, c, x, y.
Выяснить, пройдет ли кирпич с ребрами a, b, c в прямоугольное
отверстие со сторонами x и y. Просовывать кирпич в отверстие
разрешается только так, чтобы каждое из его ребер было параллельно
или перпендикулярно каждой из сторон отверстия.
"""


def can_brick_pass_through_hole(a, b, c, x, y):
    """
    Проверяет, можно ли просунуть кирпич через отверстие.
    
    Кирпич имеет три ребра: a, b, c.
    Отверстие имеет стороны: x, y.
    
    Для каждой грани кирпича (прямоугольника с двумя ребрами)
    проверяем, проходит ли она через отверстие.
    
    Args:
        a, b, c: Ребра кирпича
        x, y: Стороны прямоугольного отверстия
    
    Returns:
        tuple: (can_pass, passing_orientations)
               can_pass - bool, может ли пройти кирпич
               passing_orientations - список подходящих ориентаций
    """
    orientations = []
    
    # Три возможные ориентации кирпича (три грани):
    # 1. Грань a×b (ребро c перпендикулярно отверстию)
    # 2. Грань a×c (ребро b перпендикулярно отверстию)
    # 3. Грань b×c (ребро a перпендикулярно отверстию)
    
    faces = [
        (a, b, 'c', "a×b (ребро c ⊥ отверстию)"),
        (a, c, 'b', "a×c (ребро b ⊥ отверстию)"),
        (b, c, 'a', "b×c (ребро a ⊥ отверстию)")
    ]
    
    for face1, face2, perpendicular, description in faces:
        # Проверяем две ориентации для каждой грани
        # Ориентация 1: face1 || x, face2 || y
        if face1 <= x and face2 <= y:
            orientations.append({
                'face': description,
                'orientation': f"{face1} ≤ {x} и {face2} ≤ {y}",
                'description': f"Грань {description}: {face1}×{face2} просовывается как {face1}||x, {face2}||y"
            })
        
        # Ориентация 2: face1 || y, face2 || x
        if face1 <= y and face2 <= x:
            orientations.append({
                'face': description,
                'orientation': f"{face1} ≤ {y} и {face2} ≤ {x}",
                'description': f"Грань {description}: {face1}×{face2} просовывается как {face1}||y, {face2}||x"
            })
    
    can_pass = len(orientations) > 0
    return can_pass, orientations


def main():
    """Основная функция программы."""
    print("Проверка прохождения кирпича через прямоугольное отверстие")
    print("=" * 75)
    
    try:
        # Ввод размеров кирпича
        print("Введите размеры кирпича (длины трех ребер):")
        a = float(input("  a = "))
        b = float(input("  b = "))
        c = float(input("  c = "))
        
        # Проверка на положительность
        if a <= 0 or b <= 0 or c <= 0:
            print("Ошибка: размеры кирпича должны быть положительными!")
            return
        
        print()
        
        # Ввод размеров отверстия
        print("Введите размеры прямоугольного отверстия:")
        x = float(input("  x = "))
        y = float(input("  y = "))
        
        # Проверка на положительность
        if x <= 0 or y <= 0:
            print("Ошибка: размеры отверстия должны быть положительными!")
            return
        
        print("=" * 75)
        
        # Выводим данные
        print("Размеры кирпича:")
        print(f"  Ребра: a = {a}, b = {b}, c = {c}")
        print(f"  Объем: {a * b * c:.2f}")
        print()
        print("Размеры отверстия:")
        print(f"  Стороны: x = {x}, y = {y}")
        print(f"  Площадь: {x * y:.2f}")
        print("-" * 75)
        
        # Проверяем возможность прохождения
        can_pass, orientations = can_brick_pass_through_hole(a, b, c, x, y)
        
        # Детальная проверка всех граней
        print("Проверка всех возможных граней кирпича:")
        print()
        
        faces = [
            (a, b, 'c', f"Грань 1: {a}×{b} (ребро c = {c} перпендикулярно)"),
            (a, c, 'b', f"Грань 2: {a}×{c} (ребро b = {b} перпендикулярно)"),
            (b, c, 'a', f"Грань 3: {b}×{c} (ребро a = {a} перпендикулярно)")
        ]
        
        for face1, face2, perp, desc in faces:
            print(desc)
            
            # Проверка первой ориентации
            orient1 = face1 <= x and face2 <= y
            print(f"  Ориентация 1: {face1} ≤ {x} и {face2} ≤ {y}", end="")
            if orient1:
                print(" ✓ Проходит")
            else:
                print(" ✗ Не проходит")
                if face1 > x:
                    print(f"    ({face1} > {x})")
                if face2 > y:
                    print(f"    ({face2} > {y})")
            
            # Проверка второй ориентации
            orient2 = face1 <= y and face2 <= x
            print(f"  Ориентация 2: {face1} ≤ {y} и {face2} ≤ {x}", end="")
            if orient2:
                print(" ✓ Проходит")
            else:
                print(" ✗ Не проходит")
                if face1 > y:
                    print(f"    ({face1} > {y})")
                if face2 > x:
                    print(f"    ({face2} > {x})")
            print()
        
        print("-" * 75)
        
        # Итоговый результат
        if can_pass:
            print(f"✓ Кирпич {a}×{b}×{c} ПРОЙДЕТ через отверстие {x}×{y}")
            print()
            print(f"Найдено подходящих ориентаций: {len(orientations)}")
            print()
            print("Способы прохождения:")
            for i, orient in enumerate(orientations, 1):
                print(f"  {i}. {orient['description']}")
        else:
            print(f"✗ Кирпич {a}×{b}×{c} НЕ ПРОЙДЕТ через отверстие {x}×{y}")
            print()
            print("Ни одна из граней кирпича не проходит через отверстие")
            print("ни в какой ориентации.")
        
        print("=" * 75)
        
    except ValueError:
        print("Ошибка: необходимо вводить числа!")


if __name__ == "__main__":
    main()

input("\nНажмите Enter, чтобы завершить программу.")
