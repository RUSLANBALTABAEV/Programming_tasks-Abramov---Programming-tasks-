"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
5. Простейшие графические построения

125. Секторная диаграмма — это круг, площади секторов
которого пропорциональны соответствующим числовым величинам,
взятым из некоторой совокупности (рис. 7). Для большей наглядности
секторы диаграмм закрашивают в разные цвета.
Даны семь действительных чисел a1, a2 , … a7. Построить
секторную диаграмму для этих значений.
"""


import tkinter as tk
from tkinter import ttk, messagebox
import math

def draw_interactive_pie_chart():
    """Интерактивная секторная диаграмма с возможностью ввода данных"""
    
    def draw_pie_chart():
        """Рисует секторную диаграмму на основе введенных данных"""
        try:
            # Получаем данные из полей ввода
            data = []
            for i in range(7):
                value = float(entries[i].get())
                data.append(value)
            
            # Очищаем холст
            canvas.delete("all")
            
            # Параметры диаграммы
            center_x = canvas.winfo_width() // 3
            center_y = canvas.winfo_height() // 2
            radius = min(center_x, center_y) - 50
            
            # Цвета
            colors = ["#FF6B6B", "#4ECDC4", "#FFD166", "#06D6A0", 
                     "#118AB2", "#EF476F", "#073B4C"]
            
            # Вычисляем сумму абсолютных значений
            abs_data = [abs(x) for x in data]
            total = sum(abs_data)
            
            if total == 0:
                canvas.create_text(canvas.winfo_width() // 2, 
                                  canvas.winfo_height() // 2,
                                  text="Все данные равны нулю", 
                                  font=("Arial", 14, "bold"))
                return
            
            # Рисуем сектора
            start_angle = 0
            for i, value in enumerate(data):
                angle = (abs(value) / total) * 360
                
                # Рисуем сектор
                canvas.create_arc(center_x - radius, center_y - radius,
                                 center_x + radius, center_y + radius,
                                 start=start_angle, extent=angle,
                                 fill=colors[i], outline="black", width=1)
                
                # Подпись сектора
                mid_angle = start_angle + angle / 2
                mid_angle_rad = math.radians(mid_angle)
                label_radius = radius * 0.6
                label_x = center_x + label_radius * math.cos(mid_angle_rad)
                label_y = center_y - label_radius * math.sin(mid_angle_rad)
                
                percentage = (abs(value) / total) * 100
                canvas.create_text(label_x, label_y, text=f"{percentage:.1f}%", 
                                  font=("Arial", 9, "bold"), fill="white")
                
                start_angle += angle
            
            # Заголовок
            canvas.create_text(canvas.winfo_width() // 2, 30, 
                              text="Секторная диаграмма", 
                              font=("Arial", 14, "bold"))
            
            # Легенда
            legend_x = canvas.winfo_width() - 200
            legend_y = 80
            
            canvas.create_rectangle(legend_x - 10, legend_y - 10, 
                                   legend_x + 180, legend_y + 250, 
                                   fill="#F8F9FA", outline="gray")
            canvas.create_text(legend_x + 80, legend_y, text="Легенда", 
                              font=("Arial", 11, "bold"))
            
            for i in range(len(data)):
                canvas.create_rectangle(legend_x, legend_y + 25 + i * 30, 
                                       legend_x + 20, legend_y + 45 + i * 30, 
                                       fill=colors[i], outline="black")
                
                value_text = f"a{i+1} = {data[i]:.1f}"
                percentage = (abs(data[i]) / total) * 100
                info_text = f"{value_text} ({percentage:.1f}%)"
                
                canvas.create_text(legend_x + 30, legend_y + 35 + i * 30, 
                                  text=info_text, font=("Arial", 9), anchor="w")
            
            # Статистика
            stats_text = (f"Сумма: {sum(data):.2f} | "
                         f"Абс. сумма: {total:.2f} | "
                         f"Среднее: {sum(data)/len(data):.2f}")
            canvas.create_text(canvas.winfo_width() // 2, 
                              canvas.winfo_height() - 20,
                              text=stats_text, font=("Arial", 10))
            
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректные числовые значения!")
    
    def generate_random_data():
        """Генерирует случайные данные"""
        import random
        for i in range(7):
            entries[i].delete(0, tk.END)
            # Генерируем как положительные, так и отрицательные числа
            value = random.uniform(-20, 20)
            entries[i].insert(0, f"{value:.1f}")
    
    # Создаем главное окно
    root = tk.Tk()
    root.title("Задание 125: Интерактивная секторная диаграмма")
    root.geometry("800x600")
    
    # Панель ввода данных
    input_frame = tk.Frame(root)
    input_frame.pack(pady=10)
    
    entries = []
    tk.Label(input_frame, text="Введите 7 действительных чисел:", 
             font=("Arial", 11, "bold")).grid(row=0, column=0, columnspan=7, pady=5)
    
    for i in range(7):
        tk.Label(input_frame, text=f"a{i+1}:").grid(row=1, column=i, padx=5, pady=5)
        entry = tk.Entry(input_frame, width=8)
        entry.grid(row=2, column=i, padx=5, pady=5)
        entry.insert(0, f"{(i+1)*3.0:.1f}")  # начальные значения
        entries.append(entry)
    
    # Кнопки управления
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)
    
    tk.Button(button_frame, text="Построить диаграмму", 
              command=draw_pie_chart, bg="#4ECDC4").pack(side=tk.LEFT, padx=5)
    tk.Button(button_frame, text="Случайные данные", 
              command=generate_random_data, bg="#FFD166").pack(side=tk.LEFT, padx=5)
    tk.Button(button_frame, text="Выход", 
              command=root.quit, bg="#FF6B6B").pack(side=tk.LEFT, padx=5)
    
    # Холст для диаграммы
    canvas = tk.Canvas(root, width=750, height=400, bg="white")
    canvas.pack(pady=10)
    
    # Инструкция
    instruction = tk.Label(root, 
                          text="Введите семь действительных чисел (могут быть отрицательные).\n"
                               "Сектора строятся пропорционально абсолютным значениям.",
                          font=("Arial", 9))
    instruction.pack(pady=5)
    
    # Рисуем начальную диаграмму
    root.after(100, draw_pie_chart)
    
    root.mainloop()

if __name__ == "__main__":
    draw_interactive_pie_chart()
