"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
7. Сочетания цикла и разветвления

207. Дано натуральное число n. Выбросить из записи числа n
цифры 0 и 5, оставив прежним порядок остальных цифр. Например, из
числа 59015509 должно получиться 919.
"""


def remove_zero_and_five_detailed(n):
    """
    Удаляет цифры 0 и 5 с подробным выводом каждого шага.
    """
    print(f"Исходное число: {n}")
    
    # Разбиваем число на цифры
    digits = [int(d) for d in str(n)]
    print(f"Цифры числа: {digits}")
    
    # Фильтруем цифры, удаляя 0 и 5
    filtered_digits = [d for d in digits if d not in (0, 5)]
    print(f"Цифры после удаления 0 и 5: {filtered_digits}")
    
    # Собираем число из оставшихся цифр
    if not filtered_digits:
        result = 0
    else:
        result = int(''.join(str(d) for d in filtered_digits))
    
    print(f"Результат: {result}")
    print("-" * 40)
    
    return result


# Демонстрация работы функции с подробным выводом
print("Детальное выполнение для нескольких чисел:")
for num in [59015509, 1050, 555, 123]:
    remove_zero_and_five_detailed(num)
