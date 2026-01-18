"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
6. Пошаговый ввод данных и вывод результатов *)

174. Даны натуральные числа n, a0, a1, a2, …, a6n-1. Каждые
шесть чисел ai, ai+1, ai+2, ai+3, ai+4, ai+5, где i кратно шести, задают координаты вершин треугольника:
числа ai, ai+1 - координаты первой вершины, ai+2, ai+3 - координаты
второй вершины, ai+4, ai+5 - координаты третьей вершины. Построить треугольники, заданные последовательностью a0, a1, a2, ..., a6n-1.
"""


import tkinter as tk
import colorsys

def hsv_to_hex(h, s, v):
    """Преобразует HSV в шестнадцатеричный формат цвета"""
    r, g, b = colorsys.hsv_to_rgb(h/360, s/100, v/100)
    return f'#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}'

def draw_triangles():
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
    
    expected_count = 6 * n
    
    if len(numbers) != expected_count + 1:  # +1 потому что первое число - n
        result_label.config(text=f"Ошибка: для n={n} нужно ввести {expected_count} чисел, а получено {len(numbers)-1}")
        return
    
    # Создаем новое окно для отрисовки
    window = tk.Toplevel(root)
    window.title("Треугольники")
    window.geometry("800x600")
    
    # Создаем холст
    canvas = tk.Canvas(window, width=800, height=600, bg="white")
    canvas.pack()
    
    # Определяем область для центрирования рисунка
    triangles_data = []
    min_x = float('inf')
    max_x = float('-inf')
    min_y = float('inf')
    max_y = float('-inf')
    
    # Собираем данные о треугольниках и находим границы
    for i in range(n):
        idx = 1 + i * 6  # индекс начала шестерки (пропускаем n)
        
        # Координаты трех вершин
        x1 = numbers[idx]
        y1 = numbers[idx + 1]
        x2 = numbers[idx + 2]
        y2 = numbers[idx + 3]
        x3 = numbers[idx + 4]
        y3 = numbers[idx + 5]
        
        # Проверяем, что треугольник не вырожденный (не все точки на одной прямой)
        # Но для простоты просто добавим треугольник
        
        triangles_data.append((x1, y1, x2, y2, x3, y3))
        
        # Обновляем границы
        min_x = min(min_x, x1, x2, x3)
        max_x = max(max_x, x1, x2, x3)
        min_y = min(min_y, y1, y2, y3)
        max_y = max(max_y, y1, y2, y3)
    
    # Если есть треугольники, определяем масштаб и смещение
    if triangles_data:
        # Вычисляем центр всех треугольников
        center_x = (min_x + max_x) / 2
        center_y = (min_y + max_y) / 2
        
        # Вычисляем размер области, занимаемой треугольниками
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
        
        # Отрисовываем треугольники
        for i, (x1, y1, x2, y2, x3, y3) in enumerate(triangles_data):
            # Преобразуем координаты
            tx1, ty1 = transform(x1, y1)
            tx2, ty2 = transform(x2, y2)
            tx3, ty3 = transform(x3, y3)
            
            # Генерируем цвет в HSV и преобразуем в HEX
            hue = i * 137 % 360  # Золотой угол для распределения цветов
            color = hsv_to_hex(hue, 70, 90)
            
            # Рисуем треугольник (polygon)
            canvas.create_polygon(tx1, ty1, tx2, ty2, tx3, ty3, 
                                fill=color, outline="black", width=2)
            
            # Подписываем вершины треугольника
            labels = [f"({x1},{y1})", f"({x2},{y2})", f"({x3},{y3})"]
            canvas.create_text(tx1, ty1, text=labels[0], font=("Arial", 7), fill="black")
            canvas.create_text(tx2, ty2, text=labels[1], font=("Arial", 7), fill="black")
            canvas.create_text(tx3, ty3, text=labels[2], font=("Arial", 7), fill="black")
            
            # Подписываем номер треугольника
            # Находим центр треугольника (среднее арифметическое вершин)
            center_tx = (tx1 + tx2 + tx3) / 3
            center_ty = (ty1 + ty2 + ty3) / 3
            canvas.create_text(center_tx, center_ty, text=f"#{i+1}", 
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
        stats = f"Треугольников: {n}"
        canvas.create_text(100, 40, text=stats, font=("Arial", 10), fill="blue", anchor="w")
    
    result_label.config(text=f"Успешно нарисовано {n} треугольников")

def main():
    global root, entry, result_label
    
    root = tk.Tk()
    root.title("Построение треугольников")
    root.geometry("500x400")
    
    # Инструкция
    instruction = """Введите данные в формате:
    n a0 a1 a2 a3 a4 a5 a6 a7 ... a(6n-1)
    
    где:
    n - количество треугольников
    Каждые шесть чисел задают:
      - x1, y1 - координаты первой вершины
      - x2, y2 - координаты второй вершины  
      - x3, y3 - координаты третьей вершины
    
    Пример (для n=1):
    1 100 100 200 100 150 200
    
    Другой пример (2 треугольника):
    2 100 100 200 100 150 200 300 300 400 300 350 400
    """
    
    label = tk.Label(root, text=instruction, justify=tk.LEFT)
    label.pack(pady=10)
    
    # Поле для ввода данных
    entry = tk.Entry(root, width=70)
    entry.pack(pady=10)
    entry.insert(0, "1 100 100 200 100 150 200")  # Пример по умолчанию
    
    # Кнопка для отрисовки
    draw_button = tk.Button(root, text="Нарисовать треугольники", command=draw_triangles)
    draw_button.pack(pady=10)
    
    # Метка для вывода результатов
    result_label = tk.Label(root, text="", fg="blue")
    result_label.pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    main()
