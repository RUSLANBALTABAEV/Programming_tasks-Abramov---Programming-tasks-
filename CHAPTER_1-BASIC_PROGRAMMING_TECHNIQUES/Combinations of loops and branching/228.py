"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
7. Сочетания цикла и разветвления

228. Даны натуральное число n, действительные числа a1, …, an.
Выяснить, является ли последовательность a1, …, an упорядоченной по убыванию.
"""


def main():
    print("228. Проверка упорядоченности последовательности по убыванию")
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
        
        # Проверка упорядоченности по убыванию
        is_descending = True
        
        # Проверяем для всех i от 0 до n-2: a[i] >= a[i+1]
        for i in range(n - 1):
            if numbers[i] < numbers[i + 1]:
                is_descending = False
                # Запоминаем, где найдено нарушение
                violation_index = i
                break
        
        # Вывод результатов
        if n == 1:
            print("Последовательность состоит из одного элемента - считается упорядоченной.")
        elif is_descending:
            print("Последовательность упорядочена по убыванию.")
            print("Все элементы удовлетворяют условию: a[i] >= a[i+1]")
        else:
            print("Последовательность НЕ упорядочена по убыванию.")
            print(f"Нарушение на позиции {violation_index + 1}:")
            print(f"  a[{violation_index + 1}] = {numbers[violation_index]}")
            print(f"  a[{violation_index + 2}] = {numbers[violation_index + 1]}")
            print(f"  {numbers[violation_index]} < {numbers[violation_index + 1]} - нарушение условия")
        
        # Дополнительная информация
        print("\n" + "=" * 60)
        print("Подробный анализ последовательности:")
        
        # Выводим все пары соседних элементов
        for i in range(n - 1):
            comparison = ">=" if numbers[i] >= numbers[i + 1] else "<"
            print(f"  a[{i+1}] = {numbers[i]} {comparison} a[{i+2}] = {numbers[i+1]}")
        
        # Проверка на строгое убывание
        if n > 1:
            is_strictly_descending = all(numbers[i] > numbers[i + 1] for i in range(n - 1))
            if is_strictly_descending:
                print("\nПоследовательность строго убывающая (все неравенства строгие).")
            elif is_descending:
                print("\nПоследовательность неубывающая (некоторые элементы могут быть равны).")
        
        # Статистика
        print("\nСтатистика:")
        print(f"Количество элементов: {n}")
        if n > 1:
            # Подсчет нарушений
            violations = sum(1 for i in range(n - 1) if numbers[i] < numbers[i + 1])
            print(f"Количество нарушений порядка убывания: {violations}")
            
            # Процент упорядоченности
            ordered_pairs = sum(1 for i in range(n - 1) if numbers[i] >= numbers[i + 1])
            percentage = (ordered_pairs / (n - 1)) * 100
            print(f"Процент упорядоченных пар: {percentage:.1f}%")
        
    except ValueError as e:
        print(f"Ошибка ввода: {e}")

if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
