"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
2. Разветвления
45. Даны действительные числа a, b, c, d. 
Если a ≤ b ≤ c ≤ d, то каждое число заменить наибольшим из них;
если a > b > c > d — оставить без изменения;
в противном случае все числа заменяются их квадратами.
"""


def process_numbers(a: float, b: float, c: float, d: float) -> tuple[float, float, float, float]:
    """Обрабатывает четыре числа согласно условию задачи.
    
    Если a ≤ b ≤ c ≤ d → все числа заменяются наибольшим.
    Если a > b > c > d → остаются без изменений.
    Иначе → заменяются своими квадратами.
    """
    if a <= b <= c <= d:
        max_value = d
        return max_value, max_value, max_value, max_value
    if a > b > c > d:
        return a, b, c, d
    return a ** 2, b ** 2, c ** 2, d ** 2


def main() -> None:
    """Основная функция программы."""
    print("Обработка четырёх действительных чисел")
    print("-" * 60)

    try:
        a = float(input("Введите число a: "))
        b = float(input("Введите число b: "))
        c = float(input("Введите число c: "))
        d = float(input("Введите число d: "))

        print("-" * 60)
        print(f"Исходные значения: a = {a}, b = {b}, c = {c}, d = {d}")

        new_a, new_b, new_c, new_d = process_numbers(a, b, c, d)

        print("-" * 60)
        if a <= b <= c <= d:
            print("Условие a ≤ b ≤ c ≤ d выполняется.")
            print(f"Все числа заменены наибольшим значением: {d}")
        elif a > b > c > d:
            print("Условие a > b > c > d выполняется.")
            print("Числа оставлены без изменения.")
        else:
            print("Оба условия не выполняются.")
            print("Все числа заменены их квадратами.")

        print(
            f"Результат: a = {new_a}, b = {new_b}, "
            f"c = {new_c}, d = {new_d}"
        )

    except ValueError:
        print("Ошибка: необходимо вводить числа!")


if __name__ == "__main__":
    main()

input("\nНажмите Enter, чтобы завершить программу.")
