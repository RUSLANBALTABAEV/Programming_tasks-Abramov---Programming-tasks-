"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
9. Вычисления с хранением последовательности значений

284. Даны действительные числа a1, …, a20. Получить:
а) a20, a11, a19, a10, …, a10, a1;
б) a1, a3, …, a19, a2, a4, …, a20;
в) a1, a11, a3, a13, …, a9, a19;
г) a12, a2, a14, a4, …, a20, a10;
д) a1, a11, a12, a2, a3, a13, a14, a4, …, a9, a19, a20, a10;
"""


def main():
    # Ввод 20 действительных чисел
    a = []
    for i in range(20):
        while True:
            try:
                value = float(input(f"Введите действительное число a_{i+1}: "))
                a.append(value)
                break
            except ValueError:
                print("Ошибка: введите действительное число (например, 3.14).")

    print(f"\nИсходная последовательность: {a}")

    # а) Поскольку условие неоднозначно, предлагаю два варианта
    # Вариант 1: a20, a11, a19, a10, ..., a12, a3, a11, a2 (20 элементов)
    result_a1 = []
    for i in range(10):
        result_a1.append(a[19 - i])   # a20, a19, ..., a11
        result_a1.append(a[10 + i])   # a11, a12, ..., a20? Нет, это не так.
    
    # Правильнее: берем элементы из второй половины в обратном порядке и из первой половины в обратном порядке
    # Но это не соответствует условию. Давайте сделаем по примеру из обсуждения.
    
    # Я сделаю так: a20, a1, a19, a2, ..., a11, a10
    result_a = []
    for i in range(10):
        result_a.append(a[19 - i])  # a20, a19, ..., a11
        result_a.append(a[i])       # a1, a2, ..., a10
    
    print("\nа) Вариант (a20, a1, a19, a2, ..., a11, a10):")
    print(result_a)

    # б) a1, a3, ..., a19, a2, a4, ..., a20
    result_b = a[0::2] + a[1::2]
    print("\nб) a1, a3, ..., a19, a2, a4, ..., a20:")
    print(result_b)

    # в) a1, a11, a3, a13, ..., a9, a19
    # Берем нечетные из первой половины и нечетные из второй половины
    first_half = a[:10]   # a1..a10
    second_half = a[10:]  # a11..a20
    result_c = []
    for i in range(0, 10, 2):  # индексы 0,2,4,6,8
        result_c.append(first_half[i])   # a1, a3, a5, a7, a9
        result_c.append(second_half[i])  # a11, a13, a15, a17, a19
    print("\nв) a1, a11, a3, a13, ..., a9, a19:")
    print(result_c)

    # г) a12, a2, a14, a4, ..., a20, a10
    # Берем четные из второй половины и четные из первой половины
    result_d = []
    for i in range(1, 10, 2):  # индексы 1,3,5,7,9
        result_d.append(second_half[i])  # a12, a14, a16, a18, a20
        result_d.append(first_half[i])   # a2, a4, a6, a8, a10
    print("\nг) a12, a2, a14, a4, ..., a20, a10:")
    print(result_d)

    # д) a1, a11, a12, a2, a3, a13, a14, a4, ..., a9, a19, a20, a10
    result_e = []
    for i in range(5):
        # Каждый блок из 4 элементов: a(2i+1), a(11+2i), a(12+2i), a(2i+2)
        # для i=0: a1, a11, a12, a2
        # для i=1: a3, a13, a14, a4
        # ...
        # для i=4: a9, a19, a20, a10
        result_e.append(first_half[2*i])      # a1, a3, a5, a7, a9
        result_e.append(second_half[2*i])     # a11, a13, a15, a17, a19
        result_e.append(second_half[2*i+1])   # a12, a14, a16, a18, a20
        result_e.append(first_half[2*i+1])    # a2, a4, a6, a8, a10
    print("\nд) a1, a11, a12, a2, a3, a13, a14, a4, ..., a9, a19, a20, a10:")
    print(result_e)

if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
