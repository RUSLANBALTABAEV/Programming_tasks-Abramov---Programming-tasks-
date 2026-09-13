"""
ГЛАВА 2
ЗАДАЧИ ПО ТЕМАМ
15. Целые числа.

562. Натуральное число из n цифр является числом Армстронга, если сумма его цифр, возведенных в n-ю степень, равна числу (как, например, 153 = 1 * 1 * 1 + 5 * 5 * 5 + 3 * 3 * 3). Получить все числа Армстронга, состоящие из двух, трех и четырех цифр.
"""


def is_armstrong(num):
    """
    Проверяет, является ли число num числом Армстронга.
    Возвращает кортеж (True/False, строка-выражение).
    """
    digits = str(num)
    n = len(digits)
    total = sum(int(d) ** n for d in digits)
    expression = " + ".join(f"{d}^{n}" for d in digits)
    return total == num, expression


def find_armstrong_by_length(n):
    """Возвращает список кортежей (число, выражение) для всех n-значных чисел Армстронга."""
    start = 10 ** (n - 1)
    end = 10 ** n - 1
    result = []
    for num in range(start, end + 1):
        ok, expr = is_armstrong(num)
        if ok:
            result.append((num, expr))
    return result


def get_digit_lengths():
    """Выбор разрядностей для поиска чисел Армстронга."""
    print("Задача 562: Числа Армстронга")
    print("Выберите диапазон разрядностей:")
    print("1 — Только по условию: 2, 3, 4 знака")
    print("2 — Дополнительно проверить 5-значные")
    print("3 — Ручной ввод (через запятую, например: 2,3,4,5)")

    while True:
        choice = input("Ваш выбор (1/2/3): ").strip()
        if choice in ('1', '2', '3'):
            break
        print("Ошибка: выберите 1, 2 или 3.")

    if choice == '1':
        return [2, 3, 4]
    elif choice == '2':
        return [2, 3, 4, 5]
    else:
        while True:
            raw = input("Введите разрядности через запятую: ").strip()
            try:
                lengths = [int(x.strip()) for x in raw.split(',') if x.strip()]
                if not lengths or any(n < 1 for n in lengths):
                    print("Разрядности должны быть положительными целыми числами.")
                    continue
                return sorted(set(lengths))
            except ValueError:
                print("Ошибка: введите целые числа, разделённые запятыми.")


def main():
    lengths = get_digit_lengths()
    total_found = 0

    print()
    for n in lengths:
        found = find_armstrong_by_length(n)
        print(f"{n}-значные числа Армстронга:")
        if found:
            for num, expr in found:
                print(f"  {num} = {expr}")
        else:
            print("  не найдено")
        print("-" * 50)
        total_found += len(found)

    print(f"Всего чисел Армстронга среди выбранных разрядностей: {total_found}")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")