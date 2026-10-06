"""
ГЛАВА 2
ЗАДАЧИ ПО ТЕМАМ
15. Целые числа.

573. Даны натуральные взаимно простые числа n, p. Используя алгоритм, описанный в задаче 570а, найти натуральное m такое, что, во-первых, m < p и, во-вторых -nm при делении на р дает остаток 1.
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


def extended_gcd_signed(n, p):
    """Возвращает (d, u, v), где n * u + p * v = d = НОД(|n|, |p|)."""
    if n == 0 and p == 0:
        raise ValueError("n и p не могут быть одновременно нулями")
    a, b = abs(n), abs(p)
    d, x, y = egcd(a, b)
    u = x if n > 0 else -x
    v = y if p > 0 else -y
    return d, u, v


# ------------------------------------------------------------
# 2. Нахождение m
# ------------------------------------------------------------
def find_m(n, p):
    """
    Возвращает m, 0 < m < p, такое что (-n * m) mod p == 1.
    Возвращает None, если условие невыполнимо.
    """
    if p <= 1:
        return None   # при p = 1 остаток всегда 0
    d, u, v = extended_gcd_signed(n, p)
    if d != 1:
        return None   # числа не взаимно просты
    # n*u ≡ 1 (mod p)  =>  m ≡ -u (mod p)
    m = (-u) % p
    if m == 0:
        m = p         # теоретически невозможно, оставлено для защиты
    if not (1 <= m < p):
        return None
    if (-n * m) % p != 1:
        return None
    return m, d, u, v


# ------------------------------------------------------------
# 3. Ввод данных
# ------------------------------------------------------------
def get_params():
    """Выбор способа ввода n и p."""
    print("Задача 573: Поиск m такого, что (-n * m) mod p = 1")
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
                n = int(input("Введите натуральное число n: "))
                p = int(input("Введите натуральное число p (> 1): "))
                if n <= 0 or p <= 1:
                    print("n > 0, p > 1 (иначе условие невыполнимо).")
                    continue
                return n, p
            except ValueError:
                print("Ошибка ввода. Введите целые числа.")

    elif choice == '2':
        p = random.randint(2, 100)
        # Выбираем n взаимно простое с p
        while True:
            n = random.randint(1, p - 1)
            if __import__('math').gcd(n, p) == 1:
                break
        print(f"\nСгенерированы: n = {n}, p = {p}")
        return n, p

    else:  # готовые примеры
        examples = [
            (3, 7),     # m = 5? проверим: (-3 * 5) mod 7 = -15 mod 7 = 6, нет. m = 2: -6 mod7 = 1
            (5, 12),    # m = 7? (-35) mod 12 = 1, да
            (7, 11),    # m = 8? (-56) mod 11 = -1 = 10; m = 3: -21 mod11 = 1
            (4, 9),     # m = 2? (-8) mod9 = 1
            (10, 17),   # m = 12? (-120) mod17 = -120 + 136 = 16; m = 5: -50 + 51 = 1
        ]
        print("\nГотовые примеры (n, p):")
        for idx, (nv, pv) in enumerate(examples, 1):
            print(f"{idx}: n = {nv}, p = {pv}")
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
    n, p = get_params()

    print(f"\nИсходные данные: n = {n}, p = {p}")
    print("=" * 55)

    result = find_m(n, p)
    if result is None:
        print("Условие задачи невыполнимо: числа не взаимно просты,")
        print("или p <= 1, или решение не существует.")
        return

    m, d, u, v = result

    print(f"НОД({n}, {p}) = {d}")
    print(f"Расширенный алгоритм Евклида:")
    print(f"  {n} * ({u}) + {p} * ({v}) = {n * u + p * v}")
    print(f"  => {n} * ({u}) ≡ 1 (mod {p})")
    print(f"\nИскомое m = {m}")
    print(f"Условие m < p: {m} < {p} — {m < p}")
    print(f"Проверка: (-{n} * {m}) mod {p} = {(-n * m) % p}")
    print("=" * 55)


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")