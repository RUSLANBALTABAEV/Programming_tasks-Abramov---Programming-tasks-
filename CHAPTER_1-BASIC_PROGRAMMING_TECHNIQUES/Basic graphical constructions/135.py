"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
5. Простейшие графические построения

135. Получить на экране изображение действующих
электронных часов, показывающих текущее время. Шаблоны
используемых цифр должны соответствовать обычному для
электронных часов семисегментному шаблону.
"""


import tkinter as tk
import time
from datetime import datetime

class SevenSegmentClock:
    """Класс для отображения времени с помощью семисегментного индикатора"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Электронные часы с семисегментным индикатором")
        self.root.geometry("900x400")
        
        # Настраиваем цвета
        self.on_color = '#FF0000'     # Красный (включенные сегменты)
        self.off_color = '#300000'    # Темно-красный (выключенные сегменты)
        self.bg_color = '#000000'     # Черный фон (как у настоящих электронных часов)
        self.text_color = '#FFFFFF'   # Белый цвет для текста
        
        # Паттерны для цифр 0-9 в семисегментном индикаторе
        # Сегменты обозначаются так:
        #   0
        # 5   1
        #   6
        # 4   2
        #   3
        self.segment_patterns = {
            '0': [0, 1, 2, 3, 4, 5],
            '1': [1, 2],
            '2': [0, 1, 3, 4, 6],
            '3': [0, 1, 2, 3, 6],
            '4': [1, 2, 5, 6],
            '5': [0, 2, 3, 5, 6],
            '6': [0, 2, 3, 4, 5, 6],
            '7': [0, 1, 2],
            '8': [0, 1, 2, 3, 4, 5, 6],
            '9': [0, 1, 2, 3, 5, 6],
            ':': []  # Двоеточие (будут отдельные точки)
        }
        
        # Размеры сегментов
        self.seg_length = 40      # Длина сегмента
        self.seg_width = 10       # Ширина сегмента
        self.digit_spacing = 10   # Расстояние между цифрами
        
        # Создаем интерфейс
        self.create_widgets()
        
        # Запускаем обновление времени
        self.update_time()
    
    def create_widgets(self):
        """Создает элементы интерфейса"""
        
        # Основной Canvas для часов
        self.canvas = tk.Canvas(self.root, width=880, height=300, 
                               bg=self.bg_color, highlightthickness=0)
        self.canvas.pack(pady=10)
        
        # Метка с названием
        title_label = tk.Label(self.root, text="ЭЛЕКТРОННЫЕ ЧАСЫ", 
                              font=('Courier New', 18, 'bold'),
                              fg=self.text_color, bg=self.bg_color)
        title_label.pack()
        
        # Метка с текущей датой
        self.date_label = tk.Label(self.root, text="", 
                                  font=('Arial', 14),
                                  fg='#00FF00', bg=self.bg_color)
        self.date_label.pack(pady=5)
        
        # Информационная панель
        info_text = "Часы показывают текущее время в формате ЧЧ:ММ:СС с использованием семисегментного индикатора"
        info_label = tk.Label(self.root, text=info_text, 
                             font=('Arial', 10), fg=self.text_color, bg=self.bg_color,
                             wraplength=800, justify=tk.CENTER)
        info_label.pack(pady=10)
        
        # Кнопка для смены цвета
        color_frame = tk.Frame(self.root, bg=self.bg_color)
        color_frame.pack(pady=5)
        
        tk.Button(color_frame, text="Красный", command=lambda: self.change_color('#FF0000', '#300000'),
                 bg='#FF0000', fg='white', font=('Arial', 10)).pack(side=tk.LEFT, padx=2)
        
        tk.Button(color_frame, text="Зеленый", command=lambda: self.change_color('#00FF00', '#003000'),
                 bg='#00FF00', fg='black', font=('Arial', 10)).pack(side=tk.LEFT, padx=2)
        
        tk.Button(color_frame, text="Синий", command=lambda: self.change_color('#0000FF', '#000030'),
                 bg='#0000FF', fg='white', font=('Arial', 10)).pack(side=tk.LEFT, padx=2)
        
        tk.Button(color_frame, text="Оранжевый", command=lambda: self.change_color('#FFA500', '#302000'),
                 bg='#FFA500', fg='black', font=('Arial', 10)).pack(side=tk.LEFT, padx=2)
    
    def change_color(self, on_color, off_color):
        """Меняет цвет сегментов"""
        self.on_color = on_color
        self.off_color = off_color
    
    def draw_segment(self, x, y, horizontal=True):
        """Рисует один сегмент (горизонтальный или вертикальный)"""
        if horizontal:
            # Горизонтальный сегмент
            points = [
                (x, y),
                (x + self.seg_length, y),
                (x + self.seg_length - self.seg_width, y + self.seg_width),
                (x + self.seg_width, y + self.seg_width)
            ]
        else:
            # Вертикальный сегмент
            points = [
                (x, y),
                (x, y + self.seg_length),
                (x + self.seg_width, y + self.seg_length - self.seg_width),
                (x + self.seg_width, y + self.seg_width)
            ]
        
        # Преобразуем точки в плоский список
        flat_points = []
        for point in points:
            flat_points.extend(point)
        
        return flat_points
    
    def draw_digit(self, canvas, x, y, digit):
        """Рисует одну цифру с помощью семисегментного индикатора"""
        
        # Получаем паттерн для этой цифры
        active_segments = self.segment_patterns.get(digit, [])
        
        # Координаты для каждого сегмента
        # Сегменты располагаются в стандартном порядке для 7-сегментного индикатора
        
        # Координаты начала каждого сегмента
        segment_positions = [
            # 0: верхний горизонтальный
            (x + self.seg_width, y, True),
            # 1: верхний правый вертикальный
            (x + self.seg_length, y + self.seg_width, False),
            # 2: нижний правый вертикальный
            (x + self.seg_length, y + self.seg_length + self.seg_width, False),
            # 3: нижний горизонтальный
            (x + self.seg_width, y + 2 * self.seg_length, True),
            # 4: нижний левый вертикальный
            (x, y + self.seg_length + self.seg_width, False),
            # 5: верхний левый вертикальный
            (x, y + self.seg_width, False),
            # 6: средний горизонтальный
            (x + self.seg_width, y + self.seg_length, True)
        ]
        
        # Рисуем все 7 сегментов
        for i, (seg_x, seg_y, is_horizontal) in enumerate(segment_positions):
            color = self.on_color if i in active_segments else self.off_color
            points = self.draw_segment(seg_x, seg_y, is_horizontal)
            canvas.create_polygon(points, fill=color, outline='#202020', width=1)
    
    def draw_colon(self, canvas, x, y):
        """Рисует двоеточие для разделения часов, минут и секунд"""
        # Верхняя точка
        canvas.create_oval(x, y, 
                          x + self.seg_width * 2, y + self.seg_width * 2,
                          fill=self.on_color, outline='#202020')
        
        # Нижняя точка
        canvas.create_oval(x, y + self.seg_length, 
                          x + self.seg_width * 2, y + self.seg_length + self.seg_width * 2,
                          fill=self.on_color, outline='#202020')
    
    def draw_time(self, hours, minutes, seconds):
        """Рисует текущее время"""
        # Очищаем canvas
        self.canvas.delete("all")
        
        # Преобразуем время в строку с ведущими нулями
        time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        
        # Общая ширина одного блока (цифра + расстояние)
        block_width = self.seg_length + 2 * self.seg_width + self.digit_spacing
        
        # Начальная позиция для рисования
        start_x = 100
        y = 50
        
        # Рисуем каждую цифру
        for i, char in enumerate(time_str):
            x = start_x + i * block_width
            
            if char == ':':
                # Рисуем двоеточие
                self.draw_colon(self.canvas, x, y + self.seg_length // 3)
            else:
                # Рисуем цифру
                self.draw_digit(self.canvas, x, y, char)
    
    def update_time(self):
        """Обновляет отображение времени"""
        # Получаем текущее время
        now = datetime.now()
        hours = now.hour
        minutes = now.minute
        seconds = now.second
        
        # Рисуем время
        self.draw_time(hours, minutes, seconds)
        
        # Обновляем дату
        date_str = now.strftime("%d %B %Y года, %A")
        self.date_label.config(text=date_str)
        
        # Запланировать следующее обновление через 1 секунду
        self.root.after(1000, self.update_time)

def main():
    root = tk.Tk()
    # Устанавливаем черный фон для всего окна
    root.configure(bg='#000000')
    
    # Создаем часы
    clock = SevenSegmentClock(root)
    
    # Запускаем главный цикл
    root.mainloop()

if __name__ == "__main__":
    main()
