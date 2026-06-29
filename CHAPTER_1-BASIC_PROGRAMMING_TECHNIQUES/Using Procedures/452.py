"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
12. Использование процедур 

В задачах этого параграфа будем для краткости говорить просто о процедурах, подразумевая, что решающий задачи сам выберет подходящее средство программирования – подпрограмму, функцию и 
т. д. Этот выбор должен быть сделан с учётом как характера задач, так и особенностей используемого языка программирования.

452. Представим себе, что в центре экрана сидит жучок, который может перемещаться по прямой на указанное расстояние и поворачиваться направо и налево. У жучка есть перо, которое может оставлять след, повторяющий движение жучка. Если перо опущено, след остается; если перо поднято, следа нет. Итак, жучок может выполнять следующие приказы: 
1) Forward – переместиться на заданное расстояние;
2) Left – повернуть налево на заданный угол;
3) Right – повернуть направо на заданный угол;
4) Pen Up – поднять перо;
5) Pen Down – опустить перо.
Реализовать процедуры Forward, Left, Right, Pen Up, Pen Down.
Процедуры должны взаимодействовать через глобальные переменные xPos, yPos --координаты жучка на экране; Pen – признак, говорящий о том, поднято перо или опущено; Angle -- угол, который образует текущее направление перемещения жучка с осью абсцисс.
С помощью перечисленных процедур получить на экране:
а) Квадрат со стороной 75 единиц и центром, совпадающим с центром экрана.
б) Прямоугольник с отношением сторон 1:2 и со срезанными углами. Срезаются равнобедренные прямоугольные треугольники, катеты которых имеют длину, равную 1/20 длины большей стороны (рис. 21). Длина меньшей стороны – данная величина. 
Положение прямоугольника на экране может быть выбрано произвольно.
в) Фигуру, составленную из пятнадцати квадратов, которая изображена на рис. 22.
г) Четыре крупные цифры – текущий год; цифры должны быть написаны по девятисегментному шаблону (как на почтовых конвертах).
д) Те же цифры, что и в задании г), но написанные по семисегментному шаблону (как на электронных часах). 
е) Кривые Серпинского порядка 1 и 2, изображенные на рис. 23.
"""


import math
import turtle
import datetime

# ---------- глобальное состояние жука ----------
xPos = 0      # текущая координата X
yPos = 0      # текущая координата Y
Pen = 1       # 1 – перо опущено, 0 – поднято
Angle = 0     # угол направления (0° = вправо)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

def reset_state(x=0, y=0, ang=0):
    """Устанавливает жука в точку (x,y) с углом ang (в градусах)."""
    global xPos, yPos, Angle
    xPos, yPos, Angle = x, y, ang
    t.penup()
    t.goto(xPos, yPos)
    t.setheading(ang)

def forward(dist):
    """Переместиться вперёд на dist (след остаётся, если перо опущено)."""
    global xPos, yPos, Pen, Angle
    rad = math.radians(Angle)
    xPos += dist * math.cos(rad)
    yPos += dist * math.sin(rad)
    if Pen:
        t.pendown()
    else:
        t.penup()
    t.goto(xPos, yPos)

def right(deg):
    global Angle
    Angle -= deg
    t.right(deg)

def left(deg):
    global Angle
    Angle += deg
    t.left(deg)

def pen_up():
    global Pen
    Pen = 0
    t.penup()

def pen_down():
    global Pen
    Pen = 1
    t.pendown()

# ---------- задания ----------
def task_a():
    t.clear()
    reset_state(-37.5, 37.5, 0)
    pen_down()
    for _ in range(4):
        forward(75)
        right(90)
    turtle.update()

def task_b(L):
    """L — меньшая сторона, большая = 2L; срез = L/10."""
    t.clear()
    L = float(L)
    cut = L / 10.0
    diag = cut * math.sqrt(2)
    start_x = -L + cut
    start_y = L - cut
    reset_state(start_x, start_y, 0)
    pen_down()
    for _ in range(2):
        forward(2*L - 2*cut)      # горизонтальная сторона
        right(45)
        forward(diag)             # срез
        right(45)
        forward(2*L - 2*cut)      # вертикальная сторона
        right(45)
        forward(diag)             # срез
        right(45)
    turtle.update()

def task_c():
    t.clear()
    R, S = 120, 25          # радиус и сторона квадрата
    for i in range(15):
        ang = i * 24
        reset_state(0, 0, ang)
        pen_up()
        forward(R)
        left(90 + 45)        # чтобы угол квадрата смотрел в центр
        pen_down()
        for _ in range(4):
            forward(S)
            left(90)
    turtle.update()

# 9-сегментный шаблон (конверты)
def draw_9_segments(x, y, size, segments):
    s = size / 2.5
    seg_ends = {
        'a': ((x, y), (x + 2*s, y)),
        'b': ((x + 2*s, y), (x + 2*s, y - s)),
        'c': ((x + 2*s, y - s), (x + 2*s, y - 2*s)),
        'd': ((x, y - 2*s), (x + 2*s, y - 2*s)),
        'e': ((x, y - s), (x, y - 2*s)),
        'f': ((x, y), (x, y - s)),
        'g': ((x, y - s), (x + 2*s, y - s)),
        'h': ((x + 2*s, y), (x + 3*s, y - s)),
        'i': ((x, y - s), (x - s, y - 2*s))
    }
    for seg in segments:
        p1, p2 = seg_ends[seg]
        dx, dy = p2[0] - p1[0], p2[1] - p1[1]
        length = math.hypot(dx, dy)
        ang = math.degrees(math.atan2(dy, dx))
        reset_state(p1[0], p1[1], ang)
        pen_down()
        forward(length)

# 7-сегментный шаблон (часы)
def draw_7_segments(x, y, size, segments):
    s = size / 2.5
    seg_ends = {
        'a': ((x, y), (x + 2*s, y)),
        'b': ((x + 2*s, y), (x + 2*s, y - s)),
        'c': ((x + 2*s, y - s), (x + 2*s, y - 2*s)),
        'd': ((x, y - 2*s), (x + 2*s, y - 2*s)),
        'e': ((x, y - s), (x, y - 2*s)),
        'f': ((x, y), (x, y - s)),
        'g': ((x, y - s), (x + 2*s, y - s))
    }
    for seg in segments:
        p1, p2 = seg_ends[seg]
        dx, dy = p2[0] - p1[0], p2[1] - p1[1]
        length = math.hypot(dx, dy)
        ang = math.degrees(math.atan2(dy, dx))
        reset_state(p1[0], p1[1], ang)
        pen_down()
        forward(length)

def task_d():
    t.clear()
    digits = {
        0: 'abcdef', 1: 'bch', 2: 'abdegi', 3: 'abcdg', 4: 'bcfg',
        5: 'acdfg', 6: 'acdefg', 7: 'abc', 8: 'abcdefg', 9: 'abcdfg'
    }
    year = [int(d) for d in str(datetime.datetime.now().year)]
    x0 = -80
    for d in year:
        draw_9_segments(x0, 0, 40, digits[d])
        x0 += 60
    turtle.update()

def task_e():
    t.clear()
    digits = {
        0: 'abcdef', 1: 'bc', 2: 'abdeg', 3: 'abcdg', 4: 'bcfg',
        5: 'acdfg', 6: 'acdefg', 7: 'abc', 8: 'abcdefg', 9: 'abcdfg'
    }
    year = [int(d) for d in str(datetime.datetime.now().year)]
    x0 = -80
    for d in year:
        draw_7_segments(x0, 0, 40, digits[d])
        x0 += 60
    turtle.update()

def sierpinski(order, size):
    if order == 0:
        forward(size)
        return
    left(45)
    sierpinski(order - 1, size / 2)
    right(90)
    sierpinski(order - 1, size / 2)
    left(45)

def task_f():
    t.clear()
    # порядок 1
    reset_state(-120, 0, 90)
    for _ in range(4):
        sierpinski(1, 120)
        right(90)
    # порядок 2
    reset_state(-120, -180, 90)
    for _ in range(4):
        sierpinski(2, 120)
        right(90)
    turtle.update()

# ---------- меню ----------
def main():
    turtle.tracer(0)
    screen = turtle.Screen()
    screen.title("Задача 452")
    print("1 — Квадрат (а)")
    print("2 — Прямоугольник со срезами (б) – введите L")
    print("3 — 15 квадратов (в)")
    print("4 — Год 9-сегм. (г)")
    print("5 — Год 7-сегм. (д)")
    print("6 — Кривые Серпинского (е)")
    try:
        choice = int(input("Ваш выбор: "))
        if choice == 1:
            task_a()
        elif choice == 2:
            L = float(input("Меньшая сторона L: "))
            task_b(L)
        elif choice == 3:
            task_c()
        elif choice == 4:
            task_d()
        elif choice == 5:
            task_e()
        elif choice == 6:
            task_f()
        else:
            print("Неверный выбор.")
        turtle.update()
        print("\nОкно turtle открыто. Закройте его для выхода.")
        turtle.done()
    except ValueError:
        print("Ошибка ввода.")

if __name__ == "__main__":
    main()
