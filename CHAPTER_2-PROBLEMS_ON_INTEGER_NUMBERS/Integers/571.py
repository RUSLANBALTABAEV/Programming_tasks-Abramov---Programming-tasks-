"""
ГЛАВА 2
ЗАДАЧИ ПО ТЕМАМ
15. Целые числа.

571. Показать, что если x1, y1, x2, y2 - два целочисленных решения уравнения kx + ly = m, то x1 - x2, y1 - y2 - целочисленное решение уравнения kx + ly = 0. Вывести отсюда, что если x, y - какое-нибудь целочисленное решение уравнения kx + ly = m, то все целочисленные решения этого уравнения описываются формулами x = x2 + l't, y = y2 - k't, где k2 = k / НОД(k, l), l2 = l / НОД(k, l) t = (0, +- 1, +- 2, ...). Написать программу, которая позволяет проверить, обладает ли уравнение k * x + l * y = m решением в целых неотрицательных числах, и если обладает, то позволяет построить какое-то одно такое решение. 
"""


import random
import math


# ------------------------------------------------------------
# 1. Итеративный расширенный алгоритм Евклида
# ------------------------------------------------------------
def egcd(a, b):
    """Итеративный расширенный алгоритм Евклида для a, b >= 0.
       Возвращает (g, x, y), где a * x + b * y = g = НОД(a, b)."""
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    return old_r, old_s, old_t


def extended_gcd_signed(f, g):
    """(d, u, v), такие что f * u + g * v = d = НОД(|f|, |g|)."""
    if f == 0 and g == 0:
        raise ValueError("f и g не могут быть одновременно нулями")
    if f == 0:
        return abs(g), 0, (1 if g > 0 else -1)
    if g == 0:
        return abs(f), (1 if f > 0 else -1), 0

    a, b = abs(f), abs(g)
    d, x, y = egcd(a, b)
    u = x if f > 0 else -x
    v = y if g > 0 else -y
    return d, u, v


# ------------------------------------------------------------
# 2. Целочисленное деление с округлением вниз/вверх
# ------------------------------------------------------------
def floor_div(a, b):
    return a // b


