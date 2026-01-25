"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
7. Сочетания цикла и разветвления

218. Даны натуральное число n, действительные числа x1, …, x3n. последовательность чисел x1, …, x3n. Вычислить сумму чисел из xn+1, …, x3n, которые превосходят по величине все числа x1, …, xn.
"""


def main():
    # Ввод данных
    n = int(input("Введите натуральное число n: "))
    print(f"Введите {3*n} действительных чисел через пробел:")
    numbers = list(map(float, input().split()))
    
    if len(numbers) != 3*n:
        print("Ошибка: введено неверное количество чисел")
        return
    
    # 1. Находим максимальное значение среди первых n чисел
    max_first_n = max(numbers[:n]) if n > 0 else float('-inf')
    
    # 2. Вычисляем сумму чисел из x_{n+1} до x_{3n}, которые > max_first_n
    total_sum = 0
    for i in range(n, 3*n):  # индексы с n до 3n-1
        if numbers[i] > max_first_n:
            total_sum += numbers[i]
    
    # 3. Выводим результат
    print(f"\nМаксимум среди первых {n} чисел: {max_first_n}")
    print(f"Сумма чисел из x_{n+1}..x_{3*n}, превышающих максимум: {total_sum}")
    
    # Дополнительно: выводим найденные числа
    found_numbers = [numbers[i] for i in range(n, 3*n) if numbers[i] > max_first_n]
    if found_numbers:
        print(f"Найденные числа: {found_numbers}")
    else:
        print("Таких чисел нет")

if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
