"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
12. Использование процедур 

В задачах этого параграфа будем для краткости говорить просто о процедурах, подразумевая, что решающий задачи сам выберет подходящее средство программирования – подпрограмму, функцию и 
т. д. Этот выбор должен быть сделан с учётом как характера задач, так и особенностей используемого языка программирования.

439. Даны действительные числа u1, u2, v1, v2, w1, w2. Получить 2 * u + (3 * u * w) / (2 + w - v) - 7, где u, v, w – комплексные числа u1 + i * u2, v1 + i * v2, w1 + i * w2. (Определить процедуры выполнения арифметических операций над комплексными числами.)
"""


import random


# ------------------------------------------------------------
# Арифметические операции над комплексными числами (re, im)
# ------------------------------------------------------------
def add_complex(c1, c2):
    return (c1[0] + c2[0], c1[1] + c2[1])


def sub_complex(c1, c2):
    return (c1[0] - c2[0], c1[1] - c2[1])


def mul_complex(c1, c2):
    # (a + bi) * (c + di) = (ac - bd) + (ad + bc)i
    return (c1[0] * c2[0] - c1[1] * c2[1], c1[0] * c2[1] + c1[1] * c2[0])


def div_complex(c1, c2):
    # (a + bi)/(c + di) = ((ac + bd) + (bc - ad)i) / (c^2 + d^2)
    a, b = c1
    c, d = c2
    denom = c * c + d * d
    if denom == 0:
        raise ZeroDivisionError("Деление на ноль в комплексном знаменателе.")
    return ((a * c + b * d) / denom, (b * c - a * d) / denom)


# ------------------------------------------------------------
# Ввод данных
# ------------------------------------------------------------
def get_data():
    """Выбор способа ввода чисел u1, u2, v1, v2, w1, w2."""
    print("Задача 439: 2u + (3 * u * w) / (2 + w - v) - 7")
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
                print("Введите 6 действительных чисел: u1 u2 v1 v2 w1 w2")
                data = list(map(float, input().split()))
                if len(data) != 6:
                    print("Нужно ровно 6 чисел.")
                    continue
                return tuple(data)
            except ValueError:
                print("Ошибка ввода.")

    elif choice == '2':
        data = [round(random.uniform(-5, 5), 2) for _ in range(6)]
        print(f"Сгенерированы числа: {data}")
        return tuple(data)

    else:  # готовые примеры
        examples = [
            (1.0, 0.0, 0.0, 0.0, 1.0, 0.0),   # u = 1, v = 0, w = 1
            (0.0, 1.0, 0.0, 1.0, 0.0, 1.0),   # u = i, v = i, w = i
            (2.0, -1.0, 3.0, 0.5, -1.0, 2.0),
        ]
        print("Готовые примеры:")
        for idx, vals in enumerate(examples, 1):
            print(f"{idx}: {vals}")
        while True:
            try:
                num = int(input("Выберите номер примера: "))
                if 1 <= num <= len(examples):
                    return examples[num - 1]
                else:
                    print(f"Номер от 1 до {len(examples)}.")
            except ValueError:
                print("Введите целое число.")


# ------------------------------------------------------------
# Основная программа
# ------------------------------------------------------------
def main():
    u1, u2, v1, v2, w1, w2 = get_data()
    u = (u1, u2)
    v = (v1, v2)
    w = (w1, w2)

    # Вычисляем по частям
    two_u = mul_complex((2.0, 0.0), u)               # 2u
    three_u_w = mul_complex(mul_complex((3.0, 0.0), u), w)  # 3 * u * w
    denom = add_complex(sub_complex(w, v), (2.0, 0.0))      # 2 + w - v
    fraction = div_complex(three_u_w, denom)         # (3uw) / (2 + w-v)
    result = sub_complex(add_complex(two_u, fraction), (7.0, 0.0))

    # Вывод
    print("\nПромежуточные значения:")
    print(f"u = {u1} + {u2}i")
    print(f"v = {v1} + {v2}i")
    print(f"w = {w1} + {w2}i")
    print(f"2u = {two_u[0]:.4f} + {two_u[1]:.4f}i")
    print(f"3 * u * w = {three_u_w[0]:.4f} + {three_u_w[1]:.4f}i")
    print(f"2 + w - v = {denom[0]:.4f} + {denom[1]:.4f}i")
    print(f"(3uw) / (2 + w - v) = {fraction[0]:.4f} + {fraction[1]:.4f}i")
    if result[1] >= 0:
        print(f"Ответ: {result[0]:.4f} + {result[1]:.4f}i")
    else:
        print(f"Ответ: {result[0]:.4f} - {abs(result[1]):.4f}i")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
