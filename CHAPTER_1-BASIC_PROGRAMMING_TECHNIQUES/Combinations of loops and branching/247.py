"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
7. Сочетания цикла и разветвления

247. Даны натуральные числа n, x0, y0, r, x1, y1, …, xn, yn.
Построить на экране точки с координатами xi, yi:
а) принадлежащие кругу с центром в точке (x0, y0) и радиусом r;
б) не принадлежащие кругу с центром в точке (x0, y0) и радиусом r.
"""


import tkinter as tk
import math

class CirclePointsVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Визуализация точек и круга")
        
        # Создаем холст
        self.canvas_width = 800
        self.canvas_height = 800
        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack()
        
        # Ввод данных
        self.n = 0
        self.x0 = 0
        self.y0 = 0
        self.r = 0
        self.points = []
        
        self.setup_input_widgets()
        
        # Кнопка для построения
        self.plot_button = tk.Button(root, text="Построить точки", command=self.plot_points)
        self.plot_button.pack()
        
        # Информационная метка
        self.info_label = tk.Label(root, text="")
        self.info_label.pack()
    
    def setup_input_widgets(self):
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)
        
        # Поля для ввода основных параметров
        tk.Label(input_frame, text="n:").grid(row=0, column=0)
        self.n_entry = tk.Entry(input_frame, width=5)
        self.n_entry.grid(row=0, column=1)
        
        tk.Label(input_frame, text="x0:").grid(row=0, column=2)
        self.x0_entry = tk.Entry(input_frame, width=5)
        self.x0_entry.grid(row=0, column=3)
        
        tk.Label(input_frame, text="y0:").grid(row=0, column=4)
        self.y0_entry = tk.Entry(input_frame, width=5)
        self.y0_entry.grid(row=0, column=5)
        
        tk.Label(input_frame, text="r:").grid(row=0, column=6)
        self.r_entry = tk.Entry(input_frame, width=5)
        self.r_entry.grid(row=0, column=7)
        
        tk.Label(input_frame, text="Точки (через запятую):").grid(row=1, column=0, columnspan=8)
        self.points_entry = tk.Entry(input_frame, width=80)
        self.points_entry.grid(row=2, column=0, columnspan=8)
        
        # Пример данных
        tk.Label(input_frame, text="Пример: 5 0 0 5 1,1 2,2 3,3 4,4 5,5", 
                font=("Arial", 8), fg="gray").grid(row=3, column=0, columnspan=8)
    
    def parse_input(self):
        try:
            self.n = int(self.n_entry.get())
            self.x0 = float(self.x0_entry.get())
            self.y0 = float(self.y0_entry.get())
            self.r = float(self.r_entry.get())
            
            # Парсим точки
            points_str = self.points_entry.get()
            points_list = points_str.split()
            self.points = []
            
            for point_str in points_list:
                if ',' in point_str:
                    x_str, y_str = point_str.split(',')
                else:
                    # Пробуем разделить пробелом
                    parts = point_str.split()
                    if len(parts) >= 2:
                        x_str, y_str = parts[0], parts[1]
                    else:
                        continue
                
                x = float(x_str)
                y = float(y_str)
                self.points.append((x, y))
            
            # Проверяем количество точек
            if len(self.points) < self.n:
                self.info_label.config(text=f"Ошибка: введено {len(self.points)} точек, но n={self.n}")
                return False
            elif len(self.points) > self.n:
                self.points = self.points[:self.n]  # Берем только первые n точек
            
            return True
            
        except ValueError as e:
            self.info_label.config(text=f"Ошибка ввода: {str(e)}")
            return False
    
    def transform_coords(self, x, y, x_min, x_max, y_min, y_max):
        """Преобразует математические координаты в координаты холста."""
        margin = 50
        plot_width = self.canvas_width - 2 * margin
        plot_height = self.canvas_height - 2 * margin
        
        # Преобразуем x
        canvas_x = margin + (x - x_min) * plot_width / (x_max - x_min)
        
        # Преобразуем y (инвертируем ось Y, так как в tkinter Y направлена вниз)
        canvas_y = margin + (y_max - y) * plot_height / (y_max - y_min)
        
        return canvas_x, canvas_y
    
    def plot_points(self):
        # Очищаем холст
        self.canvas.delete("all")
        
        if not self.parse_input():
            return
        
        # Определяем границы для отображения
        all_x = [x for x, y in self.points] + [self.x0 - self.r, self.x0 + self.r]
        all_y = [y for x, y in self.points] + [self.y0 - self.r, self.y0 + self.r]
        
        x_min = min(all_x) - 1
        x_max = max(all_x) + 1
        y_min = min(all_y) - 1
        y_max = max(all_y) + 1
        
        # Преобразуем координаты центра и радиуса круга
        center_x, center_y = self.transform_coords(self.x0, self.y0, x_min, x_max, y_min, y_max)
        
        # Преобразуем радиус
        margin = 50
        plot_width = self.canvas_width - 2 * margin
        plot_height = self.canvas_height - 2 * margin
        
        # Находим масштаб для преобразования радиуса
        scale_x = plot_width / (x_max - x_min)
        scale_y = plot_height / (y_max - y_min)
        scale = min(scale_x, scale_y)  # Берем минимальный масштаб, чтобы круг не искажался
        
        radius_px = self.r * scale
        
        # Рисуем круг
        self.canvas.create_oval(
            center_x - radius_px, center_y - radius_px,
            center_x + radius_px, center_y + radius_px,
            outline="blue", fill="lightblue", width=2
        )
        
        # Рисуем центр круга
        self.canvas.create_oval(
            center_x - 5, center_y - 5,
            center_x + 5, center_y + 5,
            fill="green", outline="black"
        )
        
        # Разделяем точки на принадлежащие и не принадлежащие кругу
        points_inside = []
        points_outside = []
        
        for x, y in self.points:
            distance_squared = (x - self.x0)**2 + (y - self.y0)**2
            if distance_squared <= self.r**2:
                points_inside.append((x, y))
            else:
                points_outside.append((x, y))
        
        # Рисуем точки внутри круга
        for x, y in points_inside:
            canvas_x, canvas_y = self.transform_coords(x, y, x_min, x_max, y_min, y_max)
            self.canvas.create_oval(
                canvas_x - 5, canvas_y - 5,
                canvas_x + 5, canvas_y + 5,
                fill="blue", outline="black"
            )
            # Подпись точки
            self.canvas.create_text(canvas_x, canvas_y - 10, text=f"({x},{y})", font=("Arial", 8))
        
        # Рисуем точки вне круга
        for x, y in points_outside:
            canvas_x, canvas_y = self.transform_coords(x, y, x_min, x_max, y_min, y_max)
            self.canvas.create_oval(
                canvas_x - 5, canvas_y - 5,
                canvas_x + 5, canvas_y + 5,
                fill="red", outline="black"
            )
            # Подпись точки
            self.canvas.create_text(canvas_x, canvas_y - 10, text=f"({x},{y})", font=("Arial", 8))
        
        # Рисуем оси координат
        # Ось X
        self.canvas.create_line(
            margin, self.canvas_height - margin,
            self.canvas_width - margin, self.canvas_height - margin,
            arrow=tk.LAST, width=2
        )
        self.canvas.create_text(self.canvas_width - margin + 10, self.canvas_height - margin, text="X")
        
        # Ось Y
        self.canvas.create_line(
            margin, self.canvas_height - margin,
            margin, margin,
            arrow=tk.FIRST, width=2
        )
        self.canvas.create_text(margin, margin - 10, text="Y")
        
        # Легенда
        legend_x = self.canvas_width - 150
        legend_y = 30
        
        self.canvas.create_rectangle(legend_x - 10, legend_y - 20, legend_x + 140, legend_y + 60, fill="white", outline="black")
        self.canvas.create_text(legend_x + 60, legend_y, text="Легенда", font=("Arial", 10, "bold"))
        
        # Точки внутри круга
        self.canvas.create_oval(legend_x, legend_y + 20, legend_x + 10, legend_y + 30, fill="blue", outline="black")
        self.canvas.create_text(legend_x + 60, legend_y + 25, text="Точки внутри круга")
        
        # Точки вне круга
        self.canvas.create_oval(legend_x, legend_y + 40, legend_x + 10, legend_y + 50, fill="red", outline="black")
        self.canvas.create_text(legend_x + 60, legend_y + 45, text="Точки вне круга")
        
        # Центр круга
        self.canvas.create_oval(legend_x, legend_y + 60, legend_x + 10, legend_y + 70, fill="green", outline="black")
        self.canvas.create_text(legend_x + 60, legend_y + 65, text="Центр круга")
        
        # Обновляем информацию
        inside_count = len(points_inside)
        outside_count = len(points_outside)
        self.info_label.config(text=f"Точек внутри круга: {inside_count}, вне круга: {outside_count}")
        
        # Вывод в консоль
        print("а) Точки, принадлежащие кругу:")
        for x, y in points_inside:
            print(f"  ({x}, {y})")
        
        print("\nб) Точки, не принадлежащие кругу:")
        for x, y in points_outside:
            print(f"  ({x}, {y})")

def main():
    root = tk.Tk()
    app = CirclePointsVisualizer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
