"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
4. Простейшие циклы

95. Пусть
a0 = a1 = 1; ai = ai-2 + (ai - 1) / (2 ^ i - 1), i = 2,3,...

Найти произведение a0 * a1 *...*a14.
"""


def main():
    # Инициализация начальных значений
    a0 = 1  # a[0]
    a1 = 1  # a[1]
    
    # Список для хранения всех значений
    a_values = [a0, a1]
    
    # Вычисление последовательности от a2 до a14
    for i in range(2, 15):  # 2, 3, ..., 14
        # Формула: a_i = a_{i-2} + a_{i-1} / (2^(i-1))
        a_current = a_values[i-2] + a_values[i-1] / (2 ** (i-1))
        a_values.append(a_current)
    
    # Вычисление произведения всех элементов
    product = 1
    for value in a_values:
        product *= value
    
    # Вывод результата
    print("Значения последовательности:")
    for i, value in enumerate(a_values):
        print(f"a_{i} = {value}")
    
    print(f"\nПроизведение a0 * a1 * ... * a14 = {product}")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
