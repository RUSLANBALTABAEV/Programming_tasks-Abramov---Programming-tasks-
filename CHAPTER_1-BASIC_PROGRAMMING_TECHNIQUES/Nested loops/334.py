"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
10. Вложенные циклы

334. Вычислить
а) 100Ei=1 * 50Ej=1 * 1 / i + j * j;       б) 100Ei=1 * 60Ej=1 * sin(i * i * i + j * j * j * j);
в) 100Ei=1 * 100Ej=1 * j - i + 1 / i + j;  г) 100Ei=1 * iEj=1 * 1 / 2 * j + i
"""


import math

def compute_a():
    total = 0.0
    for i in range(1, 101):
        for j in range(1, 51):
            total += 1 / (i + j * j)
    return total

def compute_b():
    total = 0.0
    for i in range(1, 101):
        i3 = i ** 3
        for j in range(1, 61):
            total += math.sin(i3 + j ** 4)
    return total

def compute_c():
    total = 0.0
    for i in range(1, 101):
        for j in range(1, 101):
            total += (j - i + 1) / (i + j)
    return total

def compute_d():
    total = 0.0
    for i in range(1, 101):
        for j in range(1, i + 1):
            total += 1 / (2 * j + i)
    return total

def main():
    print("Вычисление сумм из задачи 334:\n")
    print("a) Σ_{i=1}^{100} Σ_{j=1}^{50} 1/(i + j^2) =", compute_a())
    print("б) Σ_{i=1}^{100} Σ_{j=1}^{60} sin(i^3 + j^4) =", compute_b())
    print("в) Σ_{i=1}^{100} Σ_{j=1}^{100} (j - i + 1)/(i + j) =", compute_c())
    print("г) Σ_{i=1}^{100} Σ_{j=1}^{i} 1/(2j + i) =", compute_d())

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
