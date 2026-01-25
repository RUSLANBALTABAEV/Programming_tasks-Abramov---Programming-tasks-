"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
7. Сочетания цикла и разветвления

224. Дано натуральное число n. Получить все его натуральные делители.
"""


import math

def get_all_divisors(n):
    """Возвращает список всех натуральных делителей числа n"""
    if n <= 0:
        return []
    
    # Списки для малых и больших делителей
    small_divisors = []
    large_divisors = []
    
    # Проверяем делители до квадратного корня из n
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            small_divisors.append(i)
            # Добавляем парный делитель (если он не совпадает с текущим)
            if i != n // i:
                large_divisors.append(n // i)
    
    # Объединяем списки: малые делители + большие делители в обратном порядке
    return small_divisors + large_divisors[::-1]

def main():
    print("224. Поиск всех натуральных делителей числа")
    print("=" * 50)
    
    # Ввод натурального числа
    try:
        n = int(input("Введите натуральное число n: "))
        
        if n <= 0:
            print("Ошибка: число должно быть натуральным (n > 0)")
            return
        
        # Получаем все делители
        divisors = get_all_divisors(n)
        
        # Вывод результатов
        print(f"\nНатуральные делители числа {n}:")
        print(f"Количество делителей: {len(divisors)}")
        print(f"Делители в порядке возрастания: {divisors}")
        
        # Вывод в виде таблицы (по 10 чисел в строке)
        print("\nВывод в виде таблицы:")
        for i in range(0, len(divisors), 10):
            row = divisors[i:i+10]
            print(" ".join(f"{d:4d}" for d in row))
        
        # Проверка, является ли число простым
        if len(divisors) == 2:
            print(f"\nЧисло {n} является простым")
        else:
            print(f"\nЧисло {n} является составным")
            print(f"Наименьший делитель (кроме 1): {min(d for d in divisors if d != 1)}")
            print(f"Наибольший делитель (кроме самого числа): {max(d for d in divisors if d != n)}")
    
    except ValueError:
        print("Ошибка: введите целое натуральное число")

if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
