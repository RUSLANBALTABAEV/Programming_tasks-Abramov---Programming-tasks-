"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
4. Простейшие циклы


115. Дано натуральное число n. Вычислить:

"""


def main():
    # Ввод натурального числа n
    n = int(input("Введите натуральное число n: "))
    
    if n <= 0:
        print("Ошибка: n должно быть натуральным числом")
        return
    
    print(f"\nВычисления для n = {n}:\n")
    
    # а) Сумма от k=1 до n: 1/k
    sum_a = 0.0
    for k in range(1, n + 1):
        sum_a += 1 / k
    print(f"а) Σ(k=1..{n}) 1/k = {sum_a}")
    
    # б) Сумма от k=1 до n: 1/k^5
    sum_b = 0.0
    for k in range(1, n + 1):
        sum_b += 1 / (k ** 5)
    print(f"б) Σ(k=1..{n}) 1/k⁵ = {sum_b}")
    
    # в) Сумма от k=1 до n: 1/(2k+1)^2
    sum_c = 0.0
    for k in range(1, n + 1):
        sum_c += 1 / ((2 * k + 1) ** 2)
    print(f"в) Σ(k=1..{n}) 1/(2k+1)² = {sum_c}")
    
    # г) Сумма от k=1 до n: (-1)^k / ((2k+1)*k)
    sum_d = 0.0
    for k in range(1, n + 1):
        sign = 1 if k % 2 == 0 else -1  # (-1)^k
        sum_d += sign / ((2 * k + 1) * k)
    print(f"г) Σ(k=1..{n}) (-1)ᵏ/((2k+1)k) = {sum_d}")
    
    # д) Сумма от k=1 до n: (-1)^(k+1) / (k*(k+1))
    sum_e = 0.0
    for k in range(1, n + 1):
        sign = 1 if (k + 1) % 2 == 0 else -1  # (-1)^(k+1)
        sum_e += sign / (k * (k + 1))
    print(f"д) Σ(k=1..{n}) (-1)ᵏ⁺¹/(k(k+1)) = {sum_e}")
    
    # е) Сумма от k=0 до n: (-1)^k * (k+1) / k!
    sum_f = 0.0
    factorial = 1  # 0! = 1
    for k in range(0, n + 1):
        if k > 0:
            factorial *= k  # k! = (k-1)! * k
        sign = 1 if k % 2 == 0 else -1  # (-1)^k
        sum_f += sign * (k + 1) / factorial
    print(f"е) Σ(k=0..{n}) (-1)ᵏ*(k+1)/k! = {sum_f}")
    
    # ж) Сумма от k=1 до n: k! / (1/2 + 1/3 + ... + 1/(k+1))
    sum_g = 0.0
    factorial = 1  # для k!
    harmonic_sum = 0.0  # для накопления суммы 1/2 + 1/3 + ... + 1/(k+1)
    
    for k in range(1, n + 1):
        factorial *= k  # k! = (k-1)! * k
        harmonic_sum += 1 / (k + 1)  # добавляем следующий член: 1/(k+1)
        sum_g += factorial / harmonic_sum
    print(f"ж) Σ(k=1..{n}) k!/(1/2+1/3+...+1/(k+1)) = {sum_g}")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
