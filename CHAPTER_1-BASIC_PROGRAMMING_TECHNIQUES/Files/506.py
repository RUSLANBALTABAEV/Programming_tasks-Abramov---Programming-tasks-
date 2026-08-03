"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

506. Багаж пассажира характеризуется количеством вещей и общим весом вещей. Дан файл f, содержащий информацию о багаже нескольких пассажиров, информация о багаже каждого отдельного пассажира представляет собой соответствующую пару чисел *). 
*) Предполагается, что либо числа каждой пары объединены в записи и компонентами файла являются эти записи (что естественно, например, для языка Паскаль), либо числа занесены в файл по отдельности и чередуются в файле в следующем порядке: целое, действительное, целое, действительное, … (это естественно, например, для языка Бейсик). В задачах 507, 517 это соглашение сохраняется – при работе с языком типа Паскаль информация о каждом отдельном предмете упрятывается в одну компоненту файла, и все компоненты имеют один и тот же тип. Компоненты файла будут массивами или записями, и элементы массива или поля записи могут иметь в свою очередь довольно сложный тип. При работе с Бейсиком простые типы компонент файла будут чередоваться в определенном порядке. 
а) Найти багаж, средний вес одной вещи в котором отличается не более чем на 0,3 кг от общего среднего веса вещи.
б) Найти число пассажиров, имеющих более двух вещей и число пассажиров, количество вещей которых превосходит среднее число вещей.
в) Определить, имеются ли два пассажира, багажи которых совпадают по числу вещей и различаются по весу не более чем на 0,5 кг.
г) Выяснить, имеется ли пассажир, багаж которого превышает багаж каждого из остальных пассажиров и по числу вещей, и по весу. 
д) Выяснить, имеется ли пассажир, багаж которого состоит из одной вещи весом не менее 30 кг.
е) Дать сведения о багаже, число вещей в котором не меньше, чем в любом другом багаже, а вес вещей не больше, чем в любом другом багаже с этим же числом вещей. 
"""


import random
import os


# ------------------------------------------------------------
# 1. Процедуры работы с файлами
# ------------------------------------------------------------
def create_text_file(filename, text):
    """Создаёт (или перезаписывает) текстовый файл с указанным содержимым."""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)


def read_file(filename):
    """Читает и возвращает содержимое текстового файла."""
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()


# ------------------------------------------------------------
# 2. Создание исходного файла f (если отсутствует или пуст)
# ------------------------------------------------------------
def create_file_f(filename):
    """Создаёт файл f с данными о багаже пассажиров."""
    print("Файл f не существует или пуст. Задайте данные о пассажирах.")
    print("Формат: каждая строка — количество вещей и общий вес через пробел.")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод (пустая строка — конец)")
    print("2 — Случайная генерация")
    print("3 — Готовый пример")

    while True:
        choice = input("Ваш выбор (1/2/3): ").strip()
        if choice in ('1', '2', '3'):
            break
        print("Ошибка: выберите 1, 2 или 3.")

    if choice == '1':
        print("Вводите по одной строке на пассажира. Для завершения — пустая строка.")
        lines = []
        while True:
            line = input().strip()
            if line == "":
                break
            parts = line.split()
            if len(parts) != 2:
                print("  Ошибка: нужно два числа (количество вещей и вес).")
                continue
            try:
                items = int(parts[0])
                weight = float(parts[1])
                if items <= 0 or weight <= 0:
                    print("  Количество вещей и вес должны быть положительными.")
                    continue
                lines.append(f"{items} {weight}")
            except ValueError:
                print("  Ошибка: введите целое и действительное число.")
        if not lines:
            print("Не введено ни одной записи. Будет использован пример.")
            lines = ["2 12.5", "3 20.0", "1 30.0", "4 25.0", "2 8.3"]
        text = "\n".join(lines)
    elif choice == '2':
        n = random.randint(5, 10)  # количество пассажиров
        lines = []
        for _ in range(n):
            items = random.randint(1, 5)
            weight = round(random.uniform(2.0, 50.0), 1)
            lines.append(f"{items} {weight}")
        text = "\n".join(lines)
        print(f"Сгенерировано {n} записей о пассажирах.")
    else:  # готовый пример
        text = """2 12.5
