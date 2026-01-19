"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
7. Сочетания цикла и разветвления

185. Даны натуральное число n, действительные числа a1, ..., an. Получить удвоенную сумму всех положительных членов
последовательности a1, ..., an.
"""


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
    
    # Вычисление удвоенной суммы положительных членов
    positive_sum = 0.0
    positive_numbers = []
    
    for num in numbers:
        if num > 0:  # строго положительные числа
            positive_sum += num
            positive_numbers.append(num)
    
    doubled_sum = 2 * positive_sum
    
    # Вывод результатов
    print("\nРезультаты:")
    print(f"Положительные числа в последовательности: {positive_numbers}")
    print(f"Их сумма: {positive_sum}")
    print(f"Удвоенная сумма положительных чисел: {doubled_sum}")

if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
