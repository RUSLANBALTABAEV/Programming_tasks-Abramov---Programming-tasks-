"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
7. Сочетания цикла и разветвления

235. Даны натуральные числа n и m. Получить (m! + n!) / (m + n)!.
"""


import math

def compute_expression(n, m):
    """Вычисляет выражение (m + n!) / (m + n)!"""
    try:
        # Вычисляем факториалы
        n_factorial = math.factorial(n)  # n!
        m_plus_n_factorial = math.factorial(m + n)  # (m + n)!
        
        # Вычисляем числитель: m + n!
        numerator = m + n_factorial
        
        # Вычисляем результат
        result = numerator / m_plus_n_factorial
        
        return result, n_factorial, m_plus_n_factorial
    except (OverflowError, ValueError) as e:
        # Если произошло переполнение, используем логарифмы
        # log((m+n)!) = sum(log(k) for k in range(1, m+n+1))
        # Но для больших чисел можем использовать формулу Стирлинга или math.lgamma
        
        # Используем логарифмы для избежания переполнения
        # result = (m + n!) / (m+n)!
        # log(result) = log(m + n!) - log((m+n)!)
        
        # Вычисляем log(n!) и log((m+n)!)
        log_n_fact = math.lgamma(n + 1)  # log(n!)
        log_mn_fact = math.lgamma(m + n + 1)  # log((m+n)!)
        
        # Вычисляем log(m + n!)
        # Это сложно, так как m + n! - это сумма
        # Для больших n, n! >> m, поэтому m + n! ≈ n!
        # Тогда log(m + n!) ≈ log(n!) = log_n_fact
        # Но если m сравнимо с n!, нужно быть аккуратнее
        
        if n_factorial_approx := math.exp(log_n_fact):
            # Приближенное значение n!
            # Сравниваем m и n!
            if m < n_factorial_approx * 1e-10:  # m намного меньше n!
                log_numerator = log_n_fact  # log(m + n!) ≈ log(n!)
            else:
                # Нужно вычислить точно: log(m + n!)
                # Используем формулу: log(a+b) = log(a) + log(1 + b/a)
                # где a = n!, b = m
                n_fact_approx = math.exp(log_n_fact)
                log_numerator = log_n_fact + math.log1p(m / n_fact_approx)
        else:
            # n! слишком велико, m пренебрежимо мало
            log_numerator = log_n_fact
        
        # Вычисляем log(result)
        log_result = log_numerator - log_mn_fact
        
        # Возвращаем результат
        result = math.exp(log_result)
        
        # Для очень малых чисел может быть underflow
        if result == 0 and log_result < -700:  # exp(-700) ≈ 0
            # Результат практически 0
            return result, None, None
        
        return result, None, None

def main():
    print("235. Вычисление выражения (m + n!) / (m + n)!")
    print("=" * 60)
    
    try:
        # Ввод натуральных чисел n и m
        n = int(input("Введите натуральное число n: "))
        m = int(input("Введите натуральное число m: "))
        
        if n < 0 or m < 0:
            print("Ошибка: числа должны быть натуральными (n ≥ 0, m ≥ 0)")
            return
        
        print(f"\nДано: n = {n}, m = {m}")
        
        # Вычисляем выражение
        result, n_fact, mn_fact = compute_expression(n, m)
        
        # Вывод результатов
        print(f"\nРезультат вычисления:")
        print(f"({m} + {n}!) / ({m} + {n})! = ", end="")
        
        if n_fact is not None and mn_fact is not None:
            print(f"({m} + {n_fact}) / {mn_fact}")
        else:
            print(f"(m + n!) / (m+n)!")
        
        print(f"≈ {result}")
        
        # Научная запись для очень больших/малых чисел
        if abs(result) < 1e-4 or abs(result) > 1e4 or (0 < abs(result) < 1e-10):
            print(f"Научная запись: {result:.6e}")
        
        # Дополнительная информация
        print("\n" + "=" * 60)
        print("Пояснение:")
        print(f"1. n! = {n}! = ", end="")
        if n <= 20:
            print(f"{math.factorial(n)}")
        else:
            print(f"≈ {math.exp(math.lgamma(n+1)):.6e}")
        
        print(f"2. (m+n)! = ({m}+{n})! = {m+n}! = ", end="")
        if m+n <= 20:
            print(f"{math.factorial(m+n)}")
        else:
            print(f"≈ {math.exp(math.lgamma(m+n+1)):.6e}")
        
        print(f"3. m + n! = {m} + {n}! = ", end="")
        if n <= 20:
            n_fact_val = math.factorial(n)
            print(f"{m} + {n_fact_val} = {m + n_fact_val}")
        else:
            n_fact_approx = math.exp(math.lgamma(n+1))
            print(f"≈ {m} + {n_fact_approx:.6e} ≈ {m + n_fact_approx:.6e}")
        
        # Анализ результата
        print("\nАнализ:")
        if result > 1:
            print(f"Результат > 1: {result:.6f} > 1")
            print("Это возможно только при небольших значениях m и n")
        elif result == 1:
            print("Результат = 1")
            print("Это означает, что m + n! = (m+n)!")
        elif result == 0:
            print("Результат практически равен 0")
            print("Знаменатель (m+n)! намного больше числителя m+n!")
        elif 0 < result < 1e-10:
            print("Результат очень мал (< 10⁻¹⁰)")
            print("Факториал (m+n)! растет очень быстро")
        else:
            print(f"Результат: {result:.10f}")
        
        # Сравнение с упрощенными выражениями
        print("\nСравнение с приближенными значениями:")
        
        # 1. Если пренебречь m в числителе
        approx1 = math.factorial(n) / math.factorial(m+n) if n <= 20 and m+n <= 20 else math.exp(math.lgamma(n+1) - math.lgamma(m+n+1))
        print(f"1. Если пренебречь m: n!/(m+n)! ≈ {approx1:.10e}")
        print(f"   Относительная ошибка: {abs((result-approx1)/result)*100 if result != 0 else '∞':.2f}%")
        
        # 2. Если считать, что m+n ≈ n (при m << n)
        if m < n:
            approx2 = (m + math.factorial(n)) / math.factorial(n) if n <= 20 else (m + math.exp(math.lgamma(n+1))) / math.exp(math.lgamma(n+1))
            approx2 = 1  # (m+n)!/(m+n)! = 1, но это неверно
            # Правильнее: если m мало, то (m+n)! ≈ n! * (n+1)^m
            # Но это сложно, поэтому пропустим
        
    except ValueError:
        print("Ошибка ввода: введите натуральные числа")
    except Exception as e:
        print(f"Ошибка вычисления: {e}")

if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
