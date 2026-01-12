"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
5. Простейшие графические построения

130. На рис. 12, а – р даны шаблоны нескольких фигур: жука,
букета цветов, робота, самолета и т. д. Закрашенный квадрат на
шаблоне соответствует высвечиваемой точке, пустой квадрат – точке,
которая не высвечивается (или, что то же самое, точке, цвет которой
совпадает с цветом фона).
"""

import tkinter as tk
from tkinter import ttk, colorchooser


class PixelArtApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Задание 130: Пиксельная графика - Шаблоны фигур")
        self.root.geometry("1000x700")
        self.root.configure(bg='#f0f0f0')
        
        # Параметры
        self.pixel_size = 20
        self.color = "#000000"
        self.show_grid = True
        self.current_template = None
        
        # Шаблоны фигур (1 = закрашенный, 0 = пустой)
        self.templates = {
            'а) Жук': [
                [0,0,1,0,0,1,0,0],
                [0,1,0,0,0,0,1,0],
                [0,0,1,1,1,1,0,0],
                [0,1,1,1,1,1,1,0],
                [1,1,1,1,1,1,1,1],
                [0,1,1,1,1,1,1,0],
                [0,1,0,0,0,0,1,0],
                [1,0,0,0,0,0,0,1]
            ],
            'б) Букет': [
                [0,0,1,1,0,0,1,1],
                [0,0,1,1,0,0,1,1],
                [0,1,1,1,1,1,1,0],
                [0,0,1,1,1,1,0,0],
                [0,0,0,1,1,0,0,0],
                [0,0,0,1,1,0,0,0],
                [0,0,0,1,1,0,0,0],
                [0,0,1,1,1,1,0,0]
            ],
            'в) Робот': [
                [0,0,1,1,1,0,0,0],
                [0,0,1,1,1,0,0,0],
                [0,1,1,1,1,1,0,0],
                [1,1,0,1,0,1,1,0],
                [0,1,1,1,1,1,0,0],
                [0,0,1,0,1,0,0,0],
                [0,0,1,0,1,0,0,0],
                [0,1,0,0,0,1,0,0]
            ],
            'г) Самолёт': [
                [0,0,0,0,1,1,0,0],
                [0,0,0,1,1,1,1,0],
                [1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1],
                [0,0,0,1,1,1,1,0],
                [0,0,0,1,1,1,0,0],
                [0,0,0,0,1,0,0,0],
                [0,0,0,1,0,1,0,0]
            ],
            'д) Робот-2': [
                [0,0,1,1,1,1,0,0],
                [0,0,1,1,1,1,0,0],
                [0,1,1,0,0,1,1,0],
                [1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1],
                [0,0,1,1,1,1,0,0],
                [0,0,1,0,0,1,0,0],
                [0,1,0,0,0,0,1,0]
            ],
            'е) Птица': [
                [0,0,0,0,0,1,1,0],
                [0,0,0,1,1,1,1,1],
                [0,1,1,1,1,1,1,0],
                [1,1,1,1,1,1,0,0],
                [1,1,1,1,1,0,0,0],
                [0,1,1,1,0,0,0,0],
                [0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,0]
            ],
            'ж) Чашка': [
                [0,0,1,1,0,0,0,0],
                [0,0,1,0,1,0,0,0],
                [0,1,1,1,1,1,0,0],
                [0,1,1,1,1,1,0,0],
                [0,1,1,1,1,1,0,0],
                [0,1,1,1,1,1,1,0],
                [0,1,1,1,1,1,1,0],
                [1,0,0,0,0,0,0,0]
            ],
            'з) Танк': [
                [0,0,0,1,1,1,0,0],
                [0,0,1,1,1,1,1,0],
                [0,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1],
                [0,0,0,1,1,0,0,0],
                [0,0,1,1,1,1,0,0],
                [1,0,1,0,1,0,1,0],
                [1,0,1,0,1,0,1,0]
            ],
            'и) Цветок': [
                [0,0,0,1,0,0,0,0],
                [0,0,1,1,1,0,0,0],
                [0,1,0,1,0,1,0,0],
                [1,0,0,1,0,0,1,0],
                [0,1,0,1,0,1,0,0],
                [0,0,1,1,1,0,0,0],
                [0,0,0,1,0,0,0,0],
                [0,0,0,1,0,0,0,0]
            ],
            'к) Кит': [
                [0,0,1,1,1,1,0,0],
                [0,1,1,1,1,1,1,0],
                [1,1,1,1,1,1,1,1],
                [1,1,0,1,1,0,1,1],
                [1,1,1,1,1,1,1,1],
                [0,1,1,1,1,1,1,0],
                [0,0,1,1,1,1,0,0],
                [0,0,0,0,0,0,0,0]
            ],
            'л) Маски': [
                [1,1,0,0,0,1,1,0],
                [1,1,0,0,0,1,1,0],
                [1,1,1,0,1,1,1,0],
                [0,1,1,1,1,1,0,0],
                [0,0,1,0,1,0,0,0],
                [0,0,1,1,1,0,0,0],
                [0,1,1,0,1,1,0,0],
                [0,1,0,0,0,1,0,0]
            ],
            'м) Кораблик': [
                [0,0,0,0,1,1,0,0],
                [0,0,0,0,1,1,1,0],
                [0,0,0,1,1,1,1,0],
                [0,0,1,1,1,1,1,0],
                [0,1,1,1,1,1,1,0],
                [1,1,1,1,1,1,1,1],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0]
            ],
            'н) Пальма': [
                [0,0,1,1,1,0,0,0],
                [0,1,1,1,1,1,0,0],
                [1,1,1,1,1,1,1,0],
                [0,0,0,1,1,0,0,0],
                [0,0,0,1,1,0,0,0],
                [0,0,0,1,1,0,0,0],
                [0,0,1,0,0,1,0,0],
                [0,0,0,0,0,0,0,0]
            ],
            'о) Ёлка': [
                [0,0,0,1,1,0,0,0],
                [0,0,1,1,1,1,0,0],
                [0,1,1,1,1,1,1,0],
                [1,1,1,1,1,1,1,1],
                [0,0,1,1,1,1,0,0],
                [0,0,0,1,1,0,0,0],
                [0,0,0,1,1,0,0,0],
                [0,0,0,0,0,0,0,0]
            ],
            'п) Дом с цветами': [
                [0,0,1,1,1,0,0,0],
                [0,1,1,1,1,1,0,0],
                [1,1,1,1,1,1,1,0],
                [0,1,1,0,1,1,0,0],
                [0,1,1,0,1,1,0,0],
                [0,1,0,0,0,1,0,0],
                [1,0,1,0,1,0,1,0],
                [0,1,0,0,0,1,0,0]
            ],
            'р) Лошадь': [
                [0,0,0,1,1,0,0,0],
                [0,0,1,1,1,1,0,1],
                [0,1,1,1,1,1,1,0],
                [1,1,1,1,1,1,1,0],
                [1,1,1,1,1,1,1,0],
                [0,1,0,0,0,1,0,0],
                [1,0,1,0,1,0,1,0],
                [1,0,0,0,0,0,0,1]
            ]
        }
        
        self.create_ui()
        
        # Выбираем первый шаблон
        self.current_template = self.templates[list(self.templates.keys())[0]]
        self.draw_main_canvas()
    
    def create_ui(self):
        """Создание интерфейса"""
        # Заголовок
        title_frame = tk.Frame(self.root, bg='#2a5298', pady=15)
        title_frame.pack(fill=tk.X)
        
        title_label = tk.Label(
            title_frame,
            text="§ 5. Простейшие графические построения",
            font=('Arial', 16, 'bold'),
            bg='#2a5298',
            fg='white'
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            title_frame,
            text="Задание 130: Шаблоны фигур (Рис. 12, а–р)",
            font=('Arial', 12),
            bg='#2a5298',
            fg='white'
        )
        subtitle_label.pack()
        
        # Основной контейнер
        main_container = tk.Frame(self.root, bg='#f0f0f0')
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Левая панель - основной холст
        left_frame = tk.Frame(main_container, bg='white', relief=tk.RAISED, bd=2)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        canvas_label = tk.Label(
            left_frame,
            text="Выбранная фигура",
            font=('Arial', 14, 'bold'),
            bg='white'
        )
        canvas_label.pack(pady=10)
        
        self.main_canvas = tk.Canvas(
            left_frame,
            width=400,
            height=400,
            bg='white',
            highlightthickness=1,
            highlightbackground='#2a5298'
        )
        self.main_canvas.pack(padx=20, pady=(0, 20))
        
        # Панель управления
        control_frame = tk.Frame(left_frame, bg='white')
        control_frame.pack(pady=10)
        
        # Кнопки управления
        tk.Button(
            control_frame,
            text="Выбрать цвет",
            command=self.choose_color,
            bg='#2a5298',
            fg='white',
            font=('Arial', 10, 'bold'),
            padx=15,
            pady=5
        ).grid(row=0, column=0, padx=5, pady=5)
        
        tk.Button(
            control_frame,
            text="Сетка вкл/выкл",
            command=self.toggle_grid,
            bg='#2a5298',
            fg='white',
            font=('Arial', 10, 'bold'),
            padx=15,
            pady=5
        ).grid(row=0, column=1, padx=5, pady=5)
        
        tk.Button(
            control_frame,
            text="Очистить",
            command=self.clear_canvas,
            bg='#d32f2f',
            fg='white',
            font=('Arial', 10, 'bold'),
            padx=15,
            pady=5
        ).grid(row=0, column=2, padx=5, pady=5)
        
        # Размер пикселя
        size_frame = tk.Frame(control_frame, bg='white')
        size_frame.grid(row=1, column=0, columnspan=3, pady=10)
        
        tk.Label(
            size_frame,
            text="Размер пикселя:",
            font=('Arial', 10),
            bg='white'
        ).pack(side=tk.LEFT, padx=5)
        
        self.size_var = tk.IntVar(value=20)
        size_scale = tk.Scale(
            size_frame,
            from_=5,
            to=40,
            orient=tk.HORIZONTAL,
            variable=self.size_var,
            command=self.on_size_change,
            length=200
        )
        size_scale.pack(side=tk.LEFT, padx=5)
        
        # Правая панель - галерея
        right_frame = tk.Frame(main_container, bg='white', relief=tk.RAISED, bd=2)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, padx=(10, 0))
        
        gallery_label = tk.Label(
            right_frame,
            text="Галерея шаблонов",
            font=('Arial', 14, 'bold'),
            bg='white'
        )
        gallery_label.pack(pady=10)
        
        # Создаем прокручиваемую область
        canvas_container = tk.Canvas(right_frame, bg='white', width=300)
        scrollbar = ttk.Scrollbar(
            right_frame,
            orient="vertical",
            command=canvas_container.yview
        )
        scrollable_frame = tk.Frame(canvas_container, bg='white')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas_container.configure(scrollregion=canvas_container.bbox("all"))
        )
        
        canvas_container.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas_container.configure(yscrollcommand=scrollbar.set)
        
        canvas_container.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Создаем галерею
        self.create_gallery(scrollable_frame)
        
        # Инструкция
        info_frame = tk.Frame(self.root, bg='#e8f5e9', relief=tk.RAISED, bd=2)
        info_frame.pack(fill=tk.X, padx=20, pady=(0, 20))
        
        info_text = """Инструкция: Выберите фигуру из галереи справа, чтобы увидеть её увеличенной. 
