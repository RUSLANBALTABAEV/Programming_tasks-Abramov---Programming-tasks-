"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
7. Сочетания цикла и разветвления

236. Даны натуральное число n, действительное число x.
Получить 10Es=0 * 1 / s! * (n + s)! * (x / 2) ^ 2 * s + n.
"""


import math

def compute_sum(n, x):
    """Вычисляет сумму sum_{s=0}^{10} 1/(s! * (n+s)!) * (x/2)^(2s+n)"""
    total = 0.0
    
    # Вычисляем каждый член суммы
    for s in range(0, 11):  # s от 0 до 10 включительно
        # Вычисляем факториалы
        s_factorial = math.factorial(s)
        n_plus_s_factorial = math.factorial(n + s)
        
        # Вычисляем (x/2)^(2s+n)
        power = (x / 2) ** (2 * s + n)
        
        # Вычисляем член суммы
        term = (1 / (s_factorial * n_plus_s_factorial)) * power
        total += term
        
        # Для отладки: выводим каждый член
        # print(f"s={s}: term={term:.10e}, total={total:.10e}")
    
    return total

def compute_sum_optimized(n, x):
    """Оптимизированная версия с использованием рекуррентной формулы"""
    # Начальный член при s=0
    current_term = (x / 2) ** n / math.factorial(n)
    total = current_term
    
    # Вычисляем остальные члены рекуррентно
    for s in range(1, 11):
        # Рекуррентная формула: term_s = term_{s-1} * (x^2/4) / (s * (n+s))
        current_term *= (x * x / 4) / (s * (n + s))
        total += current_term
    
    return total

def main():
    print("236. Вычисление суммы ∑[s=0..10] 1/(s!(n+s)!) * (x/2)^(2s+n)")
    print("=" * 70)
    
    try:
        # Ввод натурального числа n
        n = int(input("Введите натуральное число n: "))
        
        if n < 0:
            print("Ошибка: n должно быть натуральным числом (n ≥ 0)")
            return
        
        # Ввод действительного числа x
        x = float(input("Введите действительное число x: "))
        
        print(f"\nДано: n = {n}, x = {x}")
        
        # Вычисляем сумму двумя способами для проверки
        result1 = compute_sum(n, x)
        result2 = compute_sum_optimized(n, x)
        
        # Вывод результатов
        print(f"\nРезультат вычисления суммы:")
        print(f"∑[s=0..10] 1/(s!({n}+s)!) * ({x}/2)^(2s+{n})")
        print(f"= {result1:.12f}")
        
        # Проверка совпадения методов
        diff = abs(result1 - result2)
        if diff < 1e-12:
            print(f"✓ Оба метода дают одинаковый результат")
        else:
            print(f"⚠ Методы дают разные результаты: {diff:.2e}")
        
        # Дополнительная информация
        print("\n" + "=" * 70)
        print("Подробное вычисление каждого члена суммы:")
        print("s    s!      (n+s)!       (x/2)^(2s+n)        член суммы")
        print("-" * 80)
        
        total = 0.0
        for s in range(0, 11):
            s_fact = math.factorial(s)
            n_plus_s_fact = math.factorial(n + s)
            power_val = (x / 2) ** (2 * s + n)
            term = (1 / (s_fact * n_plus_s_fact)) * power_val
            total += term
            
            print(f"{s:2d} {s_fact:8.0f} {n_plus_s_fact:15.0f} {power_val:20.6e} {term:20.6e}")
        
        print("-" * 80)
        print(f"Сумма: {total:54.6e}")
        
        # Анализ результата
        print("\n" + "=" * 70)
        print("Анализ результата:")
        
        # Сравнение с функцией Бесселя
        # Это похоже на модифицированную функцию Бесселя I_n(x), но с конечной суммой
        if x == 0:
            print("При x = 0:")
            if n == 0:
                print("  Сумма = 1 (только s=0 дает ненулевой член: (0/2)^0 / (0!0!) = 1)")
            else:
                print(f"  Сумма = 0 (все члены с s≥0 содержат x^{n} = 0)")
        
        # Показываем наибольший по модулю член
        max_term = 0
        max_value = 0
        for s in range(0, 11):
            term = (1 / (math.factorial(s) * math.factorial(n + s))) * ((x / 2) ** (2 * s + n))
            if abs(term) > abs(max_value):
                max_value = term
                max_term = s
        
        print(f"Наибольший по модулю член: s = {max_term}, значение = {max_value:.6e}")
        
        # Сходимость ряда (оценка остатка)
        if abs(x) > 0:
            # Приближенная оценка следующего члена (s=11)
            next_term = (1 / (math.factorial(11) * math.factorial(n + 11))) * ((x / 2) ** (2 * 11 + n))
            print(f"Следующий член (s=11): {next_term:.6e}")
            print(f"Относительная погрешность от усечения: {abs(next_term/total):.2e}" if total != 0 else "Сумма = 0")
        
        # Связь с математическими функциями
        print("\nМатематическая справка:")
        print("Данная сумма является частичной суммой (до s=10) ряда для")
        print("модифицированной функции Бесселя первого рода I_n(x):")
        print("I_n(x) = ∑[s=0..∞] (1/(s!(n+s)!)) * (x/2)^(2s+n)")
        print(f"Наша сумма — это приближение I_{n}({x}) с 11 членами.")
        
        # Для небольших x можно сравнить с библиотечной функцией
        try:
            import scipy.special
            bessel_in = scipy.special.iv(n, x)
            print(f"\nДля сравнения (используя scipy.special.iv):")
            print(f"I_{n}({x}) = {bessel_in:.12f}")
            print(f"Разность: {abs(result1 - bessel_in):.6e}")
            print(f"Относительная ошибка: {abs((result1 - bessel_in)/bessel_in):.6e}" if bessel_in != 0 else "Бесконечная")
        except ImportError:
            print("\nДля более точного сравнения установите scipy (pip install scipy)")
        
    except ValueError:
        print("Ошибка ввода: проверьте, что введены корректные числа")
    except OverflowError:
        print("Ошибка переполнения: слишком большие значения n или x")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")

if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
