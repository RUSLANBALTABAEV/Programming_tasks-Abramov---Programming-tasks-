"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
5. Простейшие графические построения

122. Построить и закрасить прямоугольник со сторонами 30 и 50 пиксел, центр которого совмещен с центром экрана. Стороны прямоугольника должны быть параллельны осям координат экрана.
"""


import tkinter as tk

def draw_centered_rectangle_tkinter():
    """Рисует прямоугольник со сторонами 30 и 50 пикселей в центре экрана"""
    root = tk.Tk()
    root.title("Задание 122: Центрированный прямоугольник")
    
    # Устанавливаем размер окна
    window_width = 400
    window_height = 400
    root.geometry(f"{window_width}x{window_height}")
    
    # Создаем холст
    canvas = tk.Canvas(root, width=window_width, height=window_height, bg="white")
    canvas.pack()
    
    # Вычисляем центр экрана
    center_x = window_width // 2
    center_y = window_height // 2
    
    # Размеры прямоугольника
    width = 50  # ширина (по горизонтали)
    height = 30  # высота (по вертикали)
    half_width = width // 2
    half_height = height // 2
    
    # Координаты прямоугольника (центрированного)
    x1 = center_x - half_width
    y1 = center_y - half_height
    x2 = center_x + half_width
    y2 = center_y + half_height
    
    # Рисуем и закрашиваем прямоугольник
    canvas.create_rectangle(x1, y1, x2, y2, fill="lightgreen", outline="black", width=2)
    
    # Подпись
    canvas.create_text(center_x, center_y + half_height + 20, 
                      text=f"Прямоугольник {width}x{height} пикселей", 
                      font=("Arial", 10))
    canvas.create_text(center_x, center_y + half_height + 40, 
                      text="Центр: ({}, {})".format(center_x, center_y), 
                      font=("Arial", 9))
    
    # Оси координат (необязательно, для наглядности)
    canvas.create_line(center_x, 0, center_x, window_height, fill="gray", dash=(2, 2))
    canvas.create_line(0, center_y, window_width, center_y, fill="gray", dash=(2, 2))
    
    # Отметка центра
    canvas.create_oval(center_x-3, center_y-3, center_x+3, center_y+3, fill="red")
    
    # Размерные линии (необязательно, для наглядности)
    # Горизонтальная размерная линия
    canvas.create_line(x1, y1 - 10, x2, y1 - 10, fill="blue", width=1)
    canvas.create_line(x1, y1 - 15, x1, y1 - 5, fill="blue", width=1)
    canvas.create_line(x2, y1 - 15, x2, y1 - 5, fill="blue", width=1)
    canvas.create_text(center_x, y1 - 25, text=f"{width} px", fill="blue", font=("Arial", 9))
    
    # Вертикальная размерная линия
    canvas.create_line(x2 + 10, y1, x2 + 10, y2, fill="blue", width=1)
    canvas.create_line(x2 + 5, y1, x2 + 15, y1, fill="blue", width=1)
    canvas.create_line(x2 + 5, y2, x2 + 15, y2, fill="blue", width=1)
    canvas.create_text(x2 + 25, center_y, text=f"{height} px", fill="blue", font=("Arial", 9), angle=90)
    
    root.mainloop()

if __name__ == "__main__":
    draw_centered_rectangle_tkinter()
