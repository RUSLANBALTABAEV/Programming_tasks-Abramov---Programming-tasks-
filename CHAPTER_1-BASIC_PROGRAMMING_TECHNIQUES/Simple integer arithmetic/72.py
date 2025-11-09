"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
3. Простейшая целочисленная арифметика
72. Дано действительное число а. Вычислить f(a), где f –
периодическая функция с периодом 2, совпадающая на отрезке [–1,1]:
а) с функцией x ** 2 + 1;
б) с функцией, график которой изображен на рис. 5.
"""

# ==================== ЧАСТЬ a) ====================
def f_a(x):
    """Функция f(x) = x² + 1 на отрезке [-1, 1]"""
    return x**2 + 1


def calculate_f_a(a):
    """
    Вычисляет f(a) для периодической функции с периодом 2
    Использует свойство: f(a) = f(a_приведенное)
    где a_приведенное ∈ [-1, 1)
    """
    period = 2
    x = a % period
    if x >= 1:
        x -= period
    return f_a(x), x


# ==================== ЧАСТЬ б) ====================
def f_b(x):
    """
    Функция f(x), заданная графиком на рис. 5.
    По описанию — кубическая форма, симметричная около 0:
    f(x) = 1 - x³ на [-1, 1]
    """
    period = 2
    x = x % period
    if x >= 1:
        x -= period
    return 1 - x**3


def calculate_f_b(a):
    """Вычисляет f(a) для периодической функции б) с периодом 2"""
    period = 2
    x = a % period
    if x >= 1:
        x -= period
    return f_b(x), x


# ==================== ВВОД И ВЫВОД ====================
print("Введите значение a:")
a = float(input("a = "))

print(f"\n{'='*60}")
print(f"Вычисление периодической функции f(a) с периодом T = 2")
print(f"Основной отрезок: [-1, 1]")
print(f"{'='*60}")

# Часть a)
print(f"\na) f(x) = x² + 1 на [-1, 1]")
result_a, x_a = calculate_f_a(a)
print(f"   a = {a}")
print(f"   a приведённое к [-1, 1): {x_a:.4f}")
print(f"   f({a}) = f({x_a:.4f}) = {result_a:.4f}")

# Часть б)
print(f"\nб) f(x) = 1 - x³ (из графика рис. 5)")
result_b, x_b = calculate_f_b(a)
print(f"   a = {a}")
print(f"   a приведённое к [-1, 1): {x_b:.4f}")
print(f"   f({a}) = f({x_b:.4f}) = {result_b:.4f}")


# ==================== ПРИМЕРЫ ====================
print(f"\n{'='*60}")
print("--- Примеры вычислений ---\n")

test_values = [-1, -0.5, 0, 0.5, 1, 2, 3, -2, -3, 2.5]

print("Часть a) f(x) = x² + 1:")
print(f"{'a':>8} | {'приведённое':>12} | {'f(a)':>10}")
print("-" * 40)
for val in test_values:
    result, x = calculate_f_a(val)
    print(f"{val:8.2f} | {x:12.4f} | {result:10.4f}")

print("\n" + "="*60)
print("Часть б) f(x) = 1 - x³ (из графика):")
print(f"{'a':>8} | {'приведённое':>12} | {'f(a)':>10}")
print("-" * 40)
for val in test_values:
    result, x = calculate_f_b(val)
    print(f"{val:8.2f} | {x:12.4f} | {result:10.4f}")


# ==================== ТЕКСТОВЫЕ ГРАФИКИ ====================
print(f"\n{'='*60}")
print("--- Графики на основном периоде [-1, 1] ---\n")

# График а)
print("График а) f(x) = x² + 1:")
print("x\t\tf(x) = x² + 1\t\tВизуализация")
print("-" * 60)
for i in range(21):
    x = -1 + i * 2 / 20
    y = f_a(x)
    scaled = int((y - 1) * 10)  # y от 1 до 2
    bar = "█" * scaled
    print(f"{x:6.2f}\t\t{y:7.3f}\t\t{bar}")

print("\n" + "="*60)
print("График б) f(x) = 1 - x³:")
print("x\t\tf(x) = 1 - x³\t\tВизуализация")
print("-" * 60)
for i in range(21):
    x = -1 + i * 2 / 20
    y = f_b(x)
    scaled = int((y + 1) * 10)
    bar = "█" * scaled
    print(f"{x:6.2f}\t\t{y:7.3f}\t\t{bar}")


# ==================== ПРОВЕРКА ПЕРИОДИЧНОСТИ ====================
print(f"\n{'='*60}")
print("--- Проверка периодичности ---\n")

test_a = 0.3
print(f"Проверка: f(a) = f(a + период) = f(a - период)")
print(f"Пусть a = {test_a}")

result_curr = calculate_f_a(test_a)[0]
result_plus = calculate_f_a(test_a + 2)[0]
result_minus = calculate_f_a(test_a - 2)[0]

print(f"\nЧасть a):")
print(f"  f({test_a}) = {result_curr:.6f}")
print(f"  f({test_a} + 2) = {result_plus:.6f}")
print(f"  f({test_a} - 2) = {result_minus:.6f}")
print(f"  Все значения равны: {abs(result_curr - result_plus) < 0.0001 and abs(result_curr - result_minus) < 0.0001}")

result_curr_b = calculate_f_b(test_a)[0]
result_plus_b = calculate_f_b(test_a + 2)[0]
result_minus_b = calculate_f_b(test_a - 2)[0]

print(f"\nЧасть б):")
print(f"  f({test_a}) = {result_curr_b:.6f}")
print(f"  f({test_a} + 2) = {result_plus_b:.6f}")
print(f"  f({test_a} - 2) = {result_minus_b:.6f}")
print(f"  Все значения равны: {abs(result_curr_b - result_plus_b) < 0.0001 and abs(result_curr_b - result_minus_b) < 0.0001}")

input("\nНажмите Enter, чтобы завершить программу.")
