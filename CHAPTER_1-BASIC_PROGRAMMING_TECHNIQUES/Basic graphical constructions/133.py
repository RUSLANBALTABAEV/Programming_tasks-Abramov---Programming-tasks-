"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
5. Простейшие графические построения

133. Получить на экране рис. 14 и обеспечить возможность
«зажигать» и «гасить» нарисованную лампочку: включение и
выключение лампочки должно выполнятся с клавиатуры, спираль
зажженной и погашенной лампочек окрашивается в разные цвета.
"""


import tkinter as tk
from math import sin, cos, pi

class LightBulbApp:
    """Приложение с лампочкой, которая может включаться и выключаться"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Рис. 14: Лампочка с управлением с клавиатуры")
        self.root.geometry("600x700")
        
        # Состояние лампочки (включена/выключена)
        self.bulb_on = False
        
        # Цвета для разных состояний
        self.colors = {
            'on': {
                'filament': '#FFD700',      # Золотистый (горячая спираль)
                'bulb': '#FFFFE0',          # Светло-желтый (свечение)
                'base': '#C0C0C0',          # Серебристый
                'base_dark': '#808080',     # Темно-серый
                'contacts': '#FFA500',      # Оранжевый (горячий контакт)
                'reflection': '#FFFFFF'     # Белый (блик)
            },
            'off': {
                'filament': '#808080',      # Серый (холодная спираль)
                'bulb': '#F0F0F0',          # Светло-серый
                'base': '#A0A0A0',          # Серый
                'base_dark': '#606060',     # Темно-серый
                'contacts': '#808080',      # Серый (холодный контакт)
                'reflection': '#E0E0E0'     # Светло-серый
            }
        }
        
        # Создаем интерфейс
        self.create_widgets()
        
        # Рисуем лампочку в выключенном состоянии
        self.draw_bulb()
        
        # Настраиваем обработку клавиш
        self.setup_keyboard_controls()
    
    def create_widgets(self):
        """Создает элементы интерфейса"""
        
        # Фрейм для инструкций
        instructions_frame = tk.Frame(self.root, bg='white')
        instructions_frame.pack(pady=10)
        
        instructions = """
        УПРАВЛЕНИЕ С КЛАВИАТУРЫ:
        • ПРОБЕЛ или L - Включить/выключить лампочку
        • В (русская) - Включить лампочку
        • Ы (русская) - Выключить лампочку
        • ESC - Выход
        """
        
        tk.Label(instructions_frame, text=instructions, 
                font=('Arial', 10), bg='white', justify=tk.LEFT).pack()
        
        # Canvas для рисования лампочки
        self.canvas = tk.Canvas(self.root, width=550, height=500, 
                               bg='white', highlightthickness=1,
                               highlightbackground="#CCCCCC")
        self.canvas.pack(pady=10)
        
        # Фрейм для кнопок (альтернативное управление)
        button_frame = tk.Frame(self.root, bg='white')
        button_frame.pack(pady=10)
        
        tk.Button(button_frame, text="ВКЛЮЧИТЬ (Пробел/L)", 
                 command=self.turn_on, bg='#90EE90', font=('Arial', 10),
                 width=20).pack(side=tk.LEFT, padx=5)
        
        tk.Button(button_frame, text="ВЫКЛЮЧИТЬ", 
                 command=self.turn_off, bg='#FFB6C1', font=('Arial', 10),
                 width=20).pack(side=tk.LEFT, padx=5)
        
        # Индикатор состояния
        self.status_label = tk.Label(self.root, text="Лампочка: ВЫКЛЮЧЕНА", 
                                    font=('Arial', 12, 'bold'), 
                                    bg='white', fg='#FF0000')
        self.status_label.pack(pady=5)
        
        # Подпись рисунка
        tk.Label(self.root, text="Рис. 14", font=('Arial', 10, 'italic'), 
                bg='white').pack()
    
    def draw_bulb(self):
        """Рисует лампочку на canvas"""
        # Очищаем canvas
        self.canvas.delete("all")
        
        # Получаем цвета для текущего состояния
        colors = self.colors['on'] if self.bulb_on else self.colors['off']
        
        # Центральные координаты лампочки
        center_x = 275
        center_y = 200
        
        # 1. Рисуем свечение (только когда лампочка включена)
        if self.bulb_on:
            # Рисуем несколько слоев свечения с разными оттенками желтого
            glow_colors = ['#FFFFCC', '#FFFF99', '#FFFF66', '#FFFF33']
            for i, glow_color in enumerate(glow_colors):
                radius = 120 + i * 15
                self.canvas.create_oval(center_x - radius, center_y - radius,
                                       center_x + radius, center_y + radius,
                                       fill=glow_color, outline="")
        
        # 2. Рисуем колбу лампочки (стеклянную часть)
        # Основной овал
        self.canvas.create_oval(center_x - 100, center_y - 120,
                               center_x + 100, center_y + 120,
                               fill=colors['bulb'], outline='#000000', width=2)
        
        # 3. Рисуем спираль (нить накаливания)
        self.draw_filament(center_x, center_y, colors['filament'])
        
        # 4. Рисуем блики на стекле (для эффекта объема)
        # Верхний блик
        self.canvas.create_oval(center_x - 70, center_y - 100,
                               center_x + 30, center_y,
                               fill=colors['reflection'], outline="", width=0)
        
        # 5. Рисуем цоколь лампочки
        # Металлический цоколь (трапеция)
        base_points = [
            center_x - 60, center_y + 120,   # верхний левый
            center_x - 80, center_y + 180,   # нижний левый
            center_x + 80, center_y + 180,   # нижний правый
            center_x + 60, center_y + 120    # верхний правый
        ]
        self.canvas.create_polygon(base_points, fill=colors['base'], 
                                  outline='#000000', width=2)
        
        # Темная полоса на цоколе
        self.canvas.create_rectangle(center_x - 60, center_y + 140,
                                    center_x + 60, center_y + 150,
                                    fill=colors['base_dark'], outline='#000000', width=1)
        
        # 6. Рисуем контакты
        # Левый контакт
        self.canvas.create_oval(center_x - 75, center_y + 175,
                               center_x - 65, center_y + 185,
                               fill=colors['contacts'], outline='#000000', width=1)
        
        # Правый контакт
        self.canvas.create_oval(center_x + 65, center_y + 175,
                               center_x + 75, center_y + 185,
                               fill=colors['contacts'], outline='#000000', width=1)
        
        # 7. Рисуем держатели спирали внутри колбы
        # Верхний держатель
        self.canvas.create_line(center_x, center_y - 110,
                               center_x, center_y - 90,
                               fill='#404040', width=3)
        
        # Нижний держатель
        self.canvas.create_line(center_x, center_y + 90,
                               center_x, center_y + 110,
                               fill='#404040', width=3)
    
    def draw_filament(self, center_x, center_y, color):
        """Рисует спираль (нить накаливания)"""
        # Спираль состоит из нескольких витков синусоиды
        
        points = []
        num_points = 200
        amplitude = 30  # Амплитуда волны
        num_waves = 8   # Количество волн
        
        for i in range(num_points + 1):
            t = i / num_points  # от 0 до 1
            y = center_y - 90 + t * 180  # от -90 до +90 от центра
            
            # Синусоида для создания спирального эффекта
            angle = t * 2 * pi * num_waves
            x = center_x + sin(angle) * amplitude * (1 - t*0.3)
            
            points.append(x)
            points.append(y)
        
        # Рисуем спираль с градиентом цвета (толще в середине)
        for i in range(0, len(points) - 2, 2):
            x1, y1 = points[i], points[i+1]
            x2, y2 = points[i+2], points[i+3]
            
            # Толщина линии зависит от положения (толще в середине)
            t = i / (len(points) - 2)
            thickness = 2 + 3 * abs(0.5 - t) * 2  # от 2 до 5
            
            self.canvas.create_line(x1, y1, x2, y2, 
                                   fill=color, width=int(thickness))
    
    def setup_keyboard_controls(self):
        """Настраивает обработку клавиш клавиатуры"""
        # Привязываем обработчики клавиш
        self.root.bind('<Key>', self.on_key_press)
        self.root.focus_set()  # Устанавливаем фокус на окно
    
    def on_key_press(self, event):
        """Обработчик нажатия клавиш"""
        key = event.keysym.lower()
        char = event.char.lower()
        
        # Пробел или L (латинская) - переключение состояния
        if key == 'space' or char == 'l' or char == 'д':  # д - русская L
            self.toggle_bulb()
        
        # В (русская) - включить
        elif char == 'в':
            self.turn_on()
        
        # Ы (русская) - выключить (для "выкл")
        elif char == 'ы':
            self.turn_off()
        
        # ESC - выход
        elif key == 'escape':
            self.root.quit()
    
    def toggle_bulb(self):
        """Переключает состояние лампочки"""
        self.bulb_on = not self.bulb_on
        self.update_bulb()
    
    def turn_on(self):
        """Включает лампочку"""
        if not self.bulb_on:
            self.bulb_on = True
            self.update_bulb()
    
    def turn_off(self):
        """Выключает лампочку"""
        if self.bulb_on:
            self.bulb_on = False
            self.update_bulb()
    
    def update_bulb(self):
        """Обновляет отображение лампочки"""
        # Перерисовываем лампочку
        self.draw_bulb()
        
        # Обновляем индикатор состояния
        if self.bulb_on:
            self.status_label.config(text="Лампочка: ВКЛЮЧЕНА", fg='#00AA00')
        else:
            self.status_label.config(text="Лампочка: ВЫКЛЮЧЕНА", fg='#FF0000')

def main():
    root = tk.Tk()
    app = LightBulbApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
