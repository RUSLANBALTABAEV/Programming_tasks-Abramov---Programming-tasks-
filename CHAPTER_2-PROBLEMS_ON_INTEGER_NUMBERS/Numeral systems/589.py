"""
ГЛАВА 2
ЗАДАЧИ ПО ТЕМАМ
16. Системы счисления

589. Даны натуральное число n, целые числа a0,…, an , такие, что каждое ai равно нулю или единице и an != 0. Последовательность a0, ...., an задает двоичное представление некоторого целого числа p = an * 2 ^ n + ... + a1 * 2 + a0. Получить последовательность нулей и единиц, задающую двоичное представление:
a) числа p + 1;
b) числа p - 1;
c) числа 3p.
"""


# ==========================================================
# ЗАДАЧА 589: Арифметические операции над двоичными числами
# §16. Системы счисления
# ==========================================================

import random


def get_params():
    """Выбор способа ввода двоичного числа."""
    print("Задача 589: Двоичные операции (p+1, p-1, 3p)")
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
            s = input("Введите двоичное представление p (например, 1011): ").strip()
            if not all(c in '01' for c in s):
                print("Ошибка: строка должна состоять только из 0 и 1.")
                continue
            if s[0] == '0':
                print("Ошибка: старший разряд (a_n) не должен быть равен 0.")
                continue
            return s

    elif choice == '2':
        length = random.randint(1, 10)
        # Первый бит всегда 1, остальные случайно 0 или 1
        bits = '1' + ''.join(random.choice('01') for _ in range(length - 1))
        print(f"\nСгенерировано: p = {bits}_2")
        return bits

    else:  # готовые примеры
        examples = ["1", "10", "111", "1011", "10000", "111111", "1010101"]
        print("\nГотовые примеры (двоичные последовательности):")
        for idx, val in enumerate(examples, 1):
            print(f"{idx}: {val}")
        while True:
            try:
                num = int(input("Выберите номер примера: "))
                if 1 <= num <= len(examples):
                    return examples[num - 1]
                else:
                    print(f"Номер должен быть от 1 до {len(examples)}.")
            except ValueError:
                print("Ошибка ввода. Введите целое число.")


def add_one(bits):
    """
    Прибавляет 1 к двоичному числу (строка).
    Идем справа налево, меняем 1 на 0 (перенос), пока не встретим 0,
    который меняем на 1.
    """
    res = list(bits)
    i = len(res) - 1
    while i >= 0 and res[i] == '1':
        res[i] = '0'
        i -= 1
    
    if i >= 0:
        res[i] = '1'
    else:
        # Если все были 1 (например, 111 + 1 = 1000)
        res.insert(0, '1')
    return "".join(res)


def sub_one(bits):
    """
    Вычитает 1 из двоичного числа (строка).
    Идем справа налево, меняем 0 на 1 (заем), пока не встретим 1,
    которую меняем на 0.
    """
    # Особый случай: 1 - 1 = 0
    if bits == "1":
        return "0"
        
    res = list(bits)
    i = len(res) - 1
    while i >= 0 and res[i] == '0':
        res[i] = '1'
        i -= 1
        
    if i >= 0:
        res[i] = '0'
        
    # Удаляем ведущие нули (если они появились)
    idx = 0
    while idx < len(res) - 1 and res[idx] == '0':
        idx += 1
    return "".join(res[idx:])


def multiply_by_3(bits):
    """
    Умножает двоичное число на 3.
    3p = 2p + p. Умножение на 2 — это дописывание нуля справа (сдвиг).
    Затем складываем сдвинутое число и исходное побитово.
    """
    p_shifted = bits + '0'  # Это 2p
    p_orig = bits           # Это p
    
    res = []
    carry = 0
    i = len(p_shifted) - 1
    j = len(p_orig) - 1
    
    # Классическое сложение в столбик с конца
    while i >= 0 or j >= 0 or carry:
        val = carry
        if i >= 0:
            val += int(p_shifted[i])
            i -= 1
        if j >= 0:
            val += int(p_orig[j])
            j -= 1
            
        res.append(str(val % 2))
        carry = val // 2
        
    return "".join(res[::-1])


def main():
    bits = get_params()
    p = int(bits, 2)

    print(f"\nИсходные данные: p = {bits}_2 (в десятичной: {p})")
    print("=" * 60)

    # Вычисления
    res_a = add_one(bits)
    res_b = sub_one(bits) if p > 1 else "0"
    res_c = multiply_by_3(bits)

    # 1. Вывод результатов
    print("а) Двоичное представление p + 1:")
    print(f"   {res_a}_2")
    print(f"   (в десятичной: {int(res_a, 2)})")

    print("\nб) Двоичное представление p - 1:")
    print(f"   {res_b}_2")
    print(f"   (в десятичной: {int(res_b, 2)})")

    print("\nв) Двоичное представление 3p:")
    print(f"   {res_c}_2")
    print(f"   (в десятичной: {int(res_c, 2)})")

    # 2. Проверки
    print("\n--- Проверка ---")

    check_a = int(res_a, 2) == p + 1
    print(f"а) int({res_a}_2) == {p} + 1  ->  {check_a}")

    if p > 0:
        check_b = int(res_b, 2) == p - 1
        print(f"б) int({res_b}_2) == {p} - 1  ->  {check_b}")
    else:
        print("б) p = 0, вычитание не имеет смысла в натуральных числах.")

    check_c = int(res_c, 2) == 3 * p
    print(f"в) int({res_c}_2) == 3 * {p}  ->  {check_c}")

    print("=" * 60)


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")