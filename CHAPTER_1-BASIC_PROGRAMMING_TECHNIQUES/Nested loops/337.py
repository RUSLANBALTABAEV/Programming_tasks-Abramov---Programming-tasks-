"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
10. Вложенные циклы

337. Даны действительные числа a,b ...(a < b), натуральное число n , функция y = f(x) определенная на отрезке [a,b]. Вывести на печатающее устройство график функции. Для построения графика вычислить значения функции yi = f(xi), где
xi = a + i * h, i = 0,1, ...., n, h = (b - a) / n,
Ось Ox расположить вертикально, ось Oy - горизонтально. Шаг по оси Ox – это переход на новую строку, шаг по оси Oy –позиция следующего символа в текущей строке. 
Точки графика изображать символом *.
Рассмотреть следующие функции:
а) y = abs(sin(x)) + cos(x), a = 0, b = pi, n = 40;
б) y = 2 * sin(x) + 3 * cos(x), a = -pi, b = pi, n = 50;
в) y = sqrt(x * x * x * x + 1), a = -1, b = 2, n = 30;
г) y = 1 / (x * x - x + 1), a = -1, b = 3, n = 40;
д) y = (x - 3) / (x * x + 2), a = -1, b = 4, n = 50;
е) exp = x * x * exp(-abs(x)), a = -1, b = 3, n = 40;
ж) y = exp(-x) * sin(2 * x), a = -pi / 2, b = 2 * pi, n = 50;
з) pow(sqrt((x + 2) * (x + 2)) - sqrt((x - 2) * (x - 2)),1./3), a = -3, b = 3, n = 50.
"""


import math

# Определения функций
def f_a(x):
    return abs(math.sin(x)) + math.cos(abs(x))

def f_b(x):
    return 2 * math.sin(x) + 3 * math.cos(x)

def f_c(x):
    return math.sqrt(x**4 + 1)

def f_d(x):
    return 1 / (x**2 - x + 1)

def f_e(x):
    return (x - 3) / (x**2 + 2)

def f_f(x):
    return x**2 * math.exp(-abs(x))

def f_g(x):
    return math.exp(-x) * math.sin(2 * x)

def f_h(x):
    return math.sqrt((x + 2)**2) - math.sqrt((x - 2)**2)

def plot_function(f, a, b, n, width=60):
    """Выводит текстовый график функции f на отрезке [a,b] с n шагами."""
    h = (b - a) / n
    x_vals = [a + i * h for i in range(n + 1)]
    y_vals = [f(x) for x in x_vals]

    y_min = min(y_vals)
    y_max = max(y_vals)
    if y_max - y_min == 0:
        positions = [width // 2] * len(y_vals)
    else:
        positions = [int((y - y_min) / (y_max - y_min) * (width - 1)) for y in y_vals]

    print(f"\nГрафик функции на [{a:.3f}, {b:.3f}], n = {n}")
    print(f"Диапазон y: [{y_min:.3f}, {y_max:.3f}]\n")
    for x, p in zip(x_vals, positions):
        line = ' ' * p + '*'
        print(f"{x:6.3f}: {line}")

def main():
    print("Выберите функцию для построения графика:")
    print("а) y = |sin x| + cos|x|,       a=0,       b=π,   n=40")
    print("б) y = 2 sin x + 3 cos x,      a=-π,     b=π,   n=50")
    print("в) y = sqrt(x⁴+1),              a=-1,     b=2,   n=30")
    print("г) y = 1/(x² - x + 1),          a=-1,     b=3,   n=40")
    print("д) y = (x-3)/(x²+2),            a=-1,     b=4,   n=50")
    print("е) y = x² e^{-|x|},              a=-1,     b=3,   n=40")
    print("ж) y = e^{-x} sin 2x,            a=-π/2,   b=2π,  n=50")
    print("з) y = √((x+2)²) - √((x-2)²),  a=-3,     b=3,   n=50")
    choice = input("\nВведите букву (а-з): ").strip().lower()

    if choice == 'а' or choice == 'a':
        plot_function(f_a, 0, math.pi, 40)
    elif choice == 'б' or choice == 'b':
        plot_function(f_b, -math.pi, math.pi, 50)
    elif choice == 'в' or choice == 'v':
        plot_function(f_c, -1, 2, 30)
    elif choice == 'г' or choice == 'g':
        plot_function(f_d, -1, 3, 40)
    elif choice == 'д' or choice == 'd':
        plot_function(f_e, -1, 4, 50)
    elif choice == 'е' or choice == 'e':
        plot_function(f_f, -1, 3, 40)
    elif choice == 'ж' or choice == 'j':
        plot_function(f_g, -math.pi/2, 2*math.pi, 50)
    elif choice == 'з' or choice == 'z':
        plot_function(f_h, -3, 3, 50)
    else:
        print("Неверный выбор.")

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
