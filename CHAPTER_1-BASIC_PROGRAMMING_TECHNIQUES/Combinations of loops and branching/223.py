"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
7. Сочетания цикла и разветвления

223. Даны целые числа a1, a2, … Известно, что а1 > 0 и что среди а2, a3, … есть хотя бы одно отрицательное число. Пусть а1, …, аn – 
члены данной последовательности, предшествующие первому отрицательному члену (n заранее неизвестно). Получить:
а) max(a1^2, ..., an^2);
б) max(a1^3, ..., an^3);
в) min(a1, 2 * a2, ..., n * an);
г) min(a1 + a2, a2 + a3, ..., an-1+an);
д) max(a1,a1*a2,...a1*a2...an);
е) количество четных среди a1, ..., an;
ж) количество удвоенных нечетных среди a1, ..., an;
з) количество полных квадратов среди a1, ..., an;
и) количество квадратов нечетных среди a1, ..., an.
"""


import math

def is_perfect_square(x):
    """Проверяет, является ли число полным квадратом"""
    if x < 0:
        return False
    root = int(math.sqrt(x))
    return root * root == x

def is_square_of_odd(x):
    """Проверяет, является ли число квадратом нечетного числа"""
    if x < 0:
        return False
    root = int(math.sqrt(x))
    return root * root == x and root % 2 == 1

def is_doubled_odd(x):
    """Проверяет, является ли число удвоенным нечетным"""
    if x % 2 != 0:  # нечетное не может быть удвоенным нечетным
        return False
    half = x // 2
    return half % 2 == 1

def main():
    print("223. Обработка последовательности до первого отрицательного числа")
    print("Введите целые числа (одно число в строке).")
    print("Первое число должно быть положительным, последущие - любые.")
    print("Ввод завершится при вводе отрицательного числа.")
    
    # Чтение последовательности до первого отрицательного числа
    sequence = []
    
    # Читаем первое число (гарантированно положительное)
    try:
        num = int(input("Введите число: "))
        if num <= 0:
            print("Первое число должно быть положительным!")
            return
        sequence.append(num)
    except ValueError:
        print("Ошибка: введите целое число")
        return
    
    # Читаем остальные числа до первого отрицательного
    while True:
        try:
            num = int(input("Введите число: "))
            if num < 0:
                break  # Первое отрицательное - завершаем ввод
            sequence.append(num)
        except ValueError:
            print("Ошибка: введите целое число")
    
    n = len(sequence)
    print(f"\nПолучена последовательность из {n} чисел до первого отрицательного:")
    print(sequence)
    
    if n == 0:
        print("Последовательность пуста!")
        return
    
    # a) max(a1^2, ..., an^2)
    max_square = max(x * x for x in sequence)
    
    # б) max(a1^3, ..., an^3)
    max_cube = max(x * x * x for x in sequence)
    
    # в) min(a1, 2a2, ..., nan)
    min_scaled = min((i + 1) * sequence[i] for i in range(n))
    
    # г) min(a1 + a2, a2 + a3, ..., a_{n-1} + a_n)
    if n >= 2:
        min_pair_sum = min(sequence[i] + sequence[i + 1] for i in range(n - 1))
    else:
        min_pair_sum = "Не определено (нужны хотя бы 2 элемента)"
    
    # д) max(a1, a1*a2, ..., a1*a2*...*an)
    max_product = sequence[0]
    current_product = sequence[0]
    for i in range(1, n):
        current_product *= sequence[i]
        if current_product > max_product:
            max_product = current_product
    
    # е) количество четных среди a1, ..., an
    even_count = sum(1 for x in sequence if x % 2 == 0)
    
    # ж) количество удвоенных нечетных среди a1, ..., an
    doubled_odd_count = sum(1 for x in sequence if is_doubled_odd(x))
    
    # з) количество полных квадратов среди a1, ..., an
    perfect_square_count = sum(1 for x in sequence if is_perfect_square(x))
    
    # и) количество квадратов нечетных среди a1, ..., an
    square_of_odd_count = sum(1 for x in sequence if is_square_of_odd(x))
    
    # Вывод результатов
    print("\n" + "="*60)
    print("РЕЗУЛЬТАТЫ:")
    print("="*60)
    print(f"а) max(a1^2, ..., a{n}^2) = {max_square}")
    print(f"б) max(a1^3, ..., a{n}^3) = {max_cube}")
    print(f"в) min(a1, 2a2, ..., {n}a{n}) = {min_scaled}")
    print(f"г) min(a1+a2, a2+a3, ..., a{n-1}+a{n}) = {min_pair_sum}")
    print(f"д) max(a1, a1*a2, ..., a1*...*a{n}) = {max_product}")
    print(f"е) Количество четных чисел: {even_count}")
    print(f"ж) Количество удвоенных нечетных чисел: {doubled_odd_count}")
    print(f"з) Количество полных квадратов: {perfect_square_count}")
    print(f"и) Количество квадратов нечетных чисел: {square_of_odd_count}")

if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
