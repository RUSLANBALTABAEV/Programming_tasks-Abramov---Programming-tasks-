"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
9. Вычисления с хранением последовательности значений

275. Даны действительные числа x1, …, x10, y1, …, y10. Получить 10Ei=1 * xi*yi. Как упростить решение, если исходные данные будут иметь следующий порядок: x1, y1, …, x10, y10?
"""


def main():
    # Вариант 1: когда данные вводятся как x1...x10, затем y1...y10
    print("Введите 10 чисел x_i:")
    x = []
    for i in range(10):
        while True:
            try:
                val = float(input(f"x_{i+1}: "))
                x.append(val)
                break
            except ValueError:
                print("Ошибка: введите действительное число")

    print("\nВведите 10 чисел y_i:")
    y = []
    for i in range(10):
        while True:
            try:
                val = float(input(f"y_{i+1}: "))
                y.append(val)
                break
            except ValueError:
                print("Ошибка: введите действительное число")

    # Вычисление суммы попарных произведений
    sum_xy = sum(x[i] * y[i] for i in range(10))
    print(f"\nСумма попарных произведений: {sum_xy:.6f}")

    # Вариант 2: когда данные вводятся в порядке x1, y1, x2, y2, ...
    print("\n" + "="*50)
    print("Альтернативный вариант ввода (порядок: x1, y1, x2, y2, ...)")

    sum_xy_alt = 0.0
    for i in range(10):
        while True:
            try:
                x_val = float(input(f"Введите x_{i+1}: "))
                y_val = float(input(f"Введите y_{i+1}: "))
                sum_xy_alt += x_val * y_val
                break
            except ValueError:
                print("Ошибка: введите действительные числа")

    print(f"\nСумма попарных произведений (альтернативный ввод): {sum_xy_alt:.6f}")

    # Сравнение результатов
    if abs(sum_xy - sum_xy_alt) < 1e-10:
        print("Результаты совпадают.")
    else:
        print("Результаты различаются.")

if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
