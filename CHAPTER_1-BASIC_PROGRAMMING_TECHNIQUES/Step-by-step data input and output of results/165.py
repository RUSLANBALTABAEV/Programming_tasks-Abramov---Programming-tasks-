"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
6. Пошаговый ввод данных и вывод результатов *)

165. Даны действительные числа a1, a2, … Известно, что a1 > 0 и что среди a2, a3, … есть хотя бы одно отрицательное число. Пусть a1, ..., an - члены данной последовательности, предшествующие первому отрицательному члену (n заранее неизвестно). Получить:
а) a1 + a2 + ... an;
б) a1 * a2 ... an;
в) среднее арифметическое a1, ..., an;
г) среднее геометрическое a1, ..., an;
д) a1, a1 * a2, a1 * a2 * a3, ..., a1 * a2 ... an;
е) a1 + 2 * a2 + 2 * a3 + ... + 2 * an-1 + an;
ж) a1 * a2 + a2 * a3 + ... + an - 1 * an + an * a1l
з) (-1) ^ n * an;
и) n + an;
к) |a1 - an|.
"""


import math

def main():
    print("Введите действительные числа (a1 > 0, среди a2, a3, ... есть хотя бы одно отрицательное):")
    
    # Список для хранения чисел до первого отрицательного
    numbers = []
    
    # Счетчик введенных чисел
    count = 0
    
    while True:
        count += 1
        a = float(input(f"a[{count}]: "))
        
        # Проверяем, является ли число первым (должно быть положительным)
        if count == 1 and a <= 0:
            print("Ошибка: a1 должно быть > 0!")
            count -= 1
            continue
        
        # Если число отрицательное и это не первый элемент
        if a < 0 and count > 1:
            print(f"Обнаружено первое отрицательное число: {a}")
            print(f"Последовательность до первого отрицательного состоит из {len(numbers)} элементов")
            break
        
        # Добавляем число в список
        numbers.append(a)
    
    n = len(numbers)
    
    if n == 0:
        print("Ошибка: нет чисел до первого отрицательного!")
        return
    
    print(f"\nПолученная последовательность (n = {n}):")
    for i, num in enumerate(numbers, 1):
        print(f"a[{i}] = {num}")
    
    # а) Сумма всех элементов
    sum_all = sum(numbers)
    print(f"\nа) Сумма всех элементов: {sum_all:.6f}")
    
    # б) Произведение всех элементов
    product_all = 1.0
    for num in numbers:
        product_all *= num
    print(f"б) Произведение всех элементов: {product_all:.6f}")
    
    # в) Среднее арифметическое
    average_arith = sum_all / n
    print(f"в) Среднее арифметическое: {average_arith:.6f}")
    
    # г) Среднее геометрическое
    # Проверяем, что все числа неотрицательные (для геометрического среднего)
    if all(num >= 0 for num in numbers):
        # Если есть 0, то среднее геометрическое = 0
        if 0 in numbers:
            average_geom = 0.0
        else:
            average_geom = product_all ** (1/n)
        print(f"г) Среднее геометрическое: {average_geom:.6f}")
    else:
        print("г) Среднее геометрическое: невозможно вычислить (есть отрицательные числа)")
    
    # д) Последовательность произведений: a1, a1*a2, a1*a2*a3, ...
    print("\nд) Последовательность произведений:")
    cumulative_product = 1.0
    for i, num in enumerate(numbers, 1):
        cumulative_product *= num
        print(f"  P[{i}] = {cumulative_product:.6f}")
    
    # е) a1 + 2*a2 + 2*a3 + ... + 2*a_{n-1} + a_n
    if n == 1:
        sum_special = numbers[0]
    else:
        sum_special = numbers[0] + numbers[-1] + 2 * sum(numbers[1:-1])
    print(f"\nе) a1 + 2*a2 + ... + 2*a_{{n-1}} + an: {sum_special:.6f}")
    
    # ж) a1*a2 + a2*a3 + ... + a_{n-1}*a_n + a_n*a1
    sum_pairwise = 0.0
    if n == 1:
        sum_pairwise = numbers[0] * numbers[0]  # a1*a1
    else:
        for i in range(n-1):
            sum_pairwise += numbers[i] * numbers[i+1]
        sum_pairwise += numbers[-1] * numbers[0]  # a_n*a1
    print(f"ж) Сумма попарных произведений (с замыканием): {sum_pairwise:.6f}")
    
    # з) (-1)^n * a_n
    sign = 1 if n % 2 == 0 else -1
    result_h = sign * numbers[-1]
    print(f"з) (-1)^{n} * a_n = {result_h:.6f}")
    
    # и) n + a_n
    result_i = n + numbers[-1]
    print(f"и) n + a_n = {result_i:.6f}")
    
    # к) |a1 - a_n|
    result_j = abs(numbers[0] - numbers[-1])
    print(f"к) |a1 - a_n| = {result_j:.6f}")

if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
