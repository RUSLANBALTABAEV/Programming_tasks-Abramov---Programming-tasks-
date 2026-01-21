"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
7. Сочетания цикла и разветвления

201.Даны натуральное число n, действительные числа a1, ..., an.
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


# Пример использования
n = 5
a = [1.5, -2.3, 4.7, 0.8, -3.2]

results = compute_sequence_operations(n, a)
for key, value in results.items():
    print(f"{key}: {value}")
