"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
12. Использование процедур 

В задачах этого параграфа будем для краткости говорить просто о процедурах, подразумевая, что решающий задачи сам выберет подходящее средство программирования – подпрограмму, функцию и 
т. д. Этот выбор должен быть сделан с учётом как характера задач, так и особенностей используемого языка программирования.

451. Даны натуральные числа x1, y1, x2, y2, ..., x6, y6. Точки с координатами (x1, y1), (x2, y2), (x3, y3) рассматриваются как три вершины первого прямоугольника, точки с координатами (x4, y4), (x5, y5), (x6, y6) – второго. Провести построения, аналогичные тем, которые были описаны в предыдущей задаче в отношении треугольников. 
Стороны прямоугольника считаются параллельными осям экрана (рис. 20)
"""


import math
import random

# ANSI-цвета для консольного вывода
COLOR_RESET = '\033[0m'
COLOR_BLUE  = '\033[94m'
COLOR_RED   = '\033[91m'
COLOR_YELLOW= '\033[93m'

# ------------------------------------------------------------
# 1. Процедура: определение прямоугольника по трём вершинам
#    (стороны параллельны осям)
# ------------------------------------------------------------
def rect_from_three_points(x1, y1, x2, y2, x3, y3):
    """
    Возвращает кортеж (x_min, y_min, x_max, y_max, width, height).
    Предполагается, что три точки задают три разных угла прямоугольника
    со сторонами, параллельными осям координат.
    """
    xs = [x1, x2, x3]
    ys = [y1, y2, y3]
    x_min, x_max = min(xs), max(xs)
    y_min, y_max = min(ys), max(ys)
    width = x_max - x_min
    height = y_max - y_min
    return (x_min, y_min, x_max, y_max, width, height)


# ------------------------------------------------------------
# 2. Процедура: площадь прямоугольника
# ------------------------------------------------------------
def rect_area(rect):
    _, _, _, _, w, h = rect
    return w * h


# ------------------------------------------------------------
# 3. Процедура: лежит ли прямоугольник inner внутри outer
# ------------------------------------------------------------
def rect_inside(inner, outer):
    ix_min, iy_min, ix_max, iy_max, _, _ = inner
    ox_min, oy_min, ox_max, oy_max, _, _ = outer
    return (ix_min >= ox_min and ix_max <= ox_max and
            iy_min >= oy_min and iy_max <= oy_max)


# ------------------------------------------------------------
# 4. Процедура: текстовое построение сторон прямоугольника
# ------------------------------------------------------------
def draw_rect_text(rect, color, label):
    x_min, y_min, x_max, y_max, w, h = rect
    print(f"{color}{label}{COLOR_RESET}")
    print(f"  Углы: ({x_min}, {y_min}), ({x_max}, {y_min}), ({x_max}, {y_max}), ({x_min}, {y_max})")
    print(f"  Ширина: {w:.6f}, Высота: {h:.6f}, Площадь: {rect_area(rect):.6f}")
    print()


# ------------------------------------------------------------
# Ввод данных
# ------------------------------------------------------------
def get_data():
    """Выбор способа ввода координат двух прямоугольников (12 чисел)."""
    print("Задача 451: Вложенность прямоугольников и закраска области")
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
                print("Введите 12 целых или действительных чисел (x1 y1 x2 y2 x3 y3 x4 y4 x5 y5 x6 y6):")
                data = list(map(float, input().split()))
                if len(data) != 12:
                    print("Нужно ровно 12 чисел.")
                    continue
                r1 = rect_from_three_points(data[0], data[1], data[2], data[3], data[4], data[5])
                r2 = rect_from_three_points(data[6], data[7], data[8], data[9], data[10], data[11])
                return r1, r2
            except ValueError:
                print("Ошибка ввода.")

    elif choice == '2':
        # Генерируем случайные прямоугольники (иногда вложенные)
        if random.random() < 0.5:
            # внешний прямоугольник
            ox_min = random.uniform(-10, 0)
            oy_min = random.uniform(-10, 0)
            ow = random.uniform(2, 8)
            oh = random.uniform(2, 8)
            ox_max = ox_min + ow
            oy_max = oy_min + oh
            outer = (ox_min, oy_min, ox_max, oy_max, ow, oh)
            # внутренний – чуть меньше, смещён внутрь
            margin = 0.2
            ix_min = ox_min + margin
            iy_min = oy_min + margin
            iw = ow - 2 * margin
            ih = oh - 2 * margin
            ix_max = ix_min + iw
            iy_max = iy_min + ih
            inner = (ix_min, iy_min, ix_max, iy_max, iw, ih)
        else:
            # просто два случайных (могут не вкладываться)
            inner = rect_from_three_points(
                random.uniform(-5, 5), random.uniform(-5, 5),
                random.uniform(-5, 5), random.uniform(-5, 5),
                random.uniform(-5, 5), random.uniform(-5, 5))
            outer = rect_from_three_points(
                random.uniform(-5, 5), random.uniform(-5, 5),
                random.uniform(-5, 5), random.uniform(-5, 5),
                random.uniform(-5, 5), random.uniform(-5, 5))
        print(f"Сгенерирован прямоугольник 1: x_min = {inner[0]:.2f}, y_min = {inner[1]:.2f}, x_max = {inner[2]:.2f}, y_max = {inner[3]:.2f}")
        print(f"Сгенерирован прямоугольник 2: x_min = {outer[0]:.2f}, y_min = {outer[1]:.2f}, x_max = {outer[2]:.2f}, y_max = {outer[3]:.2f}")
        return inner, outer

    else:  # готовые примеры
        examples = [
            # прямоугольник 1 внутри 2
            (rect_from_three_points(2,2, 2,4, 4,4), rect_from_three_points(0,0, 5,0, 5,5)),
            # прямоугольник 2 внутри 1
            (rect_from_three_points(0,0, 5,0, 0,5), rect_from_three_points(1,1, 2,1, 1,3)),
            # ни один не внутри другого
            (rect_from_three_points(0,0, 2,0, 0,2), rect_from_three_points(1,1, 3,1, 1,3))
        ]
        print("Готовые примеры (прямоугольники заданы парами точек):")
        for idx, (r1, r2) in enumerate(examples, 1):
            print(f"{idx}: R1 x[{r1[0]}, {r1[2]}], y[{r1[1]}, {r1[3]}]; R2 x[{r2[0]}, {r2[2]}], y[{r2[1]}, {r2[3]}]")
        while True:
            try:
                num = int(input("Выберите номер примера: "))
                if 1 <= num <= len(examples):
                    return examples[num - 1]
                else:
                    print(f"Номер от 1 до {len(examples)}.")
            except ValueError:
                print("Введите целое число.")


# ------------------------------------------------------------
# Основная программа
# ------------------------------------------------------------
def main():
    rect1, rect2 = get_data()

    r1_in_r2 = rect_inside(rect1, rect2)
    r2_in_r1 = rect_inside(rect2, rect1)

    print()
    if r1_in_r2:
        print(f"{COLOR_YELLOW}Первый прямоугольник целиком лежит внутри второго.{COLOR_RESET}")
        area_outer = rect_area(rect2)
        area_inner = rect_area(rect1)
        shaded = area_outer - area_inner
        draw_rect_text(rect1, COLOR_BLUE, "Внутренний прямоугольник")
        draw_rect_text(rect2, COLOR_BLUE, "Внешний прямоугольник")
        print(f"{COLOR_BLUE}Площадь заштрихованной области (внешний - внутренний): {shaded:.6f}{COLOR_RESET}")

    elif r2_in_r1:
        print(f"{COLOR_YELLOW}Второй прямоугольник целиком лежит внутри первого.{COLOR_RESET}")
        area_outer = rect_area(rect1)
        area_inner = rect_area(rect2)
        shaded = area_outer - area_inner
        draw_rect_text(rect1, COLOR_BLUE, "Внешний прямоугольник")
        draw_rect_text(rect2, COLOR_BLUE, "Внутренний прямоугольник")
        print(f"{COLOR_BLUE}Площадь заштрихованной области (внешний - внутренний): {shaded:.6f}{COLOR_RESET}")

    else:
        print(f"{COLOR_YELLOW}Ни один из прямоугольников не лежит целиком внутри другого.{COLOR_RESET}")
        draw_rect_text(rect1, COLOR_BLUE, "Прямоугольник 1")
        draw_rect_text(rect2, COLOR_RED, "Прямоугольник 2")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
