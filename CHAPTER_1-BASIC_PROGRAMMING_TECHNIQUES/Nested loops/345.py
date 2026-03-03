"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
10. Вложенные циклы

345. Пусть 
t0 = 1, tk = t0*tk-1+t1*tk-2+...+tk-2*t1+tk-1*t0, k=1,2, ....
Получить t10.
"""


def compute_t(k):
    """Вычисляет t_k по рекуррентной формуле:
    t_0 = 1, t_k = sum_{i=0}^{k-1} t_i * t_{k-1-i} для k>=1.
    Это числа Каталана."""
    t = [1]  # t_0
    for n in range(1, k+1):
        s = 0
        for i in range(n):
            s += t[i] * t[n-1-i]
        t.append(s)
    return t[k]

def main():
    t10 = compute_t(10)
    print(f"t_10 = {t10}")

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
