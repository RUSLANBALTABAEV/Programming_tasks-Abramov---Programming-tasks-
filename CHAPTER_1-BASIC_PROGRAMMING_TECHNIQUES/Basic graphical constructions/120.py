"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
5. Простейшие графические построения

120. Построить:
а) треугольник с вершинами (100, 100), (150, 100), (80, 170);
б) прямоугольник с вершинами (80, 80), (170, 80), (170, 150), (80, 150);
в) пятиугольник с вершинами (100, 100), (150, 100), (170, 120), (150, 140), (100, 140), (80, 120);
г) шестиугольник с вершинами (120, 100), (140, 120), (140, 140), (120, 160), (100, 140), (100, 120);
д) выполнить задания а) - г), дополнив каждое из них требованием закраски построенной плоской фигуры *).
*) Построения и закраску фигур в этой и последующих на конкретной вычислительной машине.
"""


import tkinter as tk

def draw_figures_tkinter():
    """Рисование фигур с использованием Tkinter"""
    root = tk.Tk()
    root.title("Задание 120 - Tkinter")
    root.geometry("800x600")
    
    canvas = tk.Canvas(root, width=800, height=600, bg="white")
    canvas.pack()
    
    # Смещения
    offsets = [(50, 50), (300, 50), (50, 250), (300, 250)]
    
    # Треугольник
    offset = offsets[0]
    triangle = [
        100 + offset[0], 100 + offset[1],
        150 + offset[0], 100 + offset[1],
        80 + offset[0], 170 + offset[1]
    ]
    canvas.create_polygon(triangle, fill="lightblue", outline="black", width=2)
    canvas.create_text(offset[0] + 100, offset[1] + 200, text="а) Треугольник")
    
    # Прямоугольник
    offset = offsets[1]
    rect = [
        80 + offset[0], 80 + offset[1],
        170 + offset[0], 80 + offset[1],
        170 + offset[0], 150 + offset[1],
        80 + offset[0], 150 + offset[1]
    ]
    canvas.create_polygon(rect, fill="lightgreen", outline="black", width=2)
    canvas.create_text(offset[0] + 125, offset[1] + 200, text="б) Прямоугольник")
    
    # Пятиугольник
    offset = offsets[2]
    pentagon = [
        100 + offset[0], 100 + offset[1],
        150 + offset[0], 100 + offset[1],
        170 + offset[0], 120 + offset[1],
        150 + offset[0], 140 + offset[1],
        100 + offset[0], 140 + offset[1],
        80 + offset[0], 120 + offset[1]
    ]
    canvas.create_polygon(pentagon, fill="lightcoral", outline="black", width=2)
    canvas.create_text(offset[0] + 100, offset[1] + 200, text="в) Пятиугольник")
    
    # Шестиугольник
    offset = offsets[3]
    hexagon = [
        120 + offset[0], 100 + offset[1],
        140 + offset[0], 120 + offset[1],
        140 + offset[0], 140 + offset[1],
        120 + offset[0], 160 + offset[1],
        100 + offset[0], 140 + offset[1],
        100 + offset[0], 120 + offset[1]
    ]
    canvas.create_polygon(hexagon, fill="lightgoldenrod", outline="black", width=2)
    canvas.create_text(offset[0] + 125, offset[1] + 200, text="г) Шестиугольник")
    
    # Заголовок
    canvas.create_text(400, 20, text="Задание 120: Фигуры с закраской", 
                      font=("Arial", 16, "bold"))
    
    root.mainloop()

if __name__ == "__main__":
    draw_figures_tkinter()
