"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
6. Пошаговый ввод данных и вывод результатов *)

146. Даны натуральное число n, действительные числа a, b (a != b). Получить r0, r1, ..., rn, где ri = a + i * h, h = (b - a) / n.
"""


def main():
    print("Равномерное разбиение отрезка [a, b]")
    print("=" * 70)
    
    # Ввод данных
    n = int(input("Введите количество интервалов n: "))
    a = float(input("Введите начало отрезка a: "))
    b = float(input("Введите конец отрезка b: "))
    
    if a == b:
        print("Ошибка: a и b не должны совпадать!")
        return
    
    # Определяем направление
    if a < b:
        start, end = a, b
        direction = "вправо"
    else:
        start, end = b, a
        direction = "влево"
        print(f"Замечание: a > b, поэтому рассматриваем отрезок [{start}, {end}]")
    
    # Вычисление шага
    h = (end - start) / n
    
    print(f"\nОтрезок [{start}, {end}] делится на {n} равных частей")
    print(f"Длина отрезка: {end - start}")
    print(f"Длина каждой части: h = {h}")
    print(f"Точек разбиения: {n + 1}")
    
    print("\nГрафическое представление разбиения:")
    print("-" * 70)
    
    # Создаем текстовую шкалу
    scale_length = 60  # Длина шкалы в символах
    scale_start = min(start, end)
    scale_end = max(start, end)
    
    print(f"{scale_start:10.4f}", end="")
    
    # Выводим шкалу
    for i in range(scale_length + 1):
        pos = scale_start + i * (scale_end - scale_start) / scale_length
        if i == 0:
            print("|", end="")
        elif i == scale_length:
            print(f"|{scale_end:10.4f}")
        else:
            # Отмечаем точки разбиения
            is_breakpoint = False
            for j in range(n + 1):
                rj = start + j * h
                if abs(pos - rj) < (scale_end - scale_start) / (scale_length * 2):
                    is_breakpoint = True
                    break
            
            if is_breakpoint:
                print("+", end="")
            else:
                print("-", end="")
    
    print("\n" + "=" * 70)
    print("Таблица точек разбиения:")
    print(f"{'i':>4} | {'ri':>12} | {'Координата':>12} | {'% от длины':>10}")
    print("-" * 70)
    
    for i in range(0, n + 1):
        ri = start + i * h
        percentage = i / n * 100 if n > 0 else 0
        print(f"{i:4} | a + {i:2}*h | {ri:12.6f} | {percentage:9.2f}%")
    
    print("-" * 70)
    
    # Анализ равномерности
    print("\nПроверка равномерности разбиения:")
    print(f"Первый интервал: [{start:.6f}, {start + h:.6f}], длина = {h:.6f}")
    print(f"Последний интервал: [{start + (n-1)*h:.6f}, {end:.6f}], длина = {h:.6f}")
    print(f"Все интервалы имеют одинаковую длину = {h:.6f}")
    
    # Пример использования для табулирования функции
    print("\n" + "=" * 70)
    print("Пример: табулирование функции f(x) = sin(x) на отрезке [a, b]")
    import math
    
    print(f"{'i':>4} | {'x':>12} | {'sin(x)':>12}")
    print("-" * 70)
    
    for i in range(0, n + 1):
        x = start + i * h
        sin_x = math.sin(x)
        print(f"{i:4} | {x:12.6f} | {sin_x:12.6f}")

if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
