"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
6. Пошаговый ввод данных и вывод результатов *)

152. Даны натуральное число n, действительные числа a, h, b, d0, ..., dn. Вычислисть d0 + d1 * (b - a) + d2 * (b - a) * (b - a - h) + ... + dn * (b - a) * (b - a - h) ... (b - a * (n - 1) * h).
"""


def main():
    print("Вычисление суммы со сложной структурой")
    print("=" * 70)
    
    # Ввод параметров
    n = int(input("Введите n: "))
    if n < 0:
        print("Ошибка: n должно быть неотрицательным!")
        return
    
    a = float(input("Введите a: "))
    h = float(input("Введите h: "))
    b = float(input("Введите b: "))
    
    # Инициализация
    total = 0.0
    product = 1.0
    max_product = 1.0
    terms = []
    
    print("\nВычисление:")
    print(f"{'k':>4} {'d_k':>10} {'Множитель':>15} {'Произведение':>15} {'Слагаемое':>15} {'Сумма':>15}")
    print("-" * 80)
    
    for k in range(n + 1):
        d = float(input(f"d{k} = "))
        
        # Вычисляем слагаемое
        term = d * product
        total += term
        
        # Запоминаем для вывода
        if k == 0:
            factor_str = "1"
        else:
            factor_str = f"(b-a-{k-1}h)"
        
        print(f"{k:4} {d:10.4f} {factor_str:>15} {product:15.6f} {term:15.6f} {total:15.6f}")
        
        # Обновляем произведение для следующего слагаемого
        if k < n:
            factor = b - a - k * h
            product *= factor
            max_product = max(max_product, abs(product))
        
        terms.append(term)
    
    # Анализ результатов
    print("\n" + "=" * 80)
    print("Анализ:")
    print(f"Количество слагаемых: {n+1}")
    print(f"Итоговая сумма: {total}")
    
    # Проверка на переполнение
    if max_product > 1e100:
        print("Внимание: произведение множителей достигло очень больших значений!")
    
    # Наибольшее по модулю слагаемое
    max_term = max(abs(term) for term in terms)
    max_index = max(range(len(terms)), key=lambda i: abs(terms[i]))
    
    print(f"Наибольшее по модулю слагаемое: terms[{max_index}] = {terms[max_index]}")
    print(f"Его вклад: {abs(terms[max_index]/total)*100:.2f}% от итоговой суммы")
    
    # Проверка точности (если сумма мала по сравнению со слагаемыми)
    if abs(total) < 1e-10 * max_term:
        print("Внимание: возможная потеря точности - сумма мала по сравнению со слагаемыми")

if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
