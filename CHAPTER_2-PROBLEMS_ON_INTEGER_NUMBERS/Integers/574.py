"""
ГЛАВА 2
ЗАДАЧИ ПО ТЕМАМ
15. Целые числа.

574. Известная в теории чисел китайская теорема об остатках утверждает следующее. Пусть p1, ..., pr - попарно взаимно простые натуральное числа; пусть v = p1...pr. Пусть a1, ..., ar, - такие целые неотрицательные числа, что a1 < p1, ..., ar < pr. Тогда существует ровно одно целое неотрицательное u < v, которое при делении на p1, дает остаток a1, при делении на p2, дает остаток a2, ..., при делении на pr, дает остаток ar. (Процесс восстановления числа по его остаткам был известен в Китае уже около 2000 лет назад, поэтому теорема и имеет такое название.) Если даны p1, ..., pr, a1, ..., ar то на основании этой теоремы число u может быть найдено последовательной проверкой чисел 0, 1, ..., v - 1. Однако есть алгоритм значительно более быстрого решения этой задачи, который мы сформулируем без доказательства (имеет смысл попытаться самостоятельно найти доказательство). Обозначим через vi (1 <= i <= r) произведение всех pi, ..., pr кроме pi, т.е. vi = pi...pi-1 * pi+1...pr = v / pi. Пусть числа wi * (1 <= i <= r) таковы, что 1 <= wi < pi и vi * wi при делении на pi дает  остаток 1 (см. предыдующую задачу). Тогда можно положить u равным остатку от деления v1 * w1 * a1 + ... + vr * wr * ar на v. Например, если p1, p2, p3, p4 равно соответственно 2, 3, 5, 7, а a1, a2, a3, a4 равны соответственно 1, 2, 4, 3, то получится u = 59. Проверка показывает, что u удовлетворяет условию задачи: 59 < 2 * 3 * 5 * 7, 59 = 2 * 29 + 1 = 3 * 19 + 2 = 5 * 11 + 4 = 7 * 8 + 3.
Даны натуральное числа r, p1, ..., pr, целые неотрицательные числа a1, ..., ar, (p1, ..., pr - попарно взаимно простые, a1 < p1, ..., ar < pr). Найти u, удовлетворяющие сформулированным выше условиям.
"""


import random
import math


# ------------------------------------------------------------
# 1. Расширенный алгоритм Евклида (итеративный)
# ------------------------------------------------------------
def egcd(a, b):
    """Возвращает (g, x, y), где a*x + b*y = g = НОД(a, b). a,b >= 0."""
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    return old_r, old_s, old_t


def mod_inverse(a, m):
    """
    Возвращает x такое, что a*x ≡ 1 (mod m), 0 < x < m.
    Предполагается, что gcd(a, m) = 1.
    """
    g, x, _ = egcd(a % m, m)
    if g != 1:
        raise ValueError(f"Обратного элемента не существует: gcd({a}, {m}) = {g}")
    return x % m


# ------------------------------------------------------------
# 2. Решение системы сравнений (CRT)
# ------------------------------------------------------------
def chinese_remainder(p_list, a_list):
    """
    Возвращает u (0 <= u < v) такой, что u ≡ a_i (mod p_i) для всех i.
    p_list — попарно взаимно простые натуральные числа.
    a_list — неотрицательные целые, a_i < p_i.
    """
    r = len(p_list)
    v = 1
    for p in p_list:
        v *= p

    total = 0
    for i in range(r):
        pi = p_list[i]
        ai = a_list[i]
        vi = v // pi
        wi = mod_inverse(vi, pi)
        total += vi * wi * ai

    return total % v


# ------------------------------------------------------------
# 3. Проверка входных данных
# ------------------------------------------------------------
def validate(p_list, a_list):
    """Проверяет корректность входных данных."""
    if len(p_list) != len(a_list):
        return False, "Количество p и a должно совпадать."
    for p in p_list:
        if p < 2:
            return False, f"p = {p} должно быть >= 2."
    for i in range(len(a_list)):
        if not (0 <= a_list[i] < p_list[i]):
            return False, f"a[{i}] = {a_list[i]} должно быть в диапазоне [0; {p_list[i]-1}]."
    # Проверка попарной взаимной простоты
    for i in range(len(p_list)):
        for j in range(i + 1, len(p_list)):
            if math.gcd(p_list[i], p_list[j]) != 1:
                return False, f"p{i+1} = {p_list[i]} и p{j+1} = {p_list[j]} не взаимно просты."
    return True, ""


