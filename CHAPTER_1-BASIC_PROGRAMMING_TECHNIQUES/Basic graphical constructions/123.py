"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
5. Простейшие графические построения

123.Построить и закрасить круг радиуса 40 пиксел, центр которого совмещён с центром экрана.
"""


import tkinter as tk
import math

def draw_centered_circle_tkinter():
    """Рисует круг радиусом 40 пикселей в центре экрана"""
    root = tk.Tk()
    root.title("Задание 123: Центрированный круг")
    
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
    
    # Радиус круга
    radius = 40
    
    # Координаты ограничивающего прямоугольника для круга
    x1 = center_x - radius
    y1 = center_y - radius
    x2 = center_x + radius
    y2 = center_y + radius
    
    # Рисуем и закрашиваем круг
    canvas.create_oval(x1, y1, x2, y2, fill="lightblue", outline="black", width=2)
    
    # Подпись
    canvas.create_text(center_x, center_y + radius + 20, 
                      text=f"Круг радиусом {radius} пикселей", 
                      font=("Arial", 10))
    canvas.create_text(center_x, center_y + radius + 40, 
                      text="Центр: ({}, {})".format(center_x, center_y), 
                      font=("Arial", 9))
    canvas.create_text(center_x, center_y + radius + 60, 
                      text=f"Диаметр: {radius * 2} пикселей", 
                      font=("Arial", 9))
    
    # Оси координат (необязательно, для наглядности)
    canvas.create_line(center_x, 0, center_x, window_height, fill="gray", dash=(2, 2))
    canvas.create_line(0, center_y, window_width, center_y, fill="gray", dash=(2, 2))
    
    # Отметка центра
    canvas.create_oval(center_x-3, center_y-3, center_x+3, center_y+3, fill="red")
    
    # Радиусная линия (необязательно, для наглядности)
    canvas.create_line(center_x, center_y, center_x + radius, center_y, 
                      fill="blue", width=1, arrow=tk.LAST)
    canvas.create_text(center_x + radius//2, center_y - 10, 
                      text=f"R = {radius} px", fill="blue", font=("Arial", 9))
    
    # Отметка радиуса на круге
    for angle in [0, 90, 180, 270]:
        rad = math.radians(angle)
        x_end = center_x + radius * math.cos(rad)
        y_end = center_y + radius * math.sin(rad)
        canvas.create_line(center_x, center_y, x_end, y_end, 
                          fill="blue", width=1, dash=(3, 2))
    
    root.mainloop()

if __name__ == "__main__":
    draw_centered_circle_tkinter()
