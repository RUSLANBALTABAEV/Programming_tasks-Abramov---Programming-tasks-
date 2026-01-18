"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
6. Пошаговый ввод данных и вывод результатов *)

177. Даны натуральные числа n, x, y, r1, c1, r2, c2, rn, …, cn.
Построить n концентрических окружностей с общим центром в точке (x, y), имеющих радиусы r1, ..., rn и окрашенных в цвета с1, c2, …, cn.
"""


import tkinter as tk

def draw_concentric_circles():
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
    
    if len(numbers) < 3:
        result_label.config(text="Ошибка: введите хотя бы n, x, y!")
        return
    
    n = numbers[0]
    
    if n < 1:
        result_label.config(text="Ошибка: n должно быть натуральным числом!")
        return
    
    # Проверяем количество данных
    if len(numbers) != 3 + 2 * n:
        result_label.config(text=f"Ошибка: для n={n} нужно ввести {3 + 2*n} чисел, а получено {len(numbers)}")
        return
    
    # Извлекаем данные
    x_center = numbers[1]
    y_center = numbers[2]
    
    # Создаем списки радиусов и цветов
    radii = []
    colors = []
    
    for i in range(n):
        radius = numbers[3 + 2*i]
        color_code = numbers[3 + 2*i + 1]
        
        if radius <= 0:
            result_label.config(text=f"Ошибка: радиус {i+1} должен быть положительным!")
            return
        
        # Преобразуем код цвета в шестнадцатеричный формат
        color_code = color_code % (256 * 256 * 256)  # Берем по модулю 2^24
        red = (color_code >> 16) & 0xFF
        green = (color_code >> 8) & 0xFF
        blue = color_code & 0xFF
        color_hex = f'#{red:02x}{green:02x}{blue:02x}'
        
        radii.append(radius)
        colors.append((color_hex, color_code, red, green, blue))
    
    # Сортируем радиусы по возрастанию для правильного отображения (вложенные круги)
    # Но сначала сохраним исходный порядок для отображения в легенде
    sorted_indices = sorted(range(n), key=lambda i: radii[i])
    
    # Создаем новое окно для отрисовки
    window = tk.Toplevel(root)
    window.title("Концентрические окружности")
    window.geometry("800x600")
    
    # Создаем холст
    canvas = tk.Canvas(window, width=800, height=600, bg="white")
    canvas.pack()
    
    # Определяем максимальный радиус для масштабирования
    max_radius = max(radii)
    
    # Определяем область для центрирования рисунка
    min_x = x_center - max_radius
    max_x = x_center + max_radius
    min_y = y_center - max_radius
    max_y = y_center + max_radius
    
    # Вычисляем центр всех окружностей
    center_x = (min_x + max_x) / 2
    center_y = (min_y + max_y) / 2
    
    # Вычисляем размер области
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
    
    # Рисуем окружности, начиная с самой большой (чтобы маленькие были сверху)
    for idx in reversed(sorted_indices):
        radius = radii[idx]
        color_hex, color_code, red, green, blue = colors[idx]
        
        # Координаты ограничивающего прямоугольника
        x1 = x_center - radius
        y1 = y_center - radius
        x2 = x_center + radius
        y2 = y_center + radius
        
        # Преобразуем координаты
        tx1, ty1 = transform(x1, y1)
        tx2, ty2 = transform(x2, y2)
        
        # Рисуем окружность (круг)
        canvas.create_oval(tx1, ty1, tx2, ty2, 
                          fill=color_hex, outline="black", width=2)
    
    # Отмечаем центр
    tx_center, ty_center = transform(x_center, y_center)
    canvas.create_oval(tx_center - 5, ty_center - 5, tx_center + 5, ty_center + 5,
                      fill="red", outline="black", width=2)
    canvas.create_text(tx_center, ty_center - 15, 
                      text=f"Центр: ({x_center},{y_center})", 
                      font=("Arial", 10), fill="black")
    
    # Рисуем оси координат
    zero_x, zero_y = transform(0, 0)
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
    stats = f"Окружностей: {n}"
    canvas.create_text(100, 40, text=stats, font=("Arial", 10), fill="blue", anchor="w")
    
    # Создаем легенду с информацией о кругах
    legend_x = 600
    legend_y = 20
    canvas.create_text(legend_x, legend_y, text="Круги (от большего к меньшему):", 
                      font=("Arial", 10, "bold"), fill="black", anchor="w")
    
    # Отображаем информацию о каждом круге (в порядке возрастания радиуса)
    for i, idx in enumerate(sorted_indices):
        radius = radii[idx]
        color_hex, color_code, red, green, blue = colors[idx]
        
        # Рисуем цветной квадратик
        square_size = 10
        y_pos = legend_y + 25 + i * 25
        canvas.create_rectangle(legend_x, y_pos, 
                               legend_x + square_size, y_pos + square_size,
                               fill=color_hex, outline="black", width=1)
        
        # Подписываем радиус и цвет
        radius_info = f"R={radius}"
        color_info = f"RGB({red},{green},{blue})"
        canvas.create_text(legend_x + 15, y_pos + 5, text=radius_info,
                          font=("Arial", 8), fill="black", anchor="w")
        canvas.create_text(legend_x + 70, y_pos + 5, text=color_info,
                          font=("Arial", 8), fill="black", anchor="w")
    
    result_label.config(text=f"Успешно нарисовано {n} концентрических окружностей")

def main():
    global root, entry, result_label
    
    root = tk.Tk()
    root.title("Концентрические окружности")
    root.geometry("500x400")
    
    # Инструкция
    instruction = """Введите данные в формате:
    n x y r1 c1 r2 c2 ... rn cn
    
    где:
    n - количество окружностей
    x, y - координаты центра
    ri - радиус i-й окружности
    ci - код цвета i-й окружности (целое число, интерпретируемое как RGB)
    
    Пример (для n=3):
    3 100 100 50 255 30 65280 20 16711680
    
    Другой пример (4 окружности):
    4 200 150 80 16777215 60 16711680 40 65280 20 255
    """
    
    label = tk.Label(root, text=instruction, justify=tk.LEFT)
    label.pack(pady=10)
    
    # Поле для ввода данных
    entry = tk.Entry(root, width=70)
    entry.pack(pady=10)
    entry.insert(0, "3 100 100 50 255 30 65280 20 16711680")  # Пример по умолчанию
    
    # Кнопка для отрисовки
    draw_button = tk.Button(root, text="Нарисовать окружности", command=draw_concentric_circles)
    draw_button.pack(pady=10)
    
    # Метка для вывода результатов
    result_label = tk.Label(root, text="", fg="blue")
    result_label.pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    main()
