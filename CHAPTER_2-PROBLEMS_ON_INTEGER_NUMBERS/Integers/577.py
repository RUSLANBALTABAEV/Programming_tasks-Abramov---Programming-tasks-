"""
ГЛАВА 2
ЗАДАЧИ ПО ТЕМАМ
15. Целые числа.

577. Даны натуральное число a1, ..., a10. Предположим, что имеются 10 видов монет достоинством a1, ..., a10. Обозначим через bk число способов, которыми можно выплатить сумму k, т.е. bk - это число решений уравнения a1 * x1 + ... + a10 * x10 = k, где xi может принимать целые неотрицательные значения. Получить b0, ..., b20.
"""


# ==========================================================
# ЗАДАЧА 577: Число способов выплатить сумму k монетами 10 видов
# ==========================================================

import random

# Порог: если способов для данной суммы больше, чем ENUM_LIMIT,
# конкретные наборы монет не перечисляются (иначе программа зависнет).
ENUM_LIMIT = 500


def get_coins():
    """Выбор способа ввода номиналов монет."""
    print("Задача 577: Число способов выплатить сумму k монетами 10 видов")
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
                print("Введите 10 натуральных чисел a1..a10 через пробел:")
                coins = list(map(int, input().split()))
                if len(coins) != 10:
                    print(f"Ожидалось 10 чисел, получено {len(coins)}.")
                    continue
                if any(c <= 0 for c in coins):
                    print("Все номиналы должны быть натуральными (> 0).")
                    continue
                return coins
            except ValueError:
                print("Ошибка ввода. Введите целые числа.")

    elif choice == '2':
        coins = [random.randint(1, 12) for _ in range(10)]
        print(f"\nСгенерированы номиналы: {coins}")
        return coins

    else:  # готовые примеры
        examples = [
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [3, 5, 7, 11, 13, 17, 19, 23, 29, 31],
            [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],
        ]
        print("\nГотовые примеры (номиналы монет):")
        for idx, c in enumerate(examples, 1):
            print(f"{idx}: {c}")
        while True:
            try:
                num = int(input("Выберите номер примера: "))
                if 1 <= num <= len(examples):
                    return examples[num - 1]
                else:
                    print(f"Номер должен быть от 1 до {len(examples)}.")
            except ValueError:
                print("Ошибка ввода. Введите целое число.")


def count_ways_dp(coins, max_sum=20):
    """
    Возвращает b[0..max_sum], где b[k] — число способов
    выплатить сумму k монетами заданных номиналов
    (монет каждого вида — неограниченно много).
    Классическая задача о размене монет.
    """
    dp = [0] * (max_sum + 1)
    dp[0] = 1
    for w in coins:
        if w > max_sum:
            continue
        for s in range(w, max_sum + 1):
            dp[s] += dp[s - w]
    return dp


def find_ways_limited(coins, max_sum, limit):
    """
    Возвращает список наборов для каждой суммы k = 0..max_sum,
    НО только если их количество не превосходит limit.
    Иначе для этой суммы возвращается None (значит, перечисление пропущено).

    Каждый набор — список кортежей (номинал, количество),
    агрегированный по уникальным номиналам.
    """
    valid = [c for c in coins if c <= max_sum]
    ways_by_sum = [[] for _ in range(max_sum + 1)]
    too_many = [False] * (max_sum + 1)

    def rec(idx, current_sum, counts):
        if too_many[current_sum]:
            return
        if idx == len(valid):
            ways_by_sum[current_sum].append(counts[:])
            if len(ways_by_sum[current_sum]) > limit:
                too_many[current_sum] = True
                ways_by_sum[current_sum] = []
            return

        w = valid[idx]
        k = 0
        while current_sum + k * w <= max_sum:
            counts.append(k)
            rec(idx + 1, current_sum + k * w, counts)
            counts.pop()
            if too_many[current_sum]:
                return
            k += 1

    rec(0, 0, [])

    # Агрегируем по уникальным номиналам
    aggregated = []
    for k in range(max_sum + 1):
        if too_many[k]:
            aggregated.append(None)
        else:
            ways_list = []
            for counts in ways_by_sum[k]:
                total = {}
                for j, cnt in enumerate(counts):
                    if cnt > 0:
                        nom = valid[j]
                        total[nom] = total.get(nom, 0) + cnt
                ways_list.append(sorted(total.items()))
            aggregated.append(ways_list)
    return aggregated


def main():
    coins = get_coins()

    print(f"\nНоминалы монет: {coins}")
    print("=" * 60)

    b = count_ways_dp(coins, max_sum=20)

    print("Результаты (b_k — число способов выплатить сумму k):")
    print(f"{'k':>3} | {'b_k':>10}")
    print("-" * 20)
    for k in range(21):
        print(f"{k:>3} | {b[k]:>10}")

    print("\n" + "=" * 60)
    print(f"Примеры наборов монет (выводятся, если способов <= {ENUM_LIMIT}):")

    ways = find_ways_limited(coins, max_sum=20, limit=ENUM_LIMIT)

    for k in range(21):
        if b[k] == 0:
            continue
        print(f"\nk = {k}: {b[k]} способ(ов)")
        if ways[k] is None:
            print("  (слишком много способов — перечисление пропущено)")
            continue
        for i, way in enumerate(ways[k][:5], 1):
            if way:
                parts = [f"{cnt}×{nom}" for nom, cnt in way]
                print(f"  {i}. {' + '.join(parts)}")
            else:
                print(f"  {i}. (пусто)")
        if len(ways[k]) > 5:
            print(f"  ... и ещё {len(ways[k]) - 5} способ(ов)")

    print("=" * 60)


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")