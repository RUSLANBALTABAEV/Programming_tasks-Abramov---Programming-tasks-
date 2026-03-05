"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
10. Вложенные циклы

359. Даны натуральное число n , символы s1, ..., s10, t1, ..., tn*).
Получить все не превосходящие n - 9 натуральные i, для которых s1 = ti, s2 = ti+1, ..., s10 = ti+9.
*) Задачи 359-366 допускают строковые варианты (см. примечание к задаче 252).
"""


import random


def get_input():
    """Выбор способа ввода"""
    print("Выберите способ ввода:")
    print("1 — Ручной ввод")
    print("2 — Случайная генерация")
    print("3 — Готовые примеры")
    
    choice = input("Ваш выбор (1/2/3): ").strip()
    while choice not in ('1', '2', '3'):
        choice = input("Выберите 1, 2 или 3: ").strip()

    if choice == '1':
        # === РУЧНОЙ ВВОД ===
        n = int(input("\nВведите натуральное число n (≥10): "))
        if n < 10:
            print("Ошибка: n должно быть не меньше 10!")
            return None
            
        s = input("Введите 10 символов s подряд: ").strip()
        if len(s) != 10:
            print("Ошибка: s должна содержать ровно 10 символов!")
            return None
            
        t = input(f"Введите строку t длиной {n}: ").strip()
        if len(t) != n:
            print(f"Предупреждение: длина t = {len(t)}. Используем введённую длину.")
            n = len(t)
            
        return n, s, t

    elif choice == '2':
        # === СЛУЧАЙНАЯ ГЕНЕРАЦИЯ ===
        n = random.randint(15, 40)
        s = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=10))
        t = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=n))
        
        # Добавляем хотя бы одно совпадение с вероятностью 75%
        if random.random() < 0.75:
            pos = random.randint(0, n - 10)
            t = t[:pos] + s + t[pos + 10:]
        
        print(f"\nСгенерировано:")
        print(f"n = {n}")
        print(f"s = {s}")
        print(f"t = {t}")
        return n, s, t

    else:
        # === ГОТОВЫЕ ПРИМЕРЫ ===
        examples = [
            (15, "ABCDEF1234", "XXABCDEF1234ZZZ"),
            (20, "pythonrule", "javapythonrulecpp"),
            (12, "1112223334", "0001112223334555"),
            (25, "TESTPASSWD", "adminTESTPASSWDuserroot"),
            (18, "**********", "123*********45678")
        ]
        
        print("\nГотовые примеры:")
        for i, (n_val, s_val, t_val) in enumerate(examples, 1):
            print(f"{i}. n={n_val} | s={s_val} | t={t_val}")
        
        num = int(input("\nВыберите номер примера: "))
        if 1 <= num <= len(examples):
            n, s, t = examples[num-1]
            return n, s, t[:n]
        else:
            print("Неверный номер!")
            return None


def main():
    data = get_input()
    if data is None:
        return
    
    n, s, t = data

    # Поиск позиций с помощью вложенных циклов
    positions = []
    for i in range(n - 9):           # i от 0 до n-10
        match = True
        for j in range(10):          # проверяем 10 символов
            if t[i + j] != s[j]:
                match = False
                break
        if match:
            positions.append(i + 1)

    # Вывод результата
    print("\n" + "="*45)
    print("РЕЗУЛЬТАТ ЗАДАЧИ 359")
    print("="*45)
    
    if positions:
        print("Найдены позиции i:", ", ".join(map(str, positions)))
        print(f"Всего найдено совпадений: {len(positions)}")
    else:
        print("Таких позиций i не найдено.")
    
    print("="*45)


if __name__ == "__main__":
    main()
