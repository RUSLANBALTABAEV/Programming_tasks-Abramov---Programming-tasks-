"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
4. Простейшие циклы


116. Даны натуральное число n, действительное число x. Вычислить:
"""


import math

def main():
    n = int(input("Введите n: "))
    x = float(input("Введите x: "))
    
    if n <= 0:
        print("Ошибка: n должно быть натуральным")
        return
    
    # а)
    sum_a, fact, power = 0, 1, 1
    for i in range(1, n+1):
        fact *= i
        power *= x
        sum_a += power/fact
    
    # б)
    sum_b, fact = 0, 1
    root = x ** (1/n)
    for i in range(1, n+1):
        fact *= i
        sum_b += 1/fact
    sum_b += n * root
    
    # в)
    prod_c, fact = 1, 1
    for k in range(1, n+1):
        fact *= k
        prod_c *= 1 + math.sin(k*x)/fact
    
    # г)
    sum_d, pow2 = 0, 0.5
    for i in range(1, n+1):
        sum_d += (x + math.cos(i*x)) * pow2
        pow2 /= 2
    
    # д)
    prod_e, fact = 1, 1
    for k in range(1, n+1):
        prod_e *= ((1-x)**(k+1) + 1) / ((fact + 1)**2)
        fact *= k
    
    print(f"а) {sum_a}")
    print(f"б) {sum_b}")
    print(f"в) {prod_c}")
    print(f"г) {sum_d}")
    print(f"д) {prod_e}")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
