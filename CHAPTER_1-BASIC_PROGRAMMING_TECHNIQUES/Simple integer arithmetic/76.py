"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
3. Простейшая целочисленная арифметика

76. Поле шахматной доски определяется парой натуральных чисел,
каждое из которых не превосходит восьми: первое число – номер вертикали
(при счете слева направо), второе – номер горизонтали (при счете снизу вверх).
Даны натуральные числа k, l, m, n, каждое из которых не превосходит восьми.

Требуется:
а) выяснить, являются ли поля (k, l) и (m, n) полями одного цвета;
б) если на (k, l) стоит ферзь — угрожает ли он (m, n);
в) аналогично, но для коня;
г) выяснить, можно ли с поля (k, l) одним ходом ладьи попасть на (m, n);
   если нет — за два хода (указать промежуточное поле);
д) аналогично г), но для ферзя;
е) аналогично г), но для слона.

Предполагается, что указанные поля имеют один и тот же цвет.
"""


def same_color(k, l, m, n):
    """а) Проверка: поля одного цвета, если (k + l) и (m + n) одинаковой чётности."""
    return (k + l) % 2 == (m + n) % 2


def queen_threatens(k, l, m, n):
    """б) Ферзь угрожает по вертикали, горизонтали или диагонали."""
    return k == m or l == n or abs(k - m) == abs(l - n)


def knight_threatens(k, l, m, n):
    """в) Конь угрожает, если ходит буквой Г: (±1, ±2) или (±2, ±1)."""
    dk, dl = abs(k - m), abs(l - n)
    return (dk, dl) in [(1, 2), (2, 1)]


def rook_path(k, l, m, n):
    """г) Ладья: проверка одного и двух ходов."""
    if k == m or l == n:
        return True, None  # одним ходом
    return False, (k, n)  # через промежуточное поле (та же строка/столбец)


def bishop_path(k, l, m, n):
    """е) Слон: проверка одного и двух ходов."""
    # Одним ходом
    if abs(k - m) == abs(l - n):
        return True, None

    # Разные цвета → невозможно
    if not same_color(k, l, m, n):
        return False, None

    # Двумя ходами (по диагоналям одного цвета)
    for x in range(1, 9):
        for y in range(1, 9):
            if abs(k - x) == abs(l - y) and abs(m - x) == abs(n - y):
                return False, (x, y)
    return False, None


def queen_path(k, l, m, n):
    """д) Ферзь: комбинация ладьи и слона."""
    if queen_threatens(k, l, m, n):
        return True, None

    # Если не одним ходом — попробуем промежуточное поле
    for x in range(1, 9):
        for y in range(1, 9):
            if queen_threatens(k, l, x, y) and queen_threatens(x, y, m, n):
                return False, (x, y)
    return False, None


# ==================== Ввод данных ====================

print("Введите координаты первого поля (k, l):")
k = int(input("k (вертикаль, 1–8): "))
l = int(input("l (горизонталь, 1–8): "))

print("\nВведите координаты второго поля (m, n):")
m = int(input("m (вертикаль, 1–8): "))
n = int(input("n (горизонталь, 1–8): "))

if not (1 <= k <= 8 and 1 <= l <= 8 and 1 <= m <= 8 and 1 <= n <= 8):
    print("Ошибка: координаты должны быть от 1 до 8!")
else:
    print(f"\n{'='*60}")
    print(f"Анализ полей ({k}, {l}) и ({m}, {n})")
    print(f"{'='*60}\n")

    # а)
    same = same_color(k, l, m, n)
    print(f"а) Поля одного цвета: {'ДА' if same else 'НЕТ'}")

    # б)
    print(f"\nб) Ферзь угрожает: {'ДА' if queen_threatens(k, l, m, n) else 'НЕТ'}")

    # в)
    print(f"\nв) Конь угрожает: {'ДА' if knight_threatens(k, l, m, n) else 'НЕТ'}")

    # г)
    one, inter = rook_path(k, l, m, n)
    print(f"\nг) Ладья может попасть за один ход: {'ДА' if one else 'НЕТ'}")
    if not one:
        print(f"   За два хода через поле: {inter}")

    # д)
    one, inter = queen_path(k, l, m, n)
    print(f"\nд) Ферзь может попасть за один ход: {'ДА' if one else 'НЕТ'}")
    if not one and inter:
        print(f"   За два хода через поле: {inter}")

    # е)
    one, inter = bishop_path(k, l, m, n)
    print(f"\nе) Слон может попасть за один ход: {'ДА' if one else 'НЕТ'}")
    if not one and inter:
        print(f"   За два хода через поле: {inter}")
    elif not one and not inter:
        print("   Слон не может попасть (поля разного цвета)")

# ==================== Визуализация доски ====================

print(f"\n{'='*60}")
print("--- Визуализация доски ---\n")
print("Цвета полей (Б=белое, Ч=чёрное):")
print("  ", end="")
for col in range(1, 9):
    print(f"{col} ", end="")
print()

for row in range(8, 0, -1):
    print(f"{row} ", end="")
    for col in range(1, 9):
        if (col, row) == (k, l):
            print("K ", end="")  # первое поле
        elif (col, row) == (m, n):
            print("M ", end="")  # второе поле
        else:
            color = "Б" if (col + row) % 2 == 0 else "Ч"
            print(f"{color} ", end="")
    print()

print("\nK = поле (k, l)")
print("M = поле (m, n)")

input("\nНажмите Enter, чтобы завершить программу.")
