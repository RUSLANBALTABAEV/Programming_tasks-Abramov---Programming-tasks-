"""
ГЛАВА 2
ЗАДАЧИ ПО ТЕМАМ
15. Целые числа.

576. Даны натуральное числа a1, ..., a10. Предположим, что имеются 10 гирь весом a1, ..., a10. Обозначим через ck число способов, которыми можно составить вес k, т.е. ck - это число решений уравнения a1 * x1 + ... + a10 * x10 = k, где xi может принимать значение 0 или 1 (i = 1, ..., 10). Получить c0, ..., c10.
"""


import random
from itertools import combinations

# ==========================================================
# ЗАДАЧА 576: Число способов составить вес k из 10 гирь
# ==========================================================

def get_weights():
    """Выбор способа ввода весов."""
    print("Задача 576: Число способов составить вес k из 10 гирь")
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
                weights = list(map(int, input().split()))
                if len(weights) != 10:
                    print(f"Ожидалось 10 чисел, получено {len(weights)}.")
                    continue
                if any(w <= 0 for w in weights):
                    print("Все числа должны быть натуральными (> 0).")
                    continue
                return weights
            except ValueError:
                print("Ошибка ввода. Введите целые числа.")

    elif choice == '2':
        weights = [random.randint(1, 15) for _ in range(10)]
        print(f"\nСгенерированы веса: {weights}")
        return weights

    else:  # готовые примеры
        examples = [
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [3, 5, 7, 11, 13, 17, 19, 23, 29, 31],
            [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        ]
        print("\nГотовые примеры (веса):")
        for idx, w in enumerate(examples, 1):
            print(f"{idx}: {w}")
        while True:
            try:
                num = int(input("Выберите номер примера: "))
                if 1 <= num <= len(examples):
                    return examples[num - 1]
                else:
                    print(f"Номер должен быть от 1 до {len(examples)}.")
            except ValueError:
                print("Ошибка ввода. Введите целое число.")


def count_subsets_dp(weights, max_sum=10):
    """
    Возвращает список c[0..max_sum], где c[k] — количество подмножеств
    набора weights с суммой ровно k.
    """
    dp = [0] * (max_sum + 1)
    dp[0] = 1                       # пустое подмножество даёт сумму 0
    for w in weights:
        if w > max_sum:
            continue                # такой вес не может быть использован
        for s in range(max_sum - w, -1, -1):
            dp[s + w] += dp[s]
    return dp


def find_subsets(weights, max_sum=10):
    """
    Возвращает список списков подмножеств для каждой суммы k (0..max_sum).
    Каждое подмножество — список весов.
    """
    n = len(weights)
    subsets_by_sum = [[] for _ in range(max_sum + 1)]
    for mask in range(1 << n):
        total = 0
        subset = []
        for i in range(n):
            if mask & (1 << i):
                total += weights[i]
                subset.append(weights[i])
        if 0 <= total <= max_sum:
            subsets_by_sum[total].append(subset)
    return subsets_by_sum


def main():
    weights = get_weights()

    print(f"\nВеса: {weights}")
    print("=" * 60)

    c = count_subsets_dp(weights, max_sum=10)

    print("Результаты (c_k — число способов составить вес k):")
    print(f"{'k':>3} | {'c_k':>5}")
    print("-" * 20)
    for k in range(11):
        print(f"{k:>3} | {c[k]:>5}")

    print("\n" + "=" * 60)

    # Дополнительно: показать сами подмножества для каждой суммы
    print("Примеры подмножеств, дающих каждую сумму:")
    subsets_by_sum = find_subsets(weights, max_sum=10)
    for k in range(11):
        if c[k] == 0:
            continue
        print(f"\nk = {k}: {c[k]} способ(ов)")
        for s in subsets_by_sum[k]:
            print(f"  {s}")

    print("=" * 60)


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")