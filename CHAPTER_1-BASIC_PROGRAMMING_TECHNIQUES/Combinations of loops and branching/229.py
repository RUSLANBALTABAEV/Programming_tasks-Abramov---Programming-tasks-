"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
7. Сочетания цикла и разветвления

229. Даны действительные числа x, y (x > 0, y > 1). Получить целое число k (положительное, отрицательное или равное нулю),
удовлетворяющее условию y^k-1 <= x < y ^ k.
"""


import math

def find_k(x, y):
    """Находит целое число k, удовлетворяющее условию y^(k-1) ≤ x < y^k"""
    # Проверяем входные условия
    if x <= 0 or y <= 1:
        raise ValueError("Условия задачи: x > 0, y > 1")
    
    # Метод 1: Использование логарифмов
    # log_y(x) = ln(x)/ln(y)
    log_val = math.log(x) / math.log(y)
    
    # k = floor(log_y(x)) + 1
    k_guess = math.floor(log_val) + 1
    
    # Проверяем k_guess и соседние значения (k_guess-1, k_guess, k_guess+1)
    candidates = [k_guess - 1, k_guess, k_guess + 1]
    
    for k in candidates:
        # Вычисляем y^(k-1) и y^k
        # Для больших k используем более безопасные вычисления
        try:
            y_pow_k_minus_1 = y ** (k - 1)
            y_pow_k = y ** k
        except OverflowError:
            # Если степень слишком большая, используем логарифмическую проверку
            # Для k очень большого: y^(k-1) ≤ x < y^k => (k-1) ≤ log_y(x) < k
            log_x = math.log(x)
            log_y = math.log(y)
            left_cond = (k - 1) * log_y <= log_x
            right_cond = log_x < k * log_y
            if left_cond and right_cond:
                return k
            continue
        
        # Проверяем условие
        if y_pow_k_minus_1 <= x < y_pow_k:
            return k
    
    # Если не нашли среди кандидатов, используем более широкий поиск
    # Это может произойти из-за ошибок округления
    k = k_guess
    while True:
        y_pow_k_minus_1 = y ** (k - 1)
        y_pow_k = y ** k
        if y_pow_k_minus_1 <= x < y_pow_k:
            return k
        elif x < y_pow_k_minus_1:
            k -= 1  # x слишком маленький, уменьшаем k
        else:
            k += 1  # x слишком большой, увеличиваем k

def main():
    print("229. Поиск целого числа k такого, что y^(k-1) ≤ x < y^k")
    print("=" * 60)
    
    try:
        # Ввод данных
        x = float(input("Введите действительное число x (x > 0): "))
        y = float(input("Введите действительное число y (y > 1): "))
        
        if x <= 0 or y <= 1:
            print("Ошибка: должны выполняться условия x > 0, y > 1")
            return
        
        # Находим k
        k = find_k(x, y)
        
        # Вывод результатов
        print(f"\nДано: x = {x}, y = {y}")
        print(f"Найдено k = {k}")
        
        # Проверяем условие
        y_pow_k_minus_1 = y ** (k - 1)
        y_pow_k = y ** k
        
        print(f"\nПроверка условия:")
        print(f"y^(k-1) = {y}^{({k-1})} = {y_pow_k_minus_1}")
        print(f"y^k = {y}^{k} = {y_pow_k}")
        print(f"\n{y_pow_k_minus_1} ≤ {x} < {y_pow_k}")
        
        # Проверка истинности утверждений
        left_ok = y_pow_k_minus_1 <= x
        right_ok = x < y_pow_k
        
        if left_ok and right_ok:
            print("✓ Условие выполняется!")
        else:
            print("✗ Условие НЕ выполняется!")
            print(f"  Левое неравенство: {y_pow_k_minus_1} ≤ {x} = {left_ok}")
            print(f"  Правое неравенство: {x} < {y_pow_k} = {right_ok}")
        
        # Дополнительная информация
        print("\n" + "=" * 60)
        print("Дополнительная информация:")
        
        # Вычисляем логарифм
        log_y_x = math.log(x) / math.log(y)
        print(f"log_y(x) = log_{y}({x}) = {log_y_x:.6f}")
        print(f"floor(log_y(x)) = {math.floor(log_y_x)}")
        print(f"ceil(log_y(x)) = {math.ceil(log_y_x)}")
        
        # Показываем соседние значения k
        print(f"\nПроверка соседних значений:")
        for test_k in [k-1, k, k+1]:
            if test_k != k:
                y_pow_km1 = y ** (test_k - 1)
                y_pow_k_test = y ** test_k
                left_cond = y_pow_km1 <= x
                right_cond = x < y_pow_k_test
                cond_ok = left_cond and right_cond
                symbol = "✓" if cond_ok else "✗"
                print(f"  k = {test_k:3d}: {y_pow_km1:.6f} ≤ {x} < {y_pow_k_test:.6f} {symbol}")
        
        # Объяснение результата
        print(f"\nИнтерпретация:")
        print(f"k = {k} означает, что x находится между {y}^{k-1} и {y}^{k}")
        if k > 0:
            print(f"Это {k}-й интервал вида [{y}^{k-1}, {y}^{k}) на положительной полуоси")
        elif k == 0:
            print(f"x находится в интервале [{y}^{-1}, 1) = [{1/y}, 1)")
        else:
            print(f"x находится в интервале [{y}^{k-1}, {y}^{k}) = [{y**(k-1)}, {y**k})")
        
    except ValueError as e:
        print(f"Ошибка ввода: {e}")
    except OverflowError:
        print("Ошибка: переполнение при вычислении степени. Попробуйте меньшие значения.")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")

if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
