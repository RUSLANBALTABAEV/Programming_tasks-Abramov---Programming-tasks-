"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
5. Простейшие графические построения

131. Составить шаблоны рукописных букв от а до я. Используя
эти шаблоны, выполнить подрисуночные подписи к фигурам
предыдущей задачи и фигурам задачи 129. (Шаблон рукописной буквы
г см. на рис. 13.)
"""


import tkinter as tk

class HandwrittenFont:
    """Класс для создания и использования шаблонов рукописных букв"""
    
    def __init__(self):
        self.letters = self.create_letter_templates()
    
    def create_letter_templates(self):
        """Создает шаблоны рукописных букв от а до я"""
        letters = {}
        
        # Буква а
        letters['а'] = [
            [(0.2, 0.9), (0.3, 0.8), (0.4, 0.7), (0.5, 0.6), (0.6, 0.5), 
             (0.7, 0.4), (0.8, 0.4), (0.9, 0.5), (1.0, 0.6), (1.0, 0.7),
             (0.9, 0.8), (0.8, 0.9), (0.7, 1.0), (0.6, 1.0), (0.5, 0.9),
             (0.4, 0.8), (0.3, 0.8), (0.2, 0.9)],
            [(0.5, 0.3), (0.4, 0.2), (0.3, 0.1)]
        ]
        
        # Буква б
        letters['б'] = [
            [(0.8, 0.1), (0.7, 0.2), (0.6, 0.3), (0.5, 0.4), (0.4, 0.5),
             (0.3, 0.6), (0.2, 0.7), (0.2, 0.8), (0.3, 0.9), (0.4, 1.0),
             (0.5, 1.0), (0.6, 0.9), (0.7, 0.8), (0.8, 0.7), (0.9, 0.6)]
        ]
        
        # Буква в (пример рукописной)
        letters['в'] = [
            [(0.2, 0.1), (0.2, 1.0)],
            [(0.2, 0.5), (0.6, 0.4), (0.8, 0.5), (0.6, 0.6), (0.2, 0.5)],
            [(0.2, 0.8), (0.6, 0.7), (0.8, 0.8), (0.6, 0.9), (0.2, 0.8)]
        ]
        
        # Буква г (как на рис. 13)
        letters['г'] = [
            [(0.2, 0.1), (0.2, 0.7), (0.8, 0.7)]
        ]
        
        # Буква д
        letters['д'] = [
            [(0.3, 0.3), (0.7, 0.3)],
            [(0.2, 0.5), (0.3, 0.3), (0.7, 0.3), (0.8, 0.5), (0.7, 1.0), (0.3, 1.0), (0.2, 0.5)]
        ]
        
        # Буква е
        letters['е'] = [
            [(0.8, 0.3), (0.7, 0.2), (0.5, 0.1), (0.3, 0.2), (0.2, 0.4),
             (0.2, 0.6), (0.3, 0.8), (0.5, 0.9), (0.7, 0.8), (0.8, 0.6)],
            [(0.3, 0.5), (0.7, 0.5)]
        ]
        
        # Буква ё (та же е с двумя точками)
        letters['ё'] = [
            [(0.8, 0.3), (0.7, 0.2), (0.5, 0.1), (0.3, 0.2), (0.2, 0.4),
             (0.2, 0.6), (0.3, 0.8), (0.5, 0.9), (0.7, 0.8), (0.8, 0.6)],
            [(0.3, 0.5), (0.7, 0.5)],
            [(0.4, 0.0), (0.4, 0.0), (0.4, 0.1)],  # Точка 1
            [(0.6, 0.0), (0.6, 0.0), (0.6, 0.1)]   # Точка 2
        ]
        
        # Буква ж
        letters['ж'] = [
            [(0.5, 0.1), (0.5, 1.0)],
            [(0.2, 0.3), (0.5, 0.5), (0.8, 0.3)],
            [(0.2, 0.7), (0.5, 0.5), (0.8, 0.7)]
        ]
        
        # Буква з
        letters['з'] = [
            [(0.7, 0.2), (0.6, 0.1), (0.4, 0.1), (0.3, 0.2), (0.4, 0.3),
             (0.6, 0.3), (0.7, 0.4), (0.7, 0.6), (0.6, 0.7), (0.4, 0.7),
             (0.3, 0.8), (0.4, 0.9), (0.6, 0.9), (0.7, 0.8)]
        ]
        
        # Буква и
        letters['и'] = [
            [(0.2, 0.1), (0.2, 1.0)],
            [(0.2, 1.0), (0.8, 0.1), (0.8, 1.0)]
        ]
        
        # Буква й (и с крышечкой)
        letters['й'] = [
            [(0.2, 0.1), (0.2, 1.0)],
            [(0.2, 1.0), (0.8, 0.1), (0.8, 1.0)],
            [(0.1, 0.0), (0.3, 0.0)]  # Крышечка
        ]
        
        # Буква к
        letters['к'] = [
            [(0.2, 0.1), (0.2, 1.0)],
            [(0.2, 0.5), (0.7, 0.1)],
            [(0.2, 0.5), (0.7, 1.0)]
        ]
        
        # Буква л
        letters['л'] = [
            [(0.3, 0.1), (0.2, 0.3), (0.2, 0.7), (0.3, 1.0), (0.5, 1.0),
             (0.6, 0.8), (0.7, 0.4), (0.8, 0.1)]
        ]
        
        # Буква м
        letters['м'] = [
            [(0.2, 1.0), (0.2, 0.1), (0.5, 0.5), (0.8, 0.1), (0.8, 1.0)]
        ]
        
        # Буква н
        letters['н'] = [
            [(0.2, 0.1), (0.2, 1.0)],
            [(0.8, 0.1), (0.8, 1.0)],
            [(0.2, 0.5), (0.8, 0.5)]
        ]
        
        # Буква о
        letters['о'] = [
            [(0.5, 0.1), (0.3, 0.2), (0.2, 0.4), (0.2, 0.6), (0.3, 0.8),
             (0.5, 0.9), (0.7, 0.8), (0.8, 0.6), (0.8, 0.4), (0.7, 0.2),
             (0.5, 0.1), (0.5, 0.9)]  # Замыкающая линия
        ]
        
        # Создаем простые шаблоны для остальных букв
        # Для экономии места создадим базовые шаблоны
        
        # п
        letters['п'] = [
            [(0.2, 0.1), (0.2, 1.0)],
            [(0.8, 0.1), (0.8, 1.0)],
            [(0.2, 0.1), (0.8, 0.1)]
        ]
        
        # р
        letters['р'] = [
            [(0.2, 0.5), (0.2, 1.0)],
            [(0.2, 0.5), (0.5, 0.2), (0.8, 0.5), (0.2, 0.5)]
        ]
        
        # с
        letters['с'] = [
            [(0.7, 0.2), (0.6, 0.1), (0.4, 0.1), (0.3, 0.2), (0.2, 0.4),
             (0.2, 0.6), (0.3, 0.8), (0.4, 0.9), (0.6, 0.9), (0.7, 0.8)]
        ]
        
        # т
        letters['т'] = [
            [(0.5, 0.1), (0.5, 1.0)],
            [(0.2, 0.1), (0.8, 0.1)]
        ]
        
        # у
        letters['у'] = [
            [(0.8, 0.1), (0.2, 1.0)],
            [(0.2, 0.1), (0.8, 1.0)]
        ]
        
        # ф
        letters['ф'] = [
            [(0.5, 0.1), (0.5, 1.0)],
            [(0.2, 0.4), (0.8, 0.4), (0.8, 0.6), (0.2, 0.6), (0.2, 0.4)],
            [(0.5, 0.4), (0.5, 0.6)]
        ]
        
        # х
        letters['х'] = [
            [(0.2, 0.1), (0.8, 1.0)],
            [(0.8, 0.1), (0.2, 1.0)]
        ]
        
        # ц
        letters['ц'] = [
            [(0.2, 0.1), (0.2, 1.0)],
            [(0.8, 0.1), (0.8, 1.0), (1.0, 1.0)],
            [(0.2, 0.1), (0.8, 0.1)]
        ]
        
        # ч
        letters['ч'] = [
            [(0.2, 0.1), (0.2, 0.7), (0.5, 0.4), (0.8, 0.1), (0.8, 1.0)]
        ]
        
        # ш
        letters['ш'] = [
            [(0.1, 0.1), (0.1, 1.0)],
            [(0.5, 0.1), (0.5, 1.0)],
            [(0.9, 0.1), (0.9, 1.0)],
            [(0.1, 0.1), (0.9, 0.1)]
        ]
        
        # щ
        letters['щ'] = [
            [(0.1, 0.1), (0.1, 1.0)],
            [(0.5, 0.1), (0.5, 1.0)],
            [(0.9, 0.1), (0.9, 1.0), (1.1, 1.0)],
            [(0.1, 0.1), (0.9, 0.1)]
        ]
        
        # ъ
        letters['ъ'] = [
            [(0.2, 0.1), (0.2, 1.0)],
            [(0.2, 0.1), (0.8, 0.1)],
            [(0.8, 0.1), (0.8, 0.5), (0.5, 0.7), (0.2, 0.5)]
        ]
        
        # ы
        letters['ы'] = [
            [(0.1, 0.1), (0.1, 1.0)],
            [(0.4, 0.1), (0.4, 1.0)],
            [(0.4, 0.1), (0.8, 0.1), (0.9, 0.2), (0.9, 0.8), (0.8, 0.9), (0.4, 0.9)]
        ]
        
        # ь
        letters['ь'] = [
            [(0.2, 0.1), (0.2, 1.0)],
            [(0.2, 0.9), (0.5, 0.9), (0.6, 0.8), (0.6, 0.6), (0.5, 0.5), (0.2, 0.5)]
        ]
        
        # э
        letters['э'] = [
            [(0.7, 0.2), (0.6, 0.1), (0.4, 0.1), (0.3, 0.2), (0.2, 0.4),
             (0.2, 0.6), (0.3, 0.8), (0.4, 0.9), (0.6, 0.9), (0.7, 0.8)],
            [(0.4, 0.5), (0.7, 0.5)]
        ]
        
        # ю
        letters['ю'] = [
            [(0.2, 0.1), (0.2, 1.0)],
            [(0.5, 0.4), (0.8, 0.2), (0.9, 0.4), (0.9, 0.6), (0.8, 0.8), (0.5, 0.6), (0.5, 0.4)],
            [(0.5, 0.4), (0.5, 0.6)]
        ]
        
        # я
        letters['я'] = [
            [(0.8, 0.1), (0.7, 0.2), (0.6, 0.3), (0.5, 0.4), (0.4, 0.5),
             (0.3, 0.6), (0.2, 0.7), (0.2, 0.8), (0.3, 0.9), (0.4, 1.0),
             (0.6, 1.0), (0.7, 0.9), (0.8, 0.8), (0.9, 0.7), (0.8, 0.1)]
        ]
        
        return letters
    
    def draw_letter(self, canvas, letter, x, y, size=20, color='black'):
        """Рисует рукописную букву на canvas"""
        if letter not in self.letters:
            return
            
        paths = self.letters[letter]
        
        for path in paths:
            if len(path) == 3 and path[0] == path[1]:  # Точка
                canvas.create_oval(x + path[0][0]*size, y + path[0][1]*size,
                                  x + (path[0][0]+0.1)*size, y + (path[0][1]+0.1)*size,
                                  fill=color, outline=color)
            else:
                scaled_path = []
                for point in path:
                    scaled_path.append(x + point[0]*size)
                    scaled_path.append(y + point[1]*size)
                
                canvas.create_line(scaled_path, fill=color, width=2, smooth=True)

class GeometricFiguresWithHandwritten:
    """Класс для рисования фигур с рукописными подписями"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Рис. 11: Геометрические фигуры с рукописными подписями")
        
        # Создаем canvas для фигур
        self.canvas_figures = tk.Canvas(root, width=1200, height=400, bg='white')
        self.canvas_figures.pack()
        
        # Создаем canvas для алфавита
        self.canvas_alphabet = tk.Canvas(root, width=1200, height=400, bg='white')
        self.canvas_alphabet.pack()
        
        # Создаем шрифт
        self.font = HandwrittenFont()
        
        self.figures = self.create_figures()
        self.draw_all_figures()
        self.draw_alphabet()
        
    def create_figures(self):
        """Создает описания фигур для задачи 129 (первые 4 фигуры)"""
        figures = []
        
        # Цыпленок (а)
        figures.append({
            'name': 'Цыпленок',
            'shapes': [
                {'type': 'ellipse', 'coords': [50, 80, 150, 180], 'fill': 'yellow', 'outline': 'black'},
                {'type': 'oval', 'coords': [80, 20, 120, 60], 'fill': 'yellow', 'outline': 'black'},
                {'type': 'polygon', 'coords': [100, 60, 90, 80, 110, 80], 'fill': 'orange', 'outline': 'black'},
                {'type': 'polygon', 'coords': [150, 100, 180, 70, 180, 130], 'fill': 'orange', 'outline': 'black'},
                {'type': 'polygon', 'coords': [70, 100, 40, 120, 70, 140], 'fill': 'orange', 'outline': 'black'},
                {'type': 'line', 'coords': [100, 180, 90, 200], 'fill': 'brown', 'width': 3},
                {'type': 'line', 'coords': [120, 180, 130, 200], 'fill': 'brown', 'width': 3}
            ]
        })
        
        # Дом (б)
        figures.append({
            'name': 'Дом',
            'shapes': [
                {'type': 'rectangle', 'coords': [50, 100, 150, 200], 'fill': 'lightblue', 'outline': 'black'},
                {'type': 'polygon', 'coords': [50, 100, 150, 100, 100, 50], 'fill': 'red', 'outline': 'black'},
                {'type': 'rectangle', 'coords': [80, 120, 120, 160], 'fill': 'yellow', 'outline': 'black'},
                {'type': 'rectangle', 'coords': [130, 140, 150, 180], 'fill': 'brown', 'outline': 'black'},
                {'type': 'line', 'coords': [160, 60, 160, 40, 180, 40, 180, 60], 'fill': 'gray', 'width': 3}
            ]
        })
        
        # Грузовик (в)
        figures.append({
            'name': 'Грузовик',
            'shapes': [
                {'type': 'rectangle', 'coords': [50, 120, 120, 180], 'fill': 'blue', 'outline': 'black'},
                {'type': 'rectangle', 'coords': [120, 80, 180, 180], 'fill': 'green', 'outline': 'black'},
                {'type': 'rectangle', 'coords': [70, 130, 100, 150], 'fill': 'lightblue', 'outline': 'black'},
                {'type': 'oval', 'coords': [70, 180, 90, 200], 'fill': 'black', 'outline': 'black'},
                {'type': 'oval', 'coords': [140, 180, 160, 200], 'fill': 'black', 'outline': 'black'}
            ]
        })
        
        # Елка (г)
        figures.append({
            'name': 'Елка',
            'shapes': [
                {'type': 'polygon', 'coords': [100, 20, 50, 80, 150, 80], 'fill': 'green', 'outline': 'black'},
                {'type': 'polygon', 'coords': [100, 60, 30, 120, 170, 120], 'fill': 'green', 'outline': 'black'},
                {'type': 'polygon', 'coords': [100, 100, 10, 180, 190, 180], 'fill': 'green', 'outline': 'black'},
                {'type': 'rectangle', 'coords': [95, 180, 105, 200], 'fill': 'brown', 'outline': 'black'}
            ]
        })
        
        return figures
    
    def draw_figure(self, x_offset, y_offset, figure_idx):
        """Рисует одну фигуру с заданным смещением"""
        figure = self.figures[figure_idx]
        
        # Рисуем все фигуры
        for shape in figure['shapes']:
            coords = [c + (x_offset if i % 2 == 0 else y_offset) 
                     for i, c in enumerate(shape['coords'])]
            
            if shape['type'] == 'ellipse' or shape['type'] == 'oval':
                self.canvas_figures.create_oval(coords, fill=shape['fill'], 
                                               outline=shape.get('outline', 'black'))
            elif shape['type'] == 'rectangle':
                self.canvas_figures.create_rectangle(coords, fill=shape['fill'], 
                                                   outline=shape.get('outline', 'black'))
            elif shape['type'] == 'polygon':
                self.canvas_figures.create_polygon(coords, fill=shape['fill'], 
                                                 outline=shape.get('outline', 'black'))
            elif shape['type'] == 'line':
                self.canvas_figures.create_line(coords, fill=shape['fill'], 
                                              width=shape.get('width', 1))
        
        # Рисуем рукописную букву под фигурой
        letter = chr(1072 + figure_idx)  # 1072 - код буквы 'а' в Unicode
        self.font.draw_letter(self.canvas_figures, letter, 
                             x_offset + 100, y_offset + 220, 15, 'black')
        
        # Рисуем подпись печатным шрифтом
        self.canvas_figures.create_text(x_offset + 100, y_offset + 240,
                                       text=f"{letter}) {figure['name']}",
                                       font=('Arial', 10, 'bold'))
    
    def draw_all_figures(self):
        """Рисует все 4 фигуры задачи 129"""
        for i in range(len(self.figures)):
            x_offset = i * 300 + 50
            y_offset = 50
            self.draw_figure(x_offset, y_offset, i)
    
    def draw_alphabet(self):
        """Рисует все буквы русского алфавита"""
        alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        
        # Заголовок
        self.canvas_alphabet.create_text(600, 20,
                                       text="Шаблоны рукописных букв от а до я",
                                       font=('Arial', 14, 'bold'))
        
        # Рисуем все буквы в сетке
        for i, letter in enumerate(alphabet):
            row = i // 10
            col = i % 10
            
            x = col * 110 + 50
            y = row * 70 + 60
            
            # Рисуем контур буквы
            self.canvas_alphabet.create_rectangle(x-5, y-5, x+25, y+25,
                                                outline='lightgray', fill='white')
            
            # Рисуем рукописную букву
            self.font.draw_letter(self.canvas_alphabet, letter, x, y, 20, 'blue')
            
            # Подпись буквы
            self.canvas_alphabet.create_text(x + 40, y + 10,
                                           text=f"{letter} - {letter.upper()}",
                                           font=('Arial', 10))
            
            # Пример буквы г (как на рис. 13)
            if letter == 'г':
                self.canvas_alphabet.create_text(x, y + 40,
                                               text="(как на рис. 13)",
                                               font=('Arial', 8, 'italic'))

def main():
    root = tk.Tk()
    app = GeometricFiguresWithHandwritten(root)
    root.mainloop()

if __name__ == "__main__":
    main()
