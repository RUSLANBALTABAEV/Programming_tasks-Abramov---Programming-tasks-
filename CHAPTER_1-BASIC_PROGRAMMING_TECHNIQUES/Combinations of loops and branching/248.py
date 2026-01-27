"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
7. Сочетания цикла и разветвления

248. Даны натуральные числа n, x1, y1, x2, y2, …, xn, yn. Построить на экране точки с координатами xi, yi:
а) расположенные в верхней половине экрана;
б) расположенные в нижней половине экрана.
"""


import tkinter as tk
from tkinter import ttk

class PointsVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Точки в верхней и нижней половинах экрана")
        
        # Размеры холста
        self.canvas_width = 800
        self.canvas_height = 600
        
        # Создание интерфейса
        self.create_widgets()
        
        # Переменные для хранения данных
        self.n = 0
        self.points = []
        
    def create_widgets(self):
        # Создание фрейма для ввода
        input_frame = ttk.Frame(self.root, padding="10")
        input_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Ввод количества точек
        ttk.Label(input_frame, text="Количество точек (n):").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.n_entry = ttk.Entry(input_frame, width=10)
        self.n_entry.grid(row=0, column=1, sticky=tk.W, pady=5)
        
        # Ввод координат
        ttk.Label(input_frame, text="Координаты (x1 y1 x2 y2 ...):").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.coords_entry = ttk.Entry(input_frame, width=50)
        self.coords_entry.grid(row=1, column=1, sticky=tk.W, pady=5)
        
        # Кнопки
        ttk.Button(input_frame, text="Построить все точки", command=self.plot_all_points).grid(row=2, column=0, pady=10)
        ttk.Button(input_frame, text="Только верхние точки", command=self.plot_upper_points).grid(row=2, column=1, pady=10)
        ttk.Button(input_frame, text="Только нижние точки", command=self.plot_lower_points).grid(row=2, column=2, pady=10)
        
        # Пример ввода
        ttk.Label(input_frame, text="Пример: n=4, координаты: 100 250 400 100 200 350 300 200").grid(
            row=3, column=0, columnspan=3, sticky=tk.W, pady=5
        )
        
        # Создание холста
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.grid(row=1, column=0, padx=10, pady=10)
        
        # Рисуем горизонтальную линию, разделяющую экран на две половины
        self.canvas.create_line(0, self.canvas_height//2, self.canvas_width, self.canvas_height//2, 
                               fill="gray", dash=(2, 2))
        self.canvas.create_text(self.canvas_width - 50, self.canvas_height//2 - 10, text="y = h/2", fill="gray")
        
        # Статусная строка
        self.status_label = ttk.Label(self.root, text="")
        self.status_label.grid(row=2, column=0, sticky=tk.W, padx=10)
        
    def parse_input(self):
        try:
            self.n = int(self.n_entry.get())
            coords_text = self.coords_entry.get()
            coords_list = list(map(int, coords_text.split()))
            
            if len(coords_list) != 2 * self.n:
                self.status_label.config(text=f"Ошибка: ожидается {2*self.n} чисел, а получено {len(coords_list)}")
                return False
            
            # Преобразуем список в пары координат
            self.points = []
            for i in range(self.n):
                x = coords_list[2*i]
                y = coords_list[2*i + 1]
                self.points.append((x, y))
            
            return True
            
        except ValueError:
            self.status_label.config(text="Ошибка: проверьте правильность ввода данных")
            return False
    
    def clear_canvas(self):
        """Очищает холст, оставляя только разделительную линию"""
        self.canvas.delete("all")
        # Восстанавливаем разделительную линию
        self.canvas.create_line(0, self.canvas_height//2, self.canvas_width, self.canvas_height//2, 
                               fill="gray", dash=(2, 2))
        self.canvas.create_text(self.canvas_width - 50, self.canvas_height//2 - 10, text="y = h/2", fill="gray")
    
    def plot_points(self, points_to_plot, color, label):
        """Рисует точки на холсте"""
        self.clear_canvas()
        
        for x, y in points_to_plot:
            # Рисуем точку (кружок)
            self.canvas.create_oval(x-5, y-5, x+5, y+5, fill=color, outline="black", width=1)
            # Подписываем точку
            self.canvas.create_text(x, y-15, text=f"({x},{y})", font=("Arial", 8))
        
        # Отображаем легенду
        legend_x, legend_y = 20, 20
        self.canvas.create_rectangle(legend_x-10, legend_y-10, legend_x+120, legend_y+30, fill="white", outline="black")
        self.canvas.create_oval(legend_x, legend_y, legend_x+10, legend_y+10, fill=color, outline="black")
        self.canvas.create_text(legend_x+70, legend_y+5, text=label, font=("Arial", 10))
        
        self.status_label.config(text=f"Нарисовано {len(points_to_plot)} точек")
    
    def plot_all_points(self):
        if not self.parse_input():
            return
        
        # Разделяем точки на верхние и нижние
        upper_points = [(x, y) for x, y in self.points if y < self.canvas_height//2]
        lower_points = [(x, y) for x, y in self.points if y >= self.canvas_height//2]
        
        self.clear_canvas()
        
        # Рисуем верхние точки синим
        for x, y in upper_points:
            self.canvas.create_oval(x-5, y-5, x+5, y+5, fill="blue", outline="black", width=1)
            self.canvas.create_text(x, y-15, text=f"({x},{y})", font=("Arial", 8))
        
        # Рисуем нижние точки красным
        for x, y in lower_points:
            self.canvas.create_oval(x-5, y-5, x+5, y+5, fill="red", outline="black", width=1)
            self.canvas.create_text(x, y-15, text=f"({x},{y})", font=("Arial", 8))
        
        # Легенда
        legend_x, legend_y = 20, 20
        self.canvas.create_rectangle(legend_x-10, legend_y-10, legend_x+160, legend_y+60, fill="white", outline="black")
        
        self.canvas.create_oval(legend_x, legend_y, legend_x+10, legend_y+10, fill="blue", outline="black")
        self.canvas.create_text(legend_x+70, legend_y+5, text="Верхняя половина", font=("Arial", 10))
        
        self.canvas.create_oval(legend_x, legend_y+20, legend_x+10, legend_y+30, fill="red", outline="black")
        self.canvas.create_text(legend_x+70, legend_y+25, text="Нижняя половина", font=("Arial", 10))
        
        self.status_label.config(text=f"Всего точек: {len(self.points)}, верхних: {len(upper_points)}, нижних: {len(lower_points)}")
    
    def plot_upper_points(self):
        """Отображает только точки в верхней половине экрана"""
        if not self.parse_input():
            return
        
        # Фильтруем точки в верхней половине (y < h/2)
        upper_points = [(x, y) for x, y in self.points if y < self.canvas_height//2]
        
        if not upper_points:
            self.status_label.config(text="Нет точек в верхней половине экрана")
            return
        
        self.plot_points(upper_points, "blue", "Верхняя половина")
        
        # Вывод в консоль
        print("а) Точки в верхней половине экрана:")
        for x, y in upper_points:
            print(f"  ({x}, {y})")
    
    def plot_lower_points(self):
        """Отображает только точки в нижней половине экрана"""
        if not self.parse_input():
            return
        
        # Фильтруем точки в нижней половине (y >= h/2)
        lower_points = [(x, y) for x, y in self.points if y >= self.canvas_height//2]
        
        if not lower_points:
            self.status_label.config(text="Нет точек в нижней половине экрана")
            return
        
        self.plot_points(lower_points, "red", "Нижняя половина")
        
        # Вывод в консоль
        print("б) Точки в нижней половине экрана:")
        for x, y in lower_points:
            print(f"  ({x}, {y})")

def main():
    root = tk.Tk()
    app = PointsVisualizer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
