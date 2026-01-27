"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
7. Сочетания цикла и разветвления

244. Даны натуральное число n, действительные числа a1, …, an.
а) Выяснить, какое число встречается в последовательности a1,
…, an раньше – положительное или отрицательное. Если все члены
последовательности равны нулю, то сообщить об этом.
б) Найти номер первого члена последовательности a1, …, an;
если четных членов нет, то ответом должно быть число 0.
в) Найти номер последнего нечетного члена
последовательности a1, …, an; если нечетных членов нет, то ответом
должно быть число n+1.
"""


def is_integer(x: float) -> bool:
    """Проверяет, является ли число целым (с учетом погрешности)."""
    return abs(x - int(x)) < 1e-12

def is_even(x: float) -> bool:
    """Проверяет, является ли число четным."""
    if not is_integer(x):
        return False
    return int(x) % 2 == 0

def is_odd(x: float) -> bool:
    """Проверяет, является ли число нечетным."""
    if not is_integer(x):
        return False
    return int(x) % 2 == 1

def main():
    # Ввод данных
    n = int(input("Введите натуральное число n: "))
    if n <= 0:
        print("Ошибка: n должно быть натуральным числом.")
        return

    a = []
    for i in range(n):
        ai = float(input(f"Введите a[{i+1}]: "))
        a.append(ai)

    # a) Положительное или отрицательное встречается раньше?
    pos_index = None
    neg_index = None
    
    for i in range(n):
        if pos_index is None and a[i] > 0:
            pos_index = i + 1
        if neg_index is None and a[i] < 0:
            neg_index = i + 1
    
    print("\nа) Результат:")
    if pos_index is not None and neg_index is not None:
        if pos_index < neg_index:
            print(f"   Положительное число встречается раньше (на позиции {pos_index}).")
        elif neg_index < pos_index:
            print(f"   Отрицательное число встречается раньше (на позиции {neg_index}).")
        else:
            print("   Положительное и отрицательное числа найдены на одной позиции (невозможно).")
    elif pos_index is not None:
        print(f"   Только положительные числа, первое на позиции {pos_index}.")
    elif neg_index is not None:
        print(f"   Только отрицательные числа, первое на позиции {neg_index}.")
    else:
        # Проверяем, все ли нули
        all_zero = all(x == 0 for x in a)
        if all_zero:
            print("   Все члены последовательности равны нулю.")
        else:
            # В действительных числах ненулевое число либо положительное, либо отрицательное
            print("   Нет положительных и отрицательных чисел (все нули).")

    # б) Первый четный член
    print("\nб) Поиск первого четного члена:")
    first_even_index = None
    for i in range(n):
        if is_even(a[i]):
            first_even_index = i + 1
            break
    
    if first_even_index is not None:
        print(f"   Номер первого четного члена: {first_even_index}")
    else:
        print("   Четных членов нет. Ответ: 0.")

    # в) Последний нечетный член
    print("\nв) Поиск последнего нечетного члена:")
    last_odd_index = None
    for i in range(n-1, -1, -1):  # Идем с конца
        if is_odd(a[i]):
            last_odd_index = i + 1
            break
    
    if last_odd_index is not None:
        print(f"   Номер последнего нечетного члена: {last_odd_index}")
    else:
        print(f"   Нечетных членов нет. Ответ: {n + 1}.")

if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
