"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
5. Простейшие графические построения

126. Даны натуральные v1, v2, …, v8, задающие число дней в
году, в которых преобладало соответственно северное, северо-
восточное, восточное, юго-восточное, южное, юго-западное, западное
или северо-западное направление ветра. Построить розу ветров (рис. 8).
"""


import tkinter as tk
from tkinter import ttk, messagebox
import math

def draw_interactive_wind_rose():
    """Интерактивная роза ветров с возможностью ввода данных"""
    
    def draw_rose():
        """Рисует розу ветров на основе введенных данных"""
        try:
            # Получаем данные из полей ввода
            data = []
            for i in range(8):
                value = int(entries[i].get())
                if value < 0:
                    messagebox.showerror("Ошибка", "Число дней не может быть отрицательным!")
                    return
                data.append(value)
            
            # Очищаем холст
            canvas.delete("all")
            
            # Центр розы ветров
            center_x = canvas.winfo_width() // 2
            center_y = canvas.winfo_height() // 2
            
            # Максимальный радиус
            max_radius = min(center_x, center_y) - 60
            max_value = max(data)
            
            if max_value == 0:
                canvas.create_text(center_x, center_y, 
                                  text="Все значения равны нулю", 
                                  font=("Arial", 14, "bold"))
                return
            
            # Направления
            directions = ["С", "СВ", "В", "ЮВ", "Ю", "ЮЗ", "З", "СЗ"]
            direction_angles = [0, 45, 90, 135, 180, 225, 270, 315]
            
            # Цвета
            colors = ["#FF6B6B", "#4ECDC4", "#FFD166", "#06D6A0", 
                     "#118AB2", "#EF476F", "#073B4C", "#8338EC"]
            
            # Рисуем концентрические круги
            for i in range(1, 6):
                radius = max_radius * i / 5
                canvas.create_oval(center_x - radius, center_y - radius,
                                  center_x + radius, center_y + radius,
                                  outline="lightgray", width=1)
                
                value = max_value * i / 5
                canvas.create_text(center_x + radius + 10, center_y, 
                                  text=f"{value:.0f}", font=("Arial", 8))
            
            # Рисуем линии направлений
            for i, angle_deg in enumerate(direction_angles):
                angle_rad = math.radians(angle_deg)
                end_x = center_x + max_radius * math.sin(angle_rad)
                end_y = center_y - max_radius * math.cos(angle_rad)
                
                canvas.create_line(center_x, center_y, end_x, end_y, 
                                  fill="lightgray", width=1, dash=(2, 2))
                
                label_x = center_x + (max_radius + 25) * math.sin(angle_rad)
                label_y = center_y - (max_radius + 25) * math.cos(angle_rad)
                canvas.create_text(label_x, label_y, text=directions[i], 
                                  font=("Arial", 10, "bold"))
            
            # Рисуем розу ветров
            points = []
            for i, (value, angle_deg) in enumerate(zip(data, direction_angles)):
                radius = (value / max_value) * max_radius
                angle_rad = math.radians(angle_deg)
                
                x = center_x + radius * math.sin(angle_rad)
                y = center_y - radius * math.cos(angle_rad)
                points.append((x, y))
                
                canvas.create_oval(x - 3, y - 3, x + 3, y + 3, 
                                  fill="black", outline="black")
                
                canvas.create_line(center_x, center_y, x, y, 
                                  fill=colors[i], width=2)
            
            # Замыкаем и рисуем полигон
            points.append(points[0])
            
            for i in range(len(points) - 1):
                canvas.create_line(points[i][0], points[i][1], 
                                  points[i+1][0], points[i+1][1], 
                                  fill="#6A11CB", width=2)
            
            canvas.create_polygon(points, fill="#6A11CB", stipple="gray50", 
                                 outline="#6A11CB", width=2)
            
            # Заголовок
            canvas.create_text(center_x, 30, 
                              text="Роза ветров", 
                              font=("Arial", 14, "bold"))
            
            # Обновляем статистику
            total = sum(data)
            max_index = data.index(max_value)
            stats_label.config(text=f"Всего дней: {total} | Преобладающее направление: {directions[max_index]} ({data[max_index]} дней)")
            
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректные целые числа!")
    
    def generate_random_data():
        """Генерирует случайные данные"""
        import random
        for i in range(8):
            entries[i].delete(0, tk.END)
            entries[i].insert(0, str(random.randint(5, 50)))
    
    # Создаем главное окно
    root = tk.Tk()
    root.title("Задание 126: Интерактивная роза ветров")
    root.geometry("700x700")
    
    # Панель ввода данных
    input_frame = tk.Frame(root)
    input_frame.pack(pady=10)
    
    directions = ["Север", "Северо-Восток", "Восток", "Юго-Восток", 
                  "Юг", "Юго-Запад", "Запад", "Северо-Запад"]
    entries = []
    
    tk.Label(input_frame, text="Введите число дней для каждого направления:", 
             font=("Arial", 11, "bold")).pack(pady=5)
    
    for i in range(8):
        row_frame = tk.Frame(input_frame)
        row_frame.pack(pady=2)
        
        tk.Label(row_frame, text=f"{directions[i]}:", width=15, anchor="w").pack(side=tk.LEFT)
        entry = tk.Entry(row_frame, width=10)
        entry.pack(side=tk.LEFT, padx=5)
        entry.insert(0, str((i+1) * 5))  # начальные значения
        entries.append(entry)
    
    # Кнопки управления
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)
    
    tk.Button(button_frame, text="Построить розу ветров", 
              command=draw_rose, bg="#4ECDC4").pack(side=tk.LEFT, padx=5)
    tk.Button(button_frame, text="Случайные данные", 
              command=generate_random_data, bg="#FFD166").pack(side=tk.LEFT, padx=5)
    tk.Button(button_frame, text="Выход", 
              command=root.quit, bg="#FF6B6B").pack(side=tk.LEFT, padx=5)
    
    # Холст для розы ветров
    canvas = tk.Canvas(root, width=650, height=450, bg="white")
    canvas.pack(pady=10)
    
    # Метка для статистики
    stats_label = tk.Label(root, text="", font=("Arial", 10, "bold"))
    stats_label.pack(pady=5)
    
    # Инструкция
    instruction = tk.Label(root, 
                          text="Введите число дней с ветром каждого направления и нажмите 'Построить розу ветров'.",
                          font=("Arial", 9))
    instruction.pack(pady=5)
    
    # Рисуем начальную розу ветров
    root.after(100, draw_rose)
    
    root.mainloop()

if __name__ == "__main__":
    draw_interactive_wind_rose()
