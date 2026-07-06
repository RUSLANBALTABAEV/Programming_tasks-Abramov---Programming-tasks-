"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
12. Использование процедур 

В задачах этого параграфа будем для краткости говорить просто о процедурах, подразумевая, что решающий задачи сам выберет подходящее средство программирования – подпрограмму, функцию и 
т. д. Этот выбор должен быть сделан с учётом как характера задач, так и особенностей используемого языка программирования.

461. Составить процедуру построения строки символов, являющейся записью заданного действительного числа в десятичной системе счисления; строка должна содержать указанное количество цифр после запятой.
"""


import random


def number_to_decimal_string(num, k):
    """
    Процедура построения строки для заданного действительного числа num
    с k цифрами после запятой.
    """
    is_negative = num < 0
    num = abs(num)

    # Целая часть
    integer_part = int(num)

    # Дробная часть: умножаем на 10^k, округляем до ближайшего целого
    fractional_scaled = int(round((num - integer_part) * (10 ** k)))

    # Преобразуем в строку с ведущими нулями
    fractional_str = str(fractional_scaled).zfill(k)

    if k > 0:
        result = f"{integer_part}.{fractional_str}"
    else:
        result = str(integer_part)

    return f"-{result}" if is_negative else result


def get_input():
    """Выбор способа ввода числа и количества знаков."""
    print("Задача 461: Построение строки десятичного представления числа")
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
                num = float(input("Введите действительное число: "))
                k = int(input("Введите количество цифр после запятой: "))
                if k < 0:
                    print("Количество цифр должно быть >= 0.")
                    continue
                return num, k
            except ValueError:
                print("Ошибка ввода.")

    elif choice == '2':
        num = round(random.uniform(-1000, 1000), 6)
        k = random.randint(0, 6)
        print(f"Сгенерировано число: {num}, цифр после запятой: {k}")
        return num, k

    else:
        examples = [
            (123.456, 2),
            (-5.04, 3),
            (0.1, 5),
            (3.14159265, 4),
            (-0.0005, 6)
        ]
        print("Готовые примеры:")
        for idx, (val, digits) in enumerate(examples, 1):
            print(f"{idx}: число = {val}, знаков = {digits}")
        while True:
            try:
                num_ex = int(input("Выберите номер примера: "))
                if 1 <= num_ex <= len(examples):
                    return examples[num_ex - 1]
                else:
                    print(f"Номер от 1 до {len(examples)}.")
            except ValueError:
                print("Введите целое число.")


def main():
    num, k = get_input()
    result_str = number_to_decimal_string(num, k)
    print(f"\nИсходное число: {num}")
    print(f"Количество цифр после запятой: {k}")
    print(f"Строковое представление: '{result_str}'")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
