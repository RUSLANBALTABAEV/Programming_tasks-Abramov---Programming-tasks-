"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
10. Вложенные циклы

341. Даны пять различных целых чисел. Найти среди них два числа, модуль разности которых имеет:
а) наибольшее значение;
б) наименьшее значение.
"""


import random

def get_numbers():
    """Выбор способа ввода пяти различных целых чисел."""
    print("Выберите способ ввода:")
    print("1 - Ручной ввод")
    print("2 - Случайная генерация")
    print("3 - Готовый пример")
    choice = input("Ваш выбор (1/2/3): ").strip()
    while choice not in ('1', '2', '3'):
        choice = input("Некорректно. Выберите 1, 2 или 3: ")

    if choice == '1':
        try:
            print("Введите пять различных целых чисел через пробел:")
            line = input().strip()
            tokens = line.split()
            if len(tokens) != 5:
                print("Ожидалось 5 чисел.")
                return None
            nums = []
            for t in tokens:
                nums.append(int(t))
            # Проверка на различия (необязательно, но для корректности)
            if len(set(nums)) != 5:
                print("Числа должны быть различными.")
                return None
            return nums
        except ValueError:
            print("Ошибка ввода.")
            return None

    elif choice == '2':
        # Генерируем пять различных случайных чисел
        nums = random.sample(range(-100, 101), 5)  # 5 уникальных чисел из диапазона
        print("Сгенерированы числа:", nums)
        return nums

    else:  # choice == '3'
        examples = [
            [1, 2, 3, 4, 5],
            [-10, -5, 0, 5, 10],
            [100, 50, 0, -50, -100],
            [7, 14, 21, 28, 35],
            [3, 1, 4, 1, 5],  # но здесь есть повтор? Нет, 1 повторяется, так что не подходит
            # Заменим на другой пример
            [3, 1, 4, 2, 5]  # все различны
        ]
        print("Готовые примеры:")
        for idx, ex in enumerate(examples, 1):
            print(f"{idx}: {ex}")
        try:
            idx = int(input("Выберите номер примера: "))
            if 1 <= idx <= len(examples):
                nums = examples[idx-1]
                # Проверим на различия (в примерах они различны)
                return nums
            else:
                print("Неверный номер.")
                return None
        except ValueError:
            print("Ошибка ввода.")
            return None

def find_extreme_diffs(nums):
    """Находит пары для максимальной и минимальной разности."""
    sorted_nums = sorted(nums)
    # Максимальная разность
    max_pair = (sorted_nums[0], sorted_nums[-1])
    max_diff = max_pair[1] - max_pair[0]

    # Минимальная разность
    min_diff = float('inf')
    min_pair = None
    for i in range(len(sorted_nums)-1):
        diff = sorted_nums[i+1] - sorted_nums[i]
        if diff < min_diff:
            min_diff = diff
            min_pair = (sorted_nums[i], sorted_nums[i+1])

    return max_pair, max_diff, min_pair, min_diff

def main():
    nums = get_numbers()
    if nums is None:
        return

    print("\n" + "="*60)
    print("Исходные числа:", nums)
    print("="*60)

    max_pair, max_diff, min_pair, min_diff = find_extreme_diffs(nums)

    print("\nа) Наибольшее значение модуля разности:")
    print(f"   |{max_pair[0]} - {max_pair[1]}| = {max_diff}")
    print(f"   (числа: {max_pair[0]} и {max_pair[1]})")

    print("\nб) Наименьшее значение модуля разности:")
    print(f"   |{min_pair[0]} - {min_pair[1]}| = {min_diff}")
    print(f"   (числа: {min_pair[0]} и {min_pair[1]})")

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
