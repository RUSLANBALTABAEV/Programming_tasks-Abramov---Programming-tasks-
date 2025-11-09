"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
3. Простейшая целочисленная арифметика
69. Часовая стрелка образует угол φ с направлением на 12 часов
(0 < φ ≤ 2π). Определить:
а) значение угла, который образует минутная стрелка,
б) показать взаимосвязь углов.
"""

import math

# --- Ввод данных ---
print("Введите угол φ (в радианах), который образует часовая стрелка:")
print(f"(0 < φ ≤ 2π, где π ≈ {math.pi:.5f})")

phi = float(input("φ = "))

# --- Проверка диапазона ---
if not (0 < phi <= 2 * math.pi):
    print("Ошибка: угол должен быть в диапазоне (0, 2π].")
else:
    print(f"\n{'=' * 60}")
    print("Анализ положения стрелок на циферблате")
    print(f"{'=' * 60}")

    # --- Расчёт текущего времени по углу часовой стрелки ---
    # Полный оборот часовой стрелки — 12 часов = 2π радиан
    total_hours = (phi / (2 * math.pi)) * 12

    # Часы и минуты:
    hours = int(total_hours)
    minutes = int(round((total_hours - hours) * 60))

    # Корректировка отображения времени
    if minutes == 60:
        minutes = 0
        hours = (hours + 1) % 12
    if hours == 0:
        hours = 12

    # --- Угол минутной стрелки ---
    # Минутная стрелка делает полный оборот (2π) за 60 минут
    minute_angle = (2 * math.pi / 60) * minutes

    print(f"\nУгол часовой стрелки φ = {phi:.4f} рад = {math.degrees(phi):.2f}°")
    print(f"Это соответствует времени ≈ {hours:02d}:{minutes:02d}")
    print(f"\nУгол минутной стрелки: θ = {minute_angle:.4f} рад = "
          f"{math.degrees(minute_angle):.2f}°")

    # --- Дополнительная информация ---
    print(f"\n{'=' * 60}")
    print("СПРАВОЧНО:")
    print(f"1 час = π/6 ≈ {math.pi / 6:.4f} рад ≈ 30°")
    print(f"1 минута = π/30 ≈ {math.pi / 30:.4f} рад ≈ 6°")
    print(f"Часовая стрелка движется на π/360 рад ≈ 0.5° в минуту.")


# --- Функции для переиспользования ---
def hour_angle_to_time(phi: float) -> tuple[int, int]:
    """Возвращает (часы, минуты) по углу часовой стрелки φ."""
    total_hours = (phi / (2 * math.pi)) * 12
    hours = int(total_hours)
    minutes = int(round((total_hours - hours) * 60))
    if minutes == 60:
        minutes = 0
        hours = (hours + 1) % 12
    if hours == 0:
        hours = 12
    return hours, minutes


def minute_angle_from_time(minutes: int) -> float:
    """Возвращает угол минутной стрелки (в радианах) по количеству минут."""
    return (2 * math.pi / 60) * (minutes % 60)


# --- Примеры ---
print(f"\n{'=' * 60}")
print("--- Примеры ---\n")

test_angles = [math.pi / 6, math.pi / 3, math.pi / 2, math.pi, 3 * math.pi / 2]
for phi in test_angles:
    h, m = hour_angle_to_time(phi)
    minute_angle = minute_angle_from_time(m)
    print(f"φ = {phi:.4f} рад ({math.degrees(phi):6.2f}°) → "
          f"{h:02d}:{m:02d}, θ = {minute_angle:.4f} рад "
          f"({math.degrees(minute_angle):5.2f}°)")

input("\nНажмите Enter, чтобы завершить программу.")
