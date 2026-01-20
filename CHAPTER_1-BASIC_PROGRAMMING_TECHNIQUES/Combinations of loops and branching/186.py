"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
7. Сочетания цикла и разветвления

186. Даны натуральное число n, действительные числа a1, ..., an. Вычислить обратную величину произведения тех членов ai последовательности a1, ..., an, для которых выполнено i+1 < ai < i!.
"""


import math

def main():
    # Ввод количества чисел
    n = int(input("Введите натуральное число n: "))
    
    if n <= 0:
        print("Ошибка: n должно быть натуральным числом!")
        return
    
    # Ввод последовательности действительных чисел
    numbers = []
    print(f"Введите {n} действительных чисел:")
    for i in range(n):
        while True:
            try:
                num = float(input(f"a[{i+1}]: "))
                numbers.append(num)
                break
            except ValueError:
                print("Пожалуйста, введите число!")
    
    # Инициализация переменных
    product = 1.0  # начальное значение произведения (по условию)
    found = False  # флаг, что найдены подходящие числа
    
    # Вычисляем факториалы заранее для оптимизации
    factorials = [1]  # 0! = 1
    for i in range(1, n + 1):
        factorials.append(factorials[i-1] * i)
    
    # Проверка условия для каждого числа
    suitable_numbers = []  # список подходящих чисел (для отображения)
    
    for i in range(n):
        a_i = numbers[i]
        i_index = i + 1  # индекс начинается с 1
        
        # Условие: i+1 < a_i < i!
        lower_bound = i_index + 1
        upper_bound = factorials[i_index]
        
        if lower_bound < a_i < upper_bound:
            product *= a_i
            found = True
            suitable_numbers.append((i_index, a_i, lower_bound, upper_bound))
    
    # Вычисление обратной величины
    if found:
        inverse = 1.0 / product
    else:
        inverse = 1.0  # если не найдено подходящих чисел
    
    # Вывод результатов
    print("\nРезультаты:")
    
    if found:
        print("Члены последовательности, удовлетворяющие условию i+1 < a_i < i!:")
        for idx, num, lower, upper in suitable_numbers:
            print(f"  a[{idx}] = {num}, где {lower} < {num} < {upper}")
        
        print(f"\nПроизведение подходящих чисел: {product}")
        print(f"Обратная величина произведения: {inverse}")
    else:
        print("Нет членов последовательности, удовлетворяющих условию i+1 < a_i < i!")
        print(f"Обратная величина произведения (согласно условию): {inverse}")

if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
