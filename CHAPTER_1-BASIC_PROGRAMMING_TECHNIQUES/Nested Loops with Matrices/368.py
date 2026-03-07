"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
11. Вложенные циклы в матричных задачах

368. Даны действительные числа a1,...,a10,b1,...,b20. Получить действительную матрицу |cij|i=1,...,20;j=1,...,10, для которой cj=aj/(1+abs(bi)).
"""


import random

def get_input():
    """Выбор способа ввода массивов a (10 чисел) и b (20 чисел)."""
    print("=== Задача 368: Формирование матрицы c_ij = a_j / (1 + |b_i|) ===")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод")
    print("2 — Случайная генерация")
    print("3 — Готовые примеры")

    choice = input("Ваш выбор (1/2/3): ").strip()
    while choice not in ('1', '2', '3'):
        choice = input("Выберите 1, 2 или 3: ").strip()

    if choice == '1':
        try:
            print("Введите 10 действительных чисел a1...a10 через пробел:")
            a_line = input().strip()
            a_tokens = a_line.split()
            if len(a_tokens) != 10:
                print("Ожидалось 10 чисел.")
                return None
            a = [float(x) for x in a_tokens]

            print("Введите 20 действительных чисел b1...b20 через пробел:")
            b_line = input().strip()
            b_tokens = b_line.split()
            if len(b_tokens) != 20:
                print("Ожидалось 20 чисел.")
                return None
            b = [float(x) for x in b_tokens]
            return a, b
        except ValueError:
            print("Ошибка ввода. Введите действительные числа.")
            return None

    elif choice == '2':
        a = [random.uniform(-10, 10) for _ in range(10)]
        b = [random.uniform(-10, 10) for _ in range(20)]
        print("\nСгенерированы массивы:")
        print("a =", [round(x, 3) for x in a])
        print("b =", [round(x, 3) for x in b])
        return a, b

    else:
        examples = [
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),
            ([1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5],
             [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
            ([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
             [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] * 2)
        ]
        print("\nГотовые примеры:")
        for i, (a_val, b_val) in enumerate(examples, 1):
            print(f"{i}. a = {a_val[:3]}..., b = {b_val[:5]}...")
        try:
            num = int(input("Выберите номер примера: "))
            if 1 <= num <= len(examples):
                a, b = examples[num-1]
                return a, b
            else:
                print("Неверный номер!")
                return None
        except ValueError:
            print("Ошибка ввода.")
            return None

def main():
    data = get_input()
    if data is None:
        return
    a, b = data
    n_rows = len(b)   # 20
    n_cols = len(a)   # 10
    # Формирование матрицы
    c = [[0.0] * n_cols for _ in range(n_rows)]
    for i in range(n_rows):
        denom = 1 + abs(b[i])
        for j in range(n_cols):
            c[i][j] = a[j] / denom

    print("\n" + "="*60)
    print("РЕЗУЛЬТАТ: матрица C (20 строк, 10 столбцов)")
    print("="*60)
    # Вывод матрицы с форматированием
    for i in range(n_rows):
        row_str = " ".join(f"{c[i][j]:8.4f}" for j in range(n_cols))
        print(f"i={i+1}: {row_str}")
    print("="*60)

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
