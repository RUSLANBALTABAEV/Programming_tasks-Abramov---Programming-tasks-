"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
9. Вычисления с хранением последовательности значений

309. Даны натуральные числа x1, y1, r1, x2, y2, r2, …, xn, yn, rn. 
Числа xi, yi являются центрами кругов радиуса ri. Построить на экране круги, заданные последовательностью x1, y1, r1, x2, y2, r2, …, xn, yn, rn, а затем закрасить их (одним и тем же цветом или разными цветами). Процесс построения должен начинаться кругом с номером 1 и заканчиваться кругом с номером n; процесс закраски должен происходить в обратном порядке – начинаться кругом с номером n и заканчиваться кругом с номером 1.
"""


import turtle
import random
import time

def main():
    print("Программа для построения и закраски кругов.")
    print("Даны последовательно: x1, y1, r1, x2, y2, r2, ..., xn, yn, rn.")
    print("Сначала рисуются контуры кругов в порядке 1..n, затем они закрашиваются в обратном порядке.")
    
    # Выбор способа ввода
    print("\nВыберите способ задания данных:")
    print("1. Ввести числа вручную")
    print("2. Сгенерировать случайные круги")
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
    
    circles = []  # список кортежей (x, y, r)
    
    if choice == 1:
        # Ручной ввод
        while True:
            try:
                n = int(input("Введите количество кругов n: "))
                if n > 0:
                    break
                else:
                    print("Ошибка: n должно быть положительным.")
            except ValueError:
                print("Ошибка: введите целое число.")
        
        print("Введите x y r (натуральные числа) для каждого круга:")
        for i in range(n):
            while True:
                try:
                    vals = input(f"Круг {i+1}: ").split()
                    if len(vals) != 3:
                        print("Ошибка: введите три числа.")
                        continue
                    x = int(vals[0])
                    y = int(vals[1])
                    r = int(vals[2])
                    if r <= 0:
                        print("Ошибка: радиус должен быть положительным.")
                        continue
                    circles.append((x, y, r))
                    break
                except ValueError:
                    print("Ошибка: введите целые числа.")
    
    elif choice == 2:
        # Случайные круги
        n = random.randint(3, 8)
        for _ in range(n):
            x = random.randint(-200, 200)
            y = random.randint(-200, 200)
            r = random.randint(20, 80)
            circles.append((x, y, r))
        print(f"Сгенерировано {n} случайных кругов.")
    
    else:
        # Готовые примеры
        examples = [
            [(50, 50, 40), (150, 80, 30), (250, 120, 50), (350, 60, 35)],
            [(-100, -100, 50), (0, 0, 70), (100, 100, 60), (200, 50, 40)],
            [(30, 120, 30), (80, 80, 45), (130, 180, 25), (180, 60, 55), (230, 140, 40)]
        ]
        print("Выберите готовый набор:")
        for idx, ex in enumerate(examples, 1):
            print(f"{idx}. {ex[:2]}... (всего {len(ex)} кругов)")
        while True:
            try:
                ex_choice = int(input("Ваш выбор (1-3): "))
                if 1 <= ex_choice <= 3:
                    circles = examples[ex_choice-1]
                    n = len(circles)
                    break
                else:
                    print("Ошибка: введите 1-3.")
            except ValueError:
                print("Ошибка: введите целое число.")
    
    # Настройка экрана
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("white")
    screen.title("Построение и закраска кругов")
    screen.tracer(0)  # отключаем автообновление для контроля
    
    # Создаём черепаху
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.penup()
    
    # Параметры
    outline_color = "black"
    fill_colors = ["red", "green", "blue", "orange", "purple", "cyan", "magenta", "yellow", "pink", "brown"]
    
    def draw_circle_outline(x, y, r):
        t.goto(x, y - r)
        t.pendown()
        t.pencolor(outline_color)
        t.circle(r)
        t.penup()
        screen.update()
    
    def fill_circle(x, y, r, color):
        t.goto(x, y - r)
        t.pendown()
        t.fillcolor(color)
        t.begin_fill()
        t.circle(r)
        t.end_fill()
        t.penup()
        screen.update()
    
    # Рисуем контуры в прямом порядке
    print("\nРисование контуров кругов...")
    for i, (x, y, r) in enumerate(circles, 1):
        draw_circle_outline(x, y, r)
        # Подпишем номер (опционально)
        t.goto(x, y - r - 15)
        t.write(f"{i}", align="center", font=("Arial", 12, "normal"))
        time.sleep(0.3)
        screen.update()
    
    time.sleep(1)  # пауза перед закраской
    
    # Закрашиваем в обратном порядке
    print("Закраска кругов в обратном порядке...")
    for i, (x, y, r) in enumerate(reversed(circles), 1):
        # Выбираем цвет: можно один и тот же, или разные. По заданию можно одним или разными.
        # Для демонстрации используем разные цвета.
        color = fill_colors[(i-1) % len(fill_colors)]
        fill_circle(x, y, r, color)
        time.sleep(0.5)
        screen.update()
    
    print("Процесс завершен. Нажмите на окне для выхода.")
    screen.exitonclick()

if __name__ == "__main__":
    main()
