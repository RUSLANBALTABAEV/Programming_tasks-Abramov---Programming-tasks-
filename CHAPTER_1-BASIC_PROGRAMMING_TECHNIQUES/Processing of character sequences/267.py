"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
7. Сочетания цикла и разветвления

267. Даны натуральное число n, символы s1, …, sn (n >1). Преобразовать последовательность s1, …, sn, заменив запятыми все двоеточия, встречающиеся среди s1, …, s[n / 2], и заменив точками все восклицательные знаки, встречающиеся среди s[n / 2]+1, …, sn.
"""


def main():
    print("=== Задача 267 ===")
    print("Заменить в первой половине ':' на ',', во второй половине '!' на '.'")
    print()
    
    # Ввод данных
    try:
        n = int(input("Введите натуральное число n > 1: "))
        if n <= 1:
            print("Ошибка: n должно быть больше 1.")
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
        
        # Вычисляем границу (целая часть от n/2)
        border = n // 2  # Целая часть от деления
        print(f"\nГраница разделения: [{n}/2] = {border}")
        print(f"Первая половина: символы с 1 по {border}")
        print(f"Вторая половина: символы с {border + 1} по {n}")
        
        # Создаем список символов для удобства изменения
        result_list = list(symbols)
        
        # Обработка первой половины (с 1 по border)
        changes_first_half = 0
        for i in range(border):  # i от 0 до border-1
            if result_list[i] == ':':
                result_list[i] = ','
                changes_first_half += 1
        
        # Обработка второй половины (с border+1 по n)
        changes_second_half = 0
        for i in range(border, n):  # i от border до n-1
            if result_list[i] == '!':
                result_list[i] = '.'
                changes_second_half += 1
        
        # Преобразуем список обратно в строку
        result = ''.join(result_list)
        
        # Вывод результатов
        print(f"\nРезультат после преобразования: '{result}'")
        print(f"Длина результата: {len(result)}")
        
        # Статистика
        print(f"\nСтатистика:")
        print(f"В первой половине заменено ':' на ',': {changes_first_half}")
        print(f"Во второй половине заменено '!' на '.': {changes_second_half}")
        
        # Подробный вывод замен
        if changes_first_half > 0:
            print(f"\nЗамены в первой половине:")
            for i in range(border):
                if symbols[i] == ':':
                    print(f"  Позиция {i+1}: ':' -> ','")
        
        if changes_second_half > 0:
            print(f"\nЗамены во второй половине:")
            for i in range(border, n):
                if symbols[i] == '!':
                    print(f"  Позиция {i+1}: '!' -> '.'")
        
        # Дополнительная информация
        print(f"\nДополнительно:")
        print(f"Первая половина: '{symbols[:border]}' -> '{result[:border]}'")
        print(f"Вторая половина: '{symbols[border:]}' -> '{result[border:]}'")
        
        # Проверка на наличие других символов
        total_colons = symbols.count(':')
        total_exclamations = symbols.count('!')
        print(f"\nВсего ':' в строке: {total_colons}")
        print(f"Всего '!' в строке: {total_exclamations}")
        
        # Сколько замен не было сделано
        colons_second_half = symbols[border:].count(':')
        exclamations_first_half = symbols[:border].count('!')
        print(f"'!' в первой половине (не заменялись): {exclamations_first_half}")
        print(f"':' во второй половине (не заменялись): {colons_second_half}")
            
    except ValueError:
        print("Ошибка: n должно быть натуральным числом.")
        return

if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
