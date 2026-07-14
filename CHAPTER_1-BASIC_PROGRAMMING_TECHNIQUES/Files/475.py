"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

475. Последовательность x1, x2, ... образована по закону
    x_i = (i - 0.1) / (i^3 + |tg(2*i)|), i = 1, 2, ...
Дано действительное ε > 0. Записать в файл h члены последовательности
x1, x2, ..., остановившись после первого члена, для которого |x_i| < ε.
"""


import math
import random


def compute_and_write(epsilon, filename="h.txt"):
    """
    Вычисляет члены последовательности x_i, пока не будет выполнено |x_i| < epsilon.
    Записывает все вычисленные члены в файл (включая последний, удовлетворяющий условию).
    Возвращает список вычисленных значений.
    """
    results = []
    i = 1
    while True:
        numerator = i - 0.1
        denominator = i ** 3 + abs(math.tan(2 * i))
        xi = numerator / denominator
        results.append(xi)
        if abs(xi) < epsilon:
            break
        i += 1

    with open(filename, 'w', encoding='utf-8') as f:
        for num in results:
            f.write(f"{num:.8f}\n")
    return results


def get_epsilon():
    """Выбор способа ввода ε."""
    print("Задача 475: Запись последовательности x_i в файл h")
    print("Выберите способ ввода ε > 0:")
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
                eps = float(input("Введите ε > 0: "))
                if eps <= 0:
                    print("ε должно быть положительным.")
                    continue
                return eps
            except ValueError:
                print("Ошибка ввода.")

    elif choice == '2':
        # Генерируем случайное ε в диапазоне от 0.0001 до 0.1
        eps = 10 ** random.uniform(-4, -1)   # от 1e-4 до 1e-1
        print(f"Случайно выбрано ε = {eps:.6f}")
        return eps

    else:
        examples = [0.1, 0.01, 0.001, 0.0001]
        print("Готовые примеры ε:", examples)
        while True:
            try:
                num = int(input(f"Выберите номер примера (1 - {len(examples)}): "))
                if 1 <= num <= len(examples):
                    return examples[num - 1]
                else:
                    print(f"Номер от 1 до {len(examples)}.")
            except ValueError:
                print("Введите целое число.")


def main():
    epsilon = get_epsilon()
    print(f"\nГенерация последовательности до |x_i| < {epsilon} ...")
    results = compute_and_write(epsilon)

    print(f"\nВсего записано членов: {len(results)}")
    print(f"Последний член (x_{len(results)}): {results[-1]:.8f}, |x| = {abs(results[-1]):.8f}")
    print(f"Файл 'h.txt' создан.")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
