"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
6. Пошаговый ввод данных и вывод результатов *)

171. Даны натуральные числа n, a0, a1, a2, ..., a3n-1. Каждая тройка чисел ai, ai + 1, ai + 2, где i кратно трем, задает координаты центра квадрата (ai, ai + 1) 
и длину его стороны ai + 2. Предполагается, что стороны квадратов расположены параллельно осям координат экрана.
Построить и закрасить какими-либо цветами квадраты, заданные последовательностью a0, a1, a2, ..., a3n-1.
"""


import tkinter as tk
import random

def draw_squares():
    # Очищаем предыдущее сообщение об ошибке
    result_label.config(text="")
    
    # Получаем данные из текстового поля
    data = entry.get().strip()
    if not data:
        result_label.config(text="Ошибка: введите данные!")
        return
    
    try:
        numbers = list(map(int, data.split()))
    except ValueError:
        result_label.config(text="Ошибка: введите целые числа!")
        return
    
    if len(numbers) < 1:
        result_label.config(text="Ошибка: введите хотя бы число n!")
        return
    
    n = numbers[0]
    
    if n < 1:
        result_label.config(text="Ошибка: n должно быть натуральным числом!")
        return
    
    expected_count = 3 * n
    
    if len(numbers) != expected_count + 1:  # +1 потому что первое число - n
        result_label.config(text=f"Ошибка: для n={n} нужно ввести {expected_count} чисел, а получено {len(numbers)-1}")
        return
    
    # Создаем новое окно для отрисовки
    window = tk.Toplevel(root)
    window.title("Квадраты")
    
    # Определяем размеры холста на основе максимальных и минимальных координат
    min_x = float('inf')
    max_x = float('-inf')
    min_y = float('inf')
    max_y = float('-inf')
    
    # Сначала находим минимальные и максимальные координаты для определения размеров холста
    squares_data = []
    for i in range(n):
        idx = 1 + i * 3  # индекс начала тройки (пропускаем n)
        x = numbers[idx]
        y = numbers[idx + 1]
        side = numbers[idx + 2]
        
        if side <= 0:
            result_label.config(text=f"Ошибка: сторона квадрата {i+1} должна быть положительной!")
            window.destroy()
            return
        
        # Координаты углов квадрата
        x1 = x - side / 2
        y1 = y - side / 2
        x2 = x + side / 2
        y2 = y + side / 2
        
        min_x = min(min_x, x1)
        max_x = max(max_x, x2)
        min_y = min(min_y, y1)
        max_y = max(max_y, y2)
        
        squares_data.append((x, y, side, x1, y1, x2, y2))
    
    # Добавляем отступы
    padding = 20
    min_x -= padding
    max_x += padding
    min_y -= padding
    max_y += padding
    
    # Создаем холст
    canvas_width = int(max_x - min_x)
    canvas_height = int(max_y - min_y)
    
    # Ограничиваем минимальный размер окна
    canvas_width = max(400, canvas_width)
    canvas_height = max(400, canvas_height)
    
    canvas = tk.Canvas(window, width=canvas_width, height=canvas_height, bg="white")
    canvas.pack()
    
    # Отрисовываем квадраты
    for i, (x, y, side, x1, y1, x2, y2) in enumerate(squares_data):
        # Сдвигаем координаты, чтобы они вписывались в холст
        shifted_x1 = x1 - min_x
        shifted_y1 = y1 - min_y
        shifted_x2 = x2 - min_x
        shifted_y2 = y2 - min_y
        
        # Генерируем случайный цвет
        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        
        # Рисуем квадрат
        canvas.create_rectangle(shifted_x1, shifted_y1, shifted_x2, shifted_y2, 
                              fill=color, outline="black", width=2)
        
        # Подписываем квадрат
        shifted_x = x - min_x
        shifted_y = y - min_y
        canvas.create_text(shifted_x, shifted_y, text=f"({x},{y})\nсторона: {side}", 
                          font=("Arial", 8), fill="black")
        
        # Подписываем номер квадрата
        canvas.create_text(shifted_x1 + 10, shifted_y1 + 10, text=f"#{i+1}", 
                          font=("Arial", 10, "bold"), fill="black")
    
    # Рисуем оси координат (если они в пределах видимости)
    if min_x <= 0 <= max_x:
        zero_x = -min_x
        canvas.create_line(zero_x, 0, zero_x, canvas_height, fill="red", width=1)
    if min_y <= 0 <= max_y:
        zero_y = -min_y
        canvas.create_line(0, zero_y, canvas_width, zero_y, fill="red", width=1)
    
    result_label.config(text=f"Успешно нарисовано {n} квадратов")

def main():
    global root, entry, result_label
    
    root = tk.Tk()
    root.title("Построение квадратов")
    root.geometry("500x400")
    
    # Инструкция
    instruction = """Введите данные в формате:
    n a0 a1 a2 a3 a4 a5 ... a(3n-1)
    
    где:
    n - количество квадратов
    Каждая тройка чисел задает:
      - x центра квадрата
      - y центра квадрата  
      - длина стороны квадрата
    
    Пример (для n=2):
    2 100 100 50 200 200 30
    
    Другой пример:
    3 50 50 40 150 150 60 250 100 30
    """
    
    label = tk.Label(root, text=instruction, justify=tk.LEFT)
    label.pack(pady=10)
    
    # Поле для ввода данных
    entry = tk.Entry(root, width=60)
    entry.pack(pady=10)
    entry.insert(0, "2 100 100 50 200 200 30")  # Пример по умолчанию
    
    # Кнопка для отрисовки
    draw_button = tk.Button(root, text="Нарисовать квадраты", command=draw_squares)
    draw_button.pack(pady=10)
    
    # Метка для вывода результатов
    result_label = tk.Label(root, text="", fg="blue")
    result_label.pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    main()
