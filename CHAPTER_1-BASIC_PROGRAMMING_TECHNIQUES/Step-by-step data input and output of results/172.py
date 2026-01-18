"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
6. Пошаговый ввод данных и вывод результатов *)

172. Даны натуральные числа n, a0, a1, a2, ..., a3n-1. Каждая тройка чисел ai, ai + 1, ai+2, где i кратно трем, задает координаты центра круга (ai, ai + 1) и его радиус ai + 2. Построить и закрасить какими-либо цветами круги, заданные последовательностью a0, a1, a2, ..., a3n-1.
"""


import tkinter as tk
import random
import colorsys

def hsv_to_hex(h, s, v):
    """Преобразует HSV в шестнадцатеричный формат цвета"""
    r, g, b = colorsys.hsv_to_rgb(h/360, s/100, v/100)
    return f'#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}'

def draw_circles():
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
    window.title("Круги")
    window.geometry("800x600")
    
    # Создаем холст
    canvas = tk.Canvas(window, width=800, height=600, bg="white")
    canvas.pack()
    
    # Определяем область для центрирования рисунка
    circles_data = []
    min_x = float('inf')
    max_x = float('-inf')
    min_y = float('inf')
    max_y = float('-inf')
    
    # Собираем данные о кругах и находим границы
    for i in range(n):
        idx = 1 + i * 3  # индекс начала тройки (пропускаем n)
        x = numbers[idx]
        y = numbers[idx + 1]
        radius = numbers[idx + 2]
        
        if radius <= 0:
            result_label.config(text=f"Ошибка: радиус круга {i+1} должен быть положительным!")
            window.destroy()
            return
        
        # Координаты ограничивающего прямоугольника
        x1 = x - radius
        y1 = y - radius
        x2 = x + radius
        y2 = y + radius
        
        circles_data.append((x, y, radius, x1, y1, x2, y2))
        
        # Обновляем границы
        min_x = min(min_x, x1)
        max_x = max(max_x, x2)
        min_y = min(min_y, y1)
        max_y = max(max_y, y2)
    
    # Если есть круги, определяем масштаб и смещение
    if circles_data:
        # Вычисляем центр всех кругов
        center_x = (min_x + max_x) / 2
        center_y = (min_y + max_y) / 2
        
        # Вычисляем размер области, занимаемой кругами
        width = max_x - min_x
        height = max_y - min_y
        
        # Добавляем отступы
        padding = 50
        width += 2 * padding
        height += 2 * padding
        
        # Определяем масштаб для вписывания в окно 800x600
        scale_x = 750 / max(width, 1)
        scale_y = 550 / max(height, 1)
        scale = min(scale_x, scale_y)
        
        # Функция для преобразования координат
        def transform(x, y):
            # Смещаем так, чтобы центр был в середине окна
            tx = 400 + (x - center_x) * scale
            ty = 300 + (y - center_y) * scale
            return tx, ty
        
        # Отрисовываем круги
        for i, (x, y, radius, x1, y1, x2, y2) in enumerate(circles_data):
            # Преобразуем координаты
            tx1, ty1 = transform(x1, y1)
            tx2, ty2 = transform(x2, y2)
            
            # Генерируем цвет в HSV и преобразуем в HEX
            hue = i * 137 % 360  # Золотой угол для распределения цветов
            color = hsv_to_hex(hue, 70, 90)
            
            # Рисуем круг
            canvas.create_oval(tx1, ty1, tx2, ty2, fill=color, outline="black", width=2)
            
            # Подписываем центр круга
            tx, ty = transform(x, y)
            label = f"({x},{y})\nr={radius}"
            canvas.create_text(tx, ty, text=label, font=("Arial", 8), fill="black")
            
            # Подписываем номер круга
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
    
    result_label.config(text=f"Успешно нарисовано {n} кругов")

def main():
    global root, entry, result_label
    
    root = tk.Tk()
    root.title("Построение кругов")
    root.geometry("500x400")
    
    # Инструкция
    instruction = """Введите данные в формате:
    n a0 a1 a2 a3 a4 a5 ... a(3n-1)
    
    где:
    n - количество кругов
    Каждая тройка чисел задает:
      - x центра круга
      - y центра круга  
      - радиус круга
    
    Пример (для n=2):
    2 100 100 50 200 200 30
    
    Другой пример (3 круга):
    3 0 0 40 100 50 30 -50 -30 25
    """
    
    label = tk.Label(root, text=instruction, justify=tk.LEFT)
    label.pack(pady=10)
    
    # Поле для ввода данных
    entry = tk.Entry(root, width=60)
    entry.pack(pady=10)
    entry.insert(0, "2 100 100 50 200 200 30")  # Пример по умолчанию
    
    # Кнопка для отрисовки
    draw_button = tk.Button(root, text="Нарисовать круги", command=draw_circles)
    draw_button.pack(pady=10)
    
    # Метка для вывода результатов
    result_label = tk.Label(root, text="", fg="blue")
    result_label.pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    main()
