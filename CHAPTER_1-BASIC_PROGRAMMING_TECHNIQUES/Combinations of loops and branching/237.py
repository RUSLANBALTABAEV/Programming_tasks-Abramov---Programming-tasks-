"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
7. Сочетания цикла и разветвления

237. Даны натуральное число n, действительное число r.
Вычислить ((2 * r) ^ n) / n!! * (pi / 2) ^ abs(n / 2) (см. задачу 113).
"""


import math

def double_factorial(n):
    """Вычисляет n!! (двойной факториал) по задаче 113"""
    result = 1
    if n % 2 == 1:  # нечетное n
        for i in range(1, n + 1, 2):
            result *= i
    else:  # четное n
        for i in range(2, n + 1, 2):
            result *= i
    return result

def compute_expression_direct(n, r):
    """Прямое вычисление выражения (2r)^n / n! * (π/2)^[n/2]"""
    # Целая часть от n/2
    floor_n2 = n // 2
    
    # Вычисляем компоненты
    numerator = (2 * r) ** n
    factorial_n = math.factorial(n)
    pi_power = (math.pi / 2) ** floor_n2
    
    # Вычисляем результат
    result = (numerator / factorial_n) * pi_power
    return result, numerator, factorial_n, pi_power

def compute_expression_log(n, r):
    """Вычисление выражения через логарифмы (для больших n)"""
    if r == 0:
        return 0.0, None, None, None
    
    floor_n2 = n // 2
    
    # Вычисляем логарифмы
    # log((2r)^n) = n * log(|2r|)
    # знак обработаем отдельно
    abs_2r = abs(2 * r)
    
    if abs_2r == 0:
        return 0.0, None, None, None
    
    log_numerator = n * math.log(abs_2r)
    log_factorial = math.lgamma(n + 1)  # log(n!)
    log_pi_power = floor_n2 * math.log(math.pi / 2)
    
    # Суммируем логарифмы: log(result) = log_numerator - log_factorial + log_pi_power
    log_result = log_numerator - log_factorial + log_pi_power
    
    # Экспоненцируем
    abs_result = math.exp(log_result)
    
    # Учитываем знак
    if r >= 0:
        result = abs_result
    else:
        # (2r)^n = (-1)^n * (2|r|)^n
        sign = 1 if n % 2 == 0 else -1
        result = sign * abs_result
    
    # Приближенные значения компонентов для вывода
    numerator_approx = (2 * r) ** n if n <= 100 else None
    factorial_approx = math.factorial(n) if n <= 100 else None
    pi_power_approx = (math.pi / 2) ** floor_n2 if floor_n2 <= 100 else None
    
    return result, numerator_approx, factorial_approx, pi_power_approx

def main():
    print("237. Вычисление выражения (2r)^n / n! * (π/2)^[n/2]")
    print("=" * 70)
    
    try:
        # Ввод натурального числа n
        n = int(input("Введите натуральное число n: "))
        
        if n < 0:
            print("Ошибка: n должно быть натуральным числом (n ≥ 0)")
            return
        
        # Ввод действительного числа r
        r = float(input("Введите действительное число r: "))
        
        print(f"\nДано: n = {n}, r = {r}")
        print(f"[n/2] = [{n}/2] = {n // 2}")
        
        # Выбираем метод вычисления в зависимости от n
        if n <= 100:  # Для небольших n используем прямой метод
            result, numerator, factorial_n, pi_power = compute_expression_direct(n, r)
            method = "прямой"
        else:  # Для больших n используем логарифмический
            result, numerator, factorial_n, pi_power = compute_expression_log(n, r)
            method = "логарифмический"
        
        # Вывод результата
        print(f"\nРезультат вычисления ({method} метод):")
        print(f"({2*r})^{n} / {n}! * (π/2)^{n//2}")
        
        # Показываем компоненты, если они вычислены
        if numerator is not None:
            print(f"= ({numerator:.6e}) / ", end="")
        else:
            print(f"= (2r)^{n} / ", end="")
            
        if factorial_n is not None:
            print(f"({factorial_n:.6e}) * ", end="")
        else:
            print(f"{n}! * ", end="")
            
        if pi_power is not None:
            print(f"({pi_power:.6e})")
        else:
            print(f"(π/2)^{n//2}")
        
        print(f"≈ {result:.12e}")
        
        # Дополнительная информация
        print("\n" + "=" * 70)
        print("Пояснение вычислений:")
        
        floor_n2 = n // 2
        print(f"1. [n/2] = целая часть от {n}/2 = {floor_n2}")
        print(f"2. (π/2)^[n/2] = (π/2)^{floor_n2} ≈ {(math.pi/2)**floor_n2 if floor_n2 <= 20 else 'очень большое'}")
        print(f"3. n! = {math.factorial(n) if n <= 20 else 'очень большое'}")
        
        if n <= 20:
            print(f"4. (2r)^n = ({2*r})^{n} = {(2*r)**n}")
        else:
            print(f"4. (2r)^n = ({2*r})^{n} ≈ {'очень большое' if abs(2*r) > 1 else 'очень малое'}")
        
        # Анализ результата
        print("\nАнализ результата:")
        
        if r == 0:
            print("При r = 0:")
            if n == 0:
                print("  Выражение не определено (0^0)")
            else:
                print(f"  (2r)^n = 0, поэтому результат = 0")
        else:
            # Определяем поведение выражения
            ratio = abs(2 * r) / n if n > 0 else float('inf')
            
            if ratio > 1:
                print(f"  |2r|/n = {ratio:.3f} > 1, поэтому (2r)^n растет быстрее n! при больших n")
                print(f"  Но в выражении есть дополнительный множитель (π/2)^[n/2]")
            elif ratio < 1:
                print(f"  |2r|/n = {ratio:.3f} < 1, поэтому (2r)^n растет медленнее n! при больших n")
            else:
                print(f"  |2r|/n = 1, поэтому (2r)^n и n! растут сопоставимо")
        
        # Связь с двойным факториалом (задача 113)
        print("\n" + "=" * 70)
        print("Связь с задачей 113 (двойной факториал):")
        
        if n <= 50:
            n_double_fact = double_factorial(n)
            print(f"n!! = {n_double_fact}")
            
            # Интересное наблюдение: для четных n, n!! = 2^(n/2) * (n/2)!
            # Но в нашем выражении есть (π/2)^[n/2], что не связано напрямую с двойным факториалом.
            # Однако можно отметить:
            if n % 2 == 0:
                k = n // 2
                print(f"Для четного n = {n}:")
                print(f"  n!! = 2^{k} * {k}! = {2**k} * {math.factorial(k)} = {n_double_fact}")
            else:
                print(f"Для нечетного n = {n}:")
                print(f"  n!! = произведение нечетных чисел от 1 до {n}")
        
        # Сравнение методов (если применимо)
        if n <= 100:
            # Вычисляем также логарифмическим методом для сравнения
            result_log, _, _, _ = compute_expression_log(n, r)
            diff = abs(result - result_log)
            
            if diff < 1e-10:
                print(f"\n✓ Результаты прямого и логарифмического методов совпадают")
            else:
                print(f"\n⚠ Разница между методами: {diff:.2e}")
                print(f"  Прямой метод: {result:.12e}")
                print(f"  Логарифмический: {result_log:.12e}")
        
        # Приближение для больших n (формула Стирлинга)
        if n > 20:
            print("\nПриближение по формуле Стирлинга для n! (большие n):")
            stirling = math.sqrt(2 * math.pi * n) * (n / math.e) ** n
            print(f"  n! ≈ √(2πn) * (n/e)^n ≈ {stirling:.6e}")
            
            # Приближенное значение выражения
            if r != 0:
                log_stirling = 0.5 * math.log(2 * math.pi * n) + n * math.log(n / math.e)
                log_result_approx = n * math.log(abs(2 * r)) - log_stirling + floor_n2 * math.log(math.pi / 2)
                result_approx = math.exp(log_result_approx)
                
                if r < 0 and n % 2 == 1:
                    result_approx = -result_approx
                
                print(f"  Приближенное значение выражения: {result_approx:.6e}")
        
    except ValueError:
        print("Ошибка ввода: проверьте, что введены корректные числа")
    except OverflowError:
        print("Ошибка переполнения: слишком большие значения n или r")
        print("Попробуйте использовать логарифмический метод (увеличьте порог n в коде)")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")

if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
