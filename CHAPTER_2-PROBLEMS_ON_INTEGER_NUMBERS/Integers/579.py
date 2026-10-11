"""
ГЛАВА 2
ЗАДАЧИ ПО ТЕМАМ
15. Целые числа.

579. Дано натуральное число n (n >= 5). Получить все пятерки натуральных чисел x1, x2, x3, x4, x5 такие, что x1 >= x2 >= x3 >= x4 >= x5 и x1 + ... + x5 = n.
"""


# ==========================================================
# ЗАДАЧА 579: Все пятёрки натуральных чисел с суммой n
# Условие: x1 >= x2 >= x3 >= x4 >= x5, x1 + ... + x5 = n
# ==========================================================

import random


def get_n():
    """Выбор способа ввода числа n."""
    print("Задача 579: Пятёрки натуральных чисел с суммой n")
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
                n = int(input("Введите натуральное число n (n >= 5): "))
                if n < 5:
                    print("n должно быть >= 5.")
                    continue
                return n
            except ValueError:
                print("Ошибка ввода. Введите целое число.")

    elif choice == '2':
        n = random.randint(5, 30)
        print(f"\nСгенерировано n = {n}")
        return n

    else:  # готовые примеры
        examples = [5, 6, 7, 8, 10, 15, 20, 30]
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


def find_quintuples(n):
    """
    Возвращает список всех пятёрок (x1, x2, x3, x4, x5) натуральных
    чисел с суммой n и условием x1 >= x2 >= x3 >= x4 >= x5.

    Используется DFS с отсечениями:
      - верхняя граница для текущего числа: min(max_val, remaining - (k-1));
      - нижняя граница определяется условиями осуществимости:
          * remaining - v >= k - 1   (оставшиеся числа минимум по 1)
          * remaining - v <= (k - 1) * v   (максимум при всех оставшихся = v)
    """
    results = []
    current = []

    def dfs(remaining, parts_left, max_val):
        # Все 5 чисел выбраны — проверяем, что сумма сошлась
        if parts_left == 0:
            if remaining == 0:
                results.append(tuple(current))
            return

        # Верхняя граница: не больше max_val и не больше, чем
        # remaining - (parts_left - 1) (иначе оставшиеся не наберут сумму)
        upper = min(max_val, remaining - (parts_left - 1))

        for v in range(upper, 0, -1):
            rem = remaining - v
            # Проверка осуществимости
            if rem < parts_left - 1:
                continue
            if rem > (parts_left - 1) * v:
                continue

            current.append(v)
            dfs(rem, parts_left - 1, v)
            current.pop()

    # Первое число не больше n-4 (остальные 4 минимум по 1)
    dfs(n, 5, n - 4)
    return results


def partitions_of_n_into_5(n):
    """
    Точное число разбиений n на ровно 5 частей (порядок не важен).
    Формула: p(n, 5) = round((n^4 - 10n^3 + 35n^2 - 50n + 24) / 288)
    Используется только для проверки.
    """
    if n < 5:
        return 0
    value = (n**4 - 10*n**3 + 35*n**2 - 50*n + 24) / 288
    return round(value)


def main():
    n = get_n()
    quintuples = find_quintuples(n)

    print(f"\nИсходное число: n = {n}")
    print("=" * 60)

    if not quintuples:
        print("Пятёрок, удовлетворяющих условию, не найдено.")
    else:
        total = len(quintuples)
        print(f"Найдено пятёрок: {total}")

        # Если пятёрок мало — выводим все, иначе только первые 10
        if total <= 30:
            for i, (x1, x2, x3, x4, x5) in enumerate(quintuples, 1):
                s = x1 + x2 + x3 + x4 + x5
                print(f"  {i:>3}. ({x1}, {x2}, {x3}, {x4}, {x5})   "
                      f"сумма = {s}")
        else:
            print("  (первые 10 пятёрок):")
            for i, (x1, x2, x3, x4, x5) in enumerate(quintuples[:10], 1):
                s = x1 + x2 + x3 + x4 + x5
                print(f"  {i:>3}. ({x1}, {x2}, {x3}, {x4}, {x5})   "
                      f"сумма = {s}")
            print(f"  ... и ещё {total - 10} пятёрок")

        # Проверка через формулу числа разбиений
        expected = partitions_of_n_into_5(n)
        if total == expected:
            print(f"\n✅ Количество совпадает с формулой разбиений: {expected}.")
        else:
            print(f"\n⚠ Расхождение с формулой разбиений: "
                  f"получено {total}, ожидалось {expected}.")

    print("=" * 60)


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")