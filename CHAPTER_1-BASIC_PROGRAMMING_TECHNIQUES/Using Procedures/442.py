"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
12. Использование процедур 

В задачах этого параграфа будем для краткости говорить просто о процедурах, подразумевая, что решающий задачи сам выберет подходящее средство программирования – подпрограмму, функцию и 
т. д. Этот выбор должен быть сделан с учётом как характера задач, так и особенностей используемого языка программирования.

442. Даны действительные числа x1, y1, x2, y2, …, x10, y10. Найти периметр десятиугольника, вершины которого имеют соответственно координаты (x1, y1), (x2, y2), …, (x10, y10). (Определить процедуру вычисления расстояния между двумя точками, заданными своими координатами.)
"""


import math
import random


def get_distance(x1, y1, x2, y2):
    """Возвращает расстояние между точками (x1, y1) и (x2, y2)."""
    return math.hypot(x2 - x1, y2 - y1)


def get_coordinates():
    """Выбор способа ввода координат десяти вершин (20 чисел)."""
    print("Задача 442: Периметр десятиугольника")
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
                print("Введите 20 действительных чисел (x1 y1 x2 y2 ... x10 y10) через пробел:")
                data = list(map(float, input().split()))
                if len(data) != 20:
                    print("Нужно ровно 20 чисел.")
                    continue
                vertices = [(data[i], data[i+1]) for i in range(0, 20, 2)]
                return vertices
            except ValueError:
                print("Ошибка ввода.")

    elif choice == '2':
        vertices = [(round(random.uniform(-10, 10), 2), round(random.uniform(-10, 10), 2)) for _ in range(10)]
        print("Сгенерированы вершины:", vertices)
        return vertices

    else:  # готовые примеры
        # Пример: правильный десятиугольник, вписанный в окружность радиуса 5
        # (для простоты используем координаты, приближённые к правильному)
        examples = [
            # Простой замкнутый контур (квадрат 0-1-2-3-4-...-9)
            [(0,0), (1,0), (2,0), (2,1), (2,2), (1,2), (0,2), (0,1), (-1,1), (-1,0)],
            # Правильный десятиугольник (радиус 3)
            [(3 * math.cos(2 * math.pi * i / 10), 3 * math.sin(2 * math.pi * i / 10)) for i in range(10)],
        ]
        print("Готовые примеры:")
        for idx, verts in enumerate(examples, 1):
            print(f"{idx}: {verts}")
        while True:
            try:
                num = int(input("Выберите номер примера: "))
                if 1 <= num <= len(examples):
                    return examples[num-1]
                else:
                    print(f"Номер от 1 до {len(examples)}.")
            except ValueError:
                print("Введите целое число.")


def main():
    vertices = get_coordinates()
    n = len(vertices)
    perimeter = 0.0

    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]  # замыкаем контур
        perimeter += get_distance(x1, y1, x2, y2)

    print(f"\nКоординаты вершин: {vertices}")
    print(f"Периметр десятиугольника: {perimeter:.6f}")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
