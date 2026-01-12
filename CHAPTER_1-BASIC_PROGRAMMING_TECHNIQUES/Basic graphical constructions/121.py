"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
5. Простейшие графические построения

121. Построить и закрасить квадрат со стороной 30 пиксел *), центр которого совмещен с центром экрана. Стороны квадрата должны быть параллельны осям координат экрана.
*) Длины отрезков в этой и следующих задачах указываются в количестве адресуемых точек экран (пикселах).
"""


import tkinter as tk

def draw_centered_square_tkinter():
    """Рисует квадрат со стороной 30 пикселей в центре экрана с помощью Tkinter"""
    root = tk.Tk()
    root.title("Задание 121: Центрированный квадрат")
    
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
    
    # Размер квадрата
    square_size = 30
    half_size = square_size // 2
    
    # Координаты квадрата (центрированного)
    x1 = center_x - half_size
    y1 = center_y - half_size
    x2 = center_x + half_size
    y2 = center_y + half_size
    
    # Рисуем и закрашиваем квадрат
    canvas.create_rectangle(x1, y1, x2, y2, fill="lightblue", outline="black", width=2)
    
    # Подпись
    canvas.create_text(center_x, center_y + half_size + 20, 
                      text=f"Квадрат {square_size}x{square_size} пикселей", 
                      font=("Arial", 10))
    canvas.create_text(center_x, center_y + half_size + 40, 
                      text="Центр: ({}, {})".format(center_x, center_y), 
                      font=("Arial", 9))
    
    # Оси координат (необязательно, для наглядности)
    canvas.create_line(center_x, 0, center_x, window_height, fill="gray", dash=(2, 2))
    canvas.create_line(0, center_y, window_width, center_y, fill="gray", dash=(2, 2))
    
    # Отметка центра
    canvas.create_oval(center_x-3, center_y-3, center_x+3, center_y+3, fill="red")
    
    root.mainloop()

if __name__ == "__main__":
    draw_centered_square_tkinter()
