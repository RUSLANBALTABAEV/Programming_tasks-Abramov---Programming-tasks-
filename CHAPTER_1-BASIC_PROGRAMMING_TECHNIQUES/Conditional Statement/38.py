"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
2. Разветвления
38. Даны действительные числа x, y. Вычислить z:
z = x - y, если x > y,
z = y - x + 1, в противном случае.
"""

def calculate_z(x, y):
    """
    Вычисляет значение z по заданной формуле.
    
    Args:
        x (float): Первое число
        y (float): Второе число
    
    Returns:
        float: Вычисленное значение z
    """
    if x > y:
        return x - y
    else:
        return y - x + 1


def main():
    """Основная функция программы."""
    print("Вычисление z по формуле")
    print("-" * 50)
    
    try:
        # Ввод данных
        x = float(input("Введите число x: "))
        y = float(input("Введите число y: "))
        
        # Вычисление z
        z = calculate_z(x, y)
        
        # Вывод результата
        print("-" * 50)
        print(f"x = {x}, y = {y}")
        
        if x > y:
            print("Условие x > y выполняется ✅")
            print(f"z = x - y = {x} - {y} = {z}")
        else:
            print("Условие x > y не выполняется ❌")
            print(f"z = y - x + 1 = {y} - {x} + 1 = {z}")
        
    except ValueError:
        print("Ошибка: необходимо вводить числа!")

    input("\nНажмите Enter, чтобы завершить программу.")


if __name__ == "__main__":
    main()
