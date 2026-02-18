"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
9. Вычисления с хранением последовательности значений

311. Даны натуральные числа x1, y1, r1, x2, y2, r2, …, xn, yn, rn. 
Построить на экране окружности с центрами в точках (xi, yi) и радиусами ri, если среди r1, r2, …, rn найдется число, меньше 5, и квадраты с центрами в точках (xi, yi) и сторонами ri в противном случае.
"""


import turtle
import random
import time

def main():
    print("Программа для построения окружностей или квадратов по заданным точкам.")
    print("Если среди радиусов есть число меньше 5, строятся окружности, иначе — квадраты.")
    
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
    
    figures = []  # список кортежей (x, y, r)
    
    if choice == 1:
        # Ручной ввод
        while True:
            try:
                n = int(input("Введите количество фигур n: "))
                if n > 0:
                    break
                else:
                    print("Ошибка: n должно быть положительным.")
            except ValueError:
                print("Ошибка: введите целое число.")
        
        print("Введите x y r (натуральные числа) для каждой фигуры:")
        for i in range(n):
            while True:
                try:
                    vals = input(f"Фигура {i+1}: ").split()
                    if len(vals) != 3:
                        print("Ошибка: введите три числа.")
                        continue
                    x = int(vals[0])
                    y = int(vals[1])
                    r = int(vals[2])
                    if r <= 0:
                        print("Ошибка: радиус/сторона должны быть положительными.")
                        continue
                    figures.append((x, y, r))
                    break
                except ValueError:
                    print("Ошибка: введите целые числа.")
    
    elif choice == 2:
        # Случайные данные
        n = random.randint(3, 10)
        for _ in range(n):
            x = random.randint(-200, 200)
            y = random.randint(-200, 200)
            r = random.randint(1, 20)  # чтобы были и маленькие, и большие
            figures.append((x, y, r))
        print(f"Сгенерировано {n} случайных фигур.")
        print("Координаты и размеры:")
        for i, (x, y, r) in enumerate(figures, 1):
            print(f"  {i}: ({x}, {y}) r={r}")
    
    else:
        # Готовые примеры
        examples = [
            # Пример с маленькими радиусами (есть <5)
            [(50, 50, 3), (150, 80, 7), (250, 120, 2), (350, 60, 10)],
            # Пример с большими радиусами (все >=5)
            [(-100, -100, 8), (0, 0, 12), (100, 100, 6), (200, 50, 15)],
            # Смешанный, но с маленьким
            [(30, 120, 4), (80, 80, 9), (130, 180, 5), (180, 60, 11)]
        ]
        print("Выберите готовый набор:")
        for idx, ex in enumerate(examples, 1):
            has_small = any(r < 5 for _, _, r in ex)
            print(f"{idx}. {'Есть r<5' if has_small else 'Все r>=5'}: {ex[:2]}... (всего {len(ex)} фигур)")
        while True:
            try:
                ex_choice = int(input("Ваш выбор (1-3): "))
                if 1 <= ex_choice <= 3:
                    figures = examples[ex_choice-1]
                    break
                else:
                    print("Ошибка: введите 1-3.")
            except ValueError:
                print("Ошибка: введите целое число.")
    
    # Проверка условия
    has_small = any(r < 5 for _, _, r in figures)
    shape_type = "окружности" if has_small else "квадраты"
    print(f"\nОбнаружено число <5: {has_small}. Будем рисовать {shape_type}.")
    
    # Настройка экрана turtle
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("white")
    screen.title(f"Построение {shape_type}")
    screen.tracer(0)  # отключаем автообновление для контроля
    
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.penup()
    
    # Цвета
    colors = ["red", "green", "blue", "orange", "purple", "cyan", "magenta", "yellow", "pink", "brown"]
    
    def draw_circle(x, y, r, color):
        t.goto(x, y - r)
        t.pendown()
        t.pencolor(color)
        t.circle(r)
        t.penup()
    
    def draw_square(x, y, side, color):
        half = side / 2
        t.goto(x - half, y - half)
        t.pendown()
        t.pencolor(color)
        for _ in range(4):
            t.forward(side)
            t.left(90)
        t.penup()
    
    # Рисуем все фигуры
    print("Рисование...")
    for i, (x, y, r) in enumerate(figures, 1):
        color = colors[(i-1) % len(colors)]
        if has_small:
            draw_circle(x, y, r, color)
        else:
            draw_square(x, y, r, color)
        # Подпись номера
        t.goto(x, y + r + 10)
        t.write(f"{i}", align="center", font=("Arial", 12, "normal"))
        screen.update()
        time.sleep(0.3)
    
    print("Готово. Нажмите на окне для выхода.")
    screen.exitonclick()

if __name__ == "__main__":
    main()
