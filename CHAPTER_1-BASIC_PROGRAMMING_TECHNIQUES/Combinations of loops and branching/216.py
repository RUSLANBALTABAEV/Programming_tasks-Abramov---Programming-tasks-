"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
7. Сочетания цикла и разветвления

216. Даны целые числа c1, …, c95. Имеются ли в
последовательности c1, …, c95:
а) два идущих подряд нулевых члена;
б) три идущих подряд нулевых члена?
"""


def main():
    n = 95  # Фиксированное количество чисел согласно условию
    
    print(f"Введите {n} целых чисел:")
    c = []
    
    for i in range(1, n + 1):
        while True:
            try:
                num = int(input(f"c[{i}]: "))
                c.append(num)
                break
            except ValueError:
                print("Пожалуйста, введите целое число!")
    
    # Проверка условий
    has_two_consecutive_zeros = False
    has_three_consecutive_zeros = False
    
    for i in range(n - 1):
        if c[i] == 0 and c[i + 1] == 0:
            has_two_consecutive_zeros = True
            # Если нашли два подряд нуля, проверяем на три (если есть место для третьего)
            if i + 2 < n and c[i + 2] == 0:
                has_three_consecutive_zeros = True
    
    # Вывод результатов
    print("\nРезультаты:")
    if has_two_consecutive_zeros:
        print("а) Да, в последовательности есть два идущих подряд нулевых члена.")
    else:
        print("а) Нет, в последовательности нет двух идущих подряд нулевых членов.")
    
    if has_three_consecutive_zeros:
        print("б) Да, в последовательности есть три идущих подряд нулевых члена.")
    else:
        print("б) Нет, в последовательности нет трех идущих подряд нулевых членов.")

if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
