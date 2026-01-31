"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
9. Вычисления с хранением последовательности значений

272. Даны действительные числа а1901, a1902, …, а1950 – количество осадков (в миллиметрах), выпавших в Москве в течение
первых 50 лет нашего столетия. Надо вычислить среднее количество осадков и отклонение от среднего для каждого года.
"""


def main():
    # Количество лет
    n = 50
    start_year = 1901
    
    # Ввод данных по осадкам для каждого года
    precipitation = []
    for i in range(n):
        while True:
            try:
                value = float(input(f"Введите количество осадков для {start_year + i} года (мм): "))
                if value < 0:
                    print("Ошибка: количество осадков не может быть отрицательным.")
                else:
                    precipitation.append(value)
                    break
            except ValueError:
                print("Ошибка: введите действительное число (например, 45.6)")

    # Вычисляем среднее количество осадков
    average = sum(precipitation) / n

    # Вычисляем отклонение для каждого года
    deviations = [value - average for value in precipitation]

    # Выводим результаты
    print(f"\nСреднее количество осадков за {n} лет ({start_year}-{start_year + n - 1}): {average:.2f} мм")
    print("\nОтклонения от среднего по годам:")
    print("Год   | Осадки (мм) | Отклонение (мм)")
    print("-" * 40)
    
    for i in range(n):
        year = start_year + i
        print(f"{year} | {precipitation[i]:11.2f} | {deviations[i]:14.2f}")

if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
