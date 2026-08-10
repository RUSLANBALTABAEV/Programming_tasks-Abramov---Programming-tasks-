"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

529. Дан текстовый файл f. Каждая строка файла несколько натуральных чисел в их символьном представлении. Числа разделяются запятыми или пробелами и определяют вид некоторой геометрической фигуры, ее размеры и положение на экране. Приняты следующие соглашения:
1) отрезок прямой задается координатами своих концов, имеет номер 1;
2) прямоугольник задается координатами левого верхнего и правого нижнего угла, имеет номер 2;
3) окружность задается координатами центра и радиусом, имеет номер 3;
4) ломанная задается количеством ее вершин, их координатами и имеет номер 4. Так, например, строка 1, 10, 10, 30, 30 определяет отрезок прямой с координатами концов (10, 10) и (30, 30), а строка 3, 100, 100, 50 - окружность с центром в точке (100, 100) и радиусом 50. 
а) Построить на экране все геометрические фигуры, заданные в файле f.
б) Разработать способ более широкого набора фигур по сравнению с указанным и выполнить пункт а).
"""


import random
import os
import re
import turtle


# ------------------------------------------------------------
# 1. Процедуры работы с файлами
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
    """Создаёт файл f с описаниями геометрических фигур."""
    print("Файл f не существует или пуст. Задайте описания фигур.")
    print("Формат строки: номер_фигуры, параметры (через пробел или запятую).")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод строк (пустая строка — конец)")
    print("2 — Случайная генерация фигур")
    print("3 — Готовый пример")

    while True:
        choice = input("Ваш выбор (1/2/3): ").strip()
        if choice in ('1', '2', '3'):
            break
        print("Ошибка: выберите 1, 2 или 3.")

    if choice == '1':
        print("Вводите строки с фигурами. Для завершения — пустая строка.")
        lines = []
        while True:
            line = input().strip()
            if line == "":
                break
            lines.append(line)
        if not lines:
            print("Не введено ни одной строки. Будет использован готовый пример.")
            text = ("1, 10, 10, 100, 50\n"
                    "2, -100, 50, 0, -50\n"
                    "3, 0, 0, 80\n"
                    "4, 3, -50, -100, 50, -100, 0, -150\n"
                    "5, 100, 100, 200, 100, 150, 200\n"
                    "6, 150, -50, 200, -100\n"
                    "7, 0, 0, 30")
        else:
            text = "\n".join(lines)
    elif choice == '2':
        n = random.randint(3, 7)
        lines = []
        for _ in range(n):
            fig_type = random.randint(1, 7)
            if fig_type == 1:   # отрезок
                x1 = random.randint(-200, 200)
                y1 = random.randint(-200, 200)
                x2 = random.randint(-200, 200)
                y2 = random.randint(-200, 200)
                lines.append(f"1, {x1}, {y1}, {x2}, {y2}")
            elif fig_type == 2: # прямоугольник
                x1 = random.randint(-200, 200)
                y1 = random.randint(-200, 200)
                x2 = random.randint(x1+10, 250)
                y2 = random.randint(-200, y1-10)
                lines.append(f"2, {x1}, {y1}, {x2}, {y2}")
            elif fig_type == 3: # окружность
                xc = random.randint(-200, 200)
                yc = random.randint(-200, 200)
                r = random.randint(10, 100)
                lines.append(f"3, {xc}, {yc}, {r}")
            elif fig_type == 4: # ломаная
                num_verts = random.randint(2, 4)
                verts = []
                for _ in range(num_verts):
                    verts.append(str(random.randint(-200, 200)))
                    verts.append(str(random.randint(-200, 200)))
                lines.append(f"4, {num_verts}, {', '.join(verts)}")
            elif fig_type == 5: # треугольник
                x1 = random.randint(-200, 200)
                y1 = random.randint(-200, 200)
                x2 = random.randint(-200, 200)
                y2 = random.randint(-200, 200)
                x3 = random.randint(-200, 200)
                y3 = random.randint(-200, 200)
                lines.append(f"5, {x1}, {y1}, {x2}, {y2}, {x3}, {y3}")
            elif fig_type == 6: # залитый прямоугольник
                x1 = random.randint(-200, 200)
                y1 = random.randint(-200, 200)
                x2 = random.randint(x1+10, 250)
                y2 = random.randint(-200, y1-10)
                lines.append(f"6, {x1}, {y1}, {x2}, {y2}")
            elif fig_type == 7: # залитая окружность
                xc = random.randint(-200, 200)
                yc = random.randint(-200, 200)
                r = random.randint(10, 100)
                lines.append(f"7, {xc}, {yc}, {r}")
        text = "\n".join(lines)
        print(f"Сгенерировано {n} случайных фигур.")
    else:  # готовый пример
        text = ("1, 10, 10, 100, 50\n"
                "2, -100, 50, 0, -50\n"
                "3, 0, 0, 80\n"
                "4, 3, -50, -100, 50, -100, 0, -150\n"
                "5, 100, 100, 200, 100, 150, 200\n"
                "6, 150, -50, 200, -100\n"
                "7, 0, 0, 30")
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


# ------------------------------------------------------------
# 3. Парсинг строки и отрисовка фигур
# ------------------------------------------------------------
def draw_figures_from_file(filename):
    """
    Читает файл, определяет тип фигуры и рисует её на экране с помощью turtle.
    Поддерживаются как базовые, так и расширенные типы фигур.
    """
    lines = read_file(filename).splitlines()

    screen = turtle.Screen()
    screen.title("Задача 529: Геометрические фигуры из файла")
    screen.setup(800, 600)
    screen.tracer(0)

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.pensize(2)

    for line in lines:
        line = line.strip()
        if not line:
            continue
        parts = re.split(r'[ ,]+', line)  # разделяем по запятым и пробелам
        if not parts:
            continue
        try:
            fig_type = int(parts[0])
        except ValueError:
            continue

        # Базовый набор фигур
        if fig_type == 1:   # отрезок
            if len(parts) != 5: continue
            x1, y1, x2, y2 = map(int, parts[1:])
            t.penup()
            t.goto(x1, y1)
            t.pendown()
            t.goto(x2, y2)

        elif fig_type == 2: # прямоугольник
            if len(parts) != 5: continue
            x1, y1, x2, y2 = map(int, parts[1:])
            t.penup()
            t.goto(x1, y1)
            t.pendown()
            t.goto(x2, y1)
            t.goto(x2, y2)
            t.goto(x1, y2)
            t.goto(x1, y1)

        elif fig_type == 3: # окружность
            if len(parts) != 4: continue
            xc, yc, r = map(int, parts[1:])
            t.penup()
            t.goto(xc, yc - r)
            t.pendown()
            t.circle(r)

        elif fig_type == 4: # ломаная
            n = int(parts[1])
            if len(parts) != 2 + 2*n: continue
            coords = list(map(int, parts[2:]))
            t.penup()
            t.goto(coords[0], coords[1])
            t.pendown()
            for i in range(2, len(coords), 2):
                t.goto(coords[i], coords[i+1])

        # Расширенный набор фигур (пункт б)
        elif fig_type == 5: # треугольник
            if len(parts) != 7: continue
            x1, y1, x2, y2, x3, y3 = map(int, parts[1:])
            t.penup()
            t.goto(x1, y1)
            t.pendown()
            t.goto(x2, y2)
            t.goto(x3, y3)
            t.goto(x1, y1)

        elif fig_type == 6: # залитый прямоугольник
            if len(parts) != 5: continue
            x1, y1, x2, y2 = map(int, parts[1:])
            t.penup()
            t.goto(x1, y1)
            t.begin_fill()
            t.pendown()
            t.goto(x2, y1)
            t.goto(x2, y2)
            t.goto(x1, y2)
            t.goto(x1, y1)
            t.end_fill()

        elif fig_type == 7: # залитая окружность
            if len(parts) != 4: continue
            xc, yc, r = map(int, parts[1:])
            t.penup()
            t.goto(xc, yc - r)
            t.begin_fill()
            t.pendown()
            t.circle(r)
            t.end_fill()

    screen.update()
    print("Все фигуры построены. Закройте окно, чтобы завершить программу.")
    turtle.done()


# ------------------------------------------------------------
# 4. Основная программа
# ------------------------------------------------------------
def main():
    print("Задача 529: Построение геометрических фигур из файла")
    print("Базовый набор: 1-отрезок, 2-прямоугольник, 3-окружность, 4-ломаная.")
    print("Расширенный набор: 5-треугольник, 6-залитый прямоугольник, 7-залитая окружность.\n")
    file_f = "f.txt"

    ensure_file_exists(file_f)
    draw_figures_from_file(file_f)


if __name__ == "__main__":
    main()