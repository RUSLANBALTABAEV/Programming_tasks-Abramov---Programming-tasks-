"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
5. Простейшие графические построения

128. Построить оси координат
(рис. 10). Начало координат следует
поместить вблизи левого нижнего угла
экрана, полуоси Ox и Oy разместить, как
показано на рис.10.
"""


import tkinter as tk
from tkinter import messagebox

def draw_interactive_axes():
    """Интерактивные оси координат с возможностью добавления точек"""
    
    points = []  # Список для хранения точек
    
    def add_point():
        """Добавляет точку на график"""
        try:
            x = float(entry_x.get())
            y = float(entry_y.get())
            
            # Преобразуем координаты в координаты холста
            canvas_x = origin_x + x * scale
            canvas_y = origin_y - y * scale  # минус, т.к. ось Y направлена вверх
            
            # Проверяем, чтобы точка была в пределах видимой области
            if (canvas_x < origin_x - 10 or canvas_x > canvas.winfo_width() - 10 or
                canvas_y < 10 or canvas_y > canvas.winfo_height() - 10):
                messagebox.showwarning("Внимание", 
                                      f"Точка ({x}, {y}) выходит за пределы графика")
                return
            
            # Рисуем точку
            point_id = canvas.create_oval(canvas_x - 4, canvas_y - 4,
                                         canvas_x + 4, canvas_y + 4,
                                         fill="red", outline="black")
            
            # Подписываем точку
            canvas.create_text(canvas_x, canvas_y - 10, 
                              text=f"({x}, {y})", font=("Arial", 8))
            
            # Сохраняем информацию о точке
            points.append({
                "id": point_id,
                "x": x,
                "y": y,
                "canvas_x": canvas_x,
                "canvas_y": canvas_y
            })
            
            # Обновляем список точек
            update_points_list()
            
        except ValueError:
            messagebox.showerror("Ошибка", "Введите числовые значения для координат!")
    
    def clear_points():
        """Очищает все точки"""
        for point in points:
            canvas.delete(point["id"])
        points.clear()
        update_points_list()
    
    def update_points_list():
        """Обновляет список точек в интерфейсе"""
        points_text = "Точки на графике:\n"
        for i, point in enumerate(points):
            points_text += f"{i+1}. ({point['x']}, {point['y']})\n"
        
        if not points:
            points_text = "Точки на графике:\n(нет точек)"
        
        label_points.config(text=points_text)
    
    def draw_axes():
        """Рисует оси координат"""
        canvas.delete("all")  # Очищаем холст
        
        global origin_x, origin_y, scale
        origin_x = 80
        origin_y = canvas.winfo_height() - 80
        scale = 30  # Масштаб: 1 единица = 30 пикселей
        
        # Ось X
        canvas.create_line(origin_x, origin_y, canvas.winfo_width() - 50, origin_y, 
                          fill="black", width=2, arrow=tk.LAST)
        canvas.create_text(canvas.winfo_width() - 40, origin_y, text="X", 
                          font=("Arial", 12, "bold"))
        
        # Ось Y
        canvas.create_line(origin_x, origin_y, origin_x, 50, 
                          fill="black", width=2, arrow=tk.FIRST)
        canvas.create_text(origin_x, 40, text="Y", 
                          font=("Arial", 12, "bold"))
        
        # Начало координат
        canvas.create_text(origin_x - 10, origin_y + 10, text="O", 
                          font=("Arial", 12, "bold"))
        
        # Сетка и деления
        for i in range(-5, 11):  # от -5 до 10
            # Деления на оси X
            x = origin_x + i * scale
            if x > origin_x and x < canvas.winfo_width() - 50:
                canvas.create_line(x, origin_y - 3, x, origin_y + 3, fill="black")
                canvas.create_text(x, origin_y + 15, text=str(i), font=("Arial", 8))
                # Линии сетки
                canvas.create_line(x, origin_y, x, 50, fill="lightgray", dash=(2, 2))
            
            # Деления на оси Y
            y = origin_y - i * scale
            if y > 50 and y < origin_y:
                canvas.create_line(origin_x - 3, y, origin_x + 3, y, fill="black")
                canvas.create_text(origin_x - 15, y, text=str(i), font=("Arial", 8))
                # Линии сетки
                canvas.create_line(origin_x, y, canvas.winfo_width() - 50, y, 
                                  fill="lightgray", dash=(2, 2))
        
        # Перерисовываем точки
        for point in points:
            # Пересчитываем координаты на случай изменения размера
            canvas_x = origin_x + point["x"] * scale
            canvas_y = origin_y - point["y"] * scale
            
            point["id"] = canvas.create_oval(canvas_x - 4, canvas_y - 4,
                                            canvas_x + 4, canvas_y + 4,
                                            fill="red", outline="black")
            canvas.create_text(canvas_x, canvas_y - 10, 
                              text=f"({point['x']}, {point['y']})", font=("Arial", 8))
    
    # Создаем главное окно
    root = tk.Tk()
    root.title("Задание 128: Интерактивные оси координат")
    root.geometry("800x650")
    
    # Панель управления
    control_frame = tk.Frame(root)
    control_frame.pack(pady=10)
    
    tk.Label(control_frame, text="Добавить точку:", 
             font=("Arial", 10, "bold")).grid(row=0, column=0, columnspan=2, pady=5)
    
    tk.Label(control_frame, text="X:").grid(row=1, column=0, padx=5)
    entry_x = tk.Entry(control_frame, width=10)
    entry_x.grid(row=1, column=1, padx=5)
    entry_x.insert(0, "2")
    
    tk.Label(control_frame, text="Y:").grid(row=1, column=2, padx=5)
    entry_y = tk.Entry(control_frame, width=10)
    entry_y.grid(row=1, column=3, padx=5)
    entry_y.insert(0, "3")
    
    tk.Button(control_frame, text="Добавить точку", 
              command=add_point, bg="#4CAF50", fg="white").grid(row=2, column=0, 
                                                                columnspan=2, pady=10)
    tk.Button(control_frame, text="Очистить все точки", 
              command=clear_points, bg="#F44336", fg="white").grid(row=2, column=2, 
                                                                  columnspan=2, pady=10)
    
    # Основная область
    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    # Холст для осей
    canvas = tk.Canvas(main_frame, width=500, height=400, bg="white", 
                      relief="solid", bd=1)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    # Панель информации
    info_frame = tk.Frame(main_frame, width=200, bg="#F5F5F5", relief="solid", bd=1)
    info_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=(10, 0))
    
    tk.Label(info_frame, text="Информация", 
             font=("Arial", 11, "bold"), bg="#F5F5F5").pack(pady=10)
    
    # Список точек
    label_points = tk.Label(info_frame, text="Точки на графике:\n(нет точек)", 
                           font=("Arial", 9), bg="#F5F5F5", justify="left")
    label_points.pack(pady=10, padx=10)
    
    # Инструкция
    instruction = tk.Label(info_frame, 
                          text="Инструкция:\n"
                               "1. Введите координаты X и Y\n"
                               "2. Нажмите 'Добавить точку'\n"
                               "3. Точка появится на графике\n"
                               "4. Используйте 'Очистить все точки' для сброса",
                          font=("Arial", 9), bg="#F5F5F5", justify="left")
    instruction.pack(pady=10, padx=10)
    
    # Рисуем оси при запуске
    root.after(100, draw_axes)
    
    # Обработчик изменения размера окна
    def on_resize(event):
        draw_axes()
    
    canvas.bind("<Configure>", on_resize)
    
    root.mainloop()

if __name__ == "__main__":
    draw_interactive_axes()
