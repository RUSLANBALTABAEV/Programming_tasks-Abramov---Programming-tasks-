"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
7. Сочетания цикла и разветвления

227. Даны целые числа m, n (m≠ 0, n≠ 0). Получить все их общие делители (положительные и отрицательные).
"""


import math

def find_common_divisors(m, n):
    """Находит все общие делители (положительные и отрицательные) чисел m и n"""
    # Используем абсолютные значения для поиска делителей
    abs_m = abs(m)
    abs_n = abs(n)
    
    # Находим НОД
    g = math.gcd(abs_m, abs_n)
    
    # Если НОД = 0 (не должно случиться по условию), возвращаем пустой список
    if g == 0:
        return []
    
    # Находим все положительные делители g
    positive_divisors = []
    
    # Проверяем делители от 1 до sqrt(g)
    for i in range(1, int(math.sqrt(g)) + 1):
        if g % i == 0:
            positive_divisors.append(i)
            # Добавляем парный делитель, если он не совпадает
            if i != g // i:
                positive_divisors.append(g // i)
    
    # Сортируем положительные делители
    positive_divisors.sort()
    
    # Создаем список всех делителей (положительных и отрицательных)
    all_divisors = []
    for d in positive_divisors:
        all_divisors.append(d)
        all_divisors.append(-d)
    
    # Сортируем по возрастанию
    all_divisors.sort()
    
    return all_divisors, g

def main():
    print("227. Поиск всех общих делителей (положительных и отрицательных)")
    print("=" * 70)
    
    try:
        # Ввод чисел m и n
        m = int(input("Введите целое число m (m ≠ 0): "))
        n = int(input("Введите целое число n (n ≠ 0): "))
        
        if m == 0 or n == 0:
            print("Ошибка: числа не должны быть равны 0")
            return
        
        print(f"\nДаны числа: m = {m}, n = {n}")
        print(f"Абсолютные значения: |m| = {abs(m)}, |n| = {abs(n)}")
        
        # Поиск общих делителей
        divisors, gcd_val = find_common_divisors(m, n)
        
        # Вывод результатов
        print(f"\nНОД(|m|, |n|) = НОД({abs(m)}, {abs(n)}) = {gcd_val}")
        
        # Положительные делители НОД
        positive_divisors = [d for d in divisors if d > 0]
        print(f"Положительные делители НОД: {sorted(positive_divisors)}")
        
        print(f"\nВсего общих делителей: {len(divisors)}")
        print(f"Все общие делители (положительные и отрицательные):")
        
        # Вывод в виде таблицы
        cols = 8  # Количество столбцов в таблице
        for i in range(0, len(divisors), cols):
            row = divisors[i:i+cols]
            print(" ".join(f"{d:6d}" for d in row))
        
        # Проверка делимости
        print("\nПроверка (первые 5 положительных делителей):")
        count = 0
        for d in divisors:
            if d > 0 and count < 5:
                print(f"  {d}: {m} % {d} = {m % d}, {n} % {d} = {n % d}")
                count += 1
        
        # Дополнительная информация
        print("\n" + "=" * 70)
        print("Математическая справка:")
        print(f"1. НОД({m}, {n}) = НОД(|{m}|, |{n}|) = {gcd_val}")
        print(f"2. Каждый делитель d числа {gcd_val} является общим делителем {m} и {n}")
        print("3. Если d делит НОД, то d делит и m, и n")
        print("4. Поэтому множество всех общих делителей равно множеству всех делителей НОД,")
        print("   взятых со знаком '+' и '-'")
        
        # Отношение порядка
        if len(divisors) > 0:
            print(f"\nОтношение порядка делителей:")
            print(f"Наименьший положительный делитель: {min(d for d in divisors if d > 0)}")
            print(f"Наибольший положительный делитель: {max(d for d in divisors if d > 0)}")
            print(f"Наименьший делитель: {min(divisors)}")
            print(f"Наибольший делитель: {max(divisors)}")
            
    except ValueError:
        print("Ошибка: введите целые числа")

if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
