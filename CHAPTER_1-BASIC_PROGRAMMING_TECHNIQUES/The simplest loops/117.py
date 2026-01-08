"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
4. Простейшие циклы


117. Дано натуральное число n. Вычислить произведение первых n сомножителей:
а) 1 / 2 * 3 / 4 * 5 / 6 *...;
б) 1 / 1 * 3 / 2 * 5 / 3 *...
"""


def main():
    # Ввод натурального числа n
    n = int(input("Введите натуральное число n: "))
    
    if n <= 0:
        print("Ошибка: n должно быть натуральным числом")
        return
    
    print(f"\nВычисление произведений первых {n} сомножителей:\n")
    
    # а) Произведение (1/2) × (3/4) × (5/6) × ...
    product_a = 1.0
    print("а) (1/2) × (3/4) × (5/6) × ... =")
    
    for i in range(1, n + 1):
        numerator = 2 * i - 1  # нечетные числа: 1, 3, 5, ...
        denominator = 2 * i    # четные числа: 2, 4, 6, ...
        product_a *= numerator / denominator
        
        if i <= 5 or i == n:  # Показать первые 5 и последний множитель
            if i == 1:
                print(f"   {numerator}/{denominator}", end="")
            else:
                print(f" × {numerator}/{denominator}", end="")
            if i == n or i == 5:
                print(" ..." if n > 5 else "")
    
    print(f"   = {product_a}")
    
    # б) Произведение (1/1) × (3/2) × (5/3) × ...
    product_b = 1.0
    print(f"\nб) (1/1) × (3/2) × (5/3) × ... =")
    
    for i in range(1, n + 1):
        numerator = 2 * i - 1  # нечетные числа: 1, 3, 5, ...
        denominator = i        # натуральные числа: 1, 2, 3, ...
        product_b *= numerator / denominator
        
        if i <= 5 or i == n:  # Показать первые 5 и последний множитель
            if i == 1:
                print(f"   {numerator}/{denominator}", end="")
            else:
                print(f" × {numerator}/{denominator}", end="")
            if i == n or i == 5:
                print(" ..." if n > 5 else "")
    
    print(f"   = {product_b}")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
