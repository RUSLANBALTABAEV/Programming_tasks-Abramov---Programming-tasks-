"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
6. Пошаговый ввод данных и вывод результатов *)

176. Даны натуральные числа n, a1, a2, a3, …, a3n-1. Каждая
тройка чисел ai, ai+1, ai+2, где i кратно трем, задает координаты точки и ее цвет. Построить все точки, заданные последовательностью
a0, a1, a2, ..., a3n-1.
"""


import tkinter as tk

def draw_points():
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
    
    expected_count = 3 * n
    
    if len(numbers) != expected_count + 1:  # +1 потому что первое число - n
        result_label.config(text=f"Ошибка: для n={n} нужно ввести {expected_count} чисел, а получено {len(numbers)-1}")
        return
    
    # Создаем новое окно для отрисовки
    window = tk.Toplevel(root)
    window.title("Точки")
    window.geometry("800x600")
    
    # Создаем холст
    canvas = tk.Canvas(window, width=800, height=600, bg="white")
    canvas.pack()
    
    # Определяем область для центрирования рисунка
    points_data = []
    min_x = float('inf')
    max_x = float('-inf')
    min_y = float('inf')
    max_y = float('-inf')
    
    # Собираем данные о точках и находим границы
    for i in range(n):
        idx = 1 + i * 3  # индекс начала тройки (пропускаем n)
        x = numbers[idx]
        y = numbers[idx + 1]
        color_code = numbers[idx + 2]
        
        # Преобразуем код цвета в шестнадцатеричный формат
        # Берем код по модулю 2^24 (16777216) для получения допустимого диапазона RGB
        color_code = color_code % (256 * 256 * 256)
        
        # Преобразуем в RGB компоненты
        red = (color_code >> 16) & 0xFF
        green = (color_code >> 8) & 0xFF
        blue = color_code & 0xFF
        
        # Преобразуем в шестнадцатеричную строку
        color_hex = f'#{red:02x}{green:02x}{blue:02x}'
        
        points_data.append((x, y, color_hex, color_code, red, green, blue))
        
        # Обновляем границы
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)
    
    # Если есть точки, определяем масштаб и смещение
    if points_data:
        # Вычисляем центр всех точек
        center_x = (min_x + max_x) / 2
        center_y = (min_y + max_y) / 2
        
        # Вычисляем размер области, занимаемой точками
        width_area = max_x - min_x
        height_area = max_y - min_y
        
        # Добавляем отступы, чтобы точки не касались краев
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
        
        # Отрисовываем точки
        for i, (x, y, color_hex, color_code, red, green, blue) in enumerate(points_data):
            # Преобразуем координаты
            tx, ty = transform(x, y)
            
            # Рисуем точку (круг радиуса 4)
            radius = 4
            canvas.create_oval(tx - radius, ty - radius, tx + radius, ty + radius, 
                              fill=color_hex, outline="black", width=1)
            
            # Подписываем точку (можно включить/отключить)
            label = f"({x},{y})"
            canvas.create_text(tx, ty - 10, text=label, font=("Arial", 7), fill="black")
        
        # Рисуем оси координат
        # Преобразуем начало координат (0,0)
        zero_x, zero_y = transform(0, 0)
        # Проверяем, находятся ли оси в пределах видимой области
        if 0 <= zero_x <= 800 and 0 <= zero_y <= 600:
            # Ось X
            canvas.create_line(0, zero_y, 800, zero_y, fill="gray", width=1, dash=(2, 2))
            # Ось Y
            canvas.create_line(zero_x, 0, zero_x, 600, fill="gray", width=1, dash=(2, 2))
            # Подпись осей
            canvas.create_text(790, zero_y - 5, text="X", font=("Arial", 10), fill="gray", anchor="e")
            canvas.create_text(zero_x + 5, 10, text="Y", font=("Arial", 10), fill="gray", anchor="w")
        
        # Отображаем информацию о масштабе
        scale_info = f"Масштаб: 1:{1/scale:.2f}" if scale != 0 else "Масштаб: 1:1"
        canvas.create_text(100, 20, text=scale_info, font=("Arial", 10), fill="blue", anchor="w")
        
        # Отображаем статистику
        stats = f"Точек: {n}"
        canvas.create_text(100, 40, text=stats, font=("Arial", 10), fill="blue", anchor="w")
        
        # Создаем легенду с цветами (если точек не слишком много)
        if n <= 20:
            legend_x = 650
            legend_y = 20
            canvas.create_text(legend_x, legend_y, text="Цвета точек:", 
                              font=("Arial", 10), fill="black", anchor="w")
            
            for i, (_, _, color_hex, color_code, red, green, blue) in enumerate(points_data[:10]):
                # Рисуем цветной квадратик
                square_size = 10
                canvas.create_rectangle(legend_x, legend_y + 20 + i*20, 
                                       legend_x + square_size, legend_y + 20 + i*20 + square_size,
                                       fill=color_hex, outline="black", width=1)
                
                # Подписываем код цвета
                color_info = f"RGB({red},{green},{blue})"
                canvas.create_text(legend_x + 20, legend_y + 25 + i*20, text=color_info,
                                  font=("Arial", 8), fill="black", anchor="w")
    
    result_label.config(text=f"Успешно нарисовано {n} точек")

def main():
    global root, entry, result_label
    
    root = tk.Tk()
    root.title("Построение точек")
    root.geometry("500x400")
    
    # Инструкция
    instruction = """Введите данные в формате:
    n a0 a1 a2 a3 a4 a5 ... a(3n-1)
    
    где:
    n - количество точек
    Каждая тройка чисел задает:
      - x координата точки
      - y координата точки  
      - код цвета (целое число, интерпретируемое как RGB)
    
    Пример (для n=3):
    3 100 100 255 200 200 65280 300 300 16711680
    
    Другой пример (5 точек):
    5 0 0 16777215 100 50 255 200 0 65535 300 150 16711935 400 250 32768
    """
    
    label = tk.Label(root, text=instruction, justify=tk.LEFT)
    label.pack(pady=10)
    
    # Поле для ввода данных
    entry = tk.Entry(root, width=70)
    entry.pack(pady=10)
    entry.insert(0, "3 100 100 255 200 200 65280 300 300 16711680")  # Пример по умолчанию
    
    # Кнопка для отрисовки
    draw_button = tk.Button(root, text="Нарисовать точки", command=draw_points)
    draw_button.pack(pady=10)
    
    # Метка для вывода результатов
    result_label = tk.Label(root, text="", fg="blue")
    result_label.pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    main()
