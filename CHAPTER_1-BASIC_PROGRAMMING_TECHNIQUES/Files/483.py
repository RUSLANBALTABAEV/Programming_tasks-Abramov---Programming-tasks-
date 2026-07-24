"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

483. Вычислить по схеме Горнера значение многочлена с рациональными коэффициентами для данного рационального значения переменной. Считать, что числители и знаменатели коэффициентов записаны в файле f : вначале числитель и знаменатель старшего коэффициента и т. д., в последнюю очередь числитель и знаменатель свободного члена *).
*) Во многих языках программирования (например, в Паскале) компоненты файла могут быть массивами. В этом случае можно предполагать, что числители и знаменатели образуют массивы длины 2. 
"""


import math
import random
import os


# ------------------------------------------------------------
# 1. Арифметика рациональных чисел
# ------------------------------------------------------------
def reduce_frac(num, den):
    if den == 0:
        raise ValueError("Знаменатель равен нулю.")
    if den < 0:
        num, den = -num, -den
    if num == 0:
        return 0, 1
    g = math.gcd(abs(num), den)
    return num // g, den // g


def add_frac(f1, f2):
    n1, d1 = f1
    n2, d2 = f2
    return reduce_frac(n1 * d2 + n2 * d1, d1 * d2)


def mul_frac(f1, f2):
    n1, d1 = f1
    n2, d2 = f2
    return reduce_frac(n1 * n2, d1 * d2)


def format_frac(f):
    num, den = f
    if den == 1:
        return str(num)
    return f"{num}/{den}"


# ------------------------------------------------------------
# 2. Вычисление по схеме Горнера
# ------------------------------------------------------------
def horner(coeffs, x):
    """coeffs: список кортежей (числитель, знаменатель) от старшей степени к свободному члену."""
    res = coeffs[0]
    for i in range(1, len(coeffs)):
        res = add_frac(mul_frac(res, x), coeffs[i])
    return res


# ------------------------------------------------------------
# 3. Ввод данных
# ------------------------------------------------------------
def get_data():
    """Формирует файл f с коэффициентами и возвращает также x."""
    print("Задача 483: Схема Горнера для рационального многочлена")
    print("Выберите способ задания коэффициентов (файл f):")
    print("1 — Ручной ввод")
    print("2 — Случайная генерация")
    print("3 — Готовый пример")

    while True:
        choice = input("Ваш выбор (1/2/3): ").strip()
        if choice in ('1', '2', '3'):
            break
        print("Ошибка: выберите 1, 2 или 3.")

    filename = "f.txt"

    if choice == '1':
        print("Введите коэффициенты, начиная со старшего. Для каждого коэффициента — два целых числа (числитель и знаменатель) через пробел.")
        print("После ввода всех коэффициентов введите пустую строку.")
        pairs = []
        while True:
            line = input()
            if line == "":
                break
            parts = line.split()
            if len(parts) != 2:
                print("Ошибка: нужно ровно два числа.")
                continue
            pairs.append((int(parts[0]), int(parts[1])))
        if len(pairs) == 0:
            print("Не введено ни одного коэффициента.")
            return None
        # Запись в файл
        with open(filename, 'w', encoding='utf-8') as f:
            for n, d in pairs:
                f.write(f"{n} {d} ")
            f.write('\n')
        print(f"Коэффициенты записаны в '{filename}'.")

    elif choice == '2':
        # Случайная генерация: степень от 2 до 4
        degree = random.randint(2, 4)
        pairs = []
        for _ in range(degree + 1):
            n = random.randint(-5, 5)
            d = random.randint(1, 5)
            pairs.append((n, d))
        with open(filename, 'w', encoding='utf-8') as f:
            for n, d in pairs:
                f.write(f"{n} {d} ")
            f.write('\n')
        print(f"Сгенерированы коэффициенты (степень {degree}): "
              f"{[format_frac(reduce_frac(n,d)) for n,d in pairs]}")
    else:
        # Готовый пример: 2x^2 + 3x + 1
        pairs = [(2, 1), (3, 1), (1, 1)]
        with open(filename, 'w', encoding='utf-8') as f:
            for n, d in pairs:
                f.write(f"{n} {d} ")
            f.write('\n')
        print(f"Готовый пример записан в '{filename}': "
              f"{[format_frac(reduce_frac(n,d)) for n,d in pairs]}")

    # Теперь ввод x
    print("Введите рациональное значение переменной x (числитель и знаменатель через пробел):")
    while True:
        try:
            parts = input().split()
            if len(parts) != 2:
                print("Нужно два целых числа.")
                continue
            x_num, x_den = int(parts[0]), int(parts[1])
            if x_den == 0:
                print("Знаменатель не может быть нулём.")
                continue
            x = reduce_frac(x_num, x_den)
            break
        except ValueError:
            print("Ошибка ввода.")

    # Чтение коэффициентов из файла
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            raw = list(map(int, f.read().split()))
        if len(raw) % 2 != 0:
            print("Ошибка: в файле нечётное количество чисел.")
            return None
        coeffs = []
        for i in range(0, len(raw), 2):
            n, d = raw[i], raw[i+1]
            if d == 0:
                print("Знаменатель коэффициента равен нулю.")
                return None
            coeffs.append(reduce_frac(n, d))
        return coeffs, x
    except Exception as e:
        print(f"Ошибка чтения файла: {e}")
        return None


# ------------------------------------------------------------
# 4. Основная программа
# ------------------------------------------------------------
def main():
    result = get_data()
    if result is None:
        return
    coeffs, x = result

    print("\nКоэффициенты (от старшего к свободному):")
    print([format_frac(c) for c in coeffs])
    print(f"x = {format_frac(x)}")

    value = horner(coeffs, x)
    print(f"\nЗначение многочлена: {format_frac(value)}")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
