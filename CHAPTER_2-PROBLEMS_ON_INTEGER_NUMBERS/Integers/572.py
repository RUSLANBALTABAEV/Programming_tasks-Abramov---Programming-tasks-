"""
ГЛАВА 2
ЗАДАЧИ ПО ТЕМАМ
15. Целые числа.

572. Даны натуральное число k, одновременно не равные 0 целые числа n1, ..., nk. Найти НОД(abs(n1), ..., abs(nk)) и целые u1, ..., uk такие, что u1 * n1 + ... + uk * nk = НОД(abs(n1), ..., abs(nk))(см. задачу 333).
"""


import random


# ------------------------------------------------------------
# 1. Итеративный расширенный алгоритм Евклида
# ------------------------------------------------------------
def egcd(a, b):
    """Возвращает (g, x, y), где a * x + b * y = g = НОД(a, b). a,b >= 0."""
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    return old_r, old_s, old_t


# ------------------------------------------------------------
# 2. НОД нескольких чисел с линейным представлением
# ------------------------------------------------------------
def gcd_multiple_with_coeffs(nums):
    """
    Возвращает (g, coeffs), где g = НОД(|nums[0]|, ..., |nums[k-1]|),
    и sum(coeffs[i] * nums[i]) = g.
    """
    # Отбрасываем нули? Нет, обрабатываем аккуратно.
    # Начнём с первого ненулевого числа, если оно есть.
    # Если все нули — это нарушение условия, но защитимся.
    non_zero_idx = None
    for i, x in enumerate(nums):
        if x != 0:
            non_zero_idx = i
            break
    if non_zero_idx is None:
        return 0, [0] * len(nums)  # все нули — НОД = 0, коэффициенты любые

    # Стартуем с первого ненулевого
    g = abs(nums[non_zero_idx])
    coeffs = [0] * len(nums)
    coeffs[non_zero_idx] = 1 if nums[non_zero_idx] > 0 else -1

    # Проходим по остальным числам
    for i in range(len(nums)):
        if i == non_zero_idx:
            continue
        ni = nums[i]
        new_g, x, y = egcd(g, abs(ni))
        # Обновляем старые коэффициенты
        coeffs = [c * x for c in coeffs]
        # Добавляем коэффициент для нового числа (с учётом знака)
        coeffs[i] = y if ni > 0 else -y
        g = new_g

    return g, coeffs


# ------------------------------------------------------------
# 3. Ввод данных
# ------------------------------------------------------------
def get_params():
    """Выбор способа ввода k и последовательности n1..nk."""
    print("Задача 572: НОД нескольких чисел и его линейное представление")
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
                k = int(input("Введите количество чисел k (k >= 1): "))
                if k < 1:
                    print("k должно быть >= 1.")
                    continue
                print(f"Введите {k} целых чисел через пробел "
                      f"(не все нули):")
                nums = list(map(int, input().split()))
                if len(nums) != k:
                    print(f"Ожидалось {k} чисел, получено {len(nums)}.")
                    continue
                if all(x == 0 for x in nums):
                    print("Не все числа могут быть нулями.")
                    continue
                return k, nums
            except ValueError:
                print("Ошибка ввода. Введите целые числа.")

    elif choice == '2':
        k = random.randint(2, 6)
        nums = [random.randint(-50, 50) for _ in range(k)]
        # Гарантируем, что не все нули
        if all(x == 0 for x in nums):
            nums[0] = 1
        print(f"\nСгенерированы: k = {k}, числа = {nums}")
        return k, nums

    else:  # готовые примеры
        examples = [
            (3, [12, 18, 24]),          # НОД = 6
            (4, [30, -42, 56, 70]),     # НОД = 2
            (2, [0, 7]),                # один ноль
            (3, [0, 0, 5]),             # два нуля
            (5, [100, 200, 300, 400, 500]),
            (3, [7, 13, 19]),           # взаимно простые
        ]
        print("\nГотовые примеры (k, числа):")
        for idx, (kv, nums_v) in enumerate(examples, 1):
            print(f"{idx}: k = {kv}, nums = {nums_v}")
        while True:
            try:
                num = int(input("Выберите номер примера: "))
                if 1 <= num <= len(examples):
                    return examples[num - 1]
                else:
                    print(f"Номер должен быть от 1 до {len(examples)}.")
            except ValueError:
                print("Ошибка ввода. Введите целое число.")


# ------------------------------------------------------------
# 4. Основная программа
# ------------------------------------------------------------
def main():
    k, nums = get_params()

    g, coeffs = gcd_multiple_with_coeffs(nums)

    print(f"\nИсходные числа: {nums}")
    print("=" * 60)
    print(f"НОД(|n1|, ..., |nk|) = {g}")

    print("\nКоэффициенты u1, ..., uk:")
    for i, (n, c) in enumerate(zip(nums, coeffs), 1):
        print(f"  u{i} = {c:>5}   (при n{i} = {n})")

    terms = [f"({c}) * {n}" for c, n in zip(coeffs, nums)]
    expression = " + ".join(terms)
    total = sum(c * n for c, n in zip(coeffs, nums))

    print("\nЛинейная комбинация:")
    print(f"  {expression}")
    print(f"  = {total}")

    if total == g:
        print(f"\n✅ Проверка пройдена: сумма = НОД = {g}")
    else:
        print(f"\n❌ Ошибка: сумма = {total}, а НОД = {g}")
    print("=" * 60)


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")