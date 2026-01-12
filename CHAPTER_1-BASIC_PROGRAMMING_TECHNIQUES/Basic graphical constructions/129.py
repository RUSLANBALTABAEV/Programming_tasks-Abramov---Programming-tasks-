"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
5. Простейшие графические построения

129. Рис. 11, а - о составлены из простейших геометрических
фигур треугольников, квадратов, окружностей, точек и т.п. Цыпленок
(рис. 11, а) состоит из эллипса (тело цыпленка), окружности (голова),
трех треугольников (нос, хвост и крыло цыпленка) и двух прямых
(лапы). Дом (рис. 11, б) состоит из двух квадратов (дом и окно),
прямоугольника (дверь), треугольника (крыша) и ломаной (труба).
Грузовик (рис. 11, в) состоит из двух прямоугольников (кабина и
кузов), квадрата (окно) и двух окружностей (колеса). Елка (рис. 11, г)
состоит из трех треугольников (ветви) и прямоугольника (ствол) и т. п.
Получить на экране и раскрасить рис .11, а - о.
"""


import tkinter as tk

class GeometricFigures:
    def __init__(self, root):
        self.root = root
        self.root.title("Рис. 11: Геометрические фигуры (а-о)")
        self.canvas = tk.Canvas(root, width=1200, height=800, bg='white')
        self.canvas.pack()
        
        self.figures = self.create_figures()
        self.draw_all_figures()
        
    def create_figures(self):
        """Создает описания всех 15 фигур"""
        figures = []
        
        # 0: Цыпленок (а)
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
        
        # 1: Дом (б)
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
        
        # 2: Грузовик (в)
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
        
        # 3: Елка (г)
        figures.append({
            'name': 'Елка',
            'shapes': [
                {'type': 'polygon', 'coords': [100, 20, 50, 80, 150, 80], 'fill': 'green', 'outline': 'black'},
                {'type': 'polygon', 'coords': [100, 60, 30, 120, 170, 120], 'fill': 'green', 'outline': 'black'},
                {'type': 'polygon', 'coords': [100, 100, 10, 180, 190, 180], 'fill': 'green', 'outline': 'black'},
                {'type': 'rectangle', 'coords': [95, 180, 105, 200], 'fill': 'brown', 'outline': 'black'}
            ]
        })
        
        # 4: Солнце (д)
        figures.append({
            'name': 'Солнце',
            'shapes': [
                {'type': 'oval', 'coords': [80, 80, 120, 120], 'fill': 'yellow', 'outline': 'orange'},
                {'type': 'polygon', 'coords': [100, 60, 95, 40, 105, 40], 'fill': 'yellow', 'outline': 'orange'},
                {'type': 'polygon', 'coords': [140, 100, 160, 95, 160, 105], 'fill': 'yellow', 'outline': 'orange'},
                {'type': 'polygon', 'coords': [100, 140, 95, 160, 105, 160], 'fill': 'yellow', 'outline': 'orange'},
                {'type': 'polygon', 'coords': [60, 100, 40, 95, 40, 105], 'fill': 'yellow', 'outline': 'orange'}
            ]
        })
        
        # 5: Облако (е)
        figures.append({
            'name': 'Облако',
            'shapes': [
                {'type': 'oval', 'coords': [60, 100, 100, 140], 'fill': 'white', 'outline': 'gray'},
                {'type': 'oval', 'coords': [80, 80, 120, 120], 'fill': 'white', 'outline': 'gray'},
                {'type': 'oval', 'coords': [100, 100, 140, 140], 'fill': 'white', 'outline': 'gray'}
            ]
        })
        
        # 6: Цветок (ж)
        figures.append({
            'name': 'Цветок',
            'shapes': [
                {'type': 'oval', 'coords': [100, 100, 120, 120], 'fill': 'yellow', 'outline': 'black'},
                {'type': 'oval', 'coords': [80, 80, 100, 100], 'fill': 'red', 'outline': 'black'},
                {'type': 'oval', 'coords': [120, 80, 140, 100], 'fill': 'red', 'outline': 'black'},
                {'type': 'oval', 'coords': [80, 120, 100, 140], 'fill': 'red', 'outline': 'black'},
                {'type': 'oval', 'coords': [120, 120, 140, 140], 'fill': 'red', 'outline': 'black'}
            ]
        })
        
        # 7: Кораблик (з)
        figures.append({
            'name': 'Кораблик',
            'shapes': [
                {'type': 'polygon', 'coords': [80, 140, 120, 140, 100, 100], 'fill': 'white', 'outline': 'black'},
                {'type': 'polygon', 'coords': [60, 180, 140, 180, 120, 140, 80, 140], 'fill': 'brown', 'outline': 'black'}
            ]
        })
        
        # 8: Машина (и)
        figures.append({
            'name': 'Машина',
            'shapes': [
                {'type': 'rectangle', 'coords': [60, 120, 140, 180], 'fill': 'red', 'outline': 'black'},
                {'type': 'rectangle', 'coords': [80, 100, 120, 120], 'fill': 'lightblue', 'outline': 'black'},
                {'type': 'oval', 'coords': [80, 180, 100, 200], 'fill': 'black', 'outline': 'black'},
                {'type': 'oval', 'coords': [120, 180, 140, 200], 'fill': 'black', 'outline': 'black'}
            ]
        })
        
        # 9: Робот (к)
        figures.append({
            'name': 'Робот',
            'shapes': [
                {'type': 'rectangle', 'coords': [80, 60, 120, 100], 'fill': 'gray', 'outline': 'black'},
                {'type': 'rectangle', 'coords': [90, 100, 110, 140], 'fill': 'silver', 'outline': 'black'},
                {'type': 'rectangle', 'coords': [60, 140, 140, 180], 'fill': 'gray', 'outline': 'black'},
                {'type': 'oval', 'coords': [70, 180, 90, 200], 'fill': 'black', 'outline': 'black'},
                {'type': 'oval', 'coords': [110, 180, 130, 200], 'fill': 'black', 'outline': 'black'},
                {'type': 'rectangle', 'coords': [40, 120, 60, 160], 'fill': 'silver', 'outline': 'black'},
                {'type': 'rectangle', 'coords': [140, 120, 160, 160], 'fill': 'silver', 'outline': 'black'}
            ]
        })
        
        # 10: Дерево (л)
        figures.append({
            'name': 'Дерево',
            'shapes': [
                {'type': 'oval', 'coords': [80, 60, 120, 100], 'fill': 'green', 'outline': 'black'},
                {'type': 'rectangle', 'coords': [95, 100, 105, 140], 'fill': 'brown', 'outline': 'black'}
            ]
        })
        
        # 11: Ракета (м)
        figures.append({
            'name': 'Ракета',
            'shapes': [
                {'type': 'polygon', 'coords': [100, 40, 80, 80, 120, 80], 'fill': 'red', 'outline': 'black'},
                {'type': 'rectangle', 'coords': [85, 80, 115, 140], 'fill': 'blue', 'outline': 'black'},
                {'type': 'polygon', 'coords': [85, 140, 115, 140, 100, 160], 'fill': 'orange', 'outline': 'black'},
                {'type': 'polygon', 'coords': [85, 100, 60, 110, 85, 120], 'fill': 'red', 'outline': 'black'},
                {'type': 'polygon', 'coords': [115, 100, 140, 110, 115, 120], 'fill': 'red', 'outline': 'black'}
            ]
        })
        
        # 12: Воздушный змей (н)
        figures.append({
            'name': 'Воздушный змей',
            'shapes': [
                {'type': 'polygon', 'coords': [100, 60, 60, 100, 100, 140, 140, 100], 'fill': 'purple', 'outline': 'black'},
                {'type': 'line', 'coords': [100, 140, 100, 180], 'fill': 'black', 'width': 2}
            ]
        })
        
        # 13: Смайлик (о)
        figures.append({
            'name': 'Смайлик',
            'shapes': [
                {'type': 'oval', 'coords': [60, 60, 140, 140], 'fill': 'yellow', 'outline': 'black'},
                {'type': 'oval', 'coords': [80, 80, 100, 100], 'fill': 'blue', 'outline': 'black'},
                {'type': 'oval', 'coords': [120, 80, 140, 100], 'fill': 'blue', 'outline': 'black'},
                {'type': 'arc', 'coords': [80, 100, 120, 140], 'fill': 'red', 'outline': 'red', 'start': 180, 'extent': 180}
            ]
        })
        
        # 14: Птица (п) - дополнительная фигура
        figures.append({
            'name': 'Птица',
            'shapes': [
                {'type': 'oval', 'coords': [70, 90, 130, 150], 'fill': 'lightblue', 'outline': 'black'},
                {'type': 'polygon', 'coords': [130, 120, 170, 100, 170, 140], 'fill': 'lightblue', 'outline': 'black'},
                {'type': 'polygon', 'coords': [70, 120, 30, 100, 30, 140], 'fill': 'lightblue', 'outline': 'black'},
                {'type': 'polygon', 'coords': [100, 120, 110, 160, 90, 160], 'fill': 'orange', 'outline': 'black'}
            ]
        })
        
        return figures
    
    def draw_figure(self, x_offset, y_offset, figure_idx):
        """Рисует одну фигуру с заданным смещением"""
        figure = self.figures[figure_idx]
        
        # Подпись
        self.canvas.create_text(x_offset + 100, y_offset - 20, 
                               text=f"{chr(1072 + figure_idx)}) {figure['name']}", 
                               font=('Arial', 12, 'bold'))
        
        # Рисуем все фигуры
        for shape in figure['shapes']:
            coords = [c + (x_offset if i % 2 == 0 else y_offset) 
                     for i, c in enumerate(shape['coords'])]
            
            if shape['type'] == 'ellipse' or shape['type'] == 'oval':
                self.canvas.create_oval(coords, fill=shape['fill'], 
                                       outline=shape.get('outline', 'black'))
            elif shape['type'] == 'rectangle':
                self.canvas.create_rectangle(coords, fill=shape['fill'], 
                                           outline=shape.get('outline', 'black'))
            elif shape['type'] == 'polygon':
                self.canvas.create_polygon(coords, fill=shape['fill'], 
                                         outline=shape.get('outline', 'black'))
            elif shape['type'] == 'line':
                self.canvas.create_line(coords, fill=shape['fill'], 
                                      width=shape.get('width', 1))
            elif shape['type'] == 'arc':
                self.canvas.create_arc(coords, fill=shape['fill'], 
                                     outline=shape.get('outline', 'black'),
                                     start=shape.get('start', 0), 
                                     extent=shape.get('extent', 90))
    
    def draw_all_figures(self):
        """Рисует все 15 фигур в сетке 3x5"""
        for i in range(15):
            row = i // 5
            col = i % 5
            x_offset = col * 240 + 20
            y_offset = row * 260 + 40
            self.draw_figure(x_offset, y_offset, i)

def main():
    root = tk.Tk()
    app = GeometricFigures(root)
    root.mainloop()

if __name__ == "__main__":
    main()
