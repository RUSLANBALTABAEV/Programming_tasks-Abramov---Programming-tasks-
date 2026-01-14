"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
6. Пошаговый ввод данных и вывод результатов *)

139. Дано натуральное число n. Получить последовательность b1, ..., bn, где при i = 1,2, ..., n значение bi равно: 

а) i;                       б) i^2;
в) i!;                      г) 2^i+1;
д) 2^i + 3^i+1;             е) 2^i / i!;
ж) 1 + 1 / 2 + ... + 1 / i; з) 1 - 1 / 2 + ... + ((-1)^i+1) / i;
и) i * (1 / 1! + 1 / 2! + ... + 1 / i!).
"""


import math

def main():
    print("Программа вычисления последовательностей b1, ..., bn по заданным формулам")
    
    # Ввод натурального числа n
    n = int(input("Введите натуральное число n: "))
    
    # Инициализация переменных для накопления результатов
    print("\nРезультаты вычислений:")
    print("=" * 80)
    
    # а) bi = i
    print("\nа) bi = i")
    print("   Последовательность:", end=" ")
    for i in range(1, n + 1):
        print(i, end=", " if i < n else "")
    
    # б) bi = i^2
    print("\n\nб) bi = i^2")
    print("   Последовательность:", end=" ")
    for i in range(1, n + 1):
        print(i ** 2, end=", " if i < n else "")
    
    # в) bi = i!
    print("\n\nв) bi = i!")
    print("   Последовательность:", end=" ")
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        print(factorial, end=", " if i < n else "")
    
    # г) bi = 2^(i+1)
    print("\n\nг) bi = 2^(i+1)")
    print("   Последовательность:", end=" ")
    for i in range(1, n + 1):
        print(2 ** (i + 1), end=", " if i < n else "")
    
    # д) bi = 2^i + 3^(i+1)
    print("\n\nд) bi = 2^i + 3^(i+1)")
    print("   Последовательность:", end=" ")
    for i in range(1, n + 1):
        value = (2 ** i) + (3 ** (i + 1))
        print(value, end=", " if i < n else "")
    
    # е) bi = 2^i / i!
    print("\n\nе) bi = 2^i / i!")
    print("   Последовательность:", end=" ")
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        value = (2 ** i) / factorial
        print(f"{value:.6f}", end=", " if i < n else "")
    
    # ж) bi = 1 + 1/2 + ... + 1/i
    print("\n\nж) bi = 1 + 1/2 + ... + 1/i")
    print("   Последовательность:", end=" ")
    harmonic_sum = 0
    for i in range(1, n + 1):
        harmonic_sum += 1 / i
        print(f"{harmonic_sum:.6f}", end=", " if i < n else "")
    
    # з) bi = 1 - 1/2 + ... + (-1)^(i+1)/i
    print("\n\nз) bi = 1 - 1/2 + ... + (-1)^(i+1)/i")
    print("   Последовательность:", end=" ")
    alt_harmonic_sum = 0
    for i in range(1, n + 1):
        sign = 1 if i % 2 == 1 else -1
        alt_harmonic_sum += sign / i
        print(f"{alt_harmonic_sum:.6f}", end=", " if i < n else "")
    
    # и) bi = i * (1/1! + 1/2! + ... + 1/i!)
    print("\n\nи) bi = i * (1/1! + 1/2! + ... + 1/i!)")
    print("   Последовательность:", end=" ")
    factorial = 1
    inv_factorial_sum = 0
    for i in range(1, n + 1):
        factorial *= i
        inv_factorial_sum += 1 / factorial
        value = i * inv_factorial_sum
        print(f"{value:.6f}", end=", " if i < n else "")
    
    # Дополнительно: табличный вывод для удобства сравнения
    print("\n\n" + "=" * 80)
    print("Сводная таблица значений (первые 10 элементов, если n > 10):")
    print("-" * 80)
    
    display_n = min(n, 10)  # Покажем первые 10 элементов для наглядности
    
    # Заголовок таблицы
    print(f"{'i':>3} | {'а) i':>8} | {'б) i^2':>8} | {'в) i!':>12} | {'г) 2^(i+1)':>12} | {'д) 2^i+3^{i+1}':>15}")
    print("-" * 80)
    
    # Восстановим вычисления для таблицы
    factorial = 1
    for i in range(1, display_n + 1):
        # Вычисляем значения для текущего i
        bi_a = i
        bi_b = i ** 2
        factorial *= i
        bi_c = factorial
        bi_d = 2 ** (i + 1)
        bi_e = (2 ** i) + (3 ** (i + 1))
        
        print(f"{i:3} | {bi_a:8} | {bi_b:8} | {bi_c:12} | {bi_d:12} | {bi_e:15}")
    
    print("\n" + "=" * 80)
    print(f"{'i':>3} | {'е) 2^i/i!':>12} | {'ж) гарм.':>10} | {'з) знакопер.':>12} | {'и) i*Σ(1/k!)':>12}")
    print("-" * 80)
    
    # Вторая часть таблицы
    factorial = 1
    harmonic_sum = 0
    alt_harmonic_sum = 0
    inv_factorial_sum = 0
    
    for i in range(1, display_n + 1):
        # Вычисляем значения для текущего i
        factorial *= i
        
        # е) 2^i / i!
        bi_e = (2 ** i) / factorial
        
        # ж) гармоническая сумма
        harmonic_sum += 1 / i
        
        # з) знакопеременная гармоническая сумма
        sign = 1 if i % 2 == 1 else -1
        alt_harmonic_sum += sign / i
        
        # и) i * Σ(1/k!)
        inv_factorial_sum += 1 / factorial
        bi_i = i * inv_factorial_sum
        
        print(f"{i:3} | {bi_e:12.6f} | {harmonic_sum:10.6f} | {alt_harmonic_sum:12.6f} | {bi_i:12.6f}")

if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
