"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
3. Простейшая целочисленная арифметика
65. Дано натуральное число n (n>99). Выяснить, верно ли, что n ** 2
равно кубу суммы цифр числа n.
"""


# Ввод данных
n = int(input("Введите натуральное число (n > 99): "))

# Проверка условия
if n <= 99:
    print("Ошибка: число должно быть больше 99")
else:
    # Вычисление суммы цифр
    digit_sum = sum(int(digit) for digit in str(n))
    
    # Вычисление n²
    n_squared = n ** 2
    
    # Вычисление куба суммы цифр
    digits_cube = digit_sum ** 3
    
    # Вывод результатов
    print(f"\nЧисло: n = {n}")
    print(f"Сумма цифр: {' + '.join(str(n))} = {digit_sum}")
    print(f"\nn² = {n}² = {n_squared}")
    print(f"(сумма цифр)³ = {digit_sum}³ = {digits_cube}")
    
    # Проверка условия
    if n_squared == digits_cube:
        print(f"\n✓ ВЕРНО: {n_squared} = {digits_cube}")
    else:
        print(f"\n✗ НЕВЕРНО: {n_squared} ≠ {digits_cube}")


# Функция для переиспользования
def check_condition(num):
    """Проверяет, верно ли, что num² = (сумма цифр)³"""
    if num <= 99:
        return None
    
    digit_sum = sum(int(digit) for digit in str(num))
    n_squared = num ** 2
    digits_cube = digit_sum ** 3
    
    return n_squared == digits_cube


# Поиск чисел, для которых условие верно
print("\n" + "="*50)
print("--- Поиск чисел, где n² = (сумма цифр)³ ---")
print("Проверка чисел от 100 до 1000:\n")

found = False
for num in range(100, 1001):
    if check_condition(num):
        digit_sum = sum(int(digit) for digit in str(num))
        print(f"n = {num} → сумма цифр = {digit_sum}")
        print(f"  {num}² = {num**2}, {digit_sum}³ = {digit_sum**3} ✓")
        found = True

if not found:
    print("Таких чисел в диапазоне [100, 1000] не найдено")

input("\nНажмите Enter, чтобы завершить программу.")
