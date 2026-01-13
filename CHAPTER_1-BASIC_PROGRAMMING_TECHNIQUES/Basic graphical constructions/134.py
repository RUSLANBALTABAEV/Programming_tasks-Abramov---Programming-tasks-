"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
5. Простейшие графические построения

134. Получить на экране рис. 15 и обеспечить возможность
«зажигать» и «гасить» свет в доме: включение и выключение света
должно выполнятся с клавиатуры, окно дома при зажженном и при
"""


import tkinter as tk

class HouseLightApp:
    """Приложение с домом, в котором можно включать и выключать свет"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Рис. 15: Дом с управлением светом")
        self.root.geometry("800x700")
        
        # Состояние света (включен/выключен)
        self.light_on = False
        
        # Цвета для разных состояний
        self.colors = {
            'on': {
                'window': '#FFFF99',        # Ярко-желтый (свет в окне)
                'window_frame': '#8B4513',  # Коричневый
                'light_glow': '#FFFF00',    # Желтое свечение
                'curtains': '#FFB6C1',      # Розовый (шторы подсвечены)
                'room_wall': '#FFE4B5'      # Светло-оранжевый (стена комнаты)
            },
            'off': {
                'window': '#2F4F4F',        # Темно-серый (темное окно)
                'window_frame': '#8B4513',  # Коричневый
                'light_glow': None,         # Нет свечения
                'curtains': '#8B6969',      # Темно-коричневый (шторы)
                'room_wall': '#D2B48C'      # Бежевый (стена комнаты без света)
            }
        }
        
        # Создаем интерфейс
        self.create_widgets()
        
        # Рисуем дом в начальном состоянии (свет выключен)
        self.draw_house()
        
        # Настраиваем обработку клавиш
        self.setup_keyboard_controls()
    
    def create_widgets(self):
        """Создает элементы интерфейса"""
        
        # Фрейм для инструкций
        instructions_frame = tk.Frame(self.root, bg='#F0F8FF')
        instructions_frame.pack(pady=10, fill=tk.X)
        
        instructions = """
        УПРАВЛЕНИЕ С КЛАВИАТУРЫ:
        • ПРОБЕЛ или L - Включить/выключить свет в доме
        • В (русская) - Включить свет
        • Ы (русская) - Выключить свет
        • ESC - Выход
        
        ЦВЕТА ОКНА:
        • Когда свет ВКЛЮЧЕН - окно желтое с подсветкой
        • Когда свет ВЫКЛЮЧЕН - окно темное
        """
        
        tk.Label(instructions_frame, text=instructions, 
                font=('Arial', 10), bg='#F0F8FF', justify=tk.LEFT).pack(padx=20, pady=5)
        
        # Canvas для рисования дома
        self.canvas = tk.Canvas(self.root, width=750, height=500, 
                               bg='#87CEEB', highlightthickness=1,
                               highlightbackground="#4682B4")
        self.canvas.pack(pady=10)
        
        # Фрейм для кнопок (альтернативное управление)
        button_frame = tk.Frame(self.root, bg='#F0F8FF')
        button_frame.pack(pady=10)
        
        tk.Button(button_frame, text="ВКЛЮЧИТЬ СВЕТ (Пробел/L)", 
                 command=self.turn_on, bg='#90EE90', font=('Arial', 10, 'bold'),
                 width=25, height=2).pack(side=tk.LEFT, padx=5)
        
        tk.Button(button_frame, text="ВЫКЛЮЧИТЬ СВЕТ", 
                 command=self.turn_off, bg='#FFB6C1', font=('Arial', 10, 'bold'),
                 width=25, height=2).pack(side=tk.LEFT, padx=5)
        
        # Индикатор состояния
        self.status_label = tk.Label(self.root, text="Свет в доме: ВЫКЛЮЧЕН", 
                                    font=('Arial', 14, 'bold'), 
                                    bg='#F0F8FF', fg='#8B0000',
                                    padx=20, pady=10)
        self.status_label.pack(pady=5)
        
        # Подпись рисунка
        tk.Label(self.root, text="Рис. 15", font=('Arial', 12, 'italic'), 
                bg='#F0F8FF', fg='#4682B4').pack()
    
    def draw_house(self):
        """Рисует дом на canvas"""
        # Очищаем canvas
        self.canvas.delete("all")
        
        # Рисуем небо
        self.canvas.create_rectangle(0, 0, 750, 300, fill='#87CEEB', outline='')
        
        # Рисуем траву (землю)
        self.canvas.create_rectangle(0, 300, 750, 500, fill='#228B22', outline='')
        
        # Получаем цвета для текущего состояния
        colors = self.colors['on'] if self.light_on else self.colors['off']
        
        # Центральные координаты дома
        house_x = 375
        house_y = 250
        
        # 1. Рисуем основную часть дома (стены)
        self.canvas.create_rectangle(house_x - 150, house_y - 80,
                                    house_x + 150, house_y + 120,
                                    fill='#FFE4B5', outline='#8B4513', width=3)
        
        # 2. Рисуем крышу
        roof_points = [
            house_x - 180, house_y - 80,    # левый нижний угол крыши
            house_x, house_y - 180,         # верхний центр крыши
            house_x + 180, house_y - 80     # правый нижний угол крыши
        ]
        self.canvas.create_polygon(roof_points, fill='#8B0000', 
                                  outline='#8B4513', width=3)
        
        # 3. Рисуем трубу на крыше
        self.canvas.create_rectangle(house_x + 80, house_y - 140,
                                    house_x + 120, house_y - 80,
                                    fill='#A0522D', outline='#8B4513', width=2)
        
        # Дым из трубы (только если включен свет - как будто топится печка)
        if self.light_on:
            self.canvas.create_oval(house_x + 90, house_y - 160,
                                   house_x + 130, house_y - 140,
                                   fill='#D3D3D3', outline='#A9A9A9')
            self.canvas.create_oval(house_x + 95, house_y - 180,
                                   house_x + 135, house_y - 160,
                                   fill='#C0C0C0', outline='#A9A9A9')
        
        # 4. Рисуем окно (главный элемент, меняет цвет)
        window_x = house_x - 100
        window_y = house_y - 30
        
        # Свечение окна (только когда свет включен)
        if self.light_on and colors['light_glow']:
            # Рисуем несколько слоев свечения
            glow_colors = ['#FFFFE0', '#FFFFC0', '#FFFFA0', '#FFFF80']
            for i, glow_color in enumerate(glow_colors):
                offset = 15 + i * 5
                self.canvas.create_rectangle(window_x - offset, window_y - offset,
                                            window_x + 80 + offset, window_y + 80 + offset,
                                            fill=glow_color, outline='')
        
        # Окно (меняет цвет в зависимости от состояния)
        self.canvas.create_rectangle(window_x, window_y,
                                    window_x + 80, window_y + 80,
                                    fill=colors['window'], outline=colors['window_frame'], width=3)
        
        # Рама окна (крест)
        self.canvas.create_line(window_x, window_y + 40,
                               window_x + 80, window_y + 40,
                               fill=colors['window_frame'], width=2)
        self.canvas.create_line(window_x + 40, window_y,
                               window_x + 40, window_y + 80,
                               fill=colors['window_frame'], width=2)
        
        # Шторы на окне
        # Левая штора
        self.canvas.create_rectangle(window_x - 15, window_y,
                                    window_x, window_y + 80,
                                    fill=colors['curtains'], outline='#8B4513', width=1)
        # Правая штора
        self.canvas.create_rectangle(window_x + 80, window_y,
                                    window_x + 95, window_y + 80,
                                    fill=colors['curtains'], outline='#8B4513', width=1)
        
        # 5. Рисуем дверь
        door_x = house_x + 60
        door_y = house_y + 40
        
        self.canvas.create_rectangle(door_x, door_y,
                                    door_x + 60, door_y + 80,
                                    fill='#8B4513', outline='#654321', width=3)
        
        # Ручка двери
        self.canvas.create_oval(door_x + 45, door_y + 40,
                               door_x + 50, door_y + 45,
                               fill='#FFD700', outline='#B8860B')
        
        # 6. Рисуем ступеньки перед дверью
        self.canvas.create_rectangle(door_x - 10, door_y + 80,
                                    door_x + 70, door_y + 90,
                                    fill='#A0522D', outline='#8B4513', width=2)
        
        # 7. Добавляем детали: цветы перед домом
        self.draw_flowers()
        
        # 8. Добавляем солнце
        self.canvas.create_oval(650, 50, 700, 100,
                               fill='#FFD700', outline='#FFA500', width=2)
        
        # Лучи солнца
        for angle in range(0, 360, 45):
            rad = angle * 3.14159 / 180
            x1 = 675 + 30 * 0.8 * (0 if angle % 90 == 0 else 1.5) * (1 if angle < 180 else -1)
            y1 = 75 + 30 * 0.8 * (0 if (angle + 45) % 90 == 0 else 1.5) * (1 if angle < 90 or angle > 270 else -1)
            self.canvas.create_line(675, 75, x1, y1, fill='#FFA500', width=2)
    
    def draw_flowers(self):
        """Рисует цветы перед домом"""
        # Несколько цветов разного цвета
        flower_positions = [
            (200, 380, '#FF0000'),  # Красный
            (250, 370, '#FF69B4'),  # Розовый
            (300, 390, '#FFA500'),  # Оранжевый
            (500, 380, '#FF0000'),  # Красный
            (550, 370, '#FFFF00'),  # Желтый
            (600, 390, '#800080')   # Фиолетовый
        ]
        
        for x, y, color in flower_positions:
            # Стебель
            self.canvas.create_line(x, y, x, y + 30, fill='#008000', width=2)
            
            # Лепестки
            self.canvas.create_oval(x - 8, y - 8, x + 8, y + 8, fill=color, outline='')
            
            # Центр цветка
            self.canvas.create_oval(x - 4, y - 4, x + 4, y + 4, fill='#FFD700', outline='')
    
    def setup_keyboard_controls(self):
        """Настраивает обработку клавиш клавиатуры"""
        # Привязываем обработчики клавиш
        self.root.bind('<Key>', self.on_key_press)
        self.root.focus_set()  # Устанавливаем фокус на окно
    
    def on_key_press(self, event):
        """Обработчик нажатия клавиш"""
        key = event.keysym.lower()
        char = event.char.lower()
        
        # Пробел или L (латинская) - переключение света
        if key == 'space' or char == 'l' or char == 'д':  # д - русская L
            self.toggle_light()
        
        # В (русская) - включить свет
        elif char == 'в':
            self.turn_on()
        
        # Ы (русская) - выключить свет (для "выкл")
        elif char == 'ы':
            self.turn_off()
        
        # ESC - выход
        elif key == 'escape':
            self.root.quit()
    
    def toggle_light(self):
        """Переключает состояние света"""
        self.light_on = not self.light_on
        self.update_house()
    
    def turn_on(self):
        """Включает свет"""
        if not self.light_on:
            self.light_on = True
            self.update_house()
    
    def turn_off(self):
        """Выключает свет"""
        if self.light_on:
            self.light_on = False
            self.update_house()
    
    def update_house(self):
        """Обновляет отображение дома"""
        # Перерисовываем дом
        self.draw_house()
        
        # Обновляем индикатор состояния
        if self.light_on:
            self.status_label.config(text="Свет в доме: ВКЛЮЧЕН", fg='#006400')
        else:
            self.status_label.config(text="Свет в доме: ВЫКЛЮЧЕН", fg='#8B0000')

def main():
    root = tk.Tk()
    app = HouseLightApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