def ceil_div(a, b):
    return -((-a) // b)


# ------------------------------------------------------------
# 3. Все неотрицательные решения
# ------------------------------------------------------------
def solve_nonnegative(k, l, m):
    """
    Возвращает список пар (x, y), x >= 0, y >= 0, k * x + l * y = m.
    Список может быть пустым.
    """
    # Особые случаи
    if k == 0 and l == 0:
        if m == 0:
            return [(0, 0)]   # любое неотрицательное решение; берём (0,0)
        return []

    d, u, v = extended_gcd_signed(k, l)
    if m % d != 0:
        return []

    factor = m // d
    x0, y0 = u * factor, v * factor

    A = l // d       # шаг по x
    B = k // d       # шаг по y (со знаком минус в общем решении)

    # x = x0 + A*t >= 0  →  границы для t
    L = None
    U = None

    if A > 0:
        L = ceil_div(-x0, A)
    elif A < 0:
        U = floor_div(-x0, A)
    else:
        if x0 < 0:
            return []

    if B > 0:
        bound = floor_div(y0, B)
        U = bound if U is None else min(U, bound)
    elif B < 0:
        bound = ceil_div(y0, B)
        L = bound if L is None else max(L, bound)
    else:
        if y0 < 0:
            return []

    # Собираем диапазон допустимых t
    if L is None and U is None:
        t_range = [0]
    elif L is None:
        t_range = [U]
    elif U is None:
        t_range = [L]
    else:
        if L > U:
            return []
        t_range = range(L, U + 1)

    solutions = []
    for t in t_range:
        x = x0 + A * t
        y = y0 - B * t
        if x >= 0 and y >= 0 and k * x + l * y == m:
            solutions.append((x, y))
    return solutions


# ------------------------------------------------------------
# 4. Грубая проверка (для отладки и наглядности)
# ------------------------------------------------------------
def brute_force(k, l, m, limit = 1000):
    """Переборный поиск неотрицательных решений для малых значений."""
    result = []
    for x in range(0, limit + 1):
        rem = m - k * x
        if rem < 0:
            continue
        if l != 0 and rem % l == 0:
            y = rem // l
            if y >= 0:
                result.append((x, y))
        elif l == 0 and rem == 0:
            result.append((x, 0))
    return result


# ------------------------------------------------------------
# 5. Ввод данных
# ------------------------------------------------------------
def get_params():
    """Выбор способа ввода k, l, m."""
    print("Задача 571: Решение уравнения kx + ly = m в неотрицательных числах")
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
                k = int(input("Введите k: "))
                l = int(input("Введите l: "))
                m = int(input("Введите m: "))
                if k == 0 and l == 0:
                    print("k и l не могут быть нулями одновременно.")
                    continue
                return k, l, m
            except ValueError:
                print("Ошибка ввода. Введите целые числа.")

    elif choice == '2':
        k = random.randint(-10, 10)
        l = random.randint(-10, 10)
        while k == 0 and l == 0:
            l = random.randint(-10, 10)
        m = random.randint(-50, 50)
        print(f"\nСгенерированы: k = {k}, l = {l}, m = {m}")
        return k, l, m

    else:  # готовые примеры
        examples = [
            (4, 6, 10),      # есть решения (1,1), (4,0) и т.д.
            (4, 6, 5),       # нет решений (m не делится на НОД=2)
            (7, 11, 100),    # классический пример
            (5, 0, 15),      # вырожденный случай: l = 0
            (0, 5, 20),      # вырожденный случай: k = 0
            (-3, 4, 5),      # с отрицательным коэффициентом
        ]
        print("\nГотовые примеры (k, l, m):")
        for idx, (kv, lv, mv) in enumerate(examples, 1):
            print(f"{idx}: k = {kv}, l = {lv}, m = {mv}")
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
# 6. Основная программа
# ------------------------------------------------------------
def main():
    k, l, m = get_params()

    print(f"\nУравнение: {k} * x + {l} * y = {m}")
    print("=" * 55)

    # Расширенный НОД и частное решение
    if k == 0 and l == 0:
        print("Случай k = l = 0 разобран отдельно.")
    else:
        d, u, v = extended_gcd_signed(k, l)
        print(f"НОД(|{k}|, |{l}|) = {d}")
        print(f"Частное решение вспомогательного уравнения "
              f"{k} * u + {l} * v = {d}:")
        print(f"   u = {u}, v = {v}  →  {k} * {u} + {l} * {v} = {d}")

        if m % d != 0:
            print(f"\n{m} не делится на {d} — целых решений нет.")
        else:
            x0, y0 = u * (m // d), v * (m // d)
            print(f"\nЧастное решение исходного уравнения:")
            print(f"   x0 = {x0}, y0 = {y0}")
            print(f"   Проверка: {k} * {x0} + {l} * {y0} = {k * x0 + l * y0}")

    print("-" * 55)

    # Все неотрицательные решения
    solutions = solve_nonnegative(k, l, m)

    if not solutions:
        print("Уравнение НЕ имеет решений в целых неотрицательных числах.")
    else:
        print(f"Найдено неотрицательных решений: {len(solutions)}")
        # Показываем первые 10
        for i, (x, y) in enumerate(solutions[:10], 1):
            print(f"   {i:>2}. x = {x:>4}, y = {y:>4}  "
                  f"| {k} * {x} + {l} * {y} = {k * x + l * y}")
        if len(solutions) > 10:
            print(f"   ... и ещё {len(solutions) - 10} решений.")

        # Для сравнения: перебор (только если значения не слишком большие)
        if abs(m) <= 1000 and abs(k) <= 50 and abs(l) <= 50:
            brute = brute_force(k, l, m, limit=200)
            print(f"\nПроверка перебором: найдено {len(brute)} решений.")
            if len(brute) == len(solutions):
                print("   Результаты совпадают. ✔")
            else:
                print("   ⚠ Расхождение — возможно, ограничение перебора "
                      "или ошибка в алгоритме.")

    print("=" * 55)


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")