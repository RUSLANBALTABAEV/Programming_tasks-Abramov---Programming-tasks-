"""
ГЛАВА 2
ЗАДАЧИ ПО ТЕМАМ
15. Целые числа.

578. Дано натуральное число n. Как наименьшим количеством монет можно выплатить n копеек? Предполагается, что в достаточно большом количестве имеются монеты достоинством в 1, 2, 3, 5, 10, 15, 20 и 50 коп.
"""


# ==========================================================
# ЗАДАЧА 578: Минимальное число монет для выплаты n копеек
# Номиналы: 1, 2, 3, 5, 10, 15, 20, 50
# ==========================================================

import random

COINS = (50, 20, 15, 10, 5, 3, 2, 1)          # в порядке убывания для жадного алгоритма
COINS_ASC = (1, 2, 3, 5, 10, 15, 20, 50)      # в порядке возрастания для ДП


def get_n():
    """Выбор способа ввода числа n."""
    print("Задача 578: Минимальное число монет для выплаты n копеек")
    print("Доступные номиналы: 1, 2, 3, 5, 10, 15, 20, 50")
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
                n = int(input("Введите натуральное число n (n >= 0): "))
                if n < 0:
                    print("n должно быть неотрицательным.")
                    continue
                return n
            except ValueError:
                print("Ошибка ввода. Введите целое число.")

    elif choice == '2':
        n = random.randint(0, 200)
        print(f"\nСгенерировано n = {n}")
        return n

    else:  # готовые примеры
        examples = [0, 1, 4, 6, 9, 11, 17, 28, 49, 99, 123]
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


def min_coins_greedy(n):
    """
    Жадный алгоритм: берём самую крупную монету, которая ещё помещается,
    повторяем до обнуления суммы.
    Для системы {1,2,3,5,10,15,20,50} этот алгоритм даёт оптимум.
    Возвращает список использованных монет.
    """
    result = []
    remainder = n
    for c in COINS:
        while remainder >= c:
            result.append(c)
            remainder -= c
    return result


def min_coins_dp(n):
    """
    Точный минимум числа монет через динамическое программирование.
    Возвращает список монет (не только их количество) или None,
    если выплатить сумму невозможно (не наш случай — есть монета в 1 коп).
    """
    INF = float('inf')
    dp = [INF] * (n + 1)
    parent = [-1] * (n + 1)     # для восстановления ответа
    dp[0] = 0

    for s in range(1, n + 1):
        for c in COINS_ASC:
            if c <= s and dp[s - c] + 1 < dp[s]:
                dp[s] = dp[s - c] + 1
                parent[s] = c

    if dp[n] == INF:
        return None

    # Восстановление последовательности монет
    result = []
    cur = n
    while cur > 0:
        c = parent[cur]
        result.append(c)
        cur -= c
    return result


def main():
    n = get_n()
    print(f"\nИсходное число: n = {n}")
    print("=" * 60)

    # 1. Жадный алгоритм
    greedy_result = min_coins_greedy(n)
    print(f"Жадный алгоритм:")
    print(f"  Монеты: {greedy_result}")
    print(f"  Всего монет: {len(greedy_result)}")

    # 2. Точный алгоритм (только для разумных n, чтобы не тормозить)
    if n <= 5000:
        dp_result = min_coins_dp(n)
        print(f"\nТочный алгоритм (ДП):")
        print(f"  Монеты: {dp_result}")
        print(f"  Всего монет: {len(dp_result)}")

        if len(greedy_result) == len(dp_result):
            print("\n✅ Жадный и точный алгоритмы дали одинаковый результат.")
        else:
            print("\n⚠ Жадный алгоритм не оптимален! Используйте ДП.")
    else:
        print(f"\n(Проверка через ДП пропущена: n = {n} слишком велико.)")

    print("=" * 60)


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")