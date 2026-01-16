"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
6. Пошаговый ввод данных и вывод результатов *)

155. Даны натуральное число n, действительные числа x1, ..., xn (n >= 2). Вычислисть
(1 / (abs(x1) + 1) + x ** x) * (1 / (abs(x2) + 1) + x * x * x)...(1 / (abs(xn-1) + 1) + xn).
"""


def main():
    n = int(input("Введите натуральное число n (n >= 2): "))
    
    if n < 2:
        print("Ошибка: n должно быть >= 2")
        return
    
    x = []
    for i in range(n):
        xi = float(input(f"Введите x{i+1}: "))
        x.append(xi)
    
    # Вычисление произведения
    product = 1.0
    for i in range(n-1):
        factor = (1 / (abs(x[i]) + 1)) + x[i+1]
        product *= factor
    
    print(f"\nРезультат: {product:.6f}")

if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
