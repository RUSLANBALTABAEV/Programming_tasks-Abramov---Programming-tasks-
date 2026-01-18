"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
6. Пошаговый ввод данных и вывод результатов *)

168. Даны натуральное число n, действительные числа a1, …, an (n >= 6). Получить:
а) a6, a7, ..., an;
б) a6, a7, ..., an, a1;
в) a6, a7, ..., an, a5;
"""


def main():
    # Ввод натурального числа n с проверкой условия n >= 6
    while True:
        n = int(input("Введите натуральное число n (n >= 6): "))
        if n >= 6:
            break
        print("Ошибка: n должно быть >= 6!")
    
    # Ввод действительных чисел
    a = []
    print(f"Введите {n} действительных чисел:")
    for i in range(n):
        a_i = float(input(f"a[{i+1}]: "))
        a.append(a_i)
    
    # а) a6, a7, ..., an
    print("\nа) a6, a7, ..., an:")
    result_a = []
    for i in range(5, n):  # Индексы 5..n-1 соответствуют a6..an
        result_a.append(a[i])
        print(f"  a[{i+1}] = {a[i]:.6f}")
    
    # б) a6, a7, ..., an, a1
    print("\nб) a6, a7, ..., an, a1:")
    result_b = []
    # Сначала добавляем a6..an
    for i in range(5, n):
        result_b.append(a[i])
        print(f"  a[{i+1}] = {a[i]:.6f}")
    # Затем добавляем a1
    result_b.append(a[0])
    print(f"  a[1] = {a[0]:.6f}")
    
    # в) a6, a7, ..., an, a5
    print("\nв) a6, a7, ..., an, a5:")
    result_c = []
    # Сначала добавляем a6..an
    for i in range(5, n):
        result_c.append(a[i])
        print(f"  a[{i+1}] = {a[i]:.6f}")
    # Затем добавляем a5
    result_c.append(a[4])
    print(f"  a[5] = {a[4]:.6f}")
    
    # Дополнительно выводим результаты в виде списков для наглядности
    print("\nРезультаты в виде списков:")
    print(f"а) {[f'{x:.6f}' for x in result_a]}")
    print(f"б) {[f'{x:.6f}' for x in result_b]}")
    print(f"в) {[f'{x:.6f}' for x in result_c]}")

if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
