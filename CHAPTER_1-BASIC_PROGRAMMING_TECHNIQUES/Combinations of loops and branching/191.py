"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
7. Сочетания цикла и разветвления

191. Даны натуральное число n, целые числа a1, … , an. 
Заменить все большие семи члены последовательности a1, … , an числом 7. Вычислить количество таких членов.
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
    
    # Замена чисел, больших семи, на 7 и подсчет количества замен
    count = 0
    modified_numbers = []
    
    for num in numbers:
        if num > 7:
            modified_numbers.append(7)
            count += 1
        else:
            modified_numbers.append(num)
    
    # Вывод результатов
    print("\nРезультаты:")
    print("Изменённая последовательность (все числа >7 заменены на 7):")
    for i in range(n):
        print(f"a[{i+1}] = {modified_numbers[i]}")
    
    print(f"\nКоличество замен (чисел, больших семи): {count}")

if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
