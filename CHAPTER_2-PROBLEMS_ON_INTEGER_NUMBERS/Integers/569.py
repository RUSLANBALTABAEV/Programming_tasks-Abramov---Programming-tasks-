"""
ГЛАВА 2
ЗАДАЧИ ПО ТЕМАМ
15. Целые числа.

569. Дано натуральное число n. Получить в порядке возрастания n первый натуральных чисел, которые не делятся ни на какие простые числа, кроме 2, 3 и 5.
"""


import random


def get_n():
    """Выбор способа ввода натурального числа n."""
    print("Задача 569: 5-гладкие числа (числа Хэмминга)")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод")
    print("2 — Случайная генерация")
    print("3 — Готовые примеры")

    while True:
        choice = input("Ваш выбор (1/2/3): ").strip()
        if choice in ('1', '2', '3'):
            break
        print("Ошибка: выберите 1, 2 или 3.")

    if choice == '1':
        while True:
            try:
                n = int(input("Введите натуральное число n (>=1): "))
                if n < 1:
                    print("n должно быть >= 1.")
                    continue
                return n
            except ValueError:
                print("Ошибка ввода. Повторите.")

    elif choice == '2':
        n = random.randint(1, 30)
        print(f"\nСгенерировано n = {n}")
        return n

    else:  # готовые примеры
        examples = [5, 10, 20, 50]
        print("\nГотовые примеры n:")
        for idx, val in enumerate(examples, 1):
            print(f"{idx}: n = {val}")
        while True:
            try:
                num = int(input("Выберите номер примера: "))
                if 1 <= num <= len(examples):
                    return examples[num - 1]
                else:
                    print(f"Номер должен быть от 1 до {len(examples)}.")
            except ValueError:
                print("Ошибка ввода. Введите целое число.")


def generate_smooth_numbers(n):
    """
    Генерирует первые n натуральных чисел, которые не делятся
    ни на какие простые числа, кроме 2, 3 и 5.
    Используется алгоритм с тремя указателями (числа Хэмминга).
    """
    if n <= 0:
        return []

    result = [1]          # первое 5-гладкое число
    i2 = i3 = i5 = 0      # указатели для умножения на 2, 3 и 5

    while len(result) < n:
        next2 = result[i2] * 2
        next3 = result[i3] * 3
        next5 = result[i5] * 5

        next_val = min(next2, next3, next5)
        result.append(next_val)

        # Сдвигаем указатели, которые дали минимальное значение
        if next_val == next2:
            i2 += 1
        if next_val == next3:
            i3 += 1
        if next_val == next5:
            i5 += 1

    return result


def is_5_smooth(num):
    """Проверяет, что число не имеет простых делителей, кроме 2, 3, 5."""
    for p in (2, 3, 5):
        while num % p == 0:
            num //= p
    return num == 1


def main():
    n = get_n()
    numbers = generate_smooth_numbers(n)

    print(f"\nПервые {n} чисел, не делящихся ни на какие простые числа,")
    print("кроме 2, 3 и 5 (в порядке возрастания):")
    print("-" * 60)

    # Вывод по 10 чисел в строке
    for i in range(0, len(numbers), 10):
        chunk = numbers[i:i + 10]
        print("  " + ", ".join(f"{x:>6}" for x in chunk))

    print("-" * 60)
    print(f"Всего чисел: {len(numbers)}")
    print(f"Последнее число: {numbers[-1]}")
    print(f"Проверка последнего числа: {'OK' if is_5_smooth(numbers[-1]) else 'ОШИБКА'}")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")