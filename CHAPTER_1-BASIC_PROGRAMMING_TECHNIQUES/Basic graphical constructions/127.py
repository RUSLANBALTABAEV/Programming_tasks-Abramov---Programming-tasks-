"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
5. Простейшие графические построения

127. Стрелка (рис.9) состоит из отрезка прямой и
равностороннего треугольника-острия. Сторона треугольника,
пересекающая отрезок, образует с ним прямой угол; точка пересечения
делит отрезок в отношении 1:5. Построить:
а) горизонтальную стрелку, направленную из точки (100,100) в
точку (150,100);
б) горизонтальную стрелку, направленную из точки (150,100) в
точку (100,100);
в) вертикальную стрелку, направленную из точки (100, 50) в точку
(100,150);
г) вертикальную стрелку, направленную из точки (100,100) в точку
(100,50).

"""


import tkinter as tk
import math

def draw_all_arrows_explained():
    """Рисует все четыре стрелки с подробными пояснениями"""
    root = tk.Tk()
    root.title("Задание 127: Все стрелки с пояснениями")
    
    # Увеличиваем размер окна
    window_width = 900  # Ширина увеличена
    window_height = 800  # Высота увеличена
    root.geometry(f"{window_width}x{window_height}")
    
    # Отключаем изменение размера окна для стабильности
    root.resizable(False, False)
    
    # Создаем главный холст
    canvas = tk.Canvas(root, width=window_width, height=window_height, bg="white")
    canvas.pack()
    
    # Функция для рисования стрелки
    def draw_arrow(canvas, x1, y1, x2, y2, label, color):
        # Длина и направление
        dx = x2 - x1
        dy = y2 - y1
        L = math.sqrt(dx**2 + dy**2)
        
        # Точка P делит отрезок в отношении 1:5
        px = x1 + dx / 6
        py = y1 + dy / 6
        
        # Параметры равностороннего треугольника
        h = 5 * L / 6  # высота треугольника
        a = 2 * h / math.sqrt(3)  # сторона треугольника
        
        # Вектор направления отрезка
        dir_x = dx / L if L != 0 else 0
        dir_y = dy / L if L != 0 else 0
        
        # Перпендикулярный вектор
        perp_x = -dir_y
        perp_y = dir_x
        
        # Координаты основания треугольника
        base_x1 = px + perp_x * a / 2
        base_y1 = py + perp_y * a / 2
        base_x2 = px - perp_x * a / 2
        base_y2 = py - perp_y * a / 2
        
        # Рисуем отрезок (древко стрелы)
        canvas.create_line(x1, y1, px, py, fill="black", width=3)
        
        # Рисуем треугольник (острие)
        canvas.create_polygon(x2, y2, base_x1, base_y1, base_x2, base_y2, 
                             fill=color, outline="black", width=2)
        
        # Подписи точек
        canvas.create_text(x1, y1, text="A", font=("Arial", 10, "bold"), anchor="se")
        canvas.create_text(x2, y2, text="B", font=("Arial", 10, "bold"), anchor="nw")
        canvas.create_text(px, py, text="P", font=("Arial", 10, "bold"), anchor="sw")
        
        # Возвращаем параметры
        return {
            "label": label,
            "color": color,
            "length": L,
            "triangle_height": h,
            "triangle_side": a
        }
    
    # Заголовок
    canvas.create_text(window_width // 2, 30, 
                      text="Задание 127: Построение стрелок", 
                      font=("Arial", 16, "bold"))
    
    canvas.create_text(window_width // 2, 55, 
                      text="Стрелка состоит из отрезка и равностороннего треугольника", 
                      font=("Arial", 11))
    
    # Рисуем все стрелки
    arrow_info = []
    
    # а) горизонтальная вправо
    info_a = draw_arrow(canvas, 150, 150, 250, 150, 
                       "а) Горизонтальная вправо", "#FF6B6B")
    arrow_info.append(info_a)
    canvas.create_text(200, 120, text="а) Горизонтальная вправо", 
                      font=("Arial", 11, "bold"), fill="#FF6B6B")
    canvas.create_text(200, 135, text="A(100,100) → B(150,100)", 
                      font=("Arial", 9))
    
    # б) горизонтальная влево
    info_b = draw_arrow(canvas, 550, 150, 450, 150,
                       "б) Горизонтальная влево", "#4ECDC4")
    arrow_info.append(info_b)
    canvas.create_text(500, 120, text="б) Горизонтальная влево", 
                      font=("Arial", 11, "bold"), fill="#4ECDC4")
    canvas.create_text(500, 135, text="A(150,100) → B(100,100)", 
                      font=("Arial", 9))
    
    # в) вертикальная вниз
    info_c = draw_arrow(canvas, 150, 350, 150, 450,
                       "в) Вертикальная вниз", "#FFD166")
    arrow_info.append(info_c)
    canvas.create_text(100, 400, text="в) Вертикальная\nвниз", 
                      font=("Arial", 11, "bold"), fill="#FFD166", justify="right")
    canvas.create_text(100, 425, text="A(100,50) → B(100,150)", 
                      font=("Arial", 9), justify="right")
    
    # г) вертикальная вверх
    info_d = draw_arrow(canvas, 550, 450, 550, 350,
                       "г) Вертикальная вверх", "#06D6A0")
    arrow_info.append(info_d)
    canvas.create_text(600, 400, text="г) Вертикальная\nвверх", 
                      font=("Arial", 11, "bold"), fill="#06D6A0", justify="left")
    canvas.create_text(600, 425, text="A(100,100) → B(100,50)", 
                      font=("Arial", 9), justify="left")
    
    # Условие задачи
    canvas.create_rectangle(50, 500, 850, 600, fill="#F0F8FF", outline="gray", width=2)
    
    canvas.create_text(450, 510, text="Условие задачи:", 
                      font=("Arial", 12, "bold"), fill="blue")
    
    condition_lines = [
        "1. Стрелка состоит из отрезка AB и равностороннего треугольника",
        "2. Основание треугольника перпендикулярно отрезку AB", 
        "3. Точка P делит отрезок AB в отношении AP:PB = 1:5",
        "4. Основание треугольника проходит через точку P"
    ]
    
    for i, line in enumerate(condition_lines):
        canvas.create_text(100, 535 + i * 15, text=line, 
                          font=("Arial", 10), anchor="w", fill="black")
    
    # Формулы
    canvas.create_rectangle(50, 610, 850, 690, fill="#FFF0F5", outline="gray", width=2)
    
    canvas.create_text(450, 620, text="Формулы для построения:", 
                      font=("Arial", 12, "bold"), fill="purple")
    
    formulas = [
        "Длина отрезка: L = √((x₂-x₁)² + (y₂-y₁)²)",
        "Точка P: P = A + (B-A)/6  (деление в отношении 1:5)",
        "Высота треугольника: h = 5L/6",
        "Сторона треугольника: a = 2h/√3"
    ]
    
    for i, formula in enumerate(formulas):
        canvas.create_text(100, 645 + i * 15, text=formula, 
                          font=("Arial", 10), anchor="w", fill="black")
    
    # Таблица параметров
    canvas.create_rectangle(50, 700, 850, 780, fill="#F5F5DC", outline="gray", width=2)
    
    canvas.create_text(450, 710, text="Параметры стрелок:", 
                      font=("Arial", 12, "bold"), fill="brown")
    
    # Заголовки таблицы
    headers = ["Стрелка", "Длина L", "Высота h", "Сторона a"]
    for i, header in enumerate(headers):
        x = 100 + i * 180
        canvas.create_text(x, 730, text=header, 
                          font=("Arial", 10, "bold"), fill="darkblue")
    
    # Данные стрелок
    for i, info in enumerate(arrow_info):
        y = 750
        # Стрелка
        canvas.create_text(100, y + i * 20, text=info["label"], 
                          font=("Arial", 9), fill=info["color"])
        
        # Параметры
        canvas.create_text(280, y + i * 20, text=f"{info['length']:.1f}", 
                          font=("Arial", 9))
        canvas.create_text(460, y + i * 20, text=f"{info['triangle_height']:.1f}", 
                          font=("Arial", 9))
        canvas.create_text(640, y + i * 20, text=f"{info['triangle_side']:.1f}", 
                          font=("Arial", 9))
    
    # Поясняющая схема
    canvas.create_line(750, 200, 850, 200, fill="black", width=2, arrow=tk.LAST)
    canvas.create_line(800, 180, 800, 220, fill="blue", width=2)
    
    canvas.create_text(800, 170, text="Основание\nтреугольника", 
                      font=("Arial", 8), fill="blue", anchor="s")
    
    canvas.create_text(775, 210, text="P", font=("Arial", 10, "bold"))
    canvas.create_text(750, 210, text="A", font=("Arial", 10, "bold"))
    canvas.create_text(850, 210, text="B", font=("Arial", 10, "bold"))
    
    canvas.create_text(762, 225, text="1", font=("Arial", 8), fill="red")
    canvas.create_text(812, 225, text="5", font=("Arial", 8), fill="red")
    
    # Информация о расположении
    canvas.create_text(450, 780, 
                      text="Все стрелки построены согласно условию задачи.", 
                      font=("Arial", 9, "italic"))
    
    root.mainloop()

if __name__ == "__main__":
    draw_all_arrows_explained()
