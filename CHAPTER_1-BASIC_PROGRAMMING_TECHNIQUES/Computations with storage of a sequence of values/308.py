"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
9. Вычисления с хранением последовательности значений

308. В условие предыдущей задачи вносится изменение: поочередное построение точек следует выполнять так, чтобы после появления на экране первых трех точек построение каждой новой точки сопровождалось удалением точки, которая была построена раньше трех других видимых точек.
"""


import turtle
import random
import time
from collections import deque

def main():
    print("Программа для поочередного построения точек с отображением трёх последних.")
    print("Сначала точки строятся в порядке от 1 до n, при этом всегда видны три последние.")
    print("Затем процесс повторяется в обратном порядке от n до 1.")
    
    # Выбор способа ввода
    print("\nВыберите способ задания точек:")
    print("1. Ввести координаты вручную")
    print("2. Сгенерировать случайные точки")
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
    
    if choice == 1:
        # Ручной ввод
        while True:
            try:
                n = int(input("Введите количество точек n: "))
                if n > 0:
                    break
                else:
                    print("Ошибка: n должно быть положительным.")
            except ValueError:
                print("Ошибка: введите целое число.")
        
        points = []
        print("Введите координаты x y (целые числа) через пробел для каждой точки:")
        for i in range(n):
            while True:
                try:
                    coords = input(f"Точка {i+1}: ").split()
                    if len(coords) != 2:
                        print("Ошибка: введите два числа.")
                        continue
                    x = int(coords[0])
                    y = int(coords[1])
                    points.append((x, y))
                    break
                except ValueError:
                    print("Ошибка: введите целые числа.")
    
    elif choice == 2:
        # Случайные точки
        n = random.randint(5, 15)
        points = []
        for _ in range(n):
            x = random.randint(-200, 200)
            y = random.randint(-200, 200)
            points.append((x, y))
        print(f"Сгенерировано {n} случайных точек.")
    
    else:
        # Готовые примеры
        examples = [
            [(50, 50), (100, 100), (150, 50), (200, 150), (250, 100), (300, 200), (350, 150)],
            [(-100, -100), (-50, -50), (0, 0), (50, 50), (100, 100), (150, 150)],
            [(30, 120), (80, 80), (130, 180), (180, 60), (230, 140), (280, 200), (330, 100), (380, 250)]
        ]
        print("Выберите готовый набор:")
        for idx, ex in enumerate(examples, 1):
            print(f"{idx}. {ex[:3]}... (всего {len(ex)} точек)")
        while True:
            try:
                ex_choice = int(input("Ваш выбор (1-3): "))
                if 1 <= ex_choice <= 3:
                    points = examples[ex_choice-1]
                    n = len(points)
                    break
                else:
                    print("Ошибка: введите 1-3.")
            except ValueError:
                print("Ошибка: введите целое число.")
    
    # Настройка экрана turtle
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("white")
    screen.title("Построение точек с тремя видимыми")
    screen.tracer(0)  # отключаем автообновление для контроля
    
    # Создаём черепаху
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.penup()
    
    # Параметры
    dot_size = 10
    point_color = "blue"
    bg_color = "white"
    
    def draw_point(x, y, color=point_color):
        t.goto(x, y)
        t.dot(dot_size, color)
        screen.update()
    
    def erase_point(x, y):
        t.goto(x, y)
        t.dot(dot_size, bg_color)
        screen.update()
    
    def clear_all():
        """Очистить всё поле (белым фоном)."""
        t.clear()
        screen.update()
    
    def animate_sequence(indices, delay=0.5):
        """Проход по точкам в порядке индексов с правилом трёх последних."""
        # Очередь для хранения индексов текущих видимых точек (макс 3)
        visible = deque()
        for idx in indices:
            x, y = points[idx]
            # Если уже есть 3 видимых, удаляем самую старую
            if len(visible) == 3:
                oldest = visible.popleft()
                ox, oy = points[oldest]
                erase_point(ox, oy)
            # Рисуем новую точку
            draw_point(x, y)
            visible.append(idx)
            # Подписываем номер (опционально)
            t.goto(x, y + 15)
            t.write(f"{idx+1}", align="center", font=("Arial", 10, "normal"))
            screen.update()
            time.sleep(delay)
    
    # Первый проход: от 0 до n-1 (номера 1..n)
    print("\nПервый проход (от 1 до n):")
    animate_sequence(range(n))
    
    # Пауза между проходами
    time.sleep(2)
    print("Очистка экрана перед вторым проходом...")
    clear_all()
    time.sleep(1)
    
    # Второй проход: от n-1 до 0 (номера n..1)
    print("Второй проход (от n до 1):")
    animate_sequence(range(n-1, -1, -1))
    
    print("Процесс завершен. Нажмите на окне для выхода.")
    screen.exitonclick()

if __name__ == "__main__":
    main()
