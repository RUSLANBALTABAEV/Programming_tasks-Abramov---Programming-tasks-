"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
4. Простейшие циклы


105. Даны натуральное число n, действительное число x.
Вычислить:
а) x^n^2 / 2 ^ n;
б) x^n^3 / 3 ^ n.
"""


def main():
    # Ввод натурального числа n и действительного числа x
    n = int(input("Введите натуральное число n: "))
    x = float(input("Введите действительное число x: "))
    
    if n <= 0:
        print("n должно быть натуральным числом")
        return
    
    # Вычисление a) x^(n^2) / 2^n
    # Сначала вычисляем n^2 и n^3
    n2 = n * n
    n3 = n * n * n
    
    # Вычисляем числители и знаменатели
    numerator_a = x ** n2
    denominator_a = 2 ** n
    result_a = numerator_a / denominator_a
    
    # Вычисление б) x^(n^3) / 3^n
    numerator_b = x ** n3
    denominator_b = 3 ** n
    result_b = numerator_b / denominator_b
    
    # Вывод результатов
    print(f"\nРезультаты вычислений:")
    print(f"а) x^(n^2) / 2^n = {x}^{n2} / {2}^{n} = {result_a}")
    print(f"б) x^(n^3) / 3^n = {x}^{n3} / {3}^{n} = {result_b}")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
