"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
7. Сочетания цикла и разветвления

225. Дано натуральное число n. Получить все такие натуральные q, что n делится на q^2 и не делится на q^3.
"""


import math

def get_q_numbers_bruteforce(n):
    """Решение перебором (простой метод)"""
    result = []
    max_q = int(math.isqrt(n))  # максимальное q: q^2 <= n
    
    for q in range(1, max_q + 1):
        if n % (q * q) == 0 and n % (q * q * q) != 0:
            result.append(q)
    
    return result

def get_q_numbers_factorization(n):
    """Решение через разложение на простые множители (эффективный метод)"""
    # Функция для разложения числа на простые множители
    def factorize(num):
        factors = {}
        d = 2
        while d * d <= num:
            while num % d == 0:
                factors[d] = factors.get(d, 0) + 1
                num //= d
            d += 1 if d == 2 else 2  # пропускаем четные после 2
        if num > 1:
            factors[num] = factors.get(num, 0) + 1
        return factors
    
    # Разложение n на простые множители
    factors = factorize(n)
    
    # Если n=1, то результат пустой
    if not factors:
        return []
    
    # Получаем списки простых чисел и их степеней
    primes = list(factors.keys())
    exponents = list(factors.values())
    k = len(primes)
    
    # Максимальные значения a_i (показателей в q)
    max_a = [e // 2 for e in exponents]  # т.к. q^2 делит n => 2a_i ≤ e_i => a_i ≤ e_i/2
    
    result = []
    
    # Рекурсивная функция для перебора всех возможных q
    def generate_q(index, current_q, current_a):
        if index == k:
            # Проверяем условие: существует ли i, такое что 3*a_i > e_i
            condition_met = any(3 * current_a[i] > exponents[i] for i in range(k))
            if condition_met:
                result.append(current_q)
            return
        
        prime = primes[index]
        max_a_i = max_a[index]
        
        # Перебираем все возможные a_i от 0 до max_a_i
        for a in range(max_a_i + 1):
            # Вычисляем новый q
            new_q = current_q * (prime ** a)
            # Создаем копию списка current_a с добавлением a
            new_a = current_a[:]
            new_a.append(a)
            # Рекурсивный вызов для следующего простого числа
            generate_q(index + 1, new_q, new_a)
    
    # Начинаем рекурсию
    generate_q(0, 1, [])
    
    # Удаляем q=1 (если он есть), т.к. для него условие не выполняется
    if 1 in result:
        result.remove(1)
    
    # Сортируем результат
    result.sort()
    return result

def main():
    print("225. Поиск всех натуральных q, таких что n делится на q² и не делится на q³")
    print("=" * 70)
    
    try:
        n = int(input("Введите натуральное число n: "))
        
        if n <= 0:
            print("Ошибка: число должно быть натуральным (n > 0)")
            return
        
        print(f"\nЧисло n = {n}")
        
        # Выбираем метод в зависимости от размера n
        if n <= 10**12:  # Для чисел до 10^12 используем разложение на множители
            print("Используется метод разложения на простые множители...")
            q_numbers = get_q_numbers_factorization(n)
        else:
            print("Число очень большое, используется метод перебора...")
            q_numbers = get_q_numbers_bruteforce(n)
        
        # Вывод результатов
        print(f"\nНайдено чисел q: {len(q_numbers)}")
        
        if len(q_numbers) > 0:
            print(f"Числа q: {q_numbers}")
            
            # Проверка результатов (для отладки)
            print("\nПроверка результатов:")
            for q in q_numbers:
                print(f"  q={q}: n/(q²)={n//(q*q)}, n/(q³)={n/(q*q*q) if n % (q*q*q) != 0 else 'делится'}")
        else:
            print("Таких чисел q не существует")
        
        # Дополнительная информация
        print("\n" + "="*70)
        print("Дополнительная информация:")
        
        # Разложение на множители (если число не слишком большое)
        if n <= 10**9:
            # Простое разложение
            temp_n = n
            factors = {}
            d = 2
            while d * d <= temp_n:
                while temp_n % d == 0:
                    factors[d] = factors.get(d, 0) + 1
                    temp_n //= d
                d += 1 if d == 2 else 2
            if temp_n > 1:
                factors[temp_n] = factors.get(temp_n, 0) + 1
            
            if factors:
                factorization_str = " × ".join([f"{p}^{e}" if e > 1 else str(p) for p, e in sorted(factors.items())])
                print(f"Разложение на множители: n = {factorization_str}")
                
                # Объяснение условий
                print("\nУсловия для q:")
                print("1. q² делит n: для каждого простого p в q, 2·(степень p в q) ≤ (степень p в n)")
                print("2. q³ не делит n: существует простое p, для которого 3·(степень p в q) > (степень p в n)")
        
    except ValueError:
        print("Ошибка: введите целое натуральное число")

if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
