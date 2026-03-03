"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
10. Вложенные циклы

344. Даны действительные числа a1, ... ,a10, натуральное число m. Последовательность b1,b2,... образована по закону
b1 = a1, ..., b10 = a10,
bk = bk-1+bk-2+...+bk-10, k=11, 12, ... 
Получить bm.
"""


import random

def get_input():
    """Выбор способа ввода a1...a10 и m."""
    print("Выберите способ ввода:")
    print("1 - Ручной ввод")
    print("2 - Случайная генерация")
    print("3 - Готовый пример")
    choice = input("Ваш выбор (1/2/3): ").strip()
    while choice not in ('1', '2', '3'):
        choice = input("Некорректно. Выберите 1, 2 или 3: ")

    if choice == '1':
        try:
            print("Введите 10 действительных чисел a1...a10 через пробел:")
            line = input().strip()
            tokens = line.split()
            if len(tokens) != 10:
                print("Ожидалось 10 чисел.")
                return None
            a = [float(t) for t in tokens]
            m = int(input("Введите натуральное число m: "))
            if m <= 0:
                print("m должно быть положительным.")
                return None
            return a, m
        except ValueError:
            print("Ошибка ввода.")
            return None

    elif choice == '2':
        a = [random.uniform(-10, 10) for _ in range(10)]
        m = random.randint(1, 50)  # ограничим, чтобы избежать огромных чисел
        print(f"Сгенерировано: a = {a}")
        print(f"m = {m}")
        return a, m

    else:  # choice == '3'
        examples = [
            ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 15),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 20),
            ([0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 30),
            ([ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 12),
            ([1, 2, 4, 8, 16, 32, 64, 128, 256, 512], 15)
        ]
        print("Готовые примеры (a, m):")
        for idx, (a_vals, m_val) in enumerate(examples, 1):
            print(f"{idx}: a = {a_vals}, m = {m_val}")
        try:
            idx = int(input("Выберите номер примера: "))
            if 1 <= idx <= len(examples):
                a, m = examples[idx-1]
                return a, m
            else:
                print("Неверный номер.")
                return None
        except ValueError:
            print("Ошибка ввода.")
            return None

def compute_bm(a, m):
    """Вычисляет b_m для последовательности, где b_k = sum_{i=k-10}^{k-1} b_i (k>10)."""
    if m <= 10:
        return a[m-1]
    # Храним последние 10 значений в виде очереди
    last = a[:]  # копия
    for k in range(11, m+1):
        next_val = sum(last)
        # сдвигаем: удаляем первый, добавляем новый
        last.pop(0)
        last.append(next_val)
    return last[-1]

def main():
    data = get_input()
    if data is None:
        return
    a, m = data
    print("\n" + "="*60)
    print("a =", a)
    print("m =", m)
    print("="*60)

    result = compute_bm(a, m)
    print(f"\nb_{m} = {result}")

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
