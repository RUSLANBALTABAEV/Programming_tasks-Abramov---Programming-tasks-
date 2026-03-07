"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
11. Вложенные циклы в матричных задачах

372. Получить действительную матрицу |aij|i,j=1,...,7, первая строка которой задается формулой aj=2 * j + 3 * (j = 1,...,7), вторая строка задается формулой a2j = j - 3 / 2 + 1 / j * (j = 1,...,7),  а каждая следующая строка есть сумма двух предыдущих.
"""


import random

def get_m():
    """Выбор способа ввода количества строк m (≥2)."""
    print("=== Задача 372: Формирование матрицы по рекуррентному правилу ===")
    print("Выберите способ ввода количества строк m:")
    print("1 — Ручной ввод")
    print("2 — Случайная генерация")
    print("3 — Готовые примеры")

    choice = input("Ваш выбор (1/2/3): ").strip()
    while choice not in ('1', '2', '3'):
        choice = input("Выберите 1, 2 или 3: ").strip()

    if choice == '1':
        try:
            m = int(input("Введите количество строк m (≥2): "))
            if m < 2:
                print("m должно быть не меньше 2.")
                return None
            return m
        except ValueError:
            print("Ошибка ввода.")
            return None

    elif choice == '2':
        m = random.randint(2, 15)
        print(f"Сгенерировано m = {m}")
        return m

    else:
        examples = [3, 5, 7, 10, 12]
        print("\nГотовые примеры:")
        for i, val in enumerate(examples, 1):
            print(f"{i}. m = {val}")
        try:
            num = int(input("Выберите номер примера: "))
            if 1 <= num <= len(examples):
                return examples[num-1]
            else:
                print("Неверный номер!")
                return None
        except ValueError:
            print("Ошибка ввода.")
            return None

def compute_matrix(m):
    """Возвращает матрицу размером m x 7, где первые две строки заданы формулами."""
    n_cols = 7
    # Инициализируем матрицу нулями
    a = [[0.0] * n_cols for _ in range(m)]

    # Заполняем первую строку: a[0][j] = 2*(j+1) + 3, так как j от 1 до 7
    for j in range(n_cols):
        a[0][j] = 2 * (j + 1) + 3

    # Вторая строка: a[1][j] = (j+1) - 3 / (2 + 1/(j+1))
    for j in range(n_cols):
        j1 = j + 1
        a[1][j] = j1 - 3 / (2 + 1.0 / j1)

    # Остальные строки
    for i in range(2, m):
        for j in range(n_cols):
            a[i][j] = a[i-1][j] + a[i-2][j]

    return a

def print_matrix(a, m):
    print(f"\nМатрица размером {m} x 7:")
    for i in range(m):
        row_str = " ".join(f"{a[i][j]:10.6f}" for j in range(7))
        print(f"Строка {i+1}: {row_str}")

def main():
    m = get_m()
    if m is None:
        return
    a = compute_matrix(m)
    print_matrix(a, m)

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
