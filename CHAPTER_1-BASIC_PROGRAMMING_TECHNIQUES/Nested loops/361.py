"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
10. Вложенные циклы

361. Даны натуральное число n, символы s1,...,sn. Указать все натуральные i, для которых 2i <= n, s1 = si+1, s2 = si+2,...,si = s2i.
"""


import random

def get_input():
    """Выбор способа ввода n и строки s."""
    print("=== Задача 361: Повторяющиеся префиксы ===")
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
        n = random.randint(2, 20)
        # Генерируем случайную строку из букв и цифр
        chars = "abcdefghijklmnopqrstuvwxyz0123456789"
        s = ''.join(random.choices(chars, k=n))
        # Иногда делаем так, чтобы было совпадение (для демонстрации)
        if random.choice([True, False]):
            # Выбираем случайную длину i
            i = random.randint(1, n//2)
            # Составляем префикс длины i
            prefix = s[:i]
            # Вставляем его на позицию i (сдвигая остаток)
            # Проще: создадим строку, где первые i и следующие i равны
            prefix = ''.join(random.choices(chars, k=i))
            rest = ''.join(random.choices(chars, k=n-2*i))
            s = prefix + prefix + rest
        print(f"\nСгенерировано: n = {n}")
        print(f"s = {s}")
        return n, s

    else:
        examples = [
            (8, "abcabcab"),   # i=3? Проверим: "abc" == "abc"? да, но 2i=6, остальное "ab". i=3 подходит.
            (6, "abcabc"),      # i=3 подходит
            (4, "aaaa"),        # i=1,2 подходят? 2i=4, первые 2 "aa" и следующие 2 "aa" - да, i=2 подходит; i=1 тоже
            (5, "ababa"),       # i=2? "ab" vs "ab"? да (позиции 2-3), i=2 подходит; i=1? "a" vs "b"? нет.
            (10, "xyzxyzxyzw"), # i=3? "xyz" vs "xyz" (позиции 3-5) да
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

def main():
    data = get_input()
    if data is None:
        return
    n, s = data

    # Поиск всех i, удовлетворяющих условию
    result = []
    max_i = n // 2
    for i in range(1, max_i + 1):
        if s[:i] == s[i:2*i]:
            result.append(i)

    print("\n" + "="*45)
    print("РЕЗУЛЬТАТ ЗАДАЧИ 361")
    print("="*45)
    if result:
        print("Найдены i:", ", ".join(map(str, result)))
    else:
        print("Нет таких i.")
    print("="*45)

if __name__ == "__main__":
    main()
