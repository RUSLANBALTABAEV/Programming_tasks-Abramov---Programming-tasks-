"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
10. Вложенные циклы

353. Даны натуральные числа x1,y1,...,x10,y10. Получить на экране точки (x1,y1), (x2,y2),..., (x10,y10), которые входят в эту последовательность ровно один раз.
"""


import random
from collections import Counter

def get_points():
    """Выбор способа ввода 10 точек (x, y)."""
    print("Выберите способ ввода 10 точек (x_i, y_i):")
    print("1 - Ручной ввод")
    print("2 - Случайная генерация")
    print("3 - Готовый пример")
    choice = input("Ваш выбор (1/2/3): ").strip()
    while choice not in ('1', '2', '3'):
        choice = input("Некорректно. Выберите 1, 2 или 3: ")

    if choice == '1':
        try:
            print("Введите 20 целых чисел (x1 y1 x2 y2 ... x10 y10) через пробел:")
            line = input().strip()
            tokens = line.split()
            if len(tokens) != 20:
                print("Ожидалось 20 чисел.")
                return None
            nums = [int(t) for t in tokens]
            # Проверка натуральности (>=1)
            if any(v < 1 for v in nums):
                print("Все числа должны быть натуральными (>=1).")
                return None
            # Разбиваем на пары
            points = [(nums[i], nums[i+1]) for i in range(0, 20, 2)]
            return points
        except ValueError:
            print("Ошибка ввода. Введите целые числа.")
            return None

    elif choice == '2':
        # Случайные натуральные числа от 1 до 20
        points = []
        for _ in range(10):
            x = random.randint(1, 20)
            y = random.randint(1, 20)
            points.append((x, y))
        print("Сгенерированы точки:")
        for i, (x, y) in enumerate(points, 1):
            print(f"({x}, {y})", end=" ")
        print()
        return points

    else:  # choice == '3'
        examples = [
            [(1,1), (2,2), (3,3), (4,4), (5,5), (6,6), (7,7), (8,8), (9,9), (10,10)],
            [(1,2), (2,3), (1,2), (3,4), (4,5), (5,6), (6,7), (7,8), (8,9), (9,10)],
            [(1,1), (1,1), (2,2), (2,2), (3,3), (3,3), (4,4), (4,4), (5,5), (5,5)],
            [(1,1), (1,2), (1,3), (2,1), (2,2), (2,3), (3,1), (3,2), (3,3), (4,4)],
            [(5,5), (5,5), (5,5), (5,5), (5,5), (5,5), (5,5), (5,5), (5,5), (5,5)]
        ]
        print("Готовые примеры наборов точек:")
        for idx, ex in enumerate(examples, 1):
            print(f"{idx}: {ex[:3]}... (всего {len(ex)} точек)")
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
    points = get_points()
    if points is None:
        return

    print("\n" + "="*60)
    print("Исходные точки:")
    for i, (x, y) in enumerate(points, 1):
        print(f"({x}, {y})", end=" ")
    print("\n" + "="*60)

    # Подсчёт частот
    freq = Counter(points)
    unique_points = [p for p, cnt in freq.items() if cnt == 1]

    if unique_points:
        print("\nТочки, встречающиеся ровно один раз:")
        for p in unique_points:
            print(p)
    else:
        print("\nНет точек, встречающихся ровно один раз.")

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
