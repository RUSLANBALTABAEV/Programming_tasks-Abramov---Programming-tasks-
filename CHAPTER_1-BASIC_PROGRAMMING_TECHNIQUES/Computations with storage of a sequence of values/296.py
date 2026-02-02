"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
9. Вычисления с хранением последовательности значений

296. Даны действительные числа a1, …, a20 (все числа попарно различны). Поменять в этой последовательности местами:
а) наибольший и наименьший члены;
б) наибольший и последний члены.
"""


import random

def main():
    print("Программа для работы с последовательностью из 20 попарно различных действительных чисел.")
    print("Выберите задачу:")
    print("a) Поменять местами наибольший и наименьший члены")
    print("b) Поменять местами наибольший и последний члены")
    
    while True:
        task = input("\nВыберите задачу (a или b): ").lower()
        if task in ['a', 'b']:
            break
        else:
            print("Ошибка: введите 'a' или 'b'.")
    
    # Выбор способа ввода данных
    print("\nВыберите способ задания последовательности:")
    print("1. Ввести числа вручную")
    print("2. Использовать случайные различные числа от -100 до 100")
    print("3. Использовать готовый набор: 1, 2, 3, ..., 20")
    print("4. Использовать готовый набор: 20, 19, ..., 1")
    print("5. Использовать готовый набор: случайные, но различные числа")
    
    while True:
        try:
            choice = int(input("\nВаш выбор (1-5): "))
            if 1 <= choice <= 5:
                break
            else:
                print("Ошибка: выберите число от 1 до 5.")
        except ValueError:
            print("Ошибка: введите целое число от 1 до 5.")
    
    n = 20  # количество элементов по условию
    
    # Инициализация последовательности в зависимости от выбора
    if choice == 1:
        # Ручной ввод
        print(f"\nВведите {n} попарно различных действительных чисел:")
        a = []
        for i in range(n):
            while True:
                try:
                    value = float(input(f"a_{i+1}: "))
                    if value in a:
                        print("Ошибка: числа должны быть различными!")
                    else:
                        a.append(value)
                        break
                except ValueError:
                    print("Ошибка: введите действительное число.")
    
    elif choice == 2:
        # Случайные числа от -100 до 100, гарантируем уникальность
        random.seed()
        # Генерируем больше чисел, чтобы точно набрать 20 уникальных
        possible_values = list(range(-100, 101))  # целые для простоты
        random.shuffle(possible_values)
        a = [float(possible_values[i]) for i in range(n)]
        print(f"\nИспользуется набор из {n} случайных различных чисел от -100 до 100")
    
    elif choice == 3:
        # Готовый набор: 1, 2, 3, ..., 20
        a = [float(i) for i in range(1, n+1)]
        print("\nИспользуется готовый набор: 1, 2, 3, ..., 20")
    
    elif choice == 4:
        # Готовый набор: 20, 19, ..., 1
        a = [float(i) for i in range(n, 0, -1)]
        print("\nИспользуется готовый набор: 20, 19, ..., 1")
    
    elif choice == 5:
        # Готовый набор: случайные, но различные числа
        random.seed()
        a = random.sample(range(-50, 51), n)  # 20 различных чисел
        a = [float(x) for x in a]
        print("\nИспользуется набор случайных различных чисел от -50 до 50")
    
    # Создаем копию для вывода исходной последовательности
    original = a.copy()
    
    # Вывод исходной последовательности
    print("\nИсходная последовательность:")
    for i in range(n):
        if i % 5 == 0 and i != 0:
            print()
        print(f"a_{i+1:2} = {a[i]:7.3f}", end=" | ")
    print()
    
    # Находим индексы минимального и максимального элементов
    min_val = min(a)
    max_val = max(a)
    min_index = a.index(min_val)
    max_index = a.index(max_val)
    
    print(f"\nМинимальный элемент: a_{min_index + 1} = {min_val:.3f}")
    print(f"Максимальный элемент: a_{max_index + 1} = {max_val:.3f}")
    print(f"Последний элемент: a_{n} = {a[-1]:.3f}")
    
    # Выполняем задачу a или b
    if task == 'a':
        # Задача a: меняем местами наибольший и наименьший
        print("\nВыполняем задачу a: меняем местами наибольший и наименьший элементы")
        a[min_index], a[max_index] = a[max_index], a[min_index]
        
        print("\nПосле замены наибольшего и наименьшего:")
        for i in range(n):
            if i % 5 == 0 and i != 0:
                print()
            marker = ""
            if i == min_index:
                marker = f" (был мин={original[min_index]:.3f})"
            elif i == max_index:
                marker = f" (был макс={original[max_index]:.3f})"
            print(f"a_{i+1:2} = {a[i]:7.3f}{marker}", end=" | ")
        print()
        
    elif task == 'b':
        # Задача b: меняем местами наибольший и последний
        print("\nВыполняем задачу b: меняем местами наибольший и последний элементы")
        
        # Сохраняем значения
        last_index = n - 1
        last_val = a[last_index]
        max_val = a[max_index]
        
        # Меняем местами
        a[last_index], a[max_index] = a[max_index], a[last_index]
        
        print("\nПосле замены наибольшего и последнего:")
        for i in range(n):
            if i % 5 == 0 and i != 0:
                print()
            marker = ""
            if i == max_index:
                marker = f" (был макс={original[max_index]:.3f}, теперь={a[max_index]:.3f})"
            elif i == last_index:
                marker = f" (был последний={original[last_index]:.3f}, теперь={a[last_index]:.3f})"
            print(f"a_{i+1:2} = {a[i]:7.3f}{marker}", end=" | ")
        print()
    
    # Дополнительная информация
    print("\n" + "="*60)
    print("Сводка изменений:")
    print(f"Задача: {task}")
    print(f"Способ ввода: {choice}")
    
    if task == 'a':
        print(f"Минимальный элемент (исходный): a_{min_index + 1} = {original[min_index]:.3f}")
        print(f"Максимальный элемент (исходный): a_{max_index + 1} = {original[max_index]:.3f}")
        print(f"После замены: a_{min_index + 1} = {a[min_index]:.3f}, a_{max_index + 1} = {a[max_index]:.3f}")
        
        # Проверка, что замена произошла корректно
        new_min = min(a)
        new_max = max(a)
        print(f"\nНовый минимальный элемент: {new_min:.3f}")
        print(f"Новый максимальный элемент: {new_max:.3f}")
        
    elif task == 'b':
        print(f"Максимальный элемент (исходный): a_{max_index + 1} = {original[max_index]:.3f}")
        print(f"Последний элемент (исходный): a_{n} = {original[-1]:.3f}")
        print(f"После замены: a_{max_index + 1} = {a[max_index]:.3f}, a_{n} = {a[-1]:.3f}")
        
        # Проверка
        print(f"\nНовый максимальный элемент: {max(a):.3f}")
        print(f"Новый последний элемент: a_{n} = {a[-1]:.3f}")

if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
