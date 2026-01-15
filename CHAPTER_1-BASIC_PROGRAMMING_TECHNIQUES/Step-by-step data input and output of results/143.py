"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
6. Пошаговый ввод данных и вывод результатов *)

143. Даны действительные числа a1,a2,a3,a4,x1, ..., x50. Получить b1, ..., b50, где 
bi = (x^2i - xi - a1) / (xi - a1) * (x^3i - xi - a2) / (xi - a2) * (xi - a3) - (x^4i - xi - a4) / xi + xi * (xi + a3), i = 1,2, ..., 50. 
"""


def compute_bi(xi, a1, a2, a3, a4):
    """Вычисляет значение b_i для заданных параметров"""
    
    # Проверка особых случаев
    if xi == 0:
        # При xi = 0, второе слагаемое: -(0^4 - 0 - a4)/0 = -(-a4)/0 = a4/0
        # Это приводит к делению на ноль
        return float('inf') if a4 != 0 else float('nan')
    
    if xi == a1:
        # Первый множитель: (a1^2 - a1 - a1)/(a1 - a1) = (a1^2 - 2a1)/0
        return float('inf') if (a1**2 - 2*a1) != 0 else float('nan')
    
    if xi == a2:
        # Второй множитель: (a2^3 - a2 - a2)/(a2 - a2) = (a2^3 - 2a2)/0
        return float('inf') if (a2**3 - 2*a2) != 0 else float('nan')
    
    # Обычное вычисление
    factor1 = (xi**2 - xi - a1) / (xi - a1)
    factor2 = (xi**3 - xi - a2) / (xi - a2)
    factor3 = xi - a3
    
    term1 = factor1 * factor2 * factor3
    term2 = -(xi**4 - xi - a4) / xi
    term3 = xi * (xi + a3)
    
    return term1 + term2 + term3


def main():
    print("Вычисление последовательности b_i")
    print("=" * 70)
    
    # Ввод параметров
    print("Введите значения параметров:")
    a1 = float(input("a1 = "))
    a2 = float(input("a2 = "))
    a3 = float(input("a3 = "))
    a4 = float(input("a4 = "))
    
    print("\nАнализ формулы:")
    print(f"Особые точки (деление на ноль):")
    print(f"  1. x_i = 0 (в слагаемом -(x_i^4 - x_i - a4)/x_i)")
    print(f"  2. x_i = a1 = {a1} (в первом множителе)")
    print(f"  3. x_i = a2 = {a2} (во втором множителе)")
    print("=" * 70)
    
    # Ввод 50 значений
    print("\nВведите 50 значений x_i:")
    
    results = []
    
    for i in range(1, 51):
        xi = float(input(f"x_{i} = "))
        
        # Вычисляем b_i
        bi = compute_bi(xi, a1, a2, a3, a4)
        results.append(bi)
        
        # Проверяем на особые значения
        if abs(xi) < 1e-10:
            print(f"  Приближенно 0 -> b_{i} = {'∞' if bi > 1e10 else bi}")
        elif abs(xi - a1) < 1e-10:
            print(f"  Приближенно a1 -> b_{i} = {'∞' if bi > 1e10 else bi}")
        elif abs(xi - a2) < 1e-10:
            print(f"  Приближенно a2 -> b_{i} = {'∞' if bi > 1e10 else bi}")
        else:
            print(f"  b_{i} = {bi:.6f}")
    
    # Вывод статистики
    print("\n" + "=" * 70)
    print("Статистика (исключая бесконечности и NaN):")
    
    finite_results = [b for b in results if abs(b) < 1e10 and not math.isnan(b)]
    
    if finite_results:
        min_val = min(finite_results)
        max_val = max(finite_results)
        avg_val = sum(finite_results) / len(finite_results)
        
        print(f"Конечных значений: {len(finite_results)} из 50")
        print(f"Минимальное конечное значение: {min_val:.6f}")
        print(f"Максимальное конечное значение: {max_val:.6f}")
        print(f"Среднее конечное значение: {avg_val:.6f}")
    else:
        print("Нет конечных значений в последовательности")


if __name__ == "__main__":
    import math
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
