"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
7. Сочетания цикла и разветвления

230. Даны натуральное число n, действительные числа a1, …, an. 
Найти длину наименьшего отрезка числовой оси, содержащего числа a1, ..., an.
"""


def main():
    print("230. Длина наименьшего отрезка, содержащего все числа")
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
        
        print(f"\nПоследовательность: {numbers}")
        
        # Находим минимальное и максимальное значение
        if n == 1:
            min_val = max_val = numbers[0]
            segment_length = 0.0
            print(f"Последовательность состоит из одного элемента: {min_val}")
        else:
            min_val = min(numbers)
            max_val = max(numbers)
            segment_length = max_val - min_val
            
            # Вывод результатов
            print(f"Минимальное значение: {min_val}")
            print(f"Максимальное значение: {max_val}")
            print(f"Отрезок, содержащий все числа: [{min_val}, {max_val}]")
        
        print(f"Длина наименьшего отрезка: {segment_length}")
        
        # Дополнительная информация
        print("\n" + "=" * 60)
        print("Дополнительная информация:")
        
        # Распределение чисел на отрезке
        if n > 1:
            # Сортируем числа для наглядности
            sorted_numbers = sorted(numbers)
            print(f"Отсортированная последовательность: {sorted_numbers}")
            
            # Находим среднее значение
            average = sum(numbers) / n
            print(f"Среднее значение: {average}")
            
            # Показываем положение чисел на отрезке
            print(f"\nПоложение чисел на отрезке [{min_val}, {max_val}]:")
            scale_length = 50  # длина шкалы для визуализации
            
            for num in sorted_numbers:
                # Вычисляем позицию на шкале
                if segment_length > 0:
                    position = int((num - min_val) / segment_length * scale_length)
                else:
                    position = 0
                
                # Создаем строку с отметкой
                scale_line = [" "] * (scale_length + 1)
                scale_line[position] = "|"
                scale_str = "[" + "".join(scale_line) + "]"
                
                print(f"  {num:8.4f}: {scale_str}")
            
            # Находим наибольший разрыв между соседними числами
            if n >= 2:
                gaps = []
                for i in range(1, n):
                    gap = sorted_numbers[i] - sorted_numbers[i-1]
                    gaps.append(gap)
                
                max_gap = max(gaps) if gaps else 0
                print(f"\nНаибольший разрыв между соседними числами: {max_gap}")
                print(f"Это {max_gap/segment_length*100:.1f}% от длины всего отрезка")
                
                # Показываем, где находятся разрывы
                if max_gap > 0:
                    print("Места наибольших разрывов:")
                    for i in range(1, n):
                        if abs(sorted_numbers[i] - sorted_numbers[i-1] - max_gap) < 1e-10:
                            print(f"  Между {sorted_numbers[i-1]} и {sorted_numbers[i]}")
        
        # Статистика
        print("\nСтатистика:")
        print(f"Количество чисел: {n}")
        print(f"Размах (range): {segment_length}")
        if n > 1:
            # Выборочная дисперсия
            mean = sum(numbers) / n
            variance = sum((x - mean) ** 2 for x in numbers) / (n - 1)
            std_dev = variance ** 0.5
            print(f"Среднее арифметическое: {mean:.4f}")
            print(f"Стандартное отклонение: {std_dev:.4f}")
            print(f"Коэффициент вариации: {std_dev/mean*100 if mean != 0 else '∞':.1f}%")
        
    except ValueError as e:
        print(f"Ошибка ввода: {e}")

if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
