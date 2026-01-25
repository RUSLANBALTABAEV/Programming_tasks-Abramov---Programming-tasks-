"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
7. Сочетания цикла и разветвления

222. Даны натуральное число n, действительные числа y1, …, yn. 
Найти:
а) max(abs(z1), ..., abs(zn)), где zi = (yi, при abs(yi) <= 2, zi = 0.5 в противном случае;
б) min(abs(z1), ..., abs(zn)), где zi = yi при abs(yi) > 1, zi = 2 в противном случае;
в) z1 + ... + zn где zi = yi при 0 < yi < 10, zi = 1 в противном случае;
г) (sqrt(z1) - z1) ^ 2  + ... + (sqrt(zn - zn)) ^ 2, где
zi = yi при 0 < yi <= 15, zi = 2.7 в противном случае;
д) z1 ^ 2 + ... + zn ^ 2, где zi = yi при abs(yi) < 1, zi = 1/yi, в противном случае.
"""


import math

def read_input():
    """Чтение входных данных"""
    n = int(input("Введите натуральное число n: "))
    print(f"Введите {n} действительных чисел через пробел:")
    y = list(map(float, input().split()))
    
    if len(y) != n:
        print(f"Ошибка: введено {len(y)} чисел вместо {n}")
        return None
    
    return y

def task_a(y):
    """a) max(|z_i|) где z_i = y_i при |y_i| <= 2, иначе 0.5"""
    z = []
    for yi in y:
        if abs(yi) <= 2:
            z.append(yi)
        else:
            z.append(0.5)
    
    # Находим максимальное значение |z_i|
    max_abs_z = max(abs(zi) for zi in z)
    
    return z, max_abs_z

def task_b(y):
    """б) min(|z_i|) где z_i = y_i при |y_i| > 1, иначе 2"""
    z = []
    for yi in y:
        if abs(yi) > 1:
            z.append(yi)
        else:
            z.append(2)
    
    # Находим минимальное значение |z_i|
    min_abs_z = min(abs(zi) for zi in z)
    
    return z, min_abs_z

def task_c(y):
    """в) сумма z_i где z_i = y_i при 0 < y_i < 10, иначе 1"""
    z = []
    for yi in y:
        if 0 < yi < 10:
            z.append(yi)
        else:
            z.append(1)
    
    total_sum = sum(z)
    
    return z, total_sum

def task_d(y):
    """г) сумма (sqrt(z_i) - z_i)^2 где z_i = y_i при 0 < y_i <= 15, иначе 2.7"""
    z = []
    for yi in y:
        if 0 < yi <= 15:
            z.append(yi)
        else:
            z.append(2.7)
    
    # Вычисляем сумму (sqrt(z_i) - z_i)^2
    total = 0
    for zi in z:
        if zi >= 0:  # sqrt определен для неотрицательных
            total += (math.sqrt(zi) - zi) ** 2
        else:
            # Этот случай теоретически невозможен по условию, но для надежности
            total += (0 - zi) ** 2  # или можно считать sqrt от abs(zi)
    
    return z, total

def task_e(y):
    """д) сумма z_i^2 где z_i = y_i при |y_i| < 1, иначе 1/y_i"""
    z = []
    for yi in y:
        if abs(yi) < 1 and yi != 0:  # избегаем деления на 0
            z.append(yi)
        else:
            if yi == 0:
                # При yi=0 по условию |yi|<1, но тогда бы мы попали в первую ветку
                # Однако если |0|<1 истинно, то z_i = 0
                # Но деление на 0 возникнет только если |yi|>=1 и yi=0, что невозможно
                # Поэтому оставляем как есть
                z.append(0)
            else:
                z.append(1 / yi)
    
    # Вычисляем сумму квадратов
    total = sum(zi ** 2 for zi in z)
    
    return z, total

def main():
    print("222. Обработка последовательности чисел y1,...,yn")
    print("=" * 60)
    
    # Чтение входных данных
    y = read_input()
    if y is None:
        return
    
    n = len(y)
    
    print(f"\nВведено {n} чисел: {y}")
    print("\nРезультаты вычислений:")
    print("=" * 60)
    
    # a) max(|z_i|)
    z_a, result_a = task_a(y)
    print(f"а) Максимум |z_i|, где z_i = y_i при |y_i| <= 2, иначе 0.5")
    print(f"   z = {z_a}")
    print(f"   max(|z_i|) = {result_a:.6f}")
    print()
    
    # б) min(|z_i|)
    z_b, result_b = task_b(y)
    print(f"б) Минимум |z_i|, где z_i = y_i при |y_i| > 1, иначе 2")
    print(f"   z = {z_b}")
    print(f"   min(|z_i|) = {result_b:.6f}")
    print()
    
    # в) сумма z_i
    z_c, result_c = task_c(y)
    print(f"в) Сумма z_i, где z_i = y_i при 0 < y_i < 10, иначе 1")
    print(f"   z = {z_c}")
    print(f"   Сумма z_i = {result_c:.6f}")
    print()
    
    # г) сумма (sqrt(z_i) - z_i)^2
    z_d, result_d = task_d(y)
    print(f"г) Сумма (√z_i - z_i)², где z_i = y_i при 0 < y_i <= 15, иначе 2.7")
    print(f"   z = {z_d}")
    print(f"   Сумма (√z_i - z_i)² = {result_d:.6f}")
    print()
    
    # д) сумма z_i^2
    z_e, result_e = task_e(y)
    print(f"д) Сумма z_i², где z_i = y_i при |y_i| < 1, иначе 1/y_i")
    print(f"   z = {z_e}")
    print(f"   Сумма z_i² = {result_e:.6f}")

if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
