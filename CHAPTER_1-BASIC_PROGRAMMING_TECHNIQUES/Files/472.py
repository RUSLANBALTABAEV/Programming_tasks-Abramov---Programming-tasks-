"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

472. Дан файл f, компоненты которого являются действительными числами. Найти:
а) наибольшее из значений компонент;
б) наименьшее из значений компонент с четными номерами;
в) наибольшее из значений модулей компонент с нечетными
номерами;
г) сумму наибольшего и наименьшего из значений компонент;
д) разность первой и последней компонент файла. 
"""


import random


def create_file_with_numbers(filename, numbers):
    """Записывает последовательность чисел в файл (через пробел)."""
    with open(filename, 'w') as f:
        f.write(' '.join(str(x) for x in numbers))


def read_numbers_from_file(filename):
    """Читает действительные числа из файла, разделённые пробельными символами."""
    try:
        with open(filename, 'r') as f:
            content = f.read()
            return [float(x) for x in content.split()]
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден.")
        return None
    except ValueError:
        print("Ошибка: файл содержит некорректные данные (не числа).")
        return None


def get_file():
    """Выбор способа ввода данных и создание/использование файла f.txt."""
    filename = "f.txt"
    print("Задача 472: Анализ компонент файла действительных чисел")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод чисел")
    print("2 — Случайная генерация файла")
    print("3 — Готовый пример")

    while True:
        choice = input("Ваш выбор (1/2/3): ").strip()
        if choice in ('1', '2', '3'):
            break
        print("Ошибка: выберите 1, 2 или 3.")

    if choice == '1':
        while True:
            try:
                n = int(input("Сколько чисел записать в файл? "))
                if n <= 0:
                    print("Количество должно быть положительным.")
                    continue
                print(f"Введите {n} действительных чисел через пробел:")
                data = list(map(float, input().split()))
                if len(data) != n:
                    print(f"Ожидалось {n} чисел, получено {len(data)}.")
                    continue
                create_file_with_numbers(filename, data)
                print(f"Числа записаны в файл '{filename}'.")
                return filename
            except ValueError:
                print("Ошибка ввода. Повторите.")

    elif choice == '2':
        n = random.randint(5, 15)
        numbers = [round(random.uniform(-20, 20), 4) for _ in range(n)]
        create_file_with_numbers(filename, numbers)
        print(f"Случайно сгенерировано {n} чисел и записано в '{filename}'.")
        return filename

    else:
        # Готовый пример: создаём файл с заранее заданными числами
        example_numbers = [7.5, -3.2, 0.0, 11.1, -6.75, 4.0, -1.2, 9.33, -5.0, 2.1]
        create_file_with_numbers(filename, example_numbers)
        print(f"Готовый пример записан в '{filename}': {example_numbers}")
        return filename


def main():
    filename = get_file()
    data = read_numbers_from_file(filename)

    if not data:
        return

    print(f"\nКомпоненты файла ({len(data)}): {data}\n")

    # а) Наибольшее из значений компонент
    max_val = max(data)

    # б) Наименьшее из значений компонент с чётными номерами (нумерация с 1)
    even_positions = data[1::2]    # индексы 1,3,5... → компоненты 2,4,6...
    min_even = min(even_positions) if even_positions else None

    # в) Наибольший модуль компонент с нечётными номерами (нумерация с 1)
    odd_positions = data[0::2]    # индексы 0,2,4... → компоненты 1,3,5...
    max_abs_odd = max(abs(x) for x in odd_positions) if odd_positions else None

    # г) Сумма наибольшего и наименьшего из значений компонент
    min_val = min(data)
    sum_max_min = max_val + min_val

    # д) Разность первой и последней компонент файла
    diff_first_last = data[0] - data[-1]

    print("Результаты:")
    print(f"а) Наибольшее значение:                       {max_val:.6f}")
    print(f"б) Наименьшее значение среди чётных компонент: {min_even:.6f}" if min_even is not None else "б) Нет чётных компонент")
    print(f"в) Наибольший модуль среди нечётных компонент: {max_abs_odd:.6f}" if max_abs_odd is not None else "в) Нет нечётных компонент")
    print(f"г) Сумма максимума и минимума:                 {sum_max_min:.6f}")
    print(f"д) Разность первой и последней компонент:      {diff_first_last:.6f}")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
