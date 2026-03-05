"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
10. Вложенные циклы

366. Даны символы a1, ...,a10, натуральное число n, символы s1,...,sn. Как и в предыдущей задаче, будем рассматривать слова, входящие в последовательность s1,...,sn, по-прежнему считая, что количество символов в каждом слове не превосходит 15. Будем также считать, что среди символов a1,...,a10 нет пробелов, и поэтому последовательность a1,...,a10 может рассматриваться как одно слово. В словах могут встретиться ошибки:
1) переставлены две соседние буквы;
2) заменена одна буква;
3) пропущена одна буква.
Требуется найти в s1,...,sn все слова, из которых могло бы получиться a1,...,a10 в результате одной ошибки.
"""


import random

def get_input():
    """Выбор способа ввода a (10 символов), n и строки s."""
    print("=== Задача 366: Поиск слов с одной ошибкой ===")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод")
    print("2 — Случайная генерация")
    print("3 — Готовые примеры")

    choice = input("Ваш выбор (1/2/3): ").strip()
    while choice not in ('1', '2', '3'):
        choice = input("Выберите 1, 2 или 3: ").strip()

    if choice == '1':
        try:
            a = input("Введите 10 символов a (без пробелов): ").strip()
            if len(a) != 10:
                print("Ошибка: нужно ровно 10 символов.")
                return None
            n = int(input("Введите натуральное число n: "))
            if n <= 0:
                print("n должно быть положительным.")
                return None
            print(f"Введите строку из {n} символов (включая пробелы):")
            s = input()
            if len(s) != n:
                print(f"Предупреждение: длина введённой строки = {len(s)}. Используем её.")
            return a, s
        except ValueError:
            print("Ошибка ввода.")
            return None

    elif choice == '2':
        # Генерация случайного a и строки s
        a = ''.join(random.choices("abcdefghijklmnopqrstuvwxyz", k=10))
        num_words = random.randint(3, 8)
        words = []
        # Добавим несколько слов, которые могут подходить
        if random.random() < 0.5:
            w = list(a)
            pos = random.randint(0, 9)
            w[pos] = random.choice("abcdefghijklmnopqrstuvwxyz")
            words.append(''.join(w))
        if random.random() < 0.5:
            w = list(a)
            if len(w) >= 2:
                pos = random.randint(0, 8)
                w[pos], w[pos+1] = w[pos+1], w[pos]
                words.append(''.join(w))
        if random.random() < 0.5:
            w = list(a)
            pos = random.randint(0, 10)
            w.insert(pos, random.choice("abcdefghijklmnopqrstuvwxyz"))
            words.append(''.join(w))
        for _ in range(num_words - len(words)):
            wlen = random.randint(1, 15)
            words.append(''.join(random.choices("abcdefghijklmnopqrstuvwxyz", k=wlen)))
        random.shuffle(words)
        s = '  '.join(words)
        print(f"\nСгенерировано: a = '{a}'")
        print(f"Строка s: {s}")
        return a, s

    else:
        examples = [
            ("abcdefghij", "abcde fghij abcdefghij abcdefghij abcdefghij"),
            ("qwertyuiop", "qwertyuiop qwertyuio qwertyuip qwertyuipo qwertyuiop"),
            ("palindrome", "palindromep palindrome palindromep palindrome"),
            ("abcabcabca", "abcabcabca abcabcabca abcabcabca abcabcabca abcabcabca"),
        ]
        print("\nГотовые примеры (a, s):")
        for i, (a_val, s_val) in enumerate(examples, 1):
            print(f"{i}. a='{a_val}', s='{s_val[:30]}...'")
        try:
            num = int(input("\nВыберите номер примера: "))
            if 1 <= num <= len(examples):
                a, s = examples[num-1]
                return a, s
            else:
                print("Неверный номер!")
                return None
        except ValueError:
            print("Ошибка ввода.")
            return None

def is_one_error(word, a):
    """Проверяет, можно ли получить a из word одной ошибкой (перестановка, замена, пропуск)."""
    len_w = len(word)
    len_a = len(a)

    # Случай одинаковой длины: замена или перестановка
    if len_w == len_a:
        diff_count = 0
        diff_positions = []
        for i in range(len_a):
            if word[i] != a[i]:
                diff_count += 1
                diff_positions.append(i)
        # Замена одной буквы
        if diff_count == 1:
            return True
        # Перестановка двух соседних
        if diff_count == 2 and len(diff_positions) == 2:
            i, j = diff_positions
            if abs(i - j) == 1 and word[i] == a[j] and word[j] == a[i]:
                return True
        return False

    # Случай, когда word длиннее a на 1: пропуск буквы в word
    if len_w == len_a + 1:
        for i in range(len_w):
            if word[:i] + word[i+1:] == a:
                return True
        return False

    return False

def main():
    data = get_input()
    if data is None:
        return
    a, s = data
    print(f"\nСлово a: '{a}'")
    print(f"Строка s (длина {len(s)}): {s}")

    words = s.split()
    print(f"Найдено слов: {len(words)}")
    print("Слова:", words)

    result = [w for w in words if is_one_error(w, a)]

    print("\n" + "="*50)
    print("РЕЗУЛЬТАТ ЗАДАЧИ 366")
    print("="*50)
    if result:
        print("Слова, из которых могло получиться a одной ошибкой:")
        for w in result:
            print(f"  '{w}'")
    else:
        print("Нет таких слов.")
    print("="*50)

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
