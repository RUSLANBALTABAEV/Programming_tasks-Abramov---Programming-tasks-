"""
ГЛАВА 2
ЗАДАЧИ ПО ТЕМАМ
15. Целые числа.

580. Дано натуральное число n (n <= 99). Получить все способы выплаты суммы n с помощью монет достоинством 1, 5, 10 и 20 коп.
"""


# ==========================================================
# ЗАДАЧА 580: Способы выплаты суммы n монетами 1, 5, 10, 20 коп.
# Условие: 1 <= n <= 99
# ==========================================================

import random

COINS = (1, 5, 10, 20)   # номиналы монет


def get_n():
    """Выбор способа ввода числа n."""
    print("Задача 580: Способы выплаты суммы n монетами 1, 5, 10, 20 коп.")
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
                n = int(input("Введите натуральное число n (1 <= n <= 99): "))
                if n < 1 or n > 99:
                    print("n должно быть в диапазоне от 1 до 99.")
                    continue
                return n
            except ValueError:
                print("Ошибка ввода. Введите целое число.")

    elif choice == '2':
        n = random.randint(1, 99)
        print(f"\nСгенерировано n = {n}")
        return n

    else:  # готовые примеры
        examples = [5, 10, 13, 20, 25, 47, 99]
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


def find_ways(n):
    """
    Возвращает список кортежей (c1, c5, c10, c20),
    где c1, c5, c10, c20 — количества монет достоинством 1, 5, 10 и 20 коп.
    Перебираем c20, c10, c5, а c1 = остаток (добираем монетами по 1 копейке).
    """
    ways = []
    for c20 in range(n // 20 + 1):
        rem20 = n - c20 * 20
        for c10 in range(rem20 // 10 + 1):
            rem10 = rem20 - c10 * 10
            for c5 in range(rem10 // 5 + 1):
                rem5 = rem10 - c5 * 5
                c1 = rem5  # остаток добираем монетами по 1 копейке
                ways.append((c1, c5, c10, c20))
    return ways


def main():
    n = get_n()
    ways = find_ways(n)

    print(f"\nИсходное число: n = {n}")
    print("=" * 70)

    if not ways:
        print("Способов выплаты не найдено.")
    else:
        total = len(ways)
        print(f"Найдено способов: {total}")

        # Если способов мало — выводим все, иначе только первые 15
        if total <= 20:
            for i, (c1, c5, c10, c20) in enumerate(ways, 1):
                s = c1 * 1 + c5 * 5 + c10 * 10 + c20 * 20
                print(f"  {i:>3}. 1 коп × {c1:>2} + 5 коп × {c5:>2} + "
                      f"10 коп × {c10:>2} + 20 коп × {c20:>2}   (сумма = {s})")
        else:
            print("  (первые 15 способов):")
            for i, (c1, c5, c10, c20) in enumerate(ways[:15], 1):
                s = c1 * 1 + c5 * 5 + c10 * 10 + c20 * 20
                print(f"  {i:>3}. 1 коп × {c1:>2} + 5 коп × {c5:>2} + "
                      f"10 коп × {c10:>2} + 20 коп × {c20:>2}   (сумма = {s})")
            print(f"  ... и ещё {total - 15} способ(ов)")

        # Мини-статистика: сколько монет каждого номинала в среднем
        avg_20 = sum(w[3] for w in ways) / total
        avg_10 = sum(w[2] for w in ways) / total
        avg_5 = sum(w[1] for w in ways) / total
        avg_1 = sum(w[0] for w in ways) / total
        print(f"\nСредние количества монет по способам:")
        print(f"  1 коп: {avg_1:.2f},  5 коп: {avg_5:.2f},  "
              f"10 коп: {avg_10:.2f},  20 коп: {avg_20:.2f}")

    print("=" * 70)


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")