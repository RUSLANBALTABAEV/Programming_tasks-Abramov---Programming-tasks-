"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
5. Простейшие графические построения

132. Дано натуральное число n (
n≤999999
). Записать его
шестью цифрами, используя девятисегментный шаблон (как на
почтовых конвертах).
"""


import tkinter as tk
from tkinter import ttk, messagebox

class NineSegmentDisplay:
    """Класс для отображения цифр с помощью девятисегментного индикатора"""
    
    def __init__(self):
        # Определяем сегменты для каждой цифры (0-9) в девятисегментном индикаторе
        # Сегменты расположены как в почтовых индексах на конвертах:
        #   0: верхний горизонтальный
        #   1: верхний правый вертикальный
        #   2: нижний правый вертикальный
        #   3: нижний горизонтальный
        #   4: нижний левый вертикальный
        #   5: верхний левый вертикальный
        #   6: средний горизонтальный
        #   7: дополнительный левый диагональный (для некоторых шрифтов)
        #   8: дополнительный правый диагональный (для некоторых шрифтов)
        
        self.segment_patterns = {
            '0': [0, 1, 2, 3, 4, 5],            # 0
            '1': [1, 2],                        # 1
            '2': [0, 1, 3, 4, 6],               # 2
            '3': [0, 1, 2, 3, 6],               # 3
            '4': [1, 2, 5, 6],                  # 4
            '5': [0, 2, 3, 5, 6],               # 5
            '6': [0, 2, 3, 4, 5, 6],            # 6
            '7': [0, 1, 2],                     # 7
            '8': [0, 1, 2, 3, 4, 5, 6],         # 8
            '9': [0, 1, 2, 3, 5, 6]             # 9
        }
        
        # Цвета для сегментов
        self.on_color = '#FF0000'     # Красный (как на почтовых конвертах)
        self.off_color = '#F0F0F0'    # Светло-серый (выключенные сегменты)
        self.bg_color = '#FFFFFF'     # Белый фон
    
    def draw_digit(self, canvas, x, y, digit, size=30):
        """Рисует одну цифру с помощью девятисегментного индикатора"""
        
        # Проверяем, что цифра валидная
        if digit not in '0123456789':
            return
        
        # Получаем паттерн для этой цифры
        active_segments = self.segment_patterns.get(digit, [])
        
        # Размеры и координаты сегментов (относительно центра)
        seg_size = size
        half_size = seg_size // 2
        quarter_size = seg_size // 4
        
        # Координаты для каждого сегмента
        segments_coords = [
            # 0: верхний горизонтальный
            [(x - half_size, y - half_size), 
             (x + half_size, y - half_size),
             (x + half_size - quarter_size, y - half_size + quarter_size),
             (x - half_size + quarter_size, y - half_size + quarter_size)],
            
            # 1: верхний правый вертикальный
            [(x + half_size, y - half_size),
             (x + half_size, y),
             (x + half_size - quarter_size, y - quarter_size),
             (x + half_size - quarter_size, y - half_size + quarter_size)],
            
            # 2: нижний правый вертикальный
            [(x + half_size, y),
             (x + half_size, y + half_size),
             (x + half_size - quarter_size, y + half_size - quarter_size),
             (x + half_size - quarter_size, y + quarter_size)],
            
            # 3: нижний горизонтальный
            [(x - half_size, y + half_size),
             (x + half_size, y + half_size),
             (x + half_size - quarter_size, y + half_size - quarter_size),
             (x - half_size + quarter_size, y + half_size - quarter_size)],
            
            # 4: нижний левый вертикальный
            [(x - half_size, y),
             (x - half_size, y + half_size),
             (x - half_size + quarter_size, y + half_size - quarter_size),
             (x - half_size + quarter_size, y + quarter_size)],
            
            # 5: верхний левый вертикальный
            [(x - half_size, y - half_size),
             (x - half_size, y),
             (x - half_size + quarter_size, y - quarter_size),
             (x - half_size + quarter_size, y - half_size + quarter_size)],
            
            # 6: средний горизонтальный
            [(x - half_size, y),
             (x + half_size, y),
             (x + half_size - quarter_size, y + quarter_size),
             (x - half_size + quarter_size, y + quarter_size)],
            
            # 7: дополнительный левый диагональный
            [(x - half_size, y - quarter_size),
             (x - quarter_size, y - half_size),
             (x - quarter_size + quarter_size//2, y - half_size + quarter_size//2),
             (x - half_size + quarter_size//2, y - quarter_size + quarter_size//2)],
            
            # 8: дополнительный правый диагональный
            [(x + half_size, y - quarter_size),
             (x + quarter_size, y - half_size),
             (x + quarter_size - quarter_size//2, y - half_size + quarter_size//2),
             (x + half_size - quarter_size//2, y - quarter_size + quarter_size//2)]
        ]
        
        # Рисуем все сегменты
        for i, coords in enumerate(segments_coords):
            # Определяем цвет сегмента
            color = self.on_color if i in active_segments else self.off_color
            
            # Рисуем сегмент как многоугольник
            flat_coords = []
            for point in coords:
                flat_coords.extend(point)
            
            canvas.create_polygon(flat_coords, fill=color, outline='#AAAAAA', width=1)
    
    def draw_number(self, canvas, x, y, number_str, size=30, spacing=10):
        """Рисует число из 6 цифр"""
        
        # Преобразуем в строку и дополняем ведущими нулями до 6 цифр
        padded_number = number_str.zfill(6)
        
        # Рисуем каждую цифру
        for i, digit in enumerate(padded_number):
            digit_x = x + i * (size + spacing)
            self.draw_digit(canvas, digit_x, y, digit, size)
        
        # Добавляем подпись
        canvas.create_text(x + 3*(size + spacing), y + size + 20,
                          text=f"Число: {int(number_str):,}".replace(',', ' '),
                          font=('Arial', 10, 'bold'))

class PostalCodeDisplay:
    """Главное окно приложения для отображения чисел в девятисегментном формате"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Девятисегментный индикатор - как на почтовых конвертах")
        self.root.geometry("900x400")
        
        # Создаем дисплей
        self.display = NineSegmentDisplay()
        
        # Создаем интерфейс
        self.create_widgets()
        
        # Показываем пример по умолчанию
        self.show_number("123456")
    
    def create_widgets(self):
        """Создает элементы интерфейса"""
        
        # Фрейм для управления
        control_frame = ttk.Frame(self.root, padding="10")
        control_frame.pack(fill=tk.X)
        
        # Метка и поле ввода
        ttk.Label(control_frame, text="Введите число (до 999999):", 
                 font=('Arial', 10)).pack(side=tk.LEFT, padx=5)
        
        self.entry_var = tk.StringVar(value="123456")
        self.entry = ttk.Entry(control_frame, textvariable=self.entry_var, 
                              width=15, font=('Arial', 10))
        self.entry.pack(side=tk.LEFT, padx=5)
        
        # Кнопка отображения
        ttk.Button(control_frame, text="Показать", 
                  command=self.on_show_clicked).pack(side=tk.LEFT, padx=5)
        
        # Кнопка случайного числа
        ttk.Button(control_frame, text="Случайное число", 
                  command=self.show_random).pack(side=tk.LEFT, padx=5)
        
        # Примеры быстрого выбора
        examples_frame = ttk.Frame(control_frame)
        examples_frame.pack(side=tk.LEFT, padx=20)
        
        ttk.Label(examples_frame, text="Примеры:", 
                 font=('Arial', 9)).pack(side=tk.LEFT)
        
        examples = ["0", "123", "4567", "999999", "987654"]
        for ex in examples:
            ttk.Button(examples_frame, text=ex, width=6,
                      command=lambda e=ex: self.show_example(e)).pack(side=tk.LEFT, padx=2)
        
        # Canvas для отображения
        self.canvas = tk.Canvas(self.root, width=880, height=250, 
                               bg=self.display.bg_color, highlightthickness=1,
                               highlightbackground="#CCCCCC")
        self.canvas.pack(pady=10)
        
        # Информационная панель
        info_frame = ttk.Frame(self.root, padding="10")
        info_frame.pack(fill=tk.X)
        
        info_text = """
        Девятисегментный индикатор используется для отображения цифр на почтовых конвертах.
        • Каждая цифра формируется из 9 сегментов
        • Включенные сегменты подсвечиваются красным цветом
        • Число всегда отображается 6 цифрами (с ведущими нулями)
        """
        
        ttk.Label(info_frame, text=info_text, justify=tk.LEFT, 
                 font=('Arial', 9), relief=tk.SUNKEN, padding=5).pack(fill=tk.X)
    
    def show_number(self, number_str):
        """Отображает число на canvas"""
        # Очищаем canvas
        self.canvas.delete("all")
        
        # Проверяем корректность ввода
        try:
            num = int(number_str)
            if num < 0 or num > 999999:
                messagebox.showerror("Ошибка", "Число должно быть от 0 до 999999")
                return
        except ValueError:
            messagebox.showerror("Ошибка", "Введите целое число")
            return
        
        # Рисуем число
        self.display.draw_number(self.canvas, 50, 100, number_str, size=40, spacing=20)
    
    def on_show_clicked(self):
        """Обработчик нажатия кнопки 'Показать'"""
        number_str = self.entry_var.get().strip()
        self.show_number(number_str)
    
    def show_example(self, example):
        """Показывает пример"""
        self.entry_var.set(example)
        self.show_number(example)
    
    def show_random(self):
        """Показывает случайное число"""
        import random
        random_num = random.randint(0, 999999)
        self.entry_var.set(str(random_num))
        self.show_number(str(random_num))

def main():
    root = tk.Tk()
    app = PostalCodeDisplay(root)
    root.mainloop()

if __name__ == "__main__":
    main()
