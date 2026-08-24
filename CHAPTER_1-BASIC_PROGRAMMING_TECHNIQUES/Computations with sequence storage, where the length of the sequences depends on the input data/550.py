"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
14. Вычисления с хранением последовательностей, число членов
которых зависит от исходных данных *)
*) В некоторых языках программирования допускаются массивы с динамическими границами, и это снимает многие трудности в решении 
задач; в этом случае настоящий параграф продолжает § 9. В Паскале же, например, где такие массивы не допускаются, естественно 
использовать списки. Возможный вид этих списков указан в задачах 531-534. Для работы со списками полезны процедуры вставки 
элемента в начало списка, вставки элемента в конец списка, удаление 
элемента и т. д. (эти процедуры отдельно рассмотрены в §36). Для решения задач этого параграфа можно использовать и файлы, но это
резко увеличивает время выполнения программы и имеет смысл в том 
случае, когда все исходные данные не помещаются в памяти вычислительной машины.

550. Даны натуральные числа k, m, l, символы s1, ..., sk, t1, ..., tm, u1, ..., ul. Получить по одному разу те символы, которые входят одновременно во все три последовательности. 
"""


import random
import string


def get_data():
    """Выбор способа ввода трёх последовательностей символов."""
    print("Задача 550: Общие символы трёх последовательностей")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод")
    print("2 — Случайная генерация")
    print("3 — Готовые примеры")

    while True:
        choice = input("Ваш выбор (1/2/3): ").strip()
        if choice in ('1', '2', '3'):
            break
        print("Ошибка: выберите 1, 2 или 3.")

    if choice == '1':
        while True:
            try:
                k = int(input("Введите количество символов k (для s): "))
                m = int(input("Введите количество символов m (для t): "))
                l = int(input("Введите количество символов l (для u): "))
                if k <= 0 or m <= 0 or l <= 0:
                    print("Все размеры должны быть положительными.")
                    continue
                print("Введите последовательность s (символы слитно, например abc):")
                raw_s = input().strip()
                if len(raw_s) != k:
                    print(f"Ожидалось {k} символов, введено {len(raw_s)}.")
                    continue
                print("Введите последовательность t (слитно):")
                raw_t = input().strip()
                if len(raw_t) != m:
                    print(f"Ожидалось {m} символов, введено {len(raw_t)}.")
                    continue
                print("Введите последовательность u (слитно):")
                raw_u = input().strip()
                if len(raw_u) != l:
                    print(f"Ожидалось {l} символов, введено {len(raw_u)}.")
                    continue
                return (k, list(raw_s), m, list(raw_t), l, list(raw_u))
            except ValueError:
                print("Ошибка ввода. Повторите.")

    elif choice == '2':
        # Случайная генерация с общим алфавитом для возможности пересечений
        alphabet = string.ascii_letters + string.digits
        k = random.randint(3, 8)
        m = random.randint(3, 8)
        l = random.randint(3, 8)
        s = [random.choice(alphabet) for _ in range(k)]
        t = [random.choice(alphabet) for _ in range(m)]
        u = [random.choice(alphabet) for _ in range(l)]
        print(f"\nСгенерированы последовательности:")
        print(f"  s ({k}): {s}")
        print(f"  t ({m}): {t}")
        print(f"  u ({l}): {u}")
        return (k, s, m, t, l, u)

    else:  # готовые примеры
        examples = [
            (4, list("abcd"), 5, list("bcdef"), 6, list("bcdefg")),
            (6, list("a b c d e f".replace(" ", "")), 6, list("z x c v b n".replace(" ", "")), 6, list("q w c r t b".replace(" ", ""))),
            (5, list("12345"), 5, list("34567"), 5, list("35790")),
            (3, list("xyz"), 3, list("zyx"), 3, list("yxz")),
        ]
        print("\nГотовые примеры:")
        for idx, (k_val, s_vals, m_val, t_vals, l_val, u_vals) in enumerate(examples, 1):
            print(f"{idx}: s={s_vals}, t={t_vals}, u={u_vals}")
        while True:
            try:
                num = int(input("Выберите номер примера: "))
                if 1 <= num <= len(examples):
                    return examples[num - 1]
                else:
                    print(f"Номер должен быть от 1 до {len(examples)}.")
            except ValueError:
                print("Ошибка ввода. Введите целое число.")


def main():
    k, s, m, t, l, u = get_data()

    # Множества для быстрого поиска
    set_t = set(t)
    set_u = set(u)

    # Собираем общие символы, сохраняя порядок s и уникальность
    common = []
    for ch in s:
        if ch in set_t and ch in set_u and ch not in common:
            common.append(ch)

    # Вывод результатов
    print("\nРезультаты:")
    print(f"  Последовательность s: {s}")
    print(f"  Последовательность t: {t}")
    print(f"  Последовательность u: {u}")
    print(f"  Общие символы (по одному разу, в порядке s): {common}")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")