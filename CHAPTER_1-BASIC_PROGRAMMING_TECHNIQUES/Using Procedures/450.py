"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
12. Использование процедур 

В задачах этого параграфа будем для краткости говорить просто о процедурах, подразумевая, что решающий задачи сам выберет подходящее средство программирования – подпрограмму, функцию и 
т. д. Этот выбор должен быть сделан с учётом как характера задач, так и особенностей используемого языка программирования.

450. Два треугольника заданы координатами своих вершин так, как указано в предыдущей задаче. Выяснить, лежит ли какой-либо из треугольников целиком внутри другого. Если да, построить стороны треугольников и закрасить область, принадлежащую внешнему треугольнику и не принадлежащую внутреннему(рис. 19). Построения сторон и закраску области выполнить одним цветом. Если ни один из треугольников не лежит целиком внутри другого, построить стороны треугольников, используя для каждого треугольника свой цвет. (Определить процедуру, позволяющую выяснить, лежат ли две точки в одной полуплоскости относительно заданной прямой (см. задачу 52), и процедуру построения сторон треугольника по заданным координатам вершин и номеру цвета.) 
"""


import math
import random

# ------------------------------------------------------------
# Цвета для консольного вывода (ANSI)
# ------------------------------------------------------------
COLOR_RESET = '\033[0m'
COLOR_BLUE  = '\033[94m'
COLOR_RED   = '\033[91m'
COLOR_YELLOW= '\033[93m'
COLOR_GREEN = '\033[92m'

# ------------------------------------------------------------
# 1. Процедура: лежат ли две точки в одной полуплоскости
# ------------------------------------------------------------
def same_half_plane(x1, y1, x2, y2, p1x, p1y, p2x, p2y):
    """
    Проверяет, лежат ли точки (p1x, p1y) и (p2x, p2y) в одной полуплоскости
    (включая границу) относительно прямой (x1, y1)-(x2, y2).
    """
    # Векторное произведение (B-A) x (P-A)
    def cross(ax, ay, bx, by, px, py):
        return (bx - ax) * (py - ay) - (by - ay) * (px - ax)

    val1 = cross(x1, y1, x2, y2, p1x, p1y)
    val2 = cross(x1, y1, x2, y2, p2x, p2y)
    return val1 * val2 >= -1e-9


# ------------------------------------------------------------
# 2. Процедура построения сторон треугольника (текстовый вывод)
# ------------------------------------------------------------
def draw_triangle(vertices, color_code, label):
    """
    Выводит в консоль координаты вершин и длины сторон треугольника
    заданным цветом.
    vertices – список [(x1, y1), (x2, y2), (x3, y3)]
    color_code – ANSI-код цвета
    label – подпись треугольника
    """
    print(f"{color_code}{label} (координаты вершин):{COLOR_RESET}")
    for i, (x, y) in enumerate(vertices, start=1):
        print(f"  Вершина {i}: ({x:.6f}, {y:.6f})")

    edges = [(0,1), (1,2), (2,0)]
    print(f"{color_code}  Стороны (длины):{COLOR_RESET}")
    for i, j in edges:
        x1, y1 = vertices[i]
        x2, y2 = vertices[j]
        d = math.hypot(x2 - x1, y2 - y1)
        print(f"    ({x1:.6f}, {y1:.6f}) – ({x2:.6f}, {y2:.6f})  длина = {d:.6f}")
    print()


# ------------------------------------------------------------
# 3. Вспомогательные геометрические процедуры
# ------------------------------------------------------------
def distance(x1, y1, x2, y2):
    return math.hypot(x2 - x1, y2 - y1)


def triangle_area_by_sides(x1, y1, x2, y2, x3, y3):
    """Площадь треугольника по трём сторонам (формула Герона)."""
    a = distance(x1, y1, x2, y2)
    b = distance(x2, y2, x3, y3)
    c = distance(x3, y3, x1, y1)
    if a + b <= c or a + c <= b or b + c <= a:
        return 0.0
    p = (a + b + c) / 2.0
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


def point_in_triangle(px, py, x1, y1, x2, y2, x3, y3):
    """Лежит ли точка (px,py) внутри треугольника (включая границу)."""
    return (same_half_plane(x1, y1, x2, y2, px, py, x3, y3) and
            same_half_plane(x2, y2, x3, y3, px, py, x1, y1) and
            same_half_plane(x3, y3, x1, y1, px, py, x2, y2))


def is_triangle_inside(inner, outer):
    """Все вершины inner лежат внутри (или на границе) outer."""
    for px, py in inner:
        if not point_in_triangle(px, py, *outer[0], *outer[1], *outer[2]):
            return False
    return True


# ------------------------------------------------------------
# Ввод данных
# ------------------------------------------------------------
def get_triangles():
    """Выбор способа ввода координат двух треугольников (12 чисел)."""
    print("Задача 450: Вложенность треугольников и закраска области")
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
                print("Введите 12 чисел (x1 y1 x2 y2 x3 y3  x4 y4 x5 y5 x6 y6) через пробел:")
                data = list(map(float, input().split()))
                if len(data) != 12:
                    print("Нужно ровно 12 чисел.")
                    continue
                tri1 = [(data[0], data[1]), (data[2], data[3]), (data[4], data[5])]
                tri2 = [(data[6], data[7]), (data[8], data[9]), (data[10], data[11])]
                return tri1, tri2
            except ValueError:
                print("Ошибка ввода.")

    elif choice == '2':
        # Генерируем случайные треугольники, иногда обеспечивая вложенность
        if random.random() < 0.5:
            # Вложенный случай: строим внешний треугольник, внутренний – середины сторон
            while True:
                ox1, oy1 = random.uniform(-10, 10), random.uniform(-10, 10)
                ox2, oy2 = random.uniform(-10, 10), random.uniform(-10, 10)
                ox3, oy3 = random.uniform(-10, 10), random.uniform(-10, 10)
                # Проверка невырожденности
                if abs((ox2 - ox1) * (oy3 - oy1) - (ox3 - ox1) * (oy2 - oy1)) < 1e-6:
                    continue
                ix1, iy1 = (ox1 + ox2) / 2, (oy1 + oy2) / 2
                ix2, iy2 = (ox2 + ox3) / 2, (oy2 + oy3) / 2
                ix3, iy3 = (ox3 + ox1) / 2, (oy3 + oy1) / 2
                tri1 = [(round(ix1, 2), round(iy1, 2)), (round(ix2, 2), round(iy2, 2)), (round(ix3, 2), round(iy3, 2))]
                tri2 = [(round(ox1, 2), round(oy1, 2)), (round(ox2, 2), round(oy2, 2)), (round(ox3, 2), round(oy3, 2))]
                break
        else:
            # Просто случайные треугольники (могут не вкладываться)
            tri1 = [(round(random.uniform(-5,5), 2), round(random.uniform(-5,5), 2)) for _ in range(3)]
            tri2 = [(round(random.uniform(-5,5), 2), round(random.uniform(-5,5), 2)) for _ in range(3)]
        print(f"Сгенерирован первый треугольник: {tri1}")
        print(f"Сгенерирован второй треугольник: {tri2}")
        return tri1, tri2

    else:  # готовые примеры
        examples = [
            # треугольник 1 внутри треугольника 2
            ([(1.0, 1.0), (1.0, 4.0), (4.0, 4.0)],
             [(0.0, 0.0), (5.0, 0.0), (0.0, 5.0)]),
            # треугольник 2 внутри треугольника 1
            ([(0.0, 0.0), (4.0, 0.0), (0.0, 4.0)],
             [(1.0, 1.0), (2.0, 1.0), (1.0, 3.0)]),
            # ни один не внутри другого
            ([(0.0, 0.0), (2.0, 0.0), (0.0, 2.0)],
             [(1.0, 1.0), (3.0, 1.0), (1.0, 3.0)])
        ]
        print("Готовые примеры:")
        for idx, (t1, t2) in enumerate(examples, 1):
            print(f"{idx}: T1 = {t1}, T2 = {t2}")
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
    tri1, tri2 = get_triangles()

    t1_in_t2 = is_triangle_inside(tri1, tri2)
    t2_in_t1 = is_triangle_inside(tri2, tri1)

    print()
    if t1_in_t2:
        print(f"{COLOR_YELLOW}Первый треугольник целиком лежит внутри второго.{COLOR_RESET}")
        area_outer = triangle_area_by_sides(*tri2[0], *tri2[1], *tri2[2])
        area_inner = triangle_area_by_sides(*tri1[0], *tri1[1], *tri1[2])
        shaded = area_outer - area_inner
        # Вывод одним цветом (синий)
        draw_triangle(tri1, COLOR_BLUE, "Внутренний треугольник")
        draw_triangle(tri2, COLOR_BLUE, "Внешний треугольник")
        print(f"{COLOR_BLUE}Площадь заштрихованной области (внешний - внутренний): {shaded:.6f}{COLOR_RESET}")

    elif t2_in_t1:
        print(f"{COLOR_YELLOW}Второй треугольник целиком лежит внутри первого.{COLOR_RESET}")
        area_outer = triangle_area_by_sides(*tri1[0], *tri1[1], *tri1[2])
        area_inner = triangle_area_by_sides(*tri2[0], *tri2[1], *tri2[2])
        shaded = area_outer - area_inner
        draw_triangle(tri1, COLOR_BLUE, "Внешний треугольник")
        draw_triangle(tri2, COLOR_BLUE, "Внутренний треугольник")
        print(f"{COLOR_BLUE}Площадь заштрихованной области (внешний - внутренний): {shaded:.6f}{COLOR_RESET}")

    else:
        print(f"{COLOR_YELLOW}Ни один из треугольников не лежит целиком внутри другого.{COLOR_RESET}")
        # Разные цвета
        draw_triangle(tri1, COLOR_BLUE, "Треугольник 1")
        draw_triangle(tri2, COLOR_RED, "Треугольник 2")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
