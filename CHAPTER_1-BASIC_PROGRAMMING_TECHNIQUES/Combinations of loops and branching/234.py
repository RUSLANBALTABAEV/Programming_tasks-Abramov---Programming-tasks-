"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
7. Сочетания цикла и разветвления

234. Дано натуральное число n, действительные числа x1, …, xn.
Получить в порядке следования все xk, удовлетворяющие неравенствам
xk > x1, xk > x2, ..., xk > xk-1.
"""


def main():
    print("234. Поиск элементов, больших всех предыдущих")
    print("=" * 60)
    
    try:
        # Ввод натурального числа n
        n = int(input("Введите натуральное число n: "))
        
        if n <= 0:
            print("Ошибка: n должно быть натуральным числом (n > 0)")
            return
        
        # Ввод последовательности из n действительных чисел
        print(f"Введите {n} действительных чисел через пробел:")
        numbers = list(map(float, input().split()))
        
        if len(numbers) != n:
            print(f"Ошибка: введено {len(numbers)} чисел вместо {n}")
            return
        
        print(f"\nИсходная последовательность:")
        for i, x in enumerate(numbers, 1):
            print(f"  x{i} = {x}")
        
        # Поиск элементов, удовлетворяющих условию
        result = []
        
        # Первый элемент всегда включается (нет предыдущих для сравнения)
        if n > 0:
            result.append((1, numbers[0]))
        
        # Проверяем остальные элементы
        for k in range(2, n + 1):  # k от 2 до n
            current = numbers[k-1]
            is_greater = True
            
            # Проверяем, что x_k > x_i для всех i = 1..(k-1)
            for i in range(0, k-1):  # индексы от 0 до k-2
                if current <= numbers[i]:
                    is_greater = False
                    break
            
            if is_greater:
                result.append((k, current))
        
        # Вывод результатов
        print(f"\nНайдено элементов: {len(result)}")
        print("Элементы, которые больше всех предыдущих:")
        
        if len(result) > 0:
            print(" k   x_k")
            print("-" * 20)
            for k, value in result:
                print(f"{k:2d}   {value:.6f}")
        
        # Дополнительный анализ
        print("\n" + "=" * 60)
        print("Подробный анализ для каждого элемента:")
        
        for k in range(1, n + 1):
            current = numbers[k-1]
            comparisons = []
            
            if k == 1:
                print(f"k = {k}: x1 = {current:.6f} - нет предыдущих элементов (включается)")
            else:
                is_greater = True
                for i in range(1, k):
                    comparison = current > numbers[i-1]
                    comparisons.append(comparison)
                    
                    if not comparison:
                        is_greater = False
                
                status = "✓ Включается" if is_greater else "✗ Не включается"
                comparisons_str = ", ".join([f"x{k} > x{i} = {comp}" for i, comp in enumerate(comparisons, 1)])
                print(f"k = {k}: x{k} = {current:.6f}, {comparisons_str} → {status}")
        
        # Графическая визуализация
        print("\n" + "=" * 60)
        print("Визуализация последовательности и рекордных элементов:")
        
        if n > 0:
            # Находим минимальное и максимальное значение для масштабирования
            min_val = min(numbers)
            max_val = max(numbers)
            span = max_val - min_val if max_val != min_val else 1
            
            # Ширина графика
            width = 50
            
            print("Индекс: ", end="")
            for i in range(1, n+1):
                print(f"{i:3d}", end=" ")
            print()
            
            print("Значение:", end="")
            for x in numbers:
                print(f"{x:6.2f}", end=" ")
            print()
            
            print("График:  ", end="")
            for i, x in enumerate(numbers):
                # Масштабируем значение для отображения
                pos = int((x - min_val) / span * (width-1))
                marker = "*" if (i+1, x) in result else "·"
                print(" " * pos + marker, end="")
                # После печати маркера нужно вернуться к правильной позиции
                # Проще построить по-другому
            print()
            
            # Альтернативная визуализация
            print("\nАльтернативная визуализация:")
            for i, x in enumerate(numbers, 1):
                is_record = (i, x) in result
                marker = "← рекорд" if is_record else ""
                print(f"  x{i} = {x:.4f} {marker}")
        
        # Статистика
        print("\n" + "=" * 60)
        print("Статистика:")
        print(f"Всего элементов: {n}")
        print(f"Рекордных элементов: {len(result)} ({len(result)/n*100:.1f}%)")
        
        if len(result) > 1:
            print(f"Первый рекорд: x{result[0][0]} = {result[0][1]:.4f}")
            print(f"Последний рекорд: x{result[-1][0]} = {result[-1][1]:.4f}")
            
            # Разности между последовательными рекордами
            if len(result) > 1:
                print("\nРазности между последовательными рекордами:")
                for j in range(1, len(result)):
                    k1, val1 = result[j-1]
                    k2, val2 = result[j]
                    diff = val2 - val1
                    print(f"  x{k2} - x{k1} = {val2:.4f} - {val1:.4f} = {diff:.4f}")
        
    except ValueError:
        print("Ошибка ввода: проверьте, что введены корректные числа")

if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
