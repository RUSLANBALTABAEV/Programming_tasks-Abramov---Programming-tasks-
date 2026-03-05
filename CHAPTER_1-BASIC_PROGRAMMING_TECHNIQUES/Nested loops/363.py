"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
10. Вложенные циклы

363. Даны натуральное число n, символы s1,...,sn.
Преобразовать последовательность s1,...,sn, добавив к ней наименьшее число символов sn+1,...,sm так, чтобы последовательность s1,...,sm стала палиндромом: s1 = sm, s2 = sm-1,... .
"""


import random

def get_input():
    """Выбор способа ввода n и строки s."""
    print("=== Задача 363: Преобразование в палиндром добавлением символов в конец ===")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод")
    print("2 — Случайная генерация")
    print("3 — Готовые примеры")

    choice = input("Ваш выбор (1/2/3): ").strip()
    while choice not in ('1', '2', '3'):
        choice = input("Выберите 1, 2 или 3: ").strip()

    if choice == '1':
        try:
            n = int(input("Введите натуральное число n: "))
            if n <= 0:
                print("Ошибка: n должно быть положительным.")
                return None
            s = input(f"Введите строку из {n} символов: ").strip()
            if len(s) != n:
                print(f"Предупреждение: длина строки = {len(s)}. Используем введённую длину.")
                n = len(s)
            return n, s
        except ValueError:
            print("Ошибка ввода.")
            return None

    elif choice == '2':
        n = random.randint(1, 20)
        # Генерируем случайную строку из строчных букв
        chars = "abcdefghijklmnopqrstuvwxyz"
        s = ''.join(random.choices(chars, k=n))
        print(f"\nСгенерировано: n = {n}")
        print(f"s = {s}")
        return n, s

    else:
        examples = [
            (4, "abac"),
            (2, "ab"),
            (5, "abcba"),
            (3, "aab"),
            (6, "abcaac"),
            (1, "x"),
            (8, "abccbaab")  # последние 2? "ab" нет, "aab"? Проверим: суффиксы: "b" (да), "ab" (нет), "aab" (нет), "baab" (нет), "cbaab" (нет), "ccbaab" (нет), "bccbaab" (нет), "abccbaab" (нет) -> k=1, добавим первые 7 в обратном порядке = "baabccba"? Получится "abccbaabbaabccba" – палиндром? Проверим: зеркально? Вроде да.
        ]
        print("\nГотовые примеры (n, s):")
        for i, (n_val, s_val) in enumerate(examples, 1):
            print(f"{i}. n={n_val}, s='{s_val}'")
        try:
            num = int(input("\nВыберите номер примера: "))
            if 1 <= num <= len(examples):
                n, s = examples[num-1]
                return n, s
            else:
                print("Неверный номер!")
                return None
        except ValueError:
            print("Ошибка ввода.")
            return None

def is_palindrome(s):
    """Проверка, является ли строка палиндромом."""
    return s == s[::-1]

def find_max_palindromic_suffix(s):
    """Находит максимальную длину k (1..n) такую, что последние k символов строки - палиндром."""
    n = len(s)
    for k in range(n, 0, -1):
        if is_palindrome(s[n-k:]):
            return k
    return 1  # всегда найдётся (односимвольный суффикс)

def main():
    data = get_input()
    if data is None:
        return
    n, s = data

    k = find_max_palindromic_suffix(s)
    prefix_len = n - k
    to_add = s[:prefix_len][::-1]  # обратный порядок первых prefix_len символов
    result = s + to_add

    print("\n" + "="*50)
    print("РЕЗУЛЬТАТ ЗАДАЧИ 363")
    print("="*50)
    print(f"Исходная строка: {s}")
    print(f"Наибольший палиндромный суффикс длины k = {k}: '{s[n-k:]}'")
    print(f"Добавлено символов: {len(to_add)}")
    print(f"Результирующий палиндром: {result}")
    print("="*50)

if __name__ == "__main__":
    main()
