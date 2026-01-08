"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
4. Простейшие циклы


114. Вычислить:
"""


def main():
    print("Вычисление сумм и произведений:\n")
    
    # a) Сумма от i=1 до 100: 1/i^2
    sum_a = 0.0
    for i in range(1, 101):
        sum_a += 1 / (i ** 2)
    print(f"а) Σ(i=1..100) 1/i² = {sum_a}")
    
    # b) Сумма от i=1 до 50: 1/i^3
    sum_b = 0.0
    for i in range(1, 51):
        sum_b += 1 / (i ** 3)
    print(f"б) Σ(i=1..50) 1/i³ = {sum_b}")
    
    # c) Сумма от i=1 до 128: 1/(2i)^2 = 1/(4i^2)
    sum_c = 0.0
    for i in range(1, 129):
        sum_c += 1 / ((2 * i) ** 2)
    print(f"в) Σ(i=1..128) 1/(2i)² = {sum_c}")
    
    # d) Произведение от i=1 до 52: i^2/(i^2 + 2i + 3)
    product_d = 1.0
    for i in range(1, 53):
        product_d *= (i ** 2) / (i ** 2 + 2 * i + 3)
    print(f"г) Π(i=1..52) i²/(i²+2i+3) = {product_d}")
    
    # e) Произведение от i=1 до 10: (2 + 1/i!)
    product_e = 1.0
    factorial = 1  # для накопления факториала
    for i in range(1, 11):
        factorial *= i  # i! = (i-1)! * i
        product_e *= 2 + 1 / factorial
    print(f"д) Π(i=1..10) (2 + 1/i!) = {product_e}")
    
    # x) Произведение от i=2 до 100: (i+1)/(i+2)
    product_x = 1.0
    for i in range(2, 101):
        product_x *= (i + 1) / (i + 2)
    print(f"е) Π(i=2..100) (i+1)/(i+2) = {product_x}")
    
    # 3) Произведение от i=2 до 10: (1 - 1/i!)^2
    product_3 = 1.0
    factorial = 1  # сбрасываем факториал
    for i in range(1, 11):
        factorial *= i  # i!
        if i >= 2:  # начиная с i=2
            product_3 *= (1 - 1 / factorial) ** 2
    print(f"ж) Π(i=2..10) (1 - 1/i!)² = {product_3}")
    
    # Дополнительно: вычисление всех результатов одной функцией
    print("\n" + "="*50)
    print("Все результаты вычислены!")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
