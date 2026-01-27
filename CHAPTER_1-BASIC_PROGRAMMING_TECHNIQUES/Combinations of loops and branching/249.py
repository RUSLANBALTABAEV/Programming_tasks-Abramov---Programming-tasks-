"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
7. Сочетания цикла и разветвления

249. Даны натуральные числа n, x1, y1, r1, x2, y2, r2, …, xn, yn, rn.
Построить на экране окружности с центрами в точках (xi, yi) и радиусами ri, для которых выполнено условие ri>5.
"""


import tkinter as tk
from tkinter import ttk, messagebox

class CirclesVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Визуализация окружностей (r > 5)")
        
        # Размеры холста
        self.canvas_width = 800
        self.canvas_height = 600
        
        # Создание интерфейса
        self.create_widgets()
        
        # Переменные для хранения данных
        self.n = 0
        self.circles = []  # Список кортежей (x, y, r)
        
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
        
        # Пример ввода
        ttk.Label(input_frame, text="Пример: n=3, данные: 100 200 10 300 400 3 500 100 8").grid(
            row=3, column=0, columnspan=2, sticky=tk.W, pady=5
        )
        ttk.Label(input_frame, text="(будут построены только окружности с радиусом > 5)").grid(
            row=4, column=0, columnspan=2, sticky=tk.W, pady=5
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
            data_list = list(map(int, data_text.split()))
            
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
                self.circles.append((x, y, r))
            
            return True
            
        except ValueError:
            messagebox.showerror("Ошибка", "Проверьте правильность ввода данных (все значения должны быть целыми числами)")
            return False
    
    def clear_canvas(self):
        """Очищает холст"""
        self.canvas.delete("all")
        self.status_label.config(text="")
    
    def plot_circles(self):
        """Построение окружностей с радиусом больше 5"""
        if not self.parse_input():
            return
        
        self.clear_canvas()
        
        # Фильтруем окружности с радиусом больше 5
        filtered_circles = [(x, y, r) for x, y, r in self.circles if r > 5]
        
        if not filtered_circles:
            self.status_label.config(text="Нет окружностей с радиусом больше 5")
            return
        
        # Рисуем отфильтрованные окружности
        colors = ["red", "blue", "green", "orange", "purple", "brown", "pink", "gray"]
        
        for i, (x, y, r) in enumerate(filtered_circles):
            # Выбираем цвет (циклически)
            color = colors[i % len(colors)]
            
            # Рисуем окружность
            self.canvas.create_oval(
                x - r, y - r, 
                x + r, y + r, 
                outline=color, width=2
            )
            
            # Рисуем центр окружности
            self.canvas.create_oval(
                x - 3, y - 3, 
                x + 3, y + 3, 
                fill=color, outline="black"
            )
            
            # Подписываем окружность
            label_text = f"({x},{y},r={r})"
            self.canvas.create_text(x, y - r - 15, text=label_text, font=("Arial", 8), fill=color)
        
        # Рисуем легенду
        self.draw_legend(filtered_circles, colors)
        
        # Обновляем статус
        self.status_label.config(text=f"Построено {len(filtered_circles)} окружностей с радиусом больше 5")
        
        # Вывод в консоль
        print("Построены следующие окружности (с радиусом > 5):")
        for x, y, r in filtered_circles:
            print(f"  Центр: ({x}, {y}), радиус: {r}")
    
    def draw_legend(self, circles, colors):
        """Рисует легенду на холсте"""
        legend_x, legend_y = 20, 20
        
        # Рамка легенды
        self.canvas.create_rectangle(
            legend_x - 10, legend_y - 10, 
            legend_x + 200, legend_y + 20 + len(circles) * 20,
            fill="white", outline="black"
        )
        
        # Заголовок легенды
        self.canvas.create_text(
            legend_x + 80, legend_y + 5, 
            text="Окружности (r > 5)", 
            font=("Arial", 10, "bold")
        )
        
        # Элементы легенды
        for i, (x, y, r) in enumerate(circles):
            color = colors[i % len(colors)]
            y_pos = legend_y + 25 + i * 20
            
            # Цветной квадратик
            self.canvas.create_rectangle(
                legend_x, y_pos - 8, 
                legend_x + 10, y_pos + 2,
                fill=color, outline="black"
            )
            
            # Текст с информацией об окружности
            circle_info = f"Центр: ({x}, {y}), r={r}"
            self.canvas.create_text(
                legend_x + 100, y_pos - 3, 
                text=circle_info, 
                font=("Arial", 8), 
                anchor="w"
            )

def main():
    root = tk.Tk()
    app = CirclesVisualizer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