3 20.0
1 30.0
4 25.0
2 8.3
5 45.0
1 15.2
3 18.9"""
        print("Использован готовый пример (8 пассажиров).")

    create_text_file(filename, text)
    print(f"Данные записаны в '{filename}'.")


def ensure_file_exists(filename):
    """Проверяет, существует ли файл и содержит ли данные. Если нет – создаёт."""
    if not os.path.exists(filename):
        create_file_f(filename)
        return
    content = read_file(filename).strip()
    if not content:
        create_file_f(filename)
        return
    # Проверим, есть ли хоть одна корректная строка
    lines = content.splitlines()
    has_valid = False
    for line in lines:
        parts = line.split()
        if len(parts) == 2:
            try:
                int(parts[0])
                float(parts[1])
                has_valid = True
                break
            except ValueError:
                pass
    if not has_valid:
        print("Файл не содержит корректных записей о пассажирах.")
        create_file_f(filename)


# ------------------------------------------------------------
# 3. Чтение данных о пассажирах из файла
# ------------------------------------------------------------
def read_passengers(filename):
    """Возвращает список кортежей (количество_вещей, общий_вес)."""
    content = read_file(filename).strip()
    if not content:
        return []
    passengers = []
    for line in content.splitlines():
        parts = line.split()
        if len(parts) == 2:
            try:
                items = int(parts[0])
                weight = float(parts[1])
                passengers.append((items, weight))
            except ValueError:
                pass
    return passengers


# ------------------------------------------------------------
# 4. Решения подзадач (а–е)
# ------------------------------------------------------------
def task_a(passengers):
    """Средний вес вещи по всем пассажирам и подходящие багажи."""
    total_items = sum(p[0] for p in passengers)
    total_weight = sum(p[1] for p in passengers)
    if total_items == 0:
        return None, []
    overall_avg = total_weight / total_items
    suitable = []
    for items, weight in passengers:
        if abs(weight / items - overall_avg) <= 0.3:
            suitable.append((items, weight))
    return overall_avg, suitable


def task_b(passengers):
    """Пассажиры с >2 вещами и те, у кого вещей больше среднего."""
    n = len(passengers)
    if n == 0:
        return 0, 0, 0
    more_than_2 = sum(1 for items, _ in passengers if items > 2)
    avg_items = sum(p[0] for p in passengers) / n
    over_avg = sum(1 for items, _ in passengers if items > avg_items)
    return more_than_2, over_avg, avg_items


def task_c(passengers):
    """Два пассажира с одинаковым числом вещей и разницей веса ≤ 0.5 кг."""
    groups = {}
    for idx, (items, weight) in enumerate(passengers):
        groups.setdefault(items, []).append((idx, weight))
    for items, group in groups.items():
        for i in range(len(group)):
            for j in range(i + 1, len(group)):
                if abs(group[i][1] - group[j][1]) <= 0.5:
                    return True, (group[i][0], group[j][0])
    return False, None


def task_d(passengers):
    """Пассажир, превосходящий всех по обоим параметрам."""
    n = len(passengers)
    for i in range(n):
        items_i, weight_i = passengers[i]
        dominant = True
        for j in range(n):
            if i == j:
                continue
            items_j, weight_j = passengers[j]
            if items_i <= items_j or weight_i <= weight_j:
                dominant = False
                break
        if dominant:
            return True, i
    return False, None


def task_e(passengers):
    """Пассажир с одной вещью весом ≥ 30 кг."""
    for i, (items, weight) in enumerate(passengers):
        if items == 1 and weight >= 30.0:
            return True, i
    return False, None


def task_f(passengers):
    """Багаж с максимальным числом вещей и минимальным весом среди таких."""
    if not passengers:
        return None
    max_items = max(p[0] for p in passengers)
    candidates = [(items, weight) for items, weight in passengers if items == max_items]
    return min(candidates, key=lambda x: x[1])


# ------------------------------------------------------------
# 5. Основная программа
# ------------------------------------------------------------
def main():
    print("Задача 506: Анализ багажа пассажиров")
    file_f = "f.txt"

    ensure_file_exists(file_f)
    passengers = read_passengers(file_f)

    if not passengers:
        print("Нет данных для обработки.")
        return

    print(f"Всего пассажиров: {len(passengers)}")
    print("Данные (вещи, вес):")
    for i, (items, weight) in enumerate(passengers, 1):
        print(f"  {i}: {items} вещей, {weight:.1f} кг")
    print("-" * 50)

    # а)
    avg_all, suitable = task_a(passengers)
    print(f"а) Общий средний вес одной вещи: {avg_all:.3f} кг" if avg_all else "а) Нет данных.")
    if suitable:
        print("   Подходящие багажи (отклонение ≤ 0.3 кг):")
        for items, weight in suitable:
            print(f"     {items} вещей, {weight:.1f} кг (средний вес вещи {weight/items:.3f} кг)")
    else:
        print("   Подходящих багажей не найдено.")

    # б)
    more2, over_avg, avg_items = task_b(passengers)
    print(f"\nб) Пассажиров с >2 вещами: {more2}")
    print(f"   Среднее число вещей на пассажира: {avg_items:.2f}")
    print(f"   Пассажиров с количеством вещей выше среднего: {over_avg}")

    # в)
    has_pair, pair = task_c(passengers)
    print(f"\nв) Есть два пассажира с одинаковым числом вещей и разницей веса ≤ 0.5 кг: {'Да' if has_pair else 'Нет'}")
    if has_pair:
        print(f"   Пассажиры: №{pair[0]+1} и №{pair[1]+1}")

    # г)
    has_dominant, idx = task_d(passengers)
    print(f"\nг) Есть пассажир, превосходящий всех по вещам и весу: {'Да' if has_dominant else 'Нет'}")
    if has_dominant:
        items, weight = passengers[idx]
        print(f"   Пассажир №{idx+1}: {items} вещей, {weight:.1f} кг")

    # д)
    has_heavy, idx = task_e(passengers)
    print(f"\nд) Есть пассажир с 1 вещью весом ≥ 30 кг: {'Да' if has_heavy else 'Нет'}")
    if has_heavy:
        print(f"   Пассажир №{idx+1}: {passengers[idx][1]:.1f} кг")

    # е)
    best = task_f(passengers)
    print(f"\nе) Багаж, максимальный по вещам и минимальный по весу среди них:")
    if best:
        items, weight = best
        print(f"   {items} вещей, {weight:.1f} кг (средний вес вещи {weight/items:.2f} кг)")
    else:
        print("   Данные отсутствуют.")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")