"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
10. Вложенные циклы

333. Даны натуральные числа m,n1, ..., nm * (m >= 2). Вычислить НОД(n, ..., nm), воспользовавшись для этого соотношением НОД(n, ..., nk) = НОД(НОД(n, ..., nk-1)nk)(k = 3, ..., n) и алгоритмом Евклида (см. задачу 89).
"""


import random

def gcd(a, b):
    """Алгоритм Евклида для нахождения НОД двух натуральных чисел."""
    while b != 0:
        a, b = b, a % b
    return a

def get_numbers_by_choice():
    """Выбор способа получения чисел m и последовательности."""
    print("Выберите способ задания чисел:")
    print("1 - Ручной ввод")
    print("2 - Случайные числа")
    print("3 - Готовый набор")
    choice = input("Ваш выбор (1/2/3): ").strip()
    while choice not in ('1', '2', '3'):
        choice = input("Некорректный ввод. Выберите 1, 2 или 3: ").strip()

    if choice == '1':
        while True:
            try:
                m = int(input("Введите количество чисел m (≥2): "))
                if m < 2:
                    print("m должно быть не меньше 2.")
                    continue
                nums = []
                print(f"Введите {m} натуральных чисел:")
                for i in range(1, m+1):
                    x = int(input(f"n{i} = "))
                    if x < 1:
                        print("Число должно быть натуральным (≥1).")
                        return None  # прервём и попросим повторить ввод позже
                    nums.append(x)
                return m, nums
            except ValueError:
                print("Ошибка ввода. Введите целые числа.")

    elif choice == '2':
        m = random.randint(2, 10)
        nums = [random.randint(1, 100) for _ in range(m)]
        print(f"Сгенерировано m = {m}, числа: {nums}")
        return m, nums

    else:  # choice == '3'
        predefined = [
            (2, [15, 25]),
            (3, [12, 18, 24]),
            (4, [30, 42, 56, 70]),
            (5, [100, 200, 300, 400, 500]),
            (3, [7, 13, 19])
        ]
        print("Доступные готовые наборы (m, список чисел):")
        for idx, (m_val, nums_val) in enumerate(predefined, start=1):
            print(f"{idx} - m = {m_val}, числа: {nums_val}")
        while True:
            try:
                idx = int(input("Выберите номер набора: "))
                if 1 <= idx <= len(predefined):
                    m, nums = predefined[idx-1]
                    return m, nums
                else:
                    print(f"Введите число от 1 до {len(predefined)}")
            except ValueError:
                print("Ошибка ввода. Введите номер.")

def main():
    print("=" * 70)
    print("Задача 333: НОД последовательности чисел")
    print("=" * 70)

    result = get_numbers_by_choice()
    if result is None:
        # при ошибке в ручном вводе можно было бы повторить, но упростим
        print("Не удалось получить корректные данные.")
        return
    m, nums = result

    print("\nИсходные данные:")
    print(f"m = {m}")
    print(f"Числа: {nums}")

    # Вычисление НОД последовательно
    current_gcd = nums[0]
    for i in range(1, m):
        current_gcd = gcd(current_gcd, nums[i])

    print(f"\nНОД всех чисел = {current_gcd}")

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
