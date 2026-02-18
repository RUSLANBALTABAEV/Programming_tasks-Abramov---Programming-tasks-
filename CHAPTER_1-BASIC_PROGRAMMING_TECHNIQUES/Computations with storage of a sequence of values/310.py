"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
9. Вычисления с хранением последовательности значений

310. Даны натуральные числа x, y, r1, r2, …, rn .Числа ri являются сторонами квадратов с центрами в точке (x, y). Построить на экране квадраты, заданные последовательностью r1, r2,…, rn, а затем удалить их. Процесс построения должен начинаться квадратом с номером 1 и заканчиваться квадратом с номером n; процесс удаления должен происходить в обратном порядке – начинаться квадратом с номером n и заканчиваться квадратом с номером 1.
"""


import turtle
import random
import time

def main():
    print("Программа для построения и удаления квадратов с общим центром.")
    print("Даны натуральные числа x, y (координаты центра) и r1, r2, ..., rn (стороны квадратов).")
    print("Квадраты рисуются от 1 до n, затем удаляются в обратном порядке.")

    # Выбор способа ввода
    print("\nВыберите способ задания данных:")
    print("1. Ввести числа вручную")
    print("2. Сгенерировать случайные данные")
    print("3. Использовать готовый пример")

    while True:
        try:
            choice = int(input("\nВаш выбор (1-3): "))
            if 1 <= choice <= 3:
                break
            else:
                print("Ошибка: введите 1, 2 или 3.")
        except ValueError:
            print("Ошибка: введите целое число.")

    # Ввод центра
    if choice == 1:
        while True:
            try:
                x = int(input("Введите x центра: "))
                y = int(input("Введите y центра: "))
                break
            except ValueError:
                print("Ошибка: введите целые числа.")
    else:
        # Случайный центр в пределах экрана
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        print(f"Центр выбран случайно: ({x}, {y})")

    # Ввод списка сторон
    if choice == 1:
        while True:
            try:
                n = int(input("Введите количество квадратов n: "))
                if n > 0:
                    break
                else:
                    print("Ошибка: n должно быть положительным.")
            except ValueError:
                print("Ошибка: введите целое число.")
        radii = []
        print(f"Введите {n} натуральных чисел (стороны квадратов):")
        for i in range(n):
            while True:
                try:
                    r = int(input(f"r_{i+1}: "))
                    if r > 0:
                        radii.append(r)
                        break
                    else:
                        print("Ошибка: сторона должна быть положительной.")
                except ValueError:
                    print("Ошибка: введите целое число.")
    elif choice == 2:
        n = random.randint(3, 8)
        radii = [random.randint(20, 150) for _ in range(n)]
        print(f"Сгенерировано {n} случайных сторон: {radii}")
    else:
        # Готовые примеры
        examples = [
            [30, 60, 90, 120],
            [50, 80, 110, 140, 170],
            [25, 45, 65, 85, 105, 125]
        ]
        print("Выберите готовый набор сторон:")
        for idx, ex in enumerate(examples, 1):
            print(f"{idx}. {ex}")
        while True:
            try:
                ex_choice = int(input("Ваш выбор (1-3): "))
                if 1 <= ex_choice <= 3:
                    radii = examples[ex_choice-1]
                    n = len(radii)
                    break
                else:
                    print("Ошибка: введите 1-3.")
            except ValueError:
                print("Ошибка: введите целое число.")

    # Настройка экрана turtle
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("white")
    screen.title("Построение и удаление квадратов")
    screen.tracer(0)  # отключаем автообновление для контроля

    # Создаём черепаху
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.penup()

    # Цвета
    fill_color = "blue"
    bg_color = "white"

    def draw_square(center_x, center_y, side, color):
        """Рисует закрашенный квадрат с центром (cx, cy) и стороной side цветом color."""
        half = side / 2
        t.goto(center_x - half, center_y - half)  # левый нижний угол
        t.pendown()
        t.fillcolor(color)
        t.begin_fill()
        for _ in range(4):
            t.forward(side)
            t.left(90)
        t.end_fill()
        t.penup()
        screen.update()

    # Рисование квадратов в прямом порядке
    print("\nРисование квадратов...")
    for i, side in enumerate(radii, 1):
        draw_square(x, y, side, fill_color)
        # Подпись номера
        t.goto(x, y + side/2 + 10)  # чуть выше квадрата
        t.write(f"{i}", align="center", font=("Arial", 12, "normal"))
        time.sleep(0.5)
        screen.update()

    time.sleep(1)  # пауза перед удалением

    # Удаление квадратов в обратном порядке
    print("Удаление квадратов...")
    for i, side in enumerate(reversed(radii), 1):
        draw_square(x, y, side, bg_color)  # закрашиваем белым
        # Стираем подпись (закрашиваем белым прямоугольником)
        t.goto(x, y + side/2 + 10)
        t.dot(20, bg_color)  # белая точка для очистки текста
        time.sleep(0.5)
        screen.update()

    print("Процесс завершен. Нажмите на окне для выхода.")
    screen.exitonclick()

if __name__ == "__main__":
    main()
