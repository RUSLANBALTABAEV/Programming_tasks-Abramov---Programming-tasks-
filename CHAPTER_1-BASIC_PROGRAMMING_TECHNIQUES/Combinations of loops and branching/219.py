"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
7. Сочетания цикла и разветвления

219. Даны действительные числа а, b (а < b), натуральное число n, функция у = f(x), определенная на отрезке [a, b] . Для значений
аргумента хi = а + ih (i = 0, 1, …, n), h = (b-a)/n вычислить значения функции yi = f(xi) (i = 0,1, …,  n),
Вывести хi и уi (i = 0,1, …, n) в виде таблицы из двух колонок. В i-ю строку таблицу заносятся соответствующие значения xi и yi. 
Рассмотреть следующие функции:
а) y = sin(x) + cos(2 * x), a = -pi, b = pi, n = 50;
б) y = sin(2 * x) + cos(x), a = 0, b = 2 * pi, n = 50;
в) y = sqrt(x * x + 2), a = -1, b = 2, n = 30;
г) y = x * abs(x + 1), a = -1, b = 2, n = 30;
д) y = x * e ^ x, a = -1; b = 3, n = 40.
"""


import math

def print_table(f, a, b, n, func_name):
    """Выводит таблицу значений функции"""
    h = (b - a) / n
    
    print(f"\nТаблица значений функции: {func_name}")
    print(f"Интервал: [{a:.4f}, {b:.4f}], n = {n}, шаг h = {h:.6f}")
    print("-" * 50)
    print(f"{'i':>4} | {'x_i':>12} | {'y_i':>12}")
    print("-" * 50)
    
    for i in range(n + 1):
        x_i = a + i * h
        try:
            y_i = f(x_i)
            print(f"{i:4d} | {x_i:12.6f} | {y_i:12.6f}")
        except ValueError as e:
            print(f"{i:4d} | {x_i:12.6f} | {'не опред.':>12}")
        except Exception as e:
            print(f"{i:4d} | {x_i:12.6f} | {'ошибка':>12}")
    
    print("-" * 50)

def main():
    print("Вычисление таблицы значений функции y = f(x)")
    print("1. y = sin(x) + cos(2x), a=-π, b=π, n=50")
    print("2. y = sin(√(2x)) + cos(x), a=0, b=2π, n=50")
    print("3. y = √(x² + 2), a=-3, b=5, n=40")
    print("4. y = √(x + 1), a=-1, b=2, n=30")
    print("5. y = x·e^(-x), a=-1, b=3, n=40")
    print("6. Все функции")
    
    choice = int(input("\nВыберите функцию (1-6): "))
    
    if choice == 1:
        def f(x): return math.sin(x) + math.cos(2*x)
        print_table(f, -math.pi, math.pi, 50, "y = sin(x) + cos(2x)")
    
    elif choice == 2:
        def f(x): return math.sin(math.sqrt(2*x)) + math.cos(x)
        print_table(f, 0, 2*math.pi, 50, "y = sin(√(2x)) + cos(x)")
    
    elif choice == 3:
        def f(x): return math.sqrt(x**2 + 2)
        print_table(f, -3, 5, 40, "y = √(x² + 2)")
    
    elif choice == 4:
        def f(x): return math.sqrt(x + 1)
        print_table(f, -1, 2, 30, "y = √(x + 1)")
    
    elif choice == 5:
        def f(x): return x * math.exp(-x)
        print_table(f, -1, 3, 40, "y = x·e^(-x)")
    
    elif choice == 6:
        # Все функции
        functions = [
            (lambda x: math.sin(x) + math.cos(2*x), 
             -math.pi, math.pi, 50, "y = sin(x) + cos(2x)"),
            (lambda x: math.sin(math.sqrt(2*x)) + math.cos(x), 
             0, 2*math.pi, 50, "y = sin(√(2x)) + cos(x)"),
            (lambda x: math.sqrt(x**2 + 2), 
             -3, 5, 40, "y = √(x² + 2)"),
            (lambda x: math.sqrt(x + 1), 
             -1, 2, 30, "y = √(x + 1)"),
            (lambda x: x * math.exp(-x), 
             -1, 3, 40, "y = x·e^(-x)")
        ]
        
        for f, a, b, n, name in functions:
            print_table(f, a, b, n, name)
            input("\nНажмите Enter для продолжения...")

if __name__ == "__main__":
    main()
