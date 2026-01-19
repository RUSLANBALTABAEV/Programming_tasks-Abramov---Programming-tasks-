"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
7. Сочетания цикла и разветвления

184. Даны целые числа p, q, a1, … , a67 (p > q >= 0). В последовательности a1, … , a67 заменить нулями члены, модуль которых при делении на p дает в остатке q.
"""


def main():
    # Ввод p и q
    print("Введите целые числа p и q (p > q ≥ 0):")
    
    while True:
        try:
            p = int(input("p = "))
            q = int(input("q = "))
            
            if p > q and q >= 0:
                break
            else:
                print("Ошибка: должно выполняться условие p > q ≥ 0!")
                print("Пожалуйста, введите p и q снова.")
        except ValueError:
            print("Пожалуйста, введите целые числа!")
    
    # Инициализация списка для результатов
    result = []
    
    print(f"\nВведите 67 целых чисел:")
    
    # Ввод и обработка 67 чисел
    for i in range(1, 68):
        while True:
            try:
                a = int(input(f"a[{i}]: "))
                break
            except ValueError:
                print("Пожалуйста, введите целое число!")
        
        # Проверяем условие: |a| mod p == q
        if abs(a) % p == q:
            result.append(0)
        else:
            result.append(a)
    
    # Вывод результатов
    print("\nРезультат (замененные последовательность):")
    
    # Выводим в красивом формате - по 10 чисел в строке
    for i in range(0, 67, 10):
        # Получаем подсписок из 10 элементов (или меньше для последней строки)
        line = result[i:min(i+10, 67)]
        # Формируем строку с индексами
        line_str = []
        for j, num in enumerate(line, start=i+1):
            line_str.append(f"a[{j}]={num}")
        
        print(", ".join(line_str))

if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
