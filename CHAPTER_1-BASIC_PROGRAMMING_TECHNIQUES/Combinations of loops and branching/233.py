"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
7. Сочетания цикла и разветвления

233. Дано натуральное число n, целые числа a1, …, an. Оставить 
без изменения последовательность a1, …, an, если ее члены 
упорядочены по неубыванию или по невозрастанию. В противном
случае получить подпоследовательность a1, …, am (m < n), где m
таково, что либо a1 <= a2<=...<= am и am > am+1, либо a1 >= a2 >=...>= am и am < am+1.
"""


def check_sequence(arr):
    """Проверяет последовательность и возвращает подпоследовательность согласно условию"""
    n = len(arr)
    
    # Проверяем, является ли последовательность неубывающей
    is_non_decreasing = all(arr[i] <= arr[i+1] for i in range(n-1))
    
    # Проверяем, является ли последовательность невозрастающей
    is_non_increasing = all(arr[i] >= arr[i+1] for i in range(n-1))
    
    # Если последовательность уже упорядочена
    if is_non_decreasing or is_non_increasing:
        return arr  # Оставляем без изменения
    
    # Иначе ищем m
    # Определяем порядок в начале последовательности
    # Находим первые два различных элемента
    order = None
    for i in range(n-1):
        if arr[i] != arr[i+1]:
            if arr[i] < arr[i+1]:
                order = 'non_decreasing'
            else:
                order = 'non_increasing'
            break
    
    # Если все элементы равны (не должно случиться, т.к. тогда последовательность упорядочена)
    if order is None:
        return arr
    
    # Ищем m согласно порядку
    m = 0
    if order == 'non_decreasing':
        # Ищем первый индекс, где нарушается неубывание
        for i in range(n-1):
            if arr[i] <= arr[i+1]:
                m = i + 1
            else:
                break
    else:  # order == 'non_increasing'
        # Ищем первый индекс, где нарушается невозрастание
        for i in range(n-1):
            if arr[i] >= arr[i+1]:
                m = i + 1
            else:
                break
    
    # Возвращаем подпоследовательность a1,...,am
    return arr[:m+1]

def main():
    print("233. Обработка последовательности целых чисел")
    print("=" * 60)
    
    try:
        # Ввод натурального числа n
        n = int(input("Введите натуральное число n: "))
        
        if n <= 0:
            print("Ошибка: n должно быть натуральным числом (n > 0)")
            return
        
        # Ввод последовательности из n целых чисел
        print(f"Введите {n} целых чисел через пробел:")
        a_input = input()
        a = list(map(int, a_input.split()))
        
        if len(a) != n:
            print(f"Ошибка: введено {len(a)} чисел вместо {n}")
            return
        
        print(f"\nИсходная последовательность: a = {a}")
        
        # Обработка последовательности
        result = check_sequence(a)
        
        # Вывод результатов
        print(f"\nРезультат: {result}")
        
        # Проверяем, изменилась ли последовательность
        if len(result) == n:
            print("Последовательность оставлена без изменения (упорядочена по неубыванию или невозрастанию)")
        else:
            print(f"Получена подпоследовательность длины {len(result)}")
            
            # Проверяем свойства подпоследовательности
            if len(result) > 1:
                # Проверяем, какое свойство выполняется
                is_non_dec = all(result[i] <= result[i+1] for i in range(len(result)-1))
                is_non_inc = all(result[i] >= result[i+1] for i in range(len(result)-1))
                
                if is_non_dec:
                    print(f"Подпоследовательность неубывающая: {result}")
                    if len(result) < n:
                        print(f"Следующий элемент a[{len(result)+1}] = {a[len(result)]}")
                        print(f"Условие нарушения: {result[-1]} > {a[len(result)]}? {result[-1] > a[len(result)]}")
                elif is_non_inc:
                    print(f"Подпоследовательность невозрастающая: {result}")
                    if len(result) < n:
                        print(f"Следующий элемент a[{len(result)+1}] = {a[len(result)]}")
                        print(f"Условие нарушения: {result[-1]} < {a[len(result)]}? {result[-1] < a[len(result)]}")
        
        # Дополнительный анализ
        print("\n" + "=" * 60)
        print("Анализ последовательности:")
        
        # Проверяем упорядоченность всей последовательности
        is_non_decreasing_full = all(a[i] <= a[i+1] for i in range(n-1))
        is_non_increasing_full = all(a[i] >= a[i+1] for i in range(n-1))
        
        if is_non_decreasing_full:
            print("Вся последовательность упорядочена по неубыванию")
        elif is_non_increasing_full:
            print("Вся последовательность упорядочена по невозрастанию")
        else:
            print("Последовательность не упорядочена ни по неубыванию, ни по невозрастанию")
            
            # Находим точку нарушения
            if n > 1:
                # Определяем начальный порядок
                order = None
                for i in range(n-1):
                    if a[i] < a[i+1]:
                        order = 'non_decreasing'
                        break
                    elif a[i] > a[i+1]:
                        order = 'non_increasing'
                        break
                
                if order:
                    print(f"Начальный порядок: {'неубывание' if order == 'non_decreasing' else 'невозрастание'}")
                    
                    # Находим точку нарушения
                    violation_index = 0
                    if order == 'non_decreasing':
                        for i in range(n-1):
                            if a[i] <= a[i+1]:
                                violation_index = i + 1
                            else:
                                break
                    else:
                        for i in range(n-1):
                            if a[i] >= a[i+1]:
                                violation_index = i + 1
                            else:
                                break
                    
                    print(f"Нарушение происходит на позиции {violation_index+1}")
                    if violation_index < n-1:
                        print(f"  a[{violation_index}] = {a[violation_index-1]}")
                        print(f"  a[{violation_index+1}] = {a[violation_index]}")
        
        # Визуализация
        print("\nВизуализация:")
        print("Индексы: ", end="")
        for i in range(1, n+1):
            print(f"{i:3d}", end=" ")
        print()
        
        print("Значения: ", end="")
        for val in a:
            print(f"{val:3d}", end=" ")
        print()
        
        # Отмечаем подпоследовательность
        if len(result) < n:
            print("Выбор:    ", end="")
            for i in range(n):
                if i < len(result):
                    print("  √ ", end="")
                else:
                    print("    ", end="")
            print()
            print(f"          (взято первых {len(result)} элементов)")
        
    except ValueError:
        print("Ошибка ввода: проверьте, что введены корректные целые числа")

if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
