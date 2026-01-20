"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
7. Сочетания цикла и разветвления

190. Даны натуральное число n, целые числа a1, … , an. Получить сумму положительных и число отрицательных членов последовательности a1, ..., an.
"""


def main():
    # Ввод количества чисел
    n = int(input("Введите натуральное число n: "))
    
    if n <= 0:
        print("Ошибка: n должно быть натуральным числом!")
        return
    
    # Ввод последовательности целых чисел
    numbers = []
    print(f"Введите {n} целых чисел:")
    for i in range(n):
        while True:
            try:
                num = int(input(f"a[{i+1}]: "))
                numbers.append(num)
                break
            except ValueError:
                print("Пожалуйста, введите целое число!")
    
    # Вычисление суммы положительных и количества отрицательных
    positive_sum = 0
    negative_count = 0
    
    for num in numbers:
        if num > 0:
            positive_sum += num
        elif num < 0:
            negative_count += 1
    
    # Вывод результатов
    print("\nРезультаты:")
    print(f"Сумма положительных членов: {positive_sum}")
    print(f"Число отрицательных членов: {negative_count}")

if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
