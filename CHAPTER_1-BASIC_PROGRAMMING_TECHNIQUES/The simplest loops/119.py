"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
4. Простейшие циклы


119. Вычислить бесконечную сумму с заданной точностью ε(ε >
0). Считать что требуемая точность достигнута, если несколько первых
слагаемых и очередное слагаемое оказалось по модулю меньше, чем ε,
это и все последующие слагаемые можно уже не учитывать.
Вычислить:

"""


import math


def main():
    # Ввод точности ε
    eps = float(input("Введите точность ε (> 0): "))
    
    if eps <= 0:
        print("Ошибка: ε должно быть положительным числом")
        return
    
    print(f"\nВычисление бесконечных сумм с точностью ε = {eps}\n")
    
    # a) Сумма от i=1 до ∞: 1/i^2
    print("а) Σ(i=1..∞) 1/i²:")
    sum_a = 0.0
    i = 1
    term = 1.0  # текущее слагаемое
    
    while True:
        term = 1.0 / (i * i)
        sum_a += term
        i += 1
        
        # Проверяем условие остановки
        if term < eps:
            # Проверяем несколько следующих слагаемых
            next_terms_small = True
            for check_i in range(i, min(i + 3, i + 10)):  # проверяем 3 следующих слагаемых
                if 1.0 / (check_i * check_i) >= eps:
                    next_terms_small = False
                    break
            
            if next_terms_small:
                break
    
    print(f"   Сумма: {sum_a}")
    print(f"   Количество просуммированных слагаемых: {i-1}")
    print(f"   Известное предельное значение: π²/6 ≈ {math.pi**2/6}")
    
    # b) Сумма от i=1 до ∞: 1/(i(i+1))
    print("\nб) Σ(i=1..∞) 1/(i(i+1)):")
    sum_b = 0.0
    i = 1
    term = 1.0
    
    while True:
        term = 1.0 / (i * (i + 1))
        sum_b += term
        i += 1
        
        # Проверяем условие остановки
        if term < eps:
            # Проверяем несколько следующих слагаемых
            next_terms_small = True
            for check_i in range(i, min(i + 3, i + 10)):
                if 1.0 / (check_i * (check_i + 1)) >= eps:
                    next_terms_small = False
                    break
            
            if next_terms_small:
                break
    
    print(f"   Сумма: {sum_b}")
    print(f"   Количество просуммированных слагаемых: {i-1}")
    print(f"   Известное предельное значение: 1")
    
    # c) Сумма от i=0 до ∞: (-2)^i / i!
    print("\nв) Σ(i=0..∞) (-2)^i / i!:")
    sum_c = 0.0
    i = 0
    term = 1.0
    factorial = 1  # для вычисления факториала итерационно
    
    while True:
        # Вычисляем (-2)^i
        sign = 1 if i % 2 == 0 else -1
        power_of_2 = 2 ** i
        term = sign * power_of_2 / factorial
        
        sum_c += term
        i += 1
        
        # Обновляем факториал для следующей итерации
        factorial *= i
        
        # Проверяем условие остановки
        if abs(term) < eps:
            # Проверяем несколько следующих слагаемых
            next_terms_small = True
            next_factorial = factorial
            for check_i in range(i, min(i + 3, i + 10)):
                next_sign = 1 if check_i % 2 == 0 else -1
                next_power = 2 ** check_i
                next_term = abs(next_sign * next_power / next_factorial)
                if next_term >= eps:
                    next_terms_small = False
                    break
                next_factorial *= (check_i + 1)
            
            if next_terms_small:
                break
    
    print(f"   Сумма: {sum_c}")
    print(f"   Количество просуммированных слагаемых: {i}")
    print(f"   Известное предельное значение: e^(-2) ≈ {math.exp(-2)}")
    
    # d) Сумма от i=1 до ∞: (-1)^(i+1) / (i(i+1)(i+2))
    print("\nг) Σ(i=1..∞) (-1)^(i+1) / (i(i+1)(i+2)):")
    sum_d = 0.0
    i = 1
    
    while True:
        sign = 1 if (i + 1) % 2 == 0 else -1  # (-1)^(i+1)
        term = sign / (i * (i + 1) * (i + 2))
        
        sum_d += term
        i += 1
        
        # Проверяем условие остановки
        if abs(term) < eps:
            # Проверяем несколько следующих слагаемых
            next_terms_small = True
            for check_i in range(i, min(i + 3, i + 10)):
                next_sign = 1 if (check_i + 1) % 2 == 0 else -1
                next_term = abs(next_sign / (check_i * (check_i + 1) * (check_i + 2)))
                if next_term >= eps:
                    next_terms_small = False
                    break
            
            if next_terms_small:
                break
    
    print(f"   Сумма: {sum_d}")
    print(f"   Количество просуммированных слагаемых: {i-1}")
    
    # e) Сумма от i=0 до ∞: 1/(4^i + 5^(i+2))
    print("\nд) Σ(i=0..∞) 1/(4^i + 5^(i+2)):")
    sum_e = 0.0
    i = 0
    
    while True:
        # Вычисляем 4^i и 5^(i+2)
        power_4 = 4 ** i
        power_5 = 5 ** (i + 2)
        term = 1.0 / (power_4 + power_5)
        
        sum_e += term
        i += 1
        
        # Проверяем условие остановки
        if term < eps:
            # Проверяем несколько следующих слагаемых
            next_terms_small = True
            for check_i in range(i, min(i + 3, i + 10)):
                next_power_4 = 4 ** check_i
                next_power_5 = 5 ** (check_i + 2)
                next_term = 1.0 / (next_power_4 + next_power_5)
                if next_term >= eps:
                    next_terms_small = False
                    break
            
            if next_terms_small:
                break
    
    print(f"   Сумма: {sum_e}")
    print(f"   Количество просуммированных слагаемых: {i}")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
