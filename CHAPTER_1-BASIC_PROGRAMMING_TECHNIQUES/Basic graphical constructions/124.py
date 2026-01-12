"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
5. Простейшие графические построения

124. Столбчатая диаграмма (гистограмма) представляет собой
набор прямоугольников, основания которых равны, а высоты
пропорциональны числовым величинам, взятым из некоторой
cовокупности (рис. 6). Для большей наглядности прямоугольники диаграммы обычно закрашивают в разные цвета.
Даны семь действительных положительных чисел a1, a2 , …, a7.
Построить гистограмму для этих значений.

"""


import tkinter as tk
import random

def draw_histogram_tkinter():
    """Рисует гистограмму для семи положительных чисел"""
    # Пример данных: 7 положительных действительных чисел
    data = [5.2, 7.8, 3.5, 9.1, 2.3, 8.4, 4.6]
    
    root = tk.Tk()
    root.title("Задание 124: Гистограмма")
    
    # Устанавливаем размер окна
    window_width = 600
    window_height = 500
    root.geometry(f"{window_width}x{window_height}")
    
    # Создаем холст
    canvas = tk.Canvas(root, width=window_width, height=window_height, bg="white")
    canvas.pack()
    
    # Параметры гистограммы
    margin = 60  # отступ от краев
    chart_width = window_width - 2 * margin
    chart_height = window_height - 2 * margin
    bar_count = len(data)
    bar_width = chart_width / (bar_count + 1)  # ширина столбца с промежутками
    
    # Цвета для столбцов
    colors = ["#FF6B6B", "#4ECDC4", "#FFD166", "#06D6A0", 
              "#118AB2", "#EF476F", "#073B4C"]
    
    # Находим максимальное значение для масштабирования
    max_value = max(data)
    scale_factor = chart_height / max_value
    
    # Рисуем оси
    canvas.create_line(margin, window_height - margin, 
                      window_width - margin, window_height - margin, 
                      width=2)  # ось X
    canvas.create_line(margin, margin, margin, window_height - margin, 
                      width=2)  # ось Y
    
    # Подписи к оси Y
    for i in range(0, 11):
        y = window_height - margin - (i * chart_height / 10)
        value = i * max_value / 10
        canvas.create_line(margin - 5, y, margin, y, width=1)
        canvas.create_text(margin - 10, y, text=f"{value:.1f}", 
                          anchor="e", font=("Arial", 8))
    
    # Рисуем столбцы гистограммы
    for i, value in enumerate(data):
        # Вычисляем координаты столбца
        x1 = margin + (i + 0.5) * bar_width
        x2 = x1 + bar_width * 0.8
        y1 = window_height - margin
        y2 = y1 - value * scale_factor
        
        # Рисуем и закрашиваем столбец
        canvas.create_rectangle(x1, y1, x2, y2, fill=colors[i], outline="black", width=1)
        
        # Подпись значения над столбцом
        canvas.create_text((x1 + x2) / 2, y2 - 10, text=f"{value:.1f}", 
                          font=("Arial", 10, "bold"))
        
        # Подпись индекса под столбцом
        canvas.create_text((x1 + x2) / 2, y1 + 15, text=f"a{i+1}", 
                          font=("Arial", 10, "bold"))
        
        # Подпись значения внутри столбца (если столбец достаточно высокий)
        if value * scale_factor > 20:
            canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=f"{value:.1f}", 
                              fill="white", font=("Arial", 9, "bold"))
    
    # Заголовок
    canvas.create_text(window_width // 2, 30, 
                      text="Гистограмма для семи положительных чисел", 
                      font=("Arial", 14, "bold"))
    
    # Подпись осей
    canvas.create_text(window_width // 2, window_height - 20, 
                      text="Индексы (a₁...a₇)", font=("Arial", 10, "bold"))
    canvas.create_text(20, window_height // 2, text="Значения", 
                      font=("Arial", 10, "bold"), angle=90)
    
    # Легенда
    legend_x = window_width - 150
    legend_y = 80
    canvas.create_rectangle(legend_x - 10, legend_y - 10, 
                           legend_x + 140, legend_y + 170, 
                           fill="lightyellow", outline="gray")
    canvas.create_text(legend_x + 60, legend_y, text="Легенда", 
                      font=("Arial", 10, "bold"))
    
    for i in range(len(data)):
        canvas.create_rectangle(legend_x, legend_y + 20 + i * 20, 
                               legend_x + 15, legend_y + 35 + i * 20, 
                               fill=colors[i], outline="black")
        canvas.create_text(legend_x + 30, legend_y + 27 + i * 20, 
                          text=f"a{i+1} = {data[i]:.1f}", 
                          font=("Arial", 9), anchor="w")
    
    root.mainloop()

if __name__ == "__main__":
    draw_histogram_tkinter()
