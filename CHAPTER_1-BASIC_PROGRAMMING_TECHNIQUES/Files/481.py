"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

481. Дан файл f , компоненты u0, u1, ..., un которого являются последовательными числами Фибоначчи (см. задачу 144). Получить в файле f последовательные числа Фибоначчи u0, u1, ..., un+1.
"""


import random
import os


def read_numbers_from_file(filename):
    """Читает целые числа из файла и возвращает список."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            if not content:
                return []
            return [int(x) for x in content.split()]
    except FileNotFoundError:
        return None
    except ValueError:
        print(f"Ошибка: файл '{filename}' содержит некорректные данные.")
        return None


def write_numbers_to_file(filename, numbers):
    """Записывает список целых чисел в файл (через пробел)."""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(' '.join(str(x) for x in numbers))


def is_fibonacci_sequence(seq):
    """Проверяет, что seq — последовательные числа Фибоначчи (начиная с 0,1)."""
    if len(seq) < 2:
        return False
    if seq[0] != 0 or seq[1] != 1:
        return False
    for i in range(2, len(seq)):
        if seq[i] != seq[i-1] + seq[i-2]:
            return False
    return True


def generate_fibonacci(n):
    """Генерирует список u0, u1, ..., un чисел Фибоначчи."""
    seq = [0, 1]
    for i in range(2, n + 1):
        seq.append(seq[-1] + seq[-2])
    return seq


def create_correct_file(filename):
    """
    Запрашивает у пользователя способ создания файла
    с начальной последовательностью Фибоначчи.
    """
    print("\nФайл f должен содержать последовательные числа Фибоначчи.")
    print("Выберите способ задания начальной последовательности:")
    print("1 — Ручной ввод (не менее двух чисел Фибоначчи)")
    print("2 — Случайная длина последовательности (от 2 до 10 членов)")
    print("3 — Генерация полной последовательности u0..un")
    print("4 — Готовый пример (0,1,1,2,3,5)")

    while True:
        choice = input("Ваш выбор (1/2/3/4): ").strip()
        if choice in ('1', '2', '3', '4'):
            break
        print("Ошибка: выберите 1, 2, 3 или 4.")

    if choice == '1':
        while True:
            try:
                print("Введите последовательные числа Фибоначчи через пробел (минимум два):")
                data = list(map(int, input().split()))
                if len(data) < 2:
                    print("Нужно минимум два числа.")
                    continue
                if not is_fibonacci_sequence(data):
                    print("Это не последовательные числа Фибоначчи. Начните с 0, 1, ...")
                    continue
                write_numbers_to_file(filename, data)
                print(f"Числа записаны в '{filename}'.")
                return
            except ValueError:
                print("Ошибка ввода. Введите целые числа.")

    elif choice == '2':
        n = random.randint(2, 10)
        seq = generate_fibonacci(n)
        write_numbers_to_file(filename, seq)
        print(f"Сгенерирована последовательность длины {n+1}: {seq}")
        return

    elif choice == '3':
        while True:
            try:
                n = int(input("Введите n (n >= 1): "))
                if n < 1:
                    print("n должно быть >= 1.")
                    continue
                seq = generate_fibonacci(n)
                write_numbers_to_file(filename, seq)
                print(f"Сгенерирована последовательность u0..u{n}: {seq}")
                return
            except ValueError:
                print("Ошибка: введите целое число.")

    else:
        seq = [0, 1, 1, 2, 3, 5]
        write_numbers_to_file(filename, seq)
        print(f"Готовый пример записан в '{filename}': {seq}")


def add_next_fibonacci(filename):
    """
    Добавляет следующее число Фибоначчи в файл.
    Возвращает True, если операция выполнена успешно.
    """
    numbers = read_numbers_from_file(filename)
    if numbers is None:
        print(f"Файл '{filename}' не существует.")
        return False
    if len(numbers) < 2:
        print("Ошибка: в файле должно быть не менее двух чисел Фибоначчи.")
        return False
    if not is_fibonacci_sequence(numbers):
        print("Ошибка: последовательность в файле не является числами Фибоначчи.")
        return False

    next_fib = numbers[-1] + numbers[-2]
    numbers.append(next_fib)
    write_numbers_to_file(filename, numbers)
    print(f"Добавлено число u_{len(numbers)-1} = {next_fib}. "
          f"Файл '{filename}' обновлён.")
    return True


def main():
    filename = "f.txt"

    # Проверяем существование и содержимое файла
    numbers = read_numbers_from_file(filename)

    # Если файла нет или содержимое некорректно — создаём заново
    if numbers is None or len(numbers) < 2 or not is_fibonacci_sequence(numbers):
        if numbers is not None:
            print("Файл существует, но не содержит правильной последовательности Фибоначчи.")
        else:
            print(f"Файл '{filename}' не найден.")
        create_correct_file(filename)
    else:
        print(f"Файл '{filename}' содержит корректную последовательность Фибоначчи.")

    # Выводим текущее содержимое
    numbers = read_numbers_from_file(filename)
    print(f"\nТекущая последовательность: {numbers}")

    # Добавляем следующий член
    if add_next_fibonacci(filename):
        numbers = read_numbers_from_file(filename)
        print(f"Итоговая последовательность: {numbers}")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
