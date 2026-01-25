"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
7. Сочетания цикла и разветвления

226. Даны натуральные числа m, n. Получить все их натуральные общие кратные, меньшие mn.
"""


import math

def find_common_multiples(m, n):
    """Находит все натуральные общие кратные m и n, меньшие m·n"""
    # Вычисляем НОД и НОК
    gcd = math.gcd(m, n)  # НОД
    lcm = m * n // gcd    # НОК
    
    # Находим количество общих кратных, меньших m·n
    # Все общие кратные имеют вид: lcm * t, где t = 1, 2, 3, ...
    # Нужно lcm * t < m*n
    # t < (m*n) / lcm = gcd (т.к. m*n = lcm * gcd)
    # Поэтому t = 1, 2, ..., gcd-1
    
    multiples = []
    for t in range(1, gcd):
        multiple = lcm * t
        if multiple < m * n:
            multiples.append(multiple)
    
    return multiples, lcm, gcd

def main():
    print("226. Поиск натуральных общих кратных, меньших m·n")
    print("=" * 60)
    
    try:
        # Ввод чисел m и n
        m = int(input("Введите натуральное число m: "))
        n = int(input("Введите натуральное число n: "))
        
        if m <= 0 or n <= 0:
            print("Ошибка: числа должны быть натуральными (m > 0, n > 0)")
            return
        
        print(f"\nДаны числа: m = {m}, n = {n}")
        print(f"m·n = {m * n}")
        
        # Поиск общих кратных
        multiples, lcm, gcd = find_common_multiples(m, n)
        
        # Вывод результатов
        print(f"\nНОД({m}, {n}) = {gcd}")
        print(f"НОК({m}, {n}) = {lcm}")
        print(f"m·n = {m * n}")
        
        print(f"\nНайдено общих кратных, меньших {m * n}: {len(multiples)}")
        
        if multiples:
            print(f"Общие кратные: {sorted(multiples)}")
            
            # Проверка каждого кратного
            print("\nПроверка кратных:")
            for k in multiples:
                print(f"  {k}: {k} % {m} = {k % m}, {k} % {n} = {k % n}")
        else:
            print(f"Нет натуральных общих кратных, меньших {m * n}")
        
        # Дополнительная информация
        print("\n" + "=" * 60)
        print("Дополнительная информация:")
        print(f"1. Все общие кратные имеют вид: НОК * t, где t ∈ ℕ")
        print(f"2. Для t < НОД({m}, {n}) получаем кратные < {m}·{n}")
        
        if gcd > 1:
            print(f"3. Так как НОД({m}, {n}) = {gcd} > 1, существуют кратные:")
            print(f"   При t = 1: {lcm} * 1 = {lcm}")
            if gcd > 2:
                for t in range(2, gcd):
                    print(f"   При t = {t}: {lcm} * {t} = {lcm * t}")
        else:
            print(f"3. Так как НОД({m}, {n}) = 1, то НОК = {m}·{n} = {m * n}")
            print(f"   Единственное общее кратное, меньшее {m}·{n} должно удовлетворять:")
            print(f"   t < 1, но t натуральное - таких t нет")
            
    except ValueError:
        print("Ошибка: введите целые натуральные числа")

if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
