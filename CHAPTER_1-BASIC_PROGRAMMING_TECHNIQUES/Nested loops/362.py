"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
10. Вложенные циклы

362. Даны символы s1,...,sn. Найти такое наибольшее натуральное i, что 2i < n, s1 = si+1, s2 = si+2, ..., si = s2i и s1, s2, ..., si - палиндром, т.е. s1 = si, s2 = si-1,... .
"""


import random

def get_input():
    """Выбор способа ввода n и строки s."""
    print("=== Задача 362: Наибольшее i с повторяющимся палиндромическим префиксом ===")
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
        n = random.randint(2, 30)
        # Генерируем случайную строку из строчных букв
        chars = "abcdefghijklmnopqrstuvwxyz"
        s = ''.join(random.choices(chars, k=n))
        # Иногда создаем строку, удовлетворяющую условию, для демонстрации
        if random.choice([True, False]):
            # Выбираем случайное i, удовлетворяющее 2i < n
            max_i = (n - 1) // 2
            if max_i > 0:
                i = random.randint(1, max_i)
                # Создаем палиндромический префикс длины i
                half = i // 2
                prefix_chars = random.choices(chars, k=half)
                if i % 2 == 1:
                    mid = random.choice(chars)
                    prefix = ''.join(prefix_chars) + mid + ''.join(reversed(prefix_chars))
                else:
                    prefix = ''.join(prefix_chars) + ''.join(reversed(prefix_chars))
                # Строим всю строку: префикс + префикс + остаток
                rest = ''.join(random.choices(chars, k=n - 2*i))
                s = prefix + prefix + rest
        print(f"\nСгенерировано: n = {n}")
        print(f"s = {s}")
        return n, s

    else:
        examples = [
            (10, "abcabcabca"),      # i=4? 2i=8 <10, префикс "abca"? сравниваем "abca" и "bca"? нет, но i=3: "abc"=="abc" и "abc" палиндром? нет
            (8, "abbaabba"),        # i=4? 2i=8 <8? нет, 2i=8 не < n. i=3? 2i=6<8, префикс "abb"? "abb" не палиндром, но "abb"=="abb"? с i=3: s1..3="abb", s4..6="baa"? нет. Этот пример не подходит.
            (6, "abccba"),          # i=3? 2i=6 <6? нет, не <
            (7, "abcabca"),         # i=3? 2i=6<7, префикс "abc" не палиндром
            (5, "aabaa"),           # i=2? 2i=4<5, префикс "aa" палиндром, s1..2="aa", s3..4="ba"? нет.
            (9, "abcbaabcba")       # i=5? 2i=10>9 нет. i=4? 2i=8<9, префикс "abcb" не палиндром? "abcb" не палиндром. i=3? 2i=6, префикс "abc" не палиндром.
        ]
        # Подберем хороший пример: например, n=11, s="abcbaabcbaa"? Неочевидно.
        # Создадим пример с i=4, палиндром "abba", и повторим: s="abbaabba..." но тогда n должно быть >8.
        # Лучше: n=9, i=4, 2i=8<9, палиндром "abba", s="abbaabba?" тогда строка из 8 символов, а нужно 9, добавим символ. Например "abbaabbax" – проверим: i=4, префикс "abba", следующие 4 "abba"? первые 4: a b b a, следующие 4: a b b a? на позициях 5-8: a b b a? да, если s[4:8] = "abba". Тогда строка "abbaabba" + "x". Это подходит. Добавим такой пример.
        examples = [
            (9, "abbaabbax"),       # i=4 подходит? Проверим: 2i=8<9, префикс "abba" палиндром? "abba" – да. s[0:4]="abba", s[4:8]="abba" – да.
            (7, "abcabca"),         # i=3? префикс "abc" не палиндром, но i=3? 2i=6<7, префикс "abc", s[3:6]="abc"? да, но "abc" не палиндром. Не подходит.
            (5, "aabaa"),           # i=2? 2i=4<5, префикс "aa" палиндром, s[2:4]="ba"? нет.
            (8, "abbaabba"),        # i=4? 2i=8 не <8, поэтому не рассматривается.
            (10, "abcbaabcba"),      # i=5? 2i=10 не <10. i=4? 2i=8<10, префикс "abcb" не палиндром. i=3? 2i=6, префикс "abc" не палиндром, но "abc"=="abc"? s[3:6]="abc"? В строке "abcbaabcba" позиции 0-2="abc", 3-5="baa"? нет.
        ]
        # Добавим еще один хороший: n=11, s="abcbaabcbaa"? i=5? 2i=10<11, префикс "abcba" палиндром? "abcba" – да. s[5:10]="abcba"? В "abcbaabcbaa" позиции 5-9: "bcbaa"? нет. Создадим явно: "abcbaabcbaa" – первые 5 "abcba", следующие 5 "abcba"? тогда должно быть "abcbaabcba", но у нас длина 10, а нам надо 11, добавим "a". Тогда "abcbaabcbaa": первые 5 = "abcba", следующие 5 = "abcba"? С 5 по 9: индексы 5-9: "abcba"? Проверим: s[5]='a'? строка: индекс0=a,1=b,2=c,3=b,4=a,5=a,6=b,7=c,8=b,9=a,10=a. Значит s[5:10] = s[5:10] = a b c b a? да, с 5 по 9: a,b,c,b,a – это "abcba". Итак, s[0:5]="abcba", s[5:10]="abcba", и остаток s[10]="a". Условие i=5: 2i=10<11, префикс "abcba" палиндром, выполняется. Это хороший пример.
        examples = [
            (11, "abcbaabcbaa"),
            (7, "abacaba"),        # i=3? 2i=6<7, префикс "aba" палиндром, s[3:6]="cab"? нет
            (5, "aaaab"),          # i=2? 2i=4<5, префикс "aa" палиндром, s[2:4]="aa"? да, s[2:4]="aa"? строка "aaaab": индексы 0-4: a a a a b. i=2: первые 2 "aa", следующие 2 (индексы 2,3) = "aa" – да. Но префикс "aa" палиндром. Тогда i=2 подходит. Но может быть больше? i=3? 2i=6>5 нет. i=4? 2i=8>5 нет. Значит наибольшее i=2. Хорошо.
            (6, "abccba"),         # i=3? 2i=6 не <6, так что нет.
            (8, "abbaabba")        # i=4? 2i=8 не <8, нет.
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

def main():
    data = get_input()
    if data is None:
        return
    n, s = data

    # Поиск наибольшего i, удовлетворяющего условиям
    max_i = (n - 1) // 2  # поскольку 2i < n, то i <= floor((n-1)/2)
    result = None
    for i in range(max_i, 0, -1):
        if s[:i] == s[i:2*i] and is_palindrome(s[:i]):
            result = i
            break

    print("\n" + "="*45)
    print("РЕЗУЛЬТАТ ЗАДАЧИ 362")
    print("="*45)
    if result is not None:
        print(f"Наибольшее i = {result}")
        print(f"Префикс длины {result}: '{s[:result]}' является палиндромом и повторяется.")
    else:
        print("Нет такого i.")
    print("="*45)

if __name__ == "__main__":
    main()