Закрашенный квадрат соответствует высвечиваемой точке, пустой квадрат – точке фона.
Вы можете изменить цвет и размер пикселей, включить/выключить сетку."""
        
        tk.Label(
            info_frame,
            text=info_text,
            font=('Arial', 9),
            bg='#e8f5e9',
            justify=tk.LEFT,
            wraplength=900
        ).pack(padx=15, pady=10)
    
    def create_gallery(self, parent):
        """Создание галереи миниатюр"""
        self.gallery_buttons = []
        
        for idx, (name, template) in enumerate(self.templates.items()):
            frame = tk.Frame(
                parent,
                bg='#f0f0f0',
                relief=tk.RAISED,
                bd=2,
                cursor='hand2'
            )
            frame.pack(fill=tk.X, padx=10, pady=5)
            
            # Миниатюра
            mini_canvas = tk.Canvas(
                frame,
                width=100,
                height=100,
                bg='white',
                highlightthickness=0
            )
            mini_canvas.pack(pady=5)
            
            # Рисуем миниатюру
            self.draw_template_mini(mini_canvas, template, 10)
            
            # Подпись
            label = tk.Label(
                frame,
                text=name,
                font=('Arial', 10, 'bold'),
                bg='#f0f0f0'
            )
            label.pack(pady=(0, 5))
            
            # Обработчик клика
            frame.bind(
                '<Button-1>',
                lambda e, t=template, f=frame: self.select_template(t, f)
            )
            mini_canvas.bind(
                '<Button-1>',
                lambda e, t=template, f=frame: self.select_template(t, f)
            )
            label.bind(
                '<Button-1>',
                lambda e, t=template, f=frame: self.select_template(t, f)
            )
            
            self.gallery_buttons.append(frame)
            
            # Выделяем первый элемент
            if idx == 0:
                frame.configure(bg='#bbdefb', relief=tk.SUNKEN)
                label.configure(bg='#bbdefb')
    
    def draw_template_mini(self, canvas, template, size):
        """Рисование миниатюры шаблона"""
        rows = len(template)
        cols = len(template[0])
        
        for row in range(rows):
            for col in range(cols):
                if template[row][col] == 1:
                    canvas.create_rectangle(
                        col * size,
                        row * size,
                        (col + 1) * size,
                        (row + 1) * size,
                        fill='#333333',
                        outline=''
                    )
    
    def select_template(self, template, frame):
        """Выбор шаблона из галереи"""
        # Снимаем выделение со всех
        for btn in self.gallery_buttons:
            btn.configure(bg='#f0f0f0', relief=tk.RAISED)
            for child in btn.winfo_children():
                if isinstance(child, tk.Label):
                    child.configure(bg='#f0f0f0')
        
        # Выделяем выбранный
        frame.configure(bg='#bbdefb', relief=tk.SUNKEN)
        for child in frame.winfo_children():
            if isinstance(child, tk.Label):
                child.configure(bg='#bbdefb')
        
        self.current_template = template
        self.draw_main_canvas()
    
    def draw_main_canvas(self):
        """Рисование основного холста"""
        self.main_canvas.delete('all')
        
        if not self.current_template:
            return
        
        size = self.pixel_size
        rows = len(self.current_template)
        cols = len(self.current_template[0])
        
        # Центрирование
        offset_x = (400 - cols * size) // 2
        offset_y = (400 - rows * size) // 2
        
        # Рисуем сетку
        if self.show_grid:
            for i in range(cols + 1):
                self.main_canvas.create_line(
                    offset_x + i * size,
                    offset_y,
                    offset_x + i * size,
                    offset_y + rows * size,
                    fill='#dddddd'
                )
            for i in range(rows + 1):
                self.main_canvas.create_line(
                    offset_x,
                    offset_y + i * size,
                    offset_x + cols * size,
                    offset_y + i * size,
                    fill='#dddddd'
                )
        
        # Рисуем пиксели
        for row in range(rows):
            for col in range(cols):
                if self.current_template[row][col] == 1:
                    self.main_canvas.create_rectangle(
                        offset_x + col * size + 1,
                        offset_y + row * size + 1,
                        offset_x + (col + 1) * size - 1,
                        offset_y + (row + 1) * size - 1,
                        fill=self.color,
                        outline=''
                    )
    
    def choose_color(self):
        """Выбор цвета"""
        color = colorchooser.askcolor(initialcolor=self.color)[1]
        if color:
            self.color = color
            self.draw_main_canvas()
    
    def toggle_grid(self):
        """Переключение сетки"""
        self.show_grid = not self.show_grid
        self.draw_main_canvas()
    
    def clear_canvas(self):
        """Очистка холста"""
        self.main_canvas.delete('all')
    
    def on_size_change(self, value):
        """Изменение размера пикселя"""
        self.pixel_size = int(value)
        self.draw_main_canvas()


def main():
    """Основная функция"""
    print("=" * 60)
    print("ЗАДАНИЕ 130: Пиксельная графика")
    print("Шаблоны фигур (Рис. 12, а–р)")
    print("=" * 60)
    print("\nЗапуск графического интерфейса...")
    print("\nИнструкция:")
    print("1. Выберите фигуру из галереи справа")
    print("2. Настройте цвет и размер пикселей")
    print("3. Включите/выключите сетку по необходимости")
    print("\nФигуры включают:")
    print("а) Жук, б) Букет, в) Робот, г) Самолёт")
    print("д) Робот-2, е) Птица, ж) Чашка, з) Танк")
    print("и) Цветок, к) Кит, л) Маски, м) Кораблик")
    print("н) Пальма, о) Ёлка, п) Дом с цветами, р) Лошадь")
    print("=" * 60)
    
    root = tk.Tk()
    app = PixelArtApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
