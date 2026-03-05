"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
10. Вложенные циклы

360. Даны натуральное число n, символы s1,...,sn. Найти все палиндромические начальные отрезки последовательности s1,...,sn, т.е. такие отрезки s1,...,sk * (k <= n), что s1 = sk,s2 = sk-1,... .
"""


import random

def get_input():
    """Выбор способа ввода n и строки s."""
    print("=== Задача 360: Палиндромические начальные отрезки ===")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод")
    print("2 — Случайная генерация")
    print("3 — Готовые примеры")

    choice = input("Ваш выбор (1/2/3): ").strip()
    while choice not in ('1', '2', '3'):
        choice = input("Выберите 1, 2 или 3: ").strip()

    if choice == '1':
        # Ручной ввод
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
        # Случайная генерация
        n = random.randint(1, 20)
        # Генерируем случайную строку из букв (можно добавить цифры)
        s = ''.join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", k=n))
        print(f"\nСгенерировано: n = {n}")
        print(f"s = {s}")
        return n, s

    else:
        # Готовые примеры
        examples = [
            (5, "abcba"),
            (4, "abba"),
            (1, "a"),
            (7, "racecar"),
            (6, "abcdef"),
            (3, "aba"),
            (8, "abccbaab")  # палиндромы: k=1,2? (ab? нет), 8? (abccbaab? нет)
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

def is_palindrome_prefix(s, k):
    """Проверяет, является ли префикс длины k палиндромом."""
    for i in range(k // 2):
        if s[i] != s[k - 1 - i]:
            return False
    return True

def main():
    data = get_input()
    if data is None:
        return
    n, s = data

    # Поиск всех палиндромических префиксов
    palindromes = []
    for k in range(1, n + 1):
        if is_palindrome_prefix(s, k):
            palindromes.append(k)

    print("\n" + "="*45)
    print("РЕЗУЛЬТАТ ЗАДАЧИ 360")
    print("="*45)
    if palindromes:
        print("Найдены начальные отрезки-палиндромы длины:", ", ".join(map(str, palindromes)))
    else:
        print("Нет палиндромических начальных отрезков (хотя при k=1 всегда палиндром).")
    print("="*45)

if __name__ == "__main__":
    main()