# ------------------------------------------------------------
# 4. Генерация случайного теста
# ------------------------------------------------------------
def generate_test(r=None):
    """Генерирует попарно взаимно простые p и допустимые a."""
    if r is None:
        r = random.randint(2, 5)
    p_list = []
    used = set()
    while len(p_list) < r:
        # Генерируем простые числа (или хотя бы взаимно простые с уже выбранными)
        candidate = random.randint(2, 50)
        if candidate in used:
            continue
        ok = True
        for p in p_list:
            if math.gcd(candidate, p) != 1:
                ok = False
                break
        if ok:
            p_list.append(candidate)
            used.add(candidate)
    a_list = [random.randint(0, p - 1) for p in p_list]
    return p_list, a_list


# ------------------------------------------------------------
# 5. Ввод данных
# ------------------------------------------------------------
def get_params():
    print("Задача 574: Китайская теорема об остатках")
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
                r = int(input("Введите количество уравнений r (>= 2): "))
                if r < 2:
                    print("r должно быть >= 2.")
                    continue
                print(f"Введите {r} попарно взаимно простых натуральных чисел p1..pr (через пробел):")
                p_list = list(map(int, input().split()))
                if len(p_list) != r:
                    print(f"Ожидалось {r} чисел.")
                    continue
                print(f"Введите {r} неотрицательных чисел a1..ar (ai < pi), через пробел:")
                a_list = list(map(int, input().split()))
                if len(a_list) != r:
                    print(f"Ожидалось {r} чисел.")
                    continue
                ok, msg = validate(p_list, a_list)
                if not ok:
                    print("Ошибка:", msg)
                    continue
                return p_list, a_list
            except ValueError:
                print("Ошибка ввода. Введите целые числа.")

    elif choice == '2':
        p_list, a_list = generate_test()
        print(f"\nСгенерированы: p = {p_list}")
        print(f"                a = {a_list}")
        return p_list, a_list

    else:  # готовые примеры
        examples = [
            ([2, 3, 5, 7], [1, 2, 4, 3]),         # пример из условия: u = 59
            ([3, 5, 7], [2, 3, 2]),
            ([4, 9, 25], [3, 5, 7]),             # попарно взаимно простые, но не простые
            ([11, 13, 17], [5, 7, 9]),
        ]
        print("\nГотовые примеры (p, a):")
        for idx, (pv, av) in enumerate(examples, 1):
            print(f"{idx}: p = {pv}")
            print(f"   a = {av}")
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
    p_list, a_list = get_params()
    r = len(p_list)

    # Произведение всех p
    v = 1
    for p in p_list:
        v *= p

    print(f"\nr = {r}")
    print(f"p = {p_list}")
    print(f"a = {a_list}")
    print(f"v = p1*...*pr = {v}")
    print("=" * 60)

    # Для каждого i вычисляем vi, wi
    print("Вычисления по китайской теореме об остатках:")
    total = 0
    for i in range(r):
        pi = p_list[i]
        ai = a_list[i]
        vi = v // pi
        wi = mod_inverse(vi, pi)
        term = vi * wi * ai
        total += term
        print(f"  i = {i+1}: p{i+1} = {pi}, a{i+1} = {ai}")
        print(f"    v{i+1} = v / p{i+1} = {vi}")
        print(f"    w{i+1} = обратный к v{i+1} mod p{i+1} = {wi}")
        print(f"    Проверка: {vi} * {wi} mod {pi} = {(vi * wi) % pi}")
        print(f"    Слагаемое: v{i+1} * w{i+1} * a{i+1} = {term}")

    u = total % v
    print("-" * 60)
    print(f"Сумма всех слагаемых: {total}")
    print(f"Искомое u = {total} mod {v} = {u}")

    # Проверка
    print("\nПроверка (u mod pi должно равняться ai):")
    for i in range(r):
        rem = u % p_list[i]
        ok = "✔" if rem == a_list[i] else " ’"
        print(f"  u mod {p_list[i]} = {rem}   (ожидалось {a_list[i]})  {ok}")

    print("=" * 60)


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")