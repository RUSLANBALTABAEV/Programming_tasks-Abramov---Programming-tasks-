"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
7. Сочетания цикла и разветвления

262. Даны натуральное число n, символы s1, …, sn. Определить число вхождений в последовательность s1, …, sn группы букв:
а) abc.
б) aba.
"""


def main():
    print("=== Задача 262 ===")
    print("Подсчет вхождений групп букв 'abc' и 'aba'")
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
        
        # Функция для подсчета вхождений паттерна с учетом пересечений
        def count_pattern(pattern):
            count = 0
            pattern_len = len(pattern)
            for i in range(n - pattern_len + 1):
                if symbols[i:i+pattern_len] == pattern:
                    count += 1
            return count
        
        # a) Подсчет вхождений "abc"
        count_abc = count_pattern("abc")
        print(f"\nа) Число вхождений группы букв 'abc': {count_abc}")
        
        # б) Подсчет вхождений "aba"
        count_aba = count_pattern("aba")
        print(f"б) Число вхождений группы букв 'aba': {count_aba}")
        
        # Дополнительная информация
        print("\nДополнительная информация:")
        
        # Найдем позиции вхождений (1-индексация)
        def find_positions(pattern):
            positions = []
            pattern_len = len(pattern)
            for i in range(n - pattern_len + 1):
                if symbols[i:i+pattern_len] == pattern:
                    positions.append(i + 1)  # 1-индексация
            return positions
        
        abc_positions = find_positions("abc")
        if abc_positions:
            print(f"   'abc' найдено на позициях: {abc_positions}")
        else:
            print("   'abc' не найдено")
            
        aba_positions = find_positions("aba")
        if aba_positions:
            print(f"   'aba' найдено на позициях: {aba_positions}")
        else:
            print("   'aba' не найдено")
        
        # Подсчет всех символов
        print(f"\nОбщее количество символов: {n}")
        print(f"Количество символов 'a': {symbols.count('a')}")
        print(f"Количество символов 'b': {symbols.count('b')}")
        print(f"Количество символов 'c': {symbols.count('c')}")
            
    except ValueError:
        print("Ошибка: n должно быть натуральным числом.")
        return

if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
