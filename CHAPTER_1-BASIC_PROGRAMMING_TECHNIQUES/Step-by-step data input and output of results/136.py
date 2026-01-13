"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
6. Пошаговый ввод данных и вывод результатов *)

*) В задачах этого параграфа не требуется хранения исходных
последовательностей значений.
136. Даны натуральное число n , действительные числа a1, ..., an.
Вычислить:
"""


import math

def main():
    print("Программа вычисления различных выражений для последовательности действительных чисел")
    
    # Ввод количества чисел
    n = int(input("Введите натуральное число n: "))
    
    # Инициализация переменных для накопления результатов
    # а) сумма всех чисел
    sum_all = 0
    # б) произведение всех чисел
    product_all = 1
    # в) сумма модулей
    sum_abs = 0
    # г) произведение модулей
    product_abs = 1
    # д) сумма квадратов
    sum_squares = 0
    # ж) знакопеременная сумма
    alternating_sum = 0
    # з) знакопеременная сумма с факториалами
    alternating_factorial_sum = 0
    # и) сумма с факториалами в знаменателе
    factorial_sum = 0
    # н) сумма квадратов разностей
    sqrt_diff_sum = 0
    # о) сумма корней из (10 + a_i^2)
    sqrt_10_sum = 0
    
    # Переменные для вычисления факториалов
    factorial = 1  # для текущего i
    
    # Ввод чисел и вычисление промежуточных результатов
    for i in range(1, n + 1):
        a = float(input(f"Введите a{i}: "))
        abs_a = abs(a)
        
        # а) сумма всех чисел
        sum_all += a
        
        # б) произведение всех чисел
        product_all *= a
        
        # в) сумма модулей
        sum_abs += abs_a
        
        # г) произведение модулей
        product_abs *= abs_a
        
        # д) сумма квадратов
        sum_squares += a ** 2
        
        # ж) знакопеременная сумма: a1 - a2 + a3 - ... + (-1)^(n+1)*an
        alternating_sum += ((-1) ** (i + 1)) * a
        
        # Обновление факториала для текущего i
        factorial *= i
        
        # з) -a1/1! + a2/2! - ... + (-1)^n*an/n!
        alternating_factorial_sum += ((-1) ** i) * a / factorial
        
        # и) a1/0! + a2/1! + ... + an/(n-1)!
        # Для текущего элемента используется (i-1)!
        if i == 1:
            prev_factorial = 1  # 0! = 1
        else:
            prev_factorial = factorial // i  # (i-1)! = i! / i
        factorial_sum += a / prev_factorial
        
        # н) (sqrt(|a1|) - a1)^2 + ... + (sqrt(|an|) - an)^2
        sqrt_diff_sum += (math.sqrt(abs_a) - a) ** 2
        
        # о) sqrt(10 + a1^2) + ... + sqrt(10 + an^2)
        sqrt_10_sum += math.sqrt(10 + a ** 2)
    
    # Вычисление окончательных результатов
    # к) 2*(сумма всех чисел)^2
    double_square_sum = 2 * (sum_all ** 2)
    
    # л) квадратный корень из произведения модулей
    sqrt_product_abs = math.sqrt(product_abs)
    
    # м) синус модуля суммы всех чисел
    sin_sum_abs = math.sin(abs(sum_all))
    
    # Вывод результатов
    print("\nРезультаты вычислений:")
    print(f"а) Сумма всех чисел: {sum_all}")
    print(f"б) Произведение всех чисел: {product_all}")
    print(f"в) Сумма модулей: {sum_abs}")
    print(f"г) Произведение модулей: {product_abs}")
    print(f"д) Сумма квадратов: {sum_squares}")
    print(f"е) Сумма: {sum_all}, Произведение: {product_all}")
    print(f"ж) Знакопеременная сумма: {alternating_sum}")
    print(f"з) Знакопеременная сумма с факториалами: {alternating_factorial_sum}")
    print(f"и) Сумма с факториалами в знаменателе: {factorial_sum}")
    print(f"к) 2*(сумма)^2: {double_square_sum}")
    print(f"л) Квадратный корень из произведения модулей: {sqrt_product_abs}")
    print(f"м) sin(|сумма|): {sin_sum_abs}")
    print(f"н) Сумма квадратов разностей: {sqrt_diff_sum}")
    print(f"о) Сумма корней из (10 + a_i^2): {sqrt_10_sum}")

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
