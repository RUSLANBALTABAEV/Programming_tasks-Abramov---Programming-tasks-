"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
6. Пошаговый ввод данных и вывод результатов *)

148. Получить таблицу температур по Цельсию от 0 до 100 градусов и их эквивалентов по шкале Фаренгейта, используя для перевода формулу tF = 9 / 5 * tc + 32.
"""


def main():
    print("Таблица перевода температур из шкалы Цельсия в шкалу Фаренгейта")
    print("=" * 70)
    print("Формула перевода: °F = (9/5) * °C + 32")
    print("=" * 70)
    
    # Основная таблица с шагом 10 градусов
    print("\nОсновная таблица (с шагом 10°C):")
    print("-" * 60)
    print(f"{'Цельсий (°C)':^20} | {'Фаренгейт (°F)':^20} | {'Описание':^20}")
    print("-" * 60)
    
    for celsius in range(0, 101, 10):
        fahrenheit = (9/5) * celsius + 32
        description = get_temperature_description(celsius)
        print(f"{celsius:^20} | {fahrenheit:^20.1f} | {description:^20}")
    
    print("-" * 60)
    
    # Полная таблица с шагом 1 градус
    print("\n" + "=" * 70)
    print("Полная таблица (0-100°C с шагом 1°C):")
    print("=" * 70)
    
    # Разбиваем на несколько колонок для удобства просмотра
    num_columns = 4
    items_per_column = 101 // num_columns + (101 % num_columns > 0)
    
    # Создаем данные для таблицы
    data = []
    for celsius in range(0, 101):
        fahrenheit = (9/5) * celsius + 32
        data.append((celsius, fahrenheit))
    
    # Выводим таблицу с несколькими колонками
    print(f"\n{'°C':>5} {'°F':>7} | {'°C':>5} {'°F':>7} | {'°C':>5} {'°F':>7} | {'°C':>5} {'°F':>7}")
    print("-" * 60)
    
    for i in range(items_per_column):
        row = ""
        for col in range(num_columns):
            idx = i + col * items_per_column
            if idx < len(data):
                celsius, fahrenheit = data[idx]
                row += f"{celsius:5} {fahrenheit:7.1f} | "
            else:
                row += " " * 15 + "| "
        print(row.rstrip("| "))
    
    # Важные точки замерзания и кипения воды
    print("\n" + "=" * 70)
    print("Важные температурные точки:")
    print("-" * 70)
    
    important_points = [
        (-273.15, "Абсолютный ноль"),
        (-40, "-40°C = -40°F"),
        (0, "Точка замерзания воды"),
        (10, "Прохладная температура"),
        (20, "Комнатная температура"),
        (30, "Жаркий день"),
        (37, "Температура тела человека"),
        (40, "Очень жарко"),
        (100, "Точка кипения воды"),
    ]
    
    print(f"{'Цельсий (°C)':^15} | {'Фаренгейт (°F)':^15} | {'Описание':^30}")
    print("-" * 70)
    
    for celsius, description in important_points:
        fahrenheit = (9/5) * celsius + 32
        print(f"{celsius:^15.1f} | {fahrenheit:^15.1f} | {description:^30}")
    
    # Интерактивная часть: перевод конкретной температуры
    print("\n" + "=" * 70)
    print("Интерактивный перевод температуры")
    print("=" * 70)
    
    while True:
        try:
            user_input = input("\nВведите температуру в °C (или 'стоп' для выхода): ")
            
            if user_input.lower() in ['стоп', 'stop', 'exit', 'quit', 'выход']:
                break
            
            celsius = float(user_input)
            fahrenheit = (9/5) * celsius + 32
            
            print(f"{celsius}°C = {fahrenheit:.2f}°F")
            
            # Сравнение с важными точками
            if celsius == -40:
                print("  Особый случай: -40°C = -40°F")
            elif celsius == 0:
                print("  Точка замерзания воды")
            elif celsius == 100:
                print("  Точка кипения воды")
            elif celsius < -273.15:
                print("  Ниже абсолютного нуля!")
                
        except ValueError:
            print("Ошибка: введите числовое значение температуры")
    
    # Вывод формулы и пояснений
    print("\n" + "=" * 70)
    print("Дополнительная информация:")
    print("=" * 70)
    
    print("\nФормулы перевода температур:")
    print("  °F = (9/5) × °C + 32  (Цельсий → Фаренгейт)")
    print("  °C = (5/9) × (°F - 32)  (Фаренгейт → Цельсий)")
    
    print("\nИнтересные факты:")
    print("  1. Шкала Фаренгейта была предложена Даниелем Габриелем Фаренгейтом в 1724 году")
    print("  2. В шкале Фаренгейта точка замерзания воды - 32°F, точка кипения - 212°F")
    print("  3. Температура -40° является единственной, где шкалы Цельсия и Фаренгейта совпадают")
    print("  4. Абсолютный ноль (самая низкая возможная температура) равен -273.15°C или -459.67°F")

def get_temperature_description(celsius):
    """Возвращает описание температуры по значению в градусах Цельсия"""
    if celsius < -20:
        return "Экстремально холодно"
    elif celsius < 0:
        return "Морозно"
    elif celsius == 0:
        return "Точка замерзания"
    elif celsius < 10:
        return "Холодно"
    elif celsius < 20:
        return "Прохладно"
    elif celsius < 25:
        return "Комнатная темп."
    elif celsius < 30:
        return "Тепло"
    elif celsius < 35:
        return "Жарко"
    elif celsius < 40:
        return "Очень жарко"
    elif celsius == 100:
        return "Точка кипения"
    elif celsius > 100:
        return "Экстремально жарко"
    else:
        return "Жарко"

if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
