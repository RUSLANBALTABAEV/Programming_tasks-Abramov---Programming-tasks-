"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
7. Сочетания цикла и разветвления

250. Даны натуральные числа n, x1, y1, r1, x2, y2, r2, …, xn, yn, rn.
Построить на экране окружности с центрами в точках (xi, yi) и радиусами ri, если ri > 5, и радиусами 2ri - в противном случае.
"""


import tkinter as tk
from tkinter import ttk, messagebox
import math

class CirclesVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Визуализация окружностей с адаптивными радиусами")
        
        # Размеры холста
        self.canvas_width = 800
        self.canvas_height = 600
        
        # Создание интерфейса
        self.create_widgets()
        
        # Переменные для хранения данных
        self.n = 0
        self.circles = []  # Список кортежей (x, y, r)
        self.adjusted_circles = []  # Список кортежей (x, y, adjusted_r)
        
    def create_widgets(self):
        # Создание фрейма для ввода
        input_frame = ttk.Frame(self.root, padding="10")
        input_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Ввод количества окружностей
        ttk.Label(input_frame, text="Количество окружностей (n):").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.n_entry = ttk.Entry(input_frame, width=10)
        self.n_entry.grid(row=0, column=1, sticky=tk.W, pady=5)
        
        # Ввод данных об окружностях
        ttk.Label(input_frame, text="Данные (x1 y1 r1 x2 y2 r2 ...):").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.data_entry = ttk.Entry(input_frame, width=60)
        self.data_entry.grid(row=1, column=1, sticky=tk.W, pady=5)
        
        # Кнопки
        ttk.Button(input_frame, text="Построить окружности", command=self.plot_circles).grid(row=2, column=0, pady=10)
        ttk.Button(input_frame, text="Очистить", command=self.clear_canvas).grid(row=2, column=1, pady=10)
        ttk.Button(input_frame, text="Показать информацию", command=self.show_info).grid(row=2, column=2, pady=10)
        
        # Пример ввода
        ttk.Label(input_frame, text="Пример: n=3, данные: 100 200 10 300 400 3 500 100 5").grid(
            row=3, column=0, columnspan=3, sticky=tk.W, pady=5
        )
        ttk.Label(input_frame, text="Если r > 5, радиус = r; иначе радиус = 2*r").grid(
            row=4, column=0, columnspan=3, sticky=tk.W, pady=5
        )
        
        # Создание холста
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.grid(row=1, column=0, padx=10, pady=10)
        
        # Статусная строка
        self.status_label = ttk.Label(self.root, text="")
        self.status_label.grid(row=2, column=0, sticky=tk.W, padx=10)
        
    def parse_input(self):
        try:
            self.n = int(self.n_entry.get())
            if self.n <= 0:
                messagebox.showerror("Ошибка", "Количество окружностей должно быть положительным числом")
                return False
            
            data_text = self.data_entry.get()
            data_list = list(map(float, data_text.split()))
            
            if len(data_list) != 3 * self.n:
                messagebox.showerror("Ошибка", 
                    f"Ожидается {3*self.n} чисел (3 параметра для каждой из {self.n} окружностей), "
                    f"а получено {len(data_list)}")
                return False
            
            # Преобразуем список в список окружностей
            self.circles = []
            for i in range(self.n):
                x = data_list[3*i]
                y = data_list[3*i + 1]
                r = data_list[3*i + 2]
                if r <= 0:
                    messagebox.showerror("Ошибка", "Радиус должен быть положительным числом")
                    return False
                self.circles.append((x, y, r))
            
            return True
            
        except ValueError:
            messagebox.showerror("Ошибка", "Проверьте правильность ввода данных (все значения должны быть числами)")
            return False
    
    def adjust_radii(self):
        """Вычисляем новые радиусы согласно условию"""
        self.adjusted_circles = []
        for x, y, r in self.circles:
            if r > 5:
                adjusted_r = r
                category = "r > 5"
            else:
                adjusted_r = 2 * r
                category = "r ≤ 5"
            self.adjusted_circles.append((x, y, r, adjusted_r, category))
    
    def calculate_viewport(self):
        """Рассчитываем границы для отображения всех окружностей"""
        if not self.adjusted_circles:
            return 0, 0, self.canvas_width, self.canvas_height
        
        # Находим минимальные и максимальные координаты с учетом радиусов
        min_x = min(x - adjusted_r for x, y, r, adjusted_r, category in self.adjusted_circles)
        max_x = max(x + adjusted_r for x, y, r, adjusted_r, category in self.adjusted_circles)
        min_y = min(y - adjusted_r for x, y, r, adjusted_r, category in self.adjusted_circles)
        max_y = max(y + adjusted_r for x, y, r, adjusted_r, category in self.adjusted_circles)
        
        # Добавляем отступы
        padding = max((max_x - min_x) * 0.1, (max_y - min_y) * 0.1, 10)
        min_x -= padding
        max_x += padding
        min_y -= padding
        max_y += padding
        
        return min_x, min_y, max_x, max_y
    
    def transform_coords(self, x, y, min_x, min_y, max_x, max_y):
        """Преобразует реальные координаты в координаты холста"""
        canvas_x = ((x - min_x) / (max_x - min_x)) * self.canvas_width
        canvas_y = self.canvas_height - ((y - min_y) / (max_y - min_y)) * self.canvas_height
        return canvas_x, canvas_y
    
    def transform_radius(self, r, min_x, min_y, max_x, max_y):
        """Преобразует реальный радиус в радиус на холсте"""
        # Используем меньший масштаб из X и Y для сохранения пропорций
        scale_x = self.canvas_width / (max_x - min_x)
        scale_y = self.canvas_height / (max_y - min_y)
        scale = min(scale_x, scale_y)
        return r * scale
    
    def clear_canvas(self):
        """Очищает холст"""
        self.canvas.delete("all")
        self.status_label.config(text="")
    
    def plot_circles(self):
        """Построение окружностей с адаптивными радиусами"""
        if not self.parse_input():
            return
        
        self.clear_canvas()
        
        # Вычисляем новые радиусы
        self.adjust_radii()
        
        # Рассчитываем границы отображения
        min_x, min_y, max_x, max_y = self.calculate_viewport()
        
        # Рисуем сетку координат
        self.draw_grid(min_x, min_y, max_x, max_y)
        
        # Рисуем отфильтрованные окружности
        colors = {"r > 5": "blue", "r ≤ 5": "red"}
        
        for i, (x, y, original_r, adjusted_r, category) in enumerate(self.adjusted_circles):
            color = colors[category]
            
            # Преобразуем координаты и радиус
            canvas_x, canvas_y = self.transform_coords(x, y, min_x, min_y, max_x, max_y)
            canvas_r = self.transform_radius(adjusted_r, min_x, min_y, max_x, max_y)
            
            # Рисуем окружность
            self.canvas.create_oval(
                canvas_x - canvas_r, canvas_y - canvas_r, 
                canvas_x + canvas_r, canvas_y + canvas_r, 
                outline=color, width=2
            )
            
            # Рисуем центр окружности
            self.canvas.create_oval(
                canvas_x - 4, canvas_y - 4, 
                canvas_x + 4, canvas_y + 4, 
                fill=color, outline="black"
            )
            
            # Подписываем окружность
            label_text = f"{i+1}: r={original_r:.1f}"
            self.canvas.create_text(canvas_x, canvas_y - canvas_r - 15, 
                                   text=label_text, font=("Arial", 8), fill=color)
        
        # Рисуем легенду
        self.draw_legend(colors)
        
        # Обновляем статус
        count_r_gt_5 = sum(1 for _, _, _, _, category in self.adjusted_circles if category == "r > 5")
        count_r_le_5 = len(self.adjusted_circles) - count_r_gt_5
        self.status_label.config(text=f"Построено {len(self.adjusted_circles)} окружностей: {count_r_gt_5} с r>5, {count_r_le_5} с r≤5")
    
    def draw_grid(self, min_x, min_y, max_x, max_y):
        """Рисует координатную сетку"""
        # Горизонтальные линии
        for y in [min_y, (min_y + max_y) / 2, max_y]:
            canvas_x1, canvas_y1 = self.transform_coords(min_x, y, min_x, min_y, max_x, max_y)
            canvas_x2, canvas_y2 = self.transform_coords(max_x, y, min_x, min_y, max_x, max_y)
            self.canvas.create_line(canvas_x1, canvas_y1, canvas_x2, canvas_y2, 
                                   fill="lightgray", dash=(2, 2))
        
        # Вертикальные линии
        for x in [min_x, (min_x + max_x) / 2, max_x]:
            canvas_x1, canvas_y1 = self.transform_coords(x, min_y, min_x, min_y, max_x, max_y)
            canvas_x2, canvas_y2 = self.transform_coords(x, max_y, min_x, min_y, max_x, max_y)
            self.canvas.create_line(canvas_x1, canvas_y1, canvas_x2, canvas_y2, 
                                   fill="lightgray", dash=(2, 2))
        
        # Подписи осей
        # Ось X
        canvas_x, canvas_y = self.transform_coords(max_x, min_y, min_x, min_y, max_x, max_y)
        self.canvas.create_text(canvas_x - 20, canvas_y - 20, text="X", font=("Arial", 10, "bold"))
        
        # Ось Y
        canvas_x, canvas_y = self.transform_coords(min_x, max_y, min_x, min_y, max_x, max_y)
        self.canvas.create_text(canvas_x + 20, canvas_y + 20, text="Y", font=("Arial", 10, "bold"))
    
    def draw_legend(self, colors):
        """Рисует легенду на холсте"""
        legend_x, legend_y = 20, 20
        
        # Рамка легенды
        self.canvas.create_rectangle(
            legend_x - 10, legend_y - 10, 
            legend_x + 180, legend_y + 70,
            fill="white", outline="black"
        )
        
        # Заголовок легенды
        self.canvas.create_text(
            legend_x + 80, legend_y + 5, 
            text="Легенда", 
            font=("Arial", 10, "bold")
        )
        
        # Элементы легенды
        y_pos = legend_y + 25
        
        # Окружности с r > 5
        self.canvas.create_oval(
            legend_x, y_pos - 5, 
            legend_x + 10, y_pos + 5,
            outline=colors["r > 5"], width=2
        )
        self.canvas.create_text(
            legend_x + 100, y_pos, 
            text="r > 5 (радиус = r)", 
            font=("Arial", 8), 
            anchor="w"
        )
        
        # Окружности с r ≤ 5
        y_pos += 20
        self.canvas.create_oval(
            legend_x, y_pos - 5, 
            legend_x + 10, y_pos + 5,
            outline=colors["r ≤ 5"], width=2
        )
        self.canvas.create_text(
            legend_x + 100, y_pos, 
            text="r ≤ 5 (радиус = 2r)", 
            font=("Arial", 8), 
            anchor="w"
        )
        
        # Центры окружностей
        y_pos += 20
        self.canvas.create_oval(
            legend_x + 2, y_pos - 3, 
            legend_x + 8, y_pos + 3,
            fill="black", outline="black"
        )
        self.canvas.create_text(
            legend_x + 100, y_pos, 
            text="Центр окружности", 
            font=("Arial", 8), 
            anchor="w"
        )
    
    def show_info(self):
        """Показывает информацию об окружностях"""
        if not self.adjusted_circles:
            messagebox.showinfo("Информация", "Сначала постройте окружности")
            return
        
        info_text = "Информация об окружностях:\n\n"
        for i, (x, y, original_r, adjusted_r, category) in enumerate(self.adjusted_circles):
            info_text += f"Окружность {i+1}:\n"
            info_text += f"  Центр: ({x:.1f}, {y:.1f})\n"
            info_text += f"  Исходный радиус: {original_r:.1f}\n"
            info_text += f"  Построенный радиус: {adjusted_r:.1f}\n"
            info_text += f"  Категория: {category}\n\n"
        
        messagebox.showinfo("Детальная информация", info_text)

def main():
    root = tk.Tk()
    app = CirclesVisualizer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
