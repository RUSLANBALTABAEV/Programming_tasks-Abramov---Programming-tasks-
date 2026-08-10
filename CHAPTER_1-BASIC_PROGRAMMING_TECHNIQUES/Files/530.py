"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

530. Дан файлы f, компоненты которого являются натуральными числами. Число компоненты файла кратно четырем. Каждые две последовательные компоненты определяют координаты двух точек.
а) Считая, что заданы координаты концов отрезов, построить все такие отрезки.
б) Считая, что заданы координаты противоположных углов прямоугольника, построить все такие прямоугольники.
в) Считая, что заданы вершины A и B фигуры, представленной на рис. 24, построить все такие фигуры.
г) Считая, что заданы координаты центра окружности и одной из ее точек, построить все такие окружности.
"""


import random
import os
import turtle
import math


# ------------------------------------------------------------
# 1. Общие процедуры работы с файлами
# ------------------------------------------------------------
def create_text_file(filename, text):
    """Создаёт (или перезаписывает) текстовый файл с указанным содержимым."""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)


def read_file(filename):
    """Читает и возвращает содержимое текстового файла."""
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()


# ------------------------------------------------------------
# 2. Создание исходного файла f (если отсутствует или пуст)
# ------------------------------------------------------------
def create_file_f(filename):
    """Создаёт файл f с координатами точек."""
    print("Файл f не существует или пуст. Задайте координаты.")
    print("Формат: последовательность целых чисел (x1 y1 x2 y2 …).")
    print("Количество чисел должно быть кратно 4.")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод (все числа через пробел в одной строке)")
    print("2 — Случайная генерация координат")
    print("3 — Готовый пример")

    while True:
        choice = input("Ваш выбор (1/2/3): ").strip()
        if choice in ('1', '2', '3'):
            break
        print("Ошибка: выберите 1, 2 или 3.")

    if choice == '1':
        while True:
            try:
                raw = input("Введите координаты: ").strip()
                if not raw:
                    print("Пустой ввод. Будет использован готовый пример.")
                    numbers = [10, 10, 100, 50, -100, 50, 0, -50, 0, 0, 80, 80, -50, -100, 50, -50, 100, 100, 200, 150]
                else:
                    numbers = list(map(int, raw.split()))
                if len(numbers) % 4 != 0:
                    print(f"Ошибка: количество чисел должно быть кратно 4, а у вас {len(numbers)}.")
                    continue
                break
            except ValueError:
                print("Ошибка: введите целые числа.")
        text = ' '.join(map(str, numbers))
    elif choice == '2':
        num_pairs = random.randint(2, 5)  # число пар точек (каждая пара = 4 числа)
        numbers = []
        for _ in range(num_pairs):
            x1 = random.randint(-200, 200)
            y1 = random.randint(-200, 200)
            x2 = random.randint(-200, 200)
            y2 = random.randint(-200, 200)
            numbers.extend([x1, y1, x2, y2])
        text = ' '.join(map(str, numbers))
        print(f"Сгенерированы координаты для {num_pairs} пар точек.")
    else:  # готовый пример
        numbers = [10, 10, 100, 50, -100, 50, 0, -50, 0, 0, 80, 80,
                   -50, -100, 50, -50, 100, 100, 200, 150]
        text = ' '.join(map(str, numbers))
        print("Использован готовый пример.")

    create_text_file(filename, text)
    print(f"Данные записаны в '{filename}'.")


def ensure_file_exists(filename):
    """Проверяет, существует ли файл и содержит ли данные. Если нет – создаёт."""
    if not os.path.exists(filename):
        create_file_f(filename)
        return
    content = read_file(filename).strip()
    if not content:
        create_file_f(filename)
        return
    # Проверим, что количество чисел кратно 4
    numbers = content.split()
    if len(numbers) % 4 != 0:
        print("Количество чисел в файле не кратно 4.")
        create_file_f(filename)


# ------------------------------------------------------------
# 3. Чтение координат из файла
# ------------------------------------------------------------
def read_pairs(filename):
    """Возвращает список кортежей (x1, y1, x2, y2)."""
    content = read_file(filename).strip()
    numbers = list(map(int, content.split()))
    pairs = []
    for i in range(0, len(numbers), 4):
        pairs.append(tuple(numbers[i:i+4]))
    return pairs


# ------------------------------------------------------------
# 4. Рисование фигур (пункты а–г)
# ------------------------------------------------------------
def setup_turtle(title="Задача 530"):
    screen = turtle.Screen()
    screen.title(title)
    screen.setup(800, 600)
    screen.tracer(0)
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.pensize(2)
    return screen, t


def draw_segments(pairs):
    """а) Отрезки по координатам концов."""
    screen, t = setup_turtle("Отрезки")
    for x1, y1, x2, y2 in pairs:
        t.penup()
        t.goto(x1, y1)
        t.pendown()
        t.goto(x2, y2)
    screen.update()
    screen.exitonclick()


def draw_rectangles(pairs):
    """б) Прямоугольники, стороны параллельны осям."""
    screen, t = setup_turtle("Прямоугольники")
    for x1, y1, x2, y2 in pairs:
        x_min, x_max = min(x1, x2), max(x1, x2)
        y_min, y_max = min(y1, y2), max(y1, y2)
        t.penup()
        t.goto(x_min, y_min)
        t.pendown()
        t.goto(x_max, y_min)
        t.goto(x_max, y_max)
        t.goto(x_min, y_max)
        t.goto(x_min, y_min)
    screen.update()
    screen.exitonclick()


def draw_figure_v(pairs):
    """в) Фигура по рис. 24: прямоугольник с диагоналями."""
    screen, t = setup_turtle("Фигура по рис. 24")
    for x1, y1, x2, y2 in pairs:
        x_min, x_max = min(x1, x2), max(x1, x2)
        y_min, y_max = min(y1, y2), max(y1, y2)
        # прямоугольник
        t.penup()
        t.goto(x_min, y_min)
        t.pendown()
        t.goto(x_max, y_min)
        t.goto(x_max, y_max)
        t.goto(x_min, y_max)
        t.goto(x_min, y_min)
        # диагонали
        t.penup()
        t.goto(x_min, y_min)
        t.pendown()
        t.goto(x_max, y_max)
        t.penup()
        t.goto(x_min, y_max)
        t.pendown()
        t.goto(x_max, y_min)
    screen.update()
    screen.exitonclick()


def draw_circles(pairs):
    """г) Окружности: первая точка – центр, вторая – точка на окружности."""
    screen, t = setup_turtle("Окружности")
    for xc, yc, xp, yp in pairs:
        r = math.hypot(xp - xc, yp - yc)
        if r == 0:
            continue
        t.penup()
        t.goto(xc, yc - r)
        t.pendown()
        t.circle(r)
    screen.update()
    screen.exitonclick()


# ------------------------------------------------------------
# 5. Основная программа
# ------------------------------------------------------------
def main():
    print("Задача 530: Построение фигур по координатам из файла")
    file_f = "f.txt"

    ensure_file_exists(file_f)
    pairs = read_pairs(file_f)

    if not pairs:
        print("Нет данных для отрисовки.")
        return

    print("\nКоординаты (x1, y1), (x2, y2):")
    for i, (x1, y1, x2, y2) in enumerate(pairs, 1):
        print(f"  {i}. ({x1}, {y1}) – ({x2}, {y2})")

    print("\nВыберите тип фигуры:")
    print("  а) Отрезки")
    print("  б) Прямоугольники")
    print("  в) Фигуры по рис. 24 (прямоугольник с диагоналями)")
    print("  г) Окружности")
    choice = input("Ваш выбор (а/б/в/г): ").strip().lower()

    if choice in ('а', 'a'):
        draw_segments(pairs)
    elif choice in ('б', 'b'):
        draw_rectangles(pairs)
    elif choice in ('в', 'v'):
        draw_figure_v(pairs)
    elif choice in ('г', 'g'):
        draw_circles(pairs)
    else:
        print("Неверный выбор.")


if __name__ == "__main__":
    main()