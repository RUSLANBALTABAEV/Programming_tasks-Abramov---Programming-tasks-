"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
3. Простейшая целочисленная арифметика
75. Доказать, что любую целочисленную денежную сумму,
большую 7 руб., можно выплатить без сдачи трешками и пятерками.
Для данного n > 7 найти такие целые неотрицательные a и b, что 3a + 5b = n.
"""

# ==================== ПОИСК РЕШЕНИЯ ====================

def find_coin_combination(n):
    """
    Находит такие неотрицательные целые a и b, что 3a + 5b = n.
    Возвращает (a, b) или None, если решения нет.
    """
    for a in range(n // 3 + 1):
        remainder = n - 3 * a
        if remainder >= 0 and remainder % 5 == 0:
            b = remainder // 5
            return a, b
    return None


def explain_combination(n):
    """Объясняет решение для конкретной суммы n."""
    result = find_coin_combination(n)
    
    if result:
        a, b = result
        print(f"n = {n}:")
        print(f"  {a} трёшек + {b} пятёрок = {3*a} + {5*b} = {3*a + 5*b} ✓")
        print(f"  Остаток при делении на 3: {n % 3}")
        return True
    else:
        print(f"n = {n}: решения нет ✗")
        return False


# ==================== ВВОД ДАННЫХ ====================

print("Введите сумму n (должна быть > 7):")
n = int(input("n = "))

print(f"\n{'='*60}")
print(f"Поиск решения для суммы: {n} рублей")
print(f"{'='*60}\n")

if n <= 7:
    print("Ошибка: сумма должна быть больше 7.")
else:
    result = find_coin_combination(n)
    if result:
        a, b = result
        print("Решение найдено!")
        print(f"Трёшек (a): {a}")
        print(f"Пятёрок (b): {b}")
        print(f"\nПроверка: 3 × {a} + 5 × {b} = {3*a} + {5*b} = {3*a + 5*b} ✓")
    else:
        print("Решение не найдено (что невозможно для n > 7).")


# ==================== ДОКАЗАТЕЛЬСТВО ====================

print(f"\n{'='*60}")
print("--- Доказательство для всех n > 7 ---")
print(f"{'='*60}\n")

print("Рассмотрим остатки при делении n на 3:\n")

# Остаток 0
print("Случай 1: n ≡ 0 (mod 3)")
print("  Пример: n = 9, 12, 15, 18, ...")
print("  Решение: только трёшки (b = 0)")
print("  9 = 3×3 + 5×0")
print("  12 = 3×4 + 5×0")
print("  15 = 3×5 + 5×0\n")

# Остаток 1
print("Случай 2: n ≡ 1 (mod 3)")
print("  Пример: n = 8, 11, 14, 17, ...")
print("  Решение: одна пятёрка + несколько трёшек")
print("  8 = 3×1 + 5×1")
print("  11 = 3×2 + 5×1")
print("  14 = 3×3 + 5×1\n")

# Остаток 2
print("Случай 3: n ≡ 2 (mod 3)")
print("  Пример: n = 10, 13, 16, 19, ...")
print("  Решение: две пятёрки + несколько трёшек")
print("  10 = 3×0 + 5×2")
print("  13 = 3×1 + 5×2")
print("  16 = 3×2 + 5×2\n")


# ==================== ПРОВЕРКА ВСЕХ n ДО 100 ====================

print(f"{'='*60}")
print("--- Проверка для всех n от 8 до 100 ---")
print(f"{'='*60}\n")

all_solvable = True
for test_n in range(8, 101):
    result = find_coin_combination(test_n)
    if not result:
        print(f"ОШИБКА: n = {test_n} не имеет решения!")
        all_solvable = False

if all_solvable:
    print("✓ Подтверждено: все суммы от 8 до 100 рублей можно выплатить!\n")


# ==================== ТАБЛИЦА РЕШЕНИЙ ====================

print("Таблица решений для n от 8 до 25:")
print(f"{'n':>3} | {'a (трёшки)':>11} | {'b (пятёрки)':>12} | {'Проверка':>12} | {'Остаток mod 3':>14}")
print("-" * 70)

for test_n in range(8, 26):
    a, b = find_coin_combination(test_n)
    check = 3*a + 5*b
    remainder = test_n % 3
    print(f"{test_n:3d} | {a:11d} | {b:12d} | {check:12d} | {remainder:14d}")


# ==================== ПАТТЕРНЫ РЕШЕНИЙ ====================

print(f"\n{'='*60}")
print("--- Паттерны решений ---\n")

print("Остаток 0 (mod 3): n = 9, 12, 15, 18, 21, 24, ...")
combinations_0 = [(n, *find_coin_combination(n)) for n in range(9, 26, 3)]
for n, a, b in combinations_0:
    print(f"  n = {n:2d}: a = {a:2d}, b = {b:2d}")

print("\nОстаток 1 (mod 3): n = 8, 11, 14, 17, 20, 23, ...")
combinations_1 = [(n, *find_coin_combination(n)) for n in range(8, 26, 3)]
for n, a, b in combinations_1:
    print(f"  n = {n:2d}: a = {a:2d}, b = {b:2d}")

print("\nОстаток 2 (mod 3): n = 10, 13, 16, 19, 22, 25, ...")
combinations_2 = [(n, *find_coin_combination(n)) for n in range(10, 26, 3)]
for n, a, b in combinations_2:
    print(f"  n = {n:2d}: a = {a:2d}, b = {b:2d}")

input("\nНажмите Enter, чтобы завершить программу.")
