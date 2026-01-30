"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
7. Сочетания цикла и разветвления

261. Даны натуральное число n, символы s1, …, sn. 
а) Подсчитать наибольшее количество идущих подряд пробелов.
б) Выяснить, верно ли, что в последовательности s1, …, sn имеются пять идущих подряд букв е.
"""


def main():
    print("=== Задача 261 ===")
    print("а) Наибольшее количество идущих подряд пробелов")
    print("б) Проверка на наличие пяти идущих подряд букв 'e'")
    print()
    
    # Ввод данных
    try:
        n = int(input("Введите натуральное число n: "))
        if n < 0:
            print("Ошибка: n должно быть натуральным числом.")
            return
        
        print(f"Введите {n} символов подряд:")
        symbols = input()
        
        # Проверка длины введенной последовательности
        if len(symbols) < n:
            print(f"Предупреждение: введено только {len(symbols)} символов. Будем использовать их.")
            n = len(symbols)
        elif len(symbols) > n:
            print(f"Предупреждение: введено {len(symbols)} символов. Будем использовать первые {n}.")
            symbols = symbols[:n]
        
        print(f"\nИсходная последовательность: '{symbols}'")
        print(f"Длина последовательности: {n}")
        
        # а) Наибольшее количество идущих подряд пробелов
        max_spaces = 0
        current_spaces = 0
        
        for ch in symbols:
            if ch == ' ':
                current_spaces += 1
                if current_spaces > max_spaces:
                    max_spaces = current_spaces
            else:
                current_spaces = 0
        
        print(f"\nа) Наибольшее количество идущих подряд пробелов: {max_spaces}")
        
        # б) Проверка на наличие пяти идущих подряд букв 'e'
        has_five_e = False
        
        # Метод 1: Простой перебор
        for i in range(n - 4):  # -4 чтобы оставалось 5 символов
            if symbols[i:i+5] == 'eeeee':
                has_five_e = True
                break
        
        # Метод 2: Использование оператора in
        has_five_e_in = 'eeeee' in symbols
        
        print(f"\nб) В последовательности имеются пять идущих подряд букв 'e'?")
        print(f"   Ответ: {'Да' if has_five_e else 'Нет'}")
        
        if has_five_e:
            # Найдем позиции всех вхождений
            positions = []
            for i in range(n - 4):
                if symbols[i:i+5] == 'eeeee':
                    positions.append(i + 1)  # 1-индексация
            
            if positions:
                print(f"   Найдены на позициях: {positions}")
        
        # Дополнительная информация
        print(f"\nДополнительная информация:")
        print(f"   Всего пробелов в строке: {symbols.count(' ')}")
        print(f"   Всего букв 'e' в строке: {symbols.count('e')}")
        
        # Проверка на другие интересные последовательности
        for length in range(2, 6):
            target = 'e' * length
            if target in symbols:
                print(f"   Найдены {length} подряд идущих 'e'")
        
    except ValueError:
        print("Ошибка: n должно быть натуральным числом.")
        return

if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
