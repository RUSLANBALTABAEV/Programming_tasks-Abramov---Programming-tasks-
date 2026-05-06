"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
11. Вложенные циклы в матричных задачах

406. С помощью [xij] i = 1, 2; j = 1. ..., n - действительной матрицы на плоскости задано n точек так, что x1j, 2j - координат j-точки. Точки попарно соединены отрезками. Найти длину наибольшего отрезка.
"""


import random
import math

def get_matrix():
    """Выбор способа ввода матрицы 2xn с координатами точек."""
    print("Задача 406: Длина наибольшего отрезка среди n точек на плоскости")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод")
    print("2 — Случайная числа")
    print("3 — Готовые примеры")

    while True:
        choice = input("Ваш выбор (1/2/3): ").strip()
        if choice in ('1', '2', '3'):
            break
        print("Ошибка: выберите 1, 2 или 3.")

    if choice == '1':
        while True:
            try:
                n = int(input("Введите количество точек n (>= 2): "))
                if n < 2:
                    print("n должен быть >= 2.")
                    continue
                print("Введите координаты x для всех точек через пробел (x_1 ... x_n):")
                x_vals = list(map(float, input().split()))
                if len(x_vals) != n:
                    print(f"Ошибка: ожидалось {n} чисел.")
                    continue
                print("Введите координаты у для всех точек через пробел (y_1 ... y_n):")
                y_vals = list(map(float, input().split()))
                if len(y_vals) != n:
                    print(f"Ошибка: ожидалось {n} чисел.")
                    continue
                return n, [x_vals, y_vals]
            except ValueError:
                print("Ошибка ввода. Ожидаются числа.")

    elif choice == '2':
        n = random.randint(4, 8)
        x_vals = [round(random.uniform(-10, 10), 2) for _ in range(n)]
        y_vals = [round(random.uniform(-10, 10), 2) for _ in range(n)]
        print(f"\Сгенерировано {n} точек:")
        for j in range(n):
            print(f"  Точка {j + 1}: ({x_vals[j]:.2f}, {y_vals[j]:.2f})")
        return n, [x_vals, y_vals]
    
    else:
        # Готовые примеры
        examples = [
            (3, [[0.0, 3.0, 0.0], [0.0, 0.0, 4.0]]),              # треугольник 3-4-5
            (4, [[0.0, 1.0, 1.0, 0.0], [0.0, 0.0, 1.0, 1.0]]),    # квадрат, диагональ √2
            (5, [[0.0, 2.0, 5.0, 7.0, 10.0], [0.0, 1.0, 5.0, 2.0, 9.0]]),
            (3, [[-1.0, 2.0, -2.0], [3.0, -1.0, -4.0]])
        ]
        print("\nГотовые примеры:")
        for idx, (n_val, mat) in enumerate(examples, 1):
            print(f"{idx}: n = {n_val}")
            print("  x:", " ".join(f"{v:6.2f}" for v in mat[0]))
            print("  y:", " ".join(f"{v:6.2f}" for v in mat[1]))
        while True:
            try:
                num = int(input("Выберите номер примера: "))
                if 1 <= num <= len(examples):
                    return examples[num - 1]
                else:
                    print(f"Номер должен быть от 1 до {len(examples)}.")
            except ValueError:
                print("Ошибка ввода. Введите целое число.")


def find_longest_segment(n, matrix):
    """Находит максимальное расстояние между точками и возвращает (max_dist, p1, p2)."""
    x = matrix[0]
    y = matrix[1]
    max_dist = -1.0
    p1 = p2 = -1

    for i in range(n):
        for j in range(i + 1, n):
            dx = x[i] - x[j]
            dy = y[i] - y[j]
            dist = math.hypot(dx, dy)  # sqrt(dx^2 + dy^2)
            if dist > max_dist:
                max_dist = dist
                p1, p2 = i + 1, j + 1  # нумерация с 1
    return max_dist, p1, p2


def main():
    n, matrix = get_matrix()
    max_dist, p1, p2 = find_longest_segment(n, matrix)

    print("\n" + "=" * 60)
    print("РЕЗУЛЬТАТЫ")
    print("=" * 60)
    print("Координаты точек:")
    for j in range(n):
        print(f"  Точка {j + 1} ({matrix[0][j]:.2f}, {matrix[1][j]:.2f})")

    print(f"\nНаибольшая длина отрезка: {max_dist:.6f}")
    print(f"Отрезок соединяет точки {p1} и {p2}")
    print("=" * 60)

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
