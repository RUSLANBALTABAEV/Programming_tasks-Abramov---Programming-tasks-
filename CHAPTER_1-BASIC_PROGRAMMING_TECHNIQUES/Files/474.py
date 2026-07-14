"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

474. Дано натуральное n. Записать в файл g целые числа b1, …, bn, определенные так, как указано в заданиях а) - д) задачи 139. 
"""


import random
import math


# ------------------------------------------------------------
# 1. Функции генерации последовательностей из задачи 139 (а–д)
# ------------------------------------------------------------
def generate_a(n):
    """а) b_i = i"""
    return list(range(1, n + 1))

def generate_b(n):
    """б) b_i = i^2"""
    return [i * i for i in range(1, n + 1)]

def generate_c(n):
    """в) b_i = i!"""
    seq = []
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        seq.append(fact)
    return seq

def generate_d(n):
    """г) b_i = 2^(i+1)"""
    return [2 ** (i + 1) for i in range(1, n + 1)]

def generate_e(n):
    """д) b_i = 2^i + 3^(i+1)"""
    return [(2 ** i) + (3 ** (i + 1)) for i in range(1, n + 1)]


# ------------------------------------------------------------
# 2. Запись в файл (единый файл g.txt)
# ------------------------------------------------------------
def write_all_to_file(filename, n, seq_a, seq_b, seq_c, seq_d, seq_e):
    """
    Записывает все последовательности в один файл.
    Каждая последовательность предваряется заголовком (а) – д).
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"Последовательности b1..b{n} для задачи 139:\n\n")
        f.write("а) i:\n")
        f.write(" ".join(map(str, seq_a)) + "\n\n")
        f.write("б) i^2:\n")
        f.write(" ".join(map(str, seq_b)) + "\n\n")
        f.write("в) i!:\n")
        f.write(" ".join(map(str, seq_c)) + "\n\n")
        f.write("г) 2^(i+1):\n")
        f.write(" ".join(map(str, seq_d)) + "\n\n")
        f.write("д) 2^i + 3^(i+1):\n")
        f.write(" ".join(map(str, seq_e)) + "\n")
    print(f"Все последовательности записаны в файл '{filename}'.")


# ------------------------------------------------------------
# 3. Ввод числа n (с выбором способа)
# ------------------------------------------------------------
def get_n():
    print("Задача 474: Запись последовательностей из задачи 139 в файл g.txt")
    print("Выберите способ ввода:")
    print("1 — Ручной ввод числа n")
    print("2 — Случайная генерация n")
    print("3 — Готовые примеры")

    while True:
        choice = input("Ваш выбор (1/2/3): ").strip()
        if choice in ('1', '2', '3'):
            break
        print("Ошибка: выберите 1, 2 или 3.")

    if choice == '1':
        while True:
            try:
                n = int(input("Введите натуральное число n: "))
                if n <= 0:
                    print("n должно быть положительным.")
                    continue
                return n
            except ValueError:
                print("Ошибка ввода. Введите целое число.")

    elif choice == '2':
        n = random.randint(3, 8)
        print(f"Сгенерировано n = {n}")
        return n

    else:  # готовые примеры
        examples = [3, 5, 7]
        print("Готовые примеры n:", examples)
        while True:
            try:
                num = int(input("Выберите номер примера (1-3): "))
                if 1 <= num <= len(examples):
                    return examples[num - 1]
                else:
                    print(f"Номер от 1 до {len(examples)}.")
            except ValueError:
                print("Введите целое число.")


# ------------------------------------------------------------
# 4. Основная программа
# ------------------------------------------------------------
def main():
    n = get_n()

    print(f"\nГенерация последовательностей для n = {n}...")
    seq_a = generate_a(n)
    seq_b = generate_b(n)
    seq_c = generate_c(n)
    seq_d = generate_d(n)
    seq_e = generate_e(n)

    # Запись в файл g.txt
    write_all_to_file("g.txt", n, seq_a, seq_b, seq_c, seq_d, seq_e)

    # Дополнительно выводим для контроля
    print("\nСгенерированные последовательности (первые 10 элементов, если больше):")
    limit = min(n, 10)
    print(f"а) i:       {seq_a[:limit]}")
    print(f"б) i^2:     {seq_b[:limit]}")
    print(f"в) i!:      {seq_c[:limit]}")
    print(f"г) 2^(i+1): {seq_d[:limit]}")
    print(f"д) 2^i+3^(i+1): {seq_e[:limit]}")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
