"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

471. Дан файл f, компоненты которого являются действительными числами. Найти:
а) сумму компонент файла f;
б) произведение компонент файла f;
в) сумму квадратов компонент файла f;
г) модуль суммы и квадрат произведения компонент файла f;
д) последнюю компоненту файла.
"""


import random
import os


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
    print("Задача 471: Анализ действительных чисел из файла f")
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
        # Ручной ввод: пользователь вводит числа через пробел
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
        # Случайная генерация
        n = random.randint(5, 15)
        numbers = [round(random.uniform(-20, 20), 4) for _ in range(n)]
        create_file_with_numbers(filename, numbers)
        print(f"Случайно сгенерировано {n} чисел и записано в '{filename}'.")
        return filename

    else:
        # Готовый пример: создаём файл с заранее заданными числами
        example_numbers = [3.5, -2.1, 0.0, 10.7, -5.25, 6.0]
        create_file_with_numbers(filename, example_numbers)
        print(f"Готовый пример записан в '{filename}': {example_numbers}")
        return filename


def main():
    filename = get_file()

    numbers = read_numbers_from_file(filename)
    if not numbers:
        return

    print(f"\nЧисла из файла ({len(numbers)}): {numbers}")

    # а) Сумма
    total_sum = sum(numbers)

    # б) Произведение
    product = 1.0
    for x in numbers:
        product *= x

    # в) Сумма квадратов
    sum_squares = sum(x * x for x in numbers)

    # г) Модуль суммы и квадрат произведения
    abs_sum = abs(total_sum)
    sq_product = product ** 2

    # д) Последняя компонента
    last = numbers[-1] if numbers else None

    print("\nРезультаты:")
    print(f"а) Сумма компонент:          {total_sum:.6f}")
    print(f"б) Произведение компонент:    {product:.6f}")
    print(f"в) Сумма квадратов компонент: {sum_squares:.6f}")
    print(f"г) Модуль суммы:              {abs_sum:.6f}")
    print(f"   Квадрат произведения:      {sq_product:.6f}")
    print(f"д) Последняя компонента:      {last:.6f}" if last is not None else "д) Файл пуст.")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
