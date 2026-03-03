"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
10. Вложенные циклы

346. Даны натуральное число k , действительное число a, (a>0).
Последовательность x0,x1, .... образована по закону
x0 = a, xi = (k - 1) / k * xi-1 + a / (x^k-1 i - 1), i=1, 2, .... .
Найти первое значение xn, для которого abs(xn ^ k - a) < 10^-4
(последовательность, x0,x1, … сходится к pow(sqrt(a), 1/k).
"""


import random

def get_input():
    """Выбор способа ввода k и a."""
    print("Выберите способ ввода:")
    print("1 - Ручной ввод")
    print("2 - Случайная генерация")
    print("3 - Готовый пример")
    choice = input("Ваш выбор (1/2/3): ").strip()
    while choice not in ('1', '2', '3'):
        choice = input("Некорректно. Выберите 1, 2 или 3: ")

    if choice == '1':
        try:
            k = int(input("Введите натуральное число k (>0): "))
            if k <= 0:
                print("k должно быть положительным.")
                return None
            a = float(input("Введите действительное число a (>0): "))
            if a <= 0:
                print("a должно быть положительным.")
                return None
            return k, a
        except ValueError:
            print("Ошибка ввода.")
            return None

    elif choice == '2':
        k = random.randint(1, 10)
        a = random.uniform(0.1, 100)
        print(f"Сгенерировано: k = {k}, a = {a:.6f}")
        return k, a

    else:  # choice == '3'
        examples = [
            (2, 2.0),
            (3, 27.0),
            (4, 16.0),
            (5, 32.0),
            (2, 0.5),
            (3, 8.0)
        ]
        print("Готовые примеры (k, a):")
        for idx, (k_val, a_val) in enumerate(examples, 1):
            print(f"{idx}: k = {k_val}, a = {a_val}")
        try:
            idx = int(input("Выберите номер примера: "))
            if 1 <= idx <= len(examples):
                return examples[idx-1]
            else:
                print("Неверный номер.")
                return None
        except ValueError:
            print("Ошибка ввода.")
            return None

def main():
    data = get_input()
    if data is None:
        return
    k, a = data
    print("\n" + "="*60)
    print(f"k = {k}, a = {a}")
    print("="*60)

    x = a
    n = 0
    eps = 1e-4
    max_iter = 1000
    while n <= max_iter:
        val = x**k
        if abs(val - a) < eps:
            print(f"\nНайдено x_{n} = {x}")
            print(f"x_{n}^{k} = {val}, |{val} - {a}| = {abs(val - a)} < 1e-4")
            break
        # вычисляем следующее
        x = ((k-1)/k) * x + a / (x**k)
        n += 1
    else:
        print("Не удалось достичь точности за максимальное число итераций.")

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
