"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
7. Сочетания цикла и разветвления

201. Даны натуральное число n, действительные числа a1, ..., an.
Получить:
а) max(a1, ..., an);
б) min(a1, ..., an);
в) max(a2,a4, ...);
г) min(a1,a3, ...);
д) min(a2,a4, ...)+ max(a1,a3, ...);
е) max(|a1|, ..., |an|);
ж) max(-a1,a2,-a3, ..., (-1)^n*an);
з) (min(a1, ..., an))^2 - min(a1^2, ..., an^2).
"""

def compute_sequence_operations(n, a):
    """
    n: натуральное число (длина последовательности)
    a: список действительных чисел [a₁, a₂, ..., aₙ]
    Возвращает все искомые значения (a) — (з).
    """
    # a) Максимум всех элементов
    max_all = max(a)
    
    # b) Минимум всех элементов
    min_all = min(a)
    
    # c) Максимум элементов с чётными индексами (a₂, a₄, ...)
    # Индексация в Python с 0, поэтому чётные позиции (2,4,...) → индексы 1,3,...
    even_indices = [a[i] for i in range(1, n, 2)]  # начинаем с 1, шаг 2
    max_even = max(even_indices) if even_indices else None
    
    # d) Минимум элементов с нечётными индексами (a₁, a₃, ...)
    odd_indices = [a[i] for i in range(0, n, 2)]   # начинаем с 0, шаг 2
    min_odd = min(odd_indices) if odd_indices else None
    
    # e) min(a₂, a₄, ...) + max(a₁, a₃, ...)
    min_even = min(even_indices) if even_indices else None
    max_odd = max(odd_indices) if odd_indices else None
    sum_min_even_max_odd = (min_even + max_odd) if (min_even is not None and max_odd is not None) else None
    
    # f) Максимум модулей элементов
    max_abs = max(abs(x) for x in a)
    
    # g) Максимум последовательности (-a₁, a₂, -a₃, ...)
    alternating = [(-1)**(i+1) * a[i] for i in range(n)]  # (-1)^(i+1) даёт чередование знаков
    max_alternating = max(alternating)
    
    # з) (min(a₁, ..., aₙ))² - min(a₁², ..., aₙ²)
    min_squared = min_all ** 2
    min_of_squares = min(x**2 for x in a)
    difference = min_squared - min_of_squares

    return {
        "a) max(a₁,...,aₙ)": max_all,
        "б) min(a₁,...,aₙ)": min_all,
        "в) max(a₂,a₄,...)": max_even,
        "г) min(a₁,a₃,...)": min_odd,
        "д) min(a₂,a₄,...)+max(a₁,a₃,...)": sum_min_even_max_odd,
        "е) max(|a₁|,...,|aₙ|)": max_abs,
        "ж) max(-a₁, a₂, -a₃, ...)": max_alternating,
        "з) (min)² - min(a₁²,...,aₙ²)": difference
    }


def main():
    """
    Основная функция программы с выбором режима работы:
    1. Использовать пример из кода
    2. Ввести свои данные
    """
    print("Программа для вычисления различных характеристик последовательности чисел")
    print("=" * 60)
    
    choice = input("Выберите режим:\n1 - Использовать пример из кода\n2 - Ввести свои данные\nВведите 1 или 2: ")
    
    if choice == '1':
        # Используем пример из кода
        n = 5
        a = [1.5, -2.3, 4.7, 0.8, -3.2]
        print(f"\nИспользуется пример: n = {n}, a = {a}")
    elif choice == '2':
        # Ввод данных от пользователя
        try:
            n = int(input("\nВведите натуральное число n: "))
            if n <= 0:
                print("Ошибка: n должно быть натуральным числом!")
                return
            
            a = []
            for i in range(n):
                value = float(input(f"Введите a_{i+1}: "))
                a.append(value)
            print(f"\nВведена последовательность: a = {a}")
        except ValueError:
            print("Ошибка ввода! Убедитесь, что вводите числа в правильном формате.")
            return
    else:
        print("Неверный выбор. Программа завершена.")
        return
    
    # Вычисление результатов
    results = compute_sequence_operations(n, a)
    
    # Вывод результатов
    print("\nРезультаты вычислений:")
    print("-" * 40)
    for key, value in results.items():
        if value is not None:
            print(f"{key}: {value}")
        else:
            print(f"{key}: Недостаточно данных для вычисления")
    
    print("=" * 60)


if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
