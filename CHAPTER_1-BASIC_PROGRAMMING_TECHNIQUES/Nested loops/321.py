"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
10. Вложенные циклы

321. Даны натуральные числа m, n, действительные числа a1, a2, …, amn. Вычислить a1a2 … am+am+1am+2 … a2m+a(n – 1) m+1a(n – 1) m+2 … anm.
"""


def main():
    # Ввод размерностей
    m = int(input("Введите натуральное число m: "))
    n = int(input("Введите натуральное число n: "))
    
    # Проверка корректности
    if m <= 0 or n <= 0:
        print("Числа должны быть положительными.")
        return
    
    total = m * n
    print(f"Введите {total} действительных чисел через пробел:")
    
    # Ввод списка чисел
    line = input().strip()
    nums = list(map(float, line.split()))
    
    if len(nums) != total:
        print(f"Ошибка: ожидалось {total} чисел, получено {len(nums)}.")
        return
    
    # Вычисление суммы произведений блоков
    result = 0.0
    for i in range(n):               # внешний цикл по блокам
        product = 1.0
        start = i * m                 # начало текущего блока
        for j in range(m):            # внутренний цикл по элементам блока
            product *= nums[start + j]
        result += product
    
    print(f"Результат: {result}")

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
