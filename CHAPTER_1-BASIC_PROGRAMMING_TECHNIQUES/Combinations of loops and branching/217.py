"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
7. Сочетания цикла и разветвления

217. Даны натуральное число n, действительные числа x1, …, x3n. Последовательность чисел x1, …, x3n определяет на плоскости n
квадратов со сторонами, параллельными координатным осям: так, х1, х2 – координаты центра первого квадрата, х3 – длина его стороны;
аналогично, числа х4, х5, х6 определяют второй квадрат, х7, х8, х9 – третий и т. д. Имеются ли точки, принадлежащие всем квадратам?
Если да, то указать координаты одной из них.
"""


def main():
    # Ввод данных
    n = int(input("Введите n: "))
    print(f"Введите {3*n} чисел через пробел:")
    numbers = list(map(float, input().split()))
    
    if len(numbers) != 3*n:
        print("Ошибка: введено неверное количество чисел")
        return
    
    # Инициализация границ
    max_left_x = float('-inf')
    min_right_x = float('inf')
    max_left_y = float('-inf')
    min_right_y = float('inf')
    
    # Обработка каждого квадрата
    for k in range(1, n + 1):
        idx = 3 * (k - 1)  # индекс начала данных для k-го квадрата
        
        cx = numbers[idx]      # x-координата центра
        cy = numbers[idx + 1]  # y-координата центра
        s = numbers[idx + 2]   # длина стороны
        
        # Границы квадрата
        left_x = cx - s/2
        right_x = cx + s/2
        left_y = cy - s/2
        right_y = cy + s/2
        
        # Обновление границ пересечения
        max_left_x = max(max_left_x, left_x)
        min_right_x = min(min_right_x, right_x)
        max_left_y = max(max_left_y, left_y)
        min_right_y = min(min_right_y, right_y)
    
    # Проверка существования общей точки
    if max_left_x <= min_right_x and max_left_y <= min_right_y:
        # Вычисление координат одной из общих точек (центр прямоугольника пересечения)
        x0 = (max_left_x + min_right_x) / 2
        y0 = (max_left_y + min_right_y) / 2
        print(f"\nДа, существует общая точка.")
        print(f"Одна из общих точек: ({x0:.6f}, {y0:.6f})")
        
        # Можно также вывести весь прямоугольник пересечения
        print(f"Прямоугольник пересечения:")
        print(f"  по x: [{max_left_x:.6f}, {min_right_x:.6f}]")
        print(f"  по y: [{max_left_y:.6f}, {min_right_y:.6f}]")
    else:
        print("\nНет, общей точки нет.")
        print(f"Пересечение по x: {'есть' if max_left_x <= min_right_x else 'нет'}")
        print(f"Пересечение по y: {'есть' if max_left_y <= min_right_y else 'нет'}")

if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
