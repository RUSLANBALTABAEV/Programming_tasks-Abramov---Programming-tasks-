"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

528. Дан файл f, компоненты которого являются натуральными числами. Количество чисел в файле кратно 4. Первые два числа из каждых четырех задают координаты левого верхнего угла прямоугольника, следующие два числа - координаты его правого нижнего угла. Построить прямоугольники, заданные в файле f.
"""


import random
import os
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
    """Создаёт файл f с координатами прямоугольников."""
    print("Файл f не существует или пуст. Задайте координаты прямоугольников.")
    print("Формат файла: последовательность целых чисел x1 y1 x2 y2 (для каждого прямоугольника).")
    print("Количество чисел должно быть кратно 4.")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод координат (все числа через пробел в одной строке)")
    print("2 — Случайная генерация прямоугольников")
    print("3 — Готовый пример")

    while True:
        choice = input("Ваш выбор (1/2/3): ").strip()
        if choice in ('1', '2', '3'):
            break
        print("Ошибка: выберите 1, 2 или 3.")

    if choice == '1':
        while True:
            try:
                raw = input("Введите координаты (x1 y1 x2 y2 …) через пробел: ").strip()
                if not raw:
                    print("Пустой ввод. Будет использован готовый пример.")
                    numbers = [0, 100, 100, 0, 150, 150, 250, 50]
                else:
                    numbers = list(map(int, raw.split()))
                if len(numbers) == 0:
                    continue
                if len(numbers) % 4 != 0:
                    print(f"Ошибка: количество чисел должно быть кратно 4, а у вас {len(numbers)}.")
                    continue
                # Проверим, что координаты допустимы (левая верхняя точка левее/выше правой нижней)
                valid = True
                for i in range(0, len(numbers), 4):
                    x1, y1, x2, y2 = numbers[i], numbers[i+1], numbers[i+2], numbers[i+3]
                    if x2 <= x1 or y1 <= y2:
                        print(f"Ошибка в прямоугольнике {i//4 + 1}: должно быть x1 < x2 и y2 < y1.")
                        valid = False
                        break
                if not valid:
                    continue
                text = ' '.join(map(str, numbers))
                break
            except ValueError:
                print("Ошибка: введите целые числа.")
    elif choice == '2':
        num_rects = random.randint(2, 5)
        numbers = []
        for _ in range(num_rects):
            # Случайные координаты, чтобы левый верхний был левее и выше правого нижнего
            x1 = random.randint(-200, 150)
            x2 = random.randint(x1 + 20, 250)
            y1 = random.randint(50, 200)
            y2 = random.randint(-150, y1 - 20)
            numbers.extend([x1, y1, x2, y2])
        text = ' '.join(map(str, numbers))
        print(f"Сгенерированы координаты для {num_rects} прямоугольников.")
    else:  # готовый пример
        numbers = [0, 100, 100, 0, 150, 150, 250, 50, -150, 0, -50, -100, 50, -50, 150, -150]
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
    # Проверим корректность данных
    numbers = content.split()
    if len(numbers) % 4 != 0:
        create_file_f(filename)
        return
    try:
        for i in range(0, len(numbers), 4):
            x1, y1, x2, y2 = map(int, numbers[i:i+4])
            if x2 <= x1 or y1 <= y2:
                create_file_f(filename)
                return
    except ValueError:
        create_file_f(filename)


# ------------------------------------------------------------
# 3. Чтение прямоугольников из файла
# ------------------------------------------------------------
def read_rectangles(filename):
    """Возвращает список кортежей (x1, y1, x2, y2)."""
    content = read_file(filename).strip()
    if not content:
        return []
    numbers = list(map(int, content.split()))
    rectangles = []
    for i in range(0, len(numbers), 4):
        rectangles.append((numbers[i], numbers[i+1], numbers[i+2], numbers[i+3]))
    return rectangles


# ------------------------------------------------------------
# 4. Построение прямоугольников с помощью turtle
# ------------------------------------------------------------
def draw_rectangles(rectangles):
    """Рисует прямоугольники в графическом окне."""
    if not rectangles:
        print("Нет данных для рисования.")
        return

    screen = turtle.Screen()
    screen.title("Задача 528: Прямоугольники из файла f")
    screen.setup(800, 600)
    screen.tracer(0)

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.pensize(2)

    for x1, y1, x2, y2 in rectangles:
        t.penup()
        t.goto(x1, y1)
        t.pendown()
        t.goto(x2, y1)
        t.goto(x2, y2)
        t.goto(x1, y2)
        t.goto(x1, y1)

    screen.update()
    print("Прямоугольники отрисованы в окне turtle.")
    print("Закройте окно с графикой, чтобы завершить программу.")
    turtle.done()


# ------------------------------------------------------------
# 5. Основная программа
# ------------------------------------------------------------
def main():
    print("Задача 528: Построение прямоугольников из файла")
    file_f = "f.txt"

    ensure_file_exists(file_f)
    rectangles = read_rectangles(file_f)

    if not rectangles:
        print("Нет корректных данных.")
        return

    print("\nКоординаты прямоугольников (x1, y1) – (x2, y2):")
    for i, (x1, y1, x2, y2) in enumerate(rectangles, 1):
        width = abs(x2 - x1)
        height = abs(y1 - y2)
        print(f"  {i}. ({x1}, {y1}) – ({x2}, {y2})  [ширина: {width}, высота: {height}]")

    draw_rectangles(rectangles)


if __name__ == "__main__":
    main()