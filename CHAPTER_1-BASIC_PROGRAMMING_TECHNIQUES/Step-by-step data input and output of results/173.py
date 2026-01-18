"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
6. Пошаговый ввод данных и вывод результатов *)

173. Даны натуральные числа n, a0, a1, a2, …, a4n-1. Каждые четыре числа ai, ai + 1, ai + 2, ai + 3, где i кратно четырем, задают
прямоугольник со сторонами, параллельными осям координат экрана: числа ai, ai+1 - это координаты центра прямоугольника, ai + 2, ai + 3 - длины его сторон. Построить и закрасить каким-либо цветами прямоугольники, заданные последовательностью a0, a1, a2, ..., a4n-1. 
"""


import tkinter as tk
import random
import colorsys

def hsv_to_hex(h, s, v):
    """Преобразует HSV в шестнадцатеричный формат цвета"""
    r, g, b = colorsys.hsv_to_rgb(h/360, s/100, v/100)
    return f'#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}'

def draw_rectangles():
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
    
    expected_count = 4 * n
    
    if len(numbers) != expected_count + 1:  # +1 потому что первое число - n
        result_label.config(text=f"Ошибка: для n={n} нужно ввести {expected_count} чисел, а получено {len(numbers)-1}")
        return
    
    # Создаем новое окно для отрисовки
    window = tk.Toplevel(root)
    window.title("Прямоугольники")
    window.geometry("800x600")
    
    # Создаем холст
    canvas = tk.Canvas(window, width=800, height=600, bg="white")
    canvas.pack()
    
    # Определяем область для центрирования рисунка
    rectangles_data = []
    min_x = float('inf')
    max_x = float('-inf')
    min_y = float('inf')
    max_y = float('-inf')
    
    # Собираем данные о прямоугольниках и находим границы
    for i in range(n):
        idx = 1 + i * 4  # индекс начала четверки (пропускаем n)
        x = numbers[idx]          # x центра
        y = numbers[idx + 1]      # y центра
        width = numbers[idx + 2]  # ширина
        height = numbers[idx + 3] # высота
        
        if width <= 0 or height <= 0:
            result_label.config(text=f"Ошибка: размеры прямоугольника {i+1} должны быть положительными!")
            window.destroy()
            return
        
        # Координаты углов прямоугольника
        half_width = width / 2
        half_height = height / 2
        x1 = x - half_width
        y1 = y - half_height
        x2 = x + half_width
        y2 = y + half_height
        
        rectangles_data.append((x, y, width, height, x1, y1, x2, y2))
        
        # Обновляем границы
        min_x = min(min_x, x1)
        max_x = max(max_x, x2)
        min_y = min(min_y, y1)
        max_y = max(max_y, y2)
    
    # Если есть прямоугольники, определяем масштаб и смещение
    if rectangles_data:
        # Вычисляем центр всех прямоугольников
        center_x = (min_x + max_x) / 2
        center_y = (min_y + max_y) / 2
        
        # Вычисляем размер области, занимаемой прямоугольниками
        width_area = max_x - min_x
        height_area = max_y - min_y
        
        # Добавляем отступы
        padding = 50
        width_area += 2 * padding
        height_area += 2 * padding
        
        # Определяем масштаб для вписывания в окно 800x600
        scale_x = 750 / max(width_area, 1)
        scale_y = 550 / max(height_area, 1)
        scale = min(scale_x, scale_y)
        
        # Функция для преобразования координат
        def transform(x, y):
            # Смещаем так, чтобы центр был в середине окна
            tx = 400 + (x - center_x) * scale
            ty = 300 + (y - center_y) * scale
            return tx, ty
        
        # Отрисовываем прямоугольники
        for i, (x, y, width, height, x1, y1, x2, y2) in enumerate(rectangles_data):
            # Преобразуем координаты
            tx1, ty1 = transform(x1, y1)
            tx2, ty2 = transform(x2, y2)
            
            # Генерируем цвет в HSV и преобразуем в HEX
            hue = i * 137 % 360  # Золотой угол для распределения цветов
            color = hsv_to_hex(hue, 70, 90)
            
            # Рисуем прямоугольник
            canvas.create_rectangle(tx1, ty1, tx2, ty2, fill=color, outline="black", width=2)
            
            # Подписываем центр прямоугольника
            tx, ty = transform(x, y)
            label = f"({x},{y})\n{width}×{height}"
            canvas.create_text(tx, ty, text=label, font=("Arial", 8), fill="black")
            
            # Подписываем номер прямоугольника
            canvas.create_text(tx1 + 10, ty1 + 10, text=f"#{i+1}", 
                             font=("Arial", 10, "bold"), fill="black")
        
        # Рисуем оси координат
        # Преобразуем начало координат (0,0)
        zero_x, zero_y = transform(0, 0)
        # Проверяем, находятся ли оси в пределах видимой области
        if 0 <= zero_x <= 800 and 0 <= zero_y <= 600:
            # Ось X
            canvas.create_line(0, zero_y, 800, zero_y, fill="red", width=1, dash=(2, 2))
            # Ось Y
            canvas.create_line(zero_x, 0, zero_x, 600, fill="red", width=1, dash=(2, 2))
            # Подпись осей
            canvas.create_text(790, zero_y - 5, text="X", font=("Arial", 10), fill="red", anchor="e")
            canvas.create_text(zero_x + 5, 10, text="Y", font=("Arial", 10), fill="red", anchor="w")
        
        # Отображаем информацию о масштабе
        scale_info = f"Масштаб: 1:{1/scale:.2f}" if scale != 0 else "Масштаб: 1:1"
        canvas.create_text(100, 20, text=scale_info, font=("Arial", 10), fill="blue", anchor="w")
        
        # Отображаем статистику
        stats = f"Прямоугольников: {n}"
        canvas.create_text(100, 40, text=stats, font=("Arial", 10), fill="blue", anchor="w")
    
    result_label.config(text=f"Успешно нарисовано {n} прямоугольников")

def main():
    global root, entry, result_label
    
    root = tk.Tk()
    root.title("Построение прямоугольников")
    root.geometry("500x400")
    
    # Инструкция
    instruction = """Введите данные в формате:
    n a0 a1 a2 a3 a4 a5 a6 a7 ... a(4n-1)
    
    где:
    n - количество прямоугольников
    Каждые четыре числа задают:
      - x центра прямоугольника
      - y центра прямоугольника  
      - ширина прямоугольника
      - высота прямоугольника
    
    Пример (для n=2):
    2 100 100 80 60 200 200 50 100
    
    Другой пример (3 прямоугольника):
    3 0 0 100 50 100 100 60 80 -50 50 40 120
    """
    
    label = tk.Label(root, text=instruction, justify=tk.LEFT)
    label.pack(pady=10)
    
    # Поле для ввода данных
    entry = tk.Entry(root, width=70)
    entry.pack(pady=10)
    entry.insert(0, "2 100 100 80 60 200 200 50 100")  # Пример по умолчанию
    
    # Кнопка для отрисовки
    draw_button = tk.Button(root, text="Нарисовать прямоугольники", command=draw_rectangles)
    draw_button.pack(pady=10)
    
    # Метка для вывода результатов
    result_label = tk.Label(root, text="", fg="blue")
    result_label.pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    main()
