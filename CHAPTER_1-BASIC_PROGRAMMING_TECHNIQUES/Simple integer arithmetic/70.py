"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
3. Простейшая целочисленная арифметика
70. Даны целые числа m, n (0 < m ≤ 12, 0 ≤ n < 60),
указывающие момент времени: «m часов, n минут».
Определить:
а) через сколько минут стрелки совпадут,
б) через сколько минут они будут перпендикулярны.
"""

def get_hand_angles(hours: int, minutes: int) -> tuple[float, float]:
    """Возвращает углы часовой и минутной стрелок (в градусах)."""
    minute_angle = minutes * 6
    hour_angle = (hours % 12) * 30 + minutes * 0.5
    return hour_angle, minute_angle


def angle_between_hands(hours: int, minutes: int) -> float:
    """Возвращает меньший угол между стрелками (в градусах)."""
    h_angle, m_angle = get_hand_angles(hours, minutes)
    diff = abs(h_angle - m_angle)
    return diff if diff <= 180 else 360 - diff


def time_until_coincidence(hours: int, minutes: int) -> float:
    """Возвращает, через сколько минут стрелки совпадут."""
    # Разность углов
    diff = abs(30 * (hours % 12) + 0.5 * minutes - 6 * minutes)
    if diff == 0:
        return 0.0
    # Скорость сближения 5.5°/мин
    t = (360 - diff) / 5.5
    return round(t, 2)


def time_until_perpendicular(hours: int, minutes: int) -> float:
    """Возвращает, через сколько минут стрелки будут перпендикулярны."""
    diff = abs(30 * (hours % 12) + 0.5 * minutes - 6 * minutes)
    diff = diff if diff <= 180 else 360 - diff

    # Δθ = 90° → (5.5°/мин) * t = |90 - diff|
    t1 = abs(90 - diff) / 5.5
    t2 = abs(90 + diff) / 5.5
    t = min(t1, t2)
    return round(t, 2)


# Ввод
print("Введите текущее время:")
m = int(input("Часы (1–12): "))
n = int(input("Минуты (0–59): "))

if not (0 < m <= 12) or not (0 <= n < 60):
    print("Ошибка: часы должны быть 1–12, минуты 0–59.")
else:
    diff = angle_between_hands(m, n)
    print(f"\n{'=' * 60}")
    print(f"Текущее время: {m:02d}:{n:02d}")
    print(f"Угол между стрелками: {diff:.2f}°")
    print(f"{'=' * 60}")

    # а) Совпадение
    t_coinc = time_until_coincidence(m, n)
    print(f"\na) Стрелки совпадут через {t_coinc:.2f} мин")

    # б) Перпендикулярность
    t_perp = time_until_perpendicular(m, n)
    print(f"б) Стрелки будут перпендикулярны через {t_perp:.2f} мин")

# Примеры
print(f"\n{'=' * 60}")
print("--- Примеры ---\n")
examples = [(12, 0), (3, 0), (6, 0), (9, 0), (1, 30), (2, 15)]
for h, m in examples:
    print(f"Время {h:02d}:{m:02d} → угол {angle_between_hands(h, m):.2f}°")
    print(f"  Совпадут через {time_until_coincidence(h, m):.2f} мин")
    print(f"  Перпендикулярны через {time_until_perpendicular(h, m):.2f} мин\n")

input("\nНажмите Enter, чтобы завершить программу.")
