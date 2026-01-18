"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
6. Пошаговый ввод данных и вывод результатов *)

175. Даны натуральные числа n, a1, a2, a3, …, a2n-1. Каждая пара чисел ai, ai+1, где i кратно двум, задает координаты вершин ломаной.
а) Построить ломаную, заданную последовательностью a0, a1, a2, ..., a2n-1.
б) Построить ломаную, заданную последовательностью a0, a1, a2, …, a2n-1; последнюю вершину соединить с первой.
"""


import tkinter as tk
import colorsys

def hsv_to_hex(h, s, v):
    """Преобразует HSV в шестнадцатеричный формат цвета"""
    r, g, b = colorsys.hsv_to_rgb(h/360, s/100, v/100)
    return f'#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}'

def draw_polyline():
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
    
    expected_count = 2 * n
    
    if len(numbers) != expected_count + 1:  # +1 потому что первое число - n
        result_label.config(text=f"Ошибка: для n={n} нужно ввести {expected_count} чисел, а получено {len(numbers)-1}")
        return
    
    # Извлекаем вершины (пары чисел)
    vertices = []
    for i in range(n):
        x = numbers[1 + 2*i]
        y = numbers[1 + 2*i + 1]
        vertices.append((x, y))
    
    # Создаем два окна для отрисовки
    create_polyline_window("Ломаная (а)", vertices, closed=False)
    create_polyline_window("Замкнутая ломаная (б)", vertices, closed=True)
    
    result_label.config(text=f"Успешно построено {n} вершин ломаной")

def create_polyline_window(title, vertices, closed=False):
    """Создает окно для отрисовки ломаной"""
    # Создаем новое окно для отрисовки
    window = tk.Toplevel(root)
    window.title(title)
    window.geometry("800x600")
    
    # Создаем холст
    canvas = tk.Canvas(window, width=800, height=600, bg="white")
    canvas.pack()
    
    # Определяем область для центрирования рисунка
    min_x = float('inf')
    max_x = float('-inf')
    min_y = float('inf')
    max_y = float('-inf')
    
    # Находим границы
    for x, y in vertices:
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)
    
    # Вычисляем центр всех вершин
    center_x = (min_x + max_x) / 2
    center_y = (min_y + max_y) / 2
    
    # Вычисляем размер области, занимаемой ломаной
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
    
    # Преобразуем координаты всех вершин
    transformed_vertices = [transform(x, y) for x, y in vertices]
    
    # Отрисовываем ломаную
    if len(transformed_vertices) > 1:
        # Рисуем все отрезки
        for i in range(len(transformed_vertices) - 1):
            x1, y1 = transformed_vertices[i]
            x2, y2 = transformed_vertices[i + 1]
            canvas.create_line(x1, y1, x2, y2, fill="blue", width=3)
        
        # Если нужно замкнуть, рисуем последний отрезок от последней вершины к первой
        if closed and len(transformed_vertices) > 2:
            x1, y1 = transformed_vertices[-1]
            x2, y2 = transformed_vertices[0]
            canvas.create_line(x1, y1, x2, y2, fill="red", width=3)
    
    # Отрисовываем вершины
    for i, (x, y) in enumerate(transformed_vertices):
        # Рисуем вершину как круг
        radius = 6
        canvas.create_oval(x - radius, y - radius, x + radius, y + radius, 
                          fill="red", outline="black", width=2)
        
        # Подписываем вершину
        original_x, original_y = vertices[i]
        label = f"V{i+1}:({original_x},{original_y})"
        canvas.create_text(x, y - 15, text=label, font=("Arial", 8), fill="black")
        
        # Подписываем номер вершины внутри круга
        canvas.create_text(x, y, text=str(i+1), font=("Arial", 8, "bold"), fill="white")
    
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
    stats = f"Вершин: {len(vertices)}"
    canvas.create_text(100, 40, text=stats, font=("Arial", 10), fill="blue", anchor="w")
    
    # Указываем тип ломаной
    poly_type = "Замкнутая ломаная" if closed else "Ломаная"
    canvas.create_text(400, 580, text=poly_type, font=("Arial", 12, "bold"), fill="blue")

def main():
    global root, entry, result_label
    
    root = tk.Tk()
    root.title("Построение ломаной")
    root.geometry("500x400")
    
    # Инструкция
    instruction = """Введите данные в формате:
    n a0 a1 a2 a3 ... a(2n-1)
    
    где:
    n - количество вершин ломаной
    Каждая пара чисел задает:
      - x координата вершины
      - y координата вершины
    
    Пример (для n=4):
    4 100 100 200 100 200 200 100 200
    
    Другой пример (5 вершин):
    5 0 0 100 50 200 0 150 150 50 200
    """
    
    label = tk.Label(root, text=instruction, justify=tk.LEFT)
    label.pack(pady=10)
    
    # Поле для ввода данных
    entry = tk.Entry(root, width=70)
    entry.pack(pady=10)
    entry.insert(0, "4 100 100 200 100 200 200 100 200")  # Пример по умолчанию
    
    # Кнопка для отрисовки
    draw_button = tk.Button(root, text="Построить ломаные", command=draw_polyline)
    draw_button.pack(pady=10)
    
    # Метка для вывода результатов
    result_label = tk.Label(root, text="", fg="blue")
    result_label.pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    main()
