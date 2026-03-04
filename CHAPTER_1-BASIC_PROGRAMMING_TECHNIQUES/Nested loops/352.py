"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
10. Вложенные циклы

352. Пусть цвета экрана имеют номера 0, 1, ... ,k. Высветить все
точки экрана (или точки некоторой прямоугольной области) различными цветами, используя для точки с координатами i,j цвет с номером, равным остатку от деления abs(m) на k + 1, где m может быть взято, например, равным:
а) i + j;                                                    б) (i - 10) * (i - 10) + 25 * j * 25 * j;
в) (i - 50) * (i - 50) - j;                                  г) 25 * (i + 5) + (i - 5) * j * j;
д) (i - 50) * (i - 50) - (j - 50) * (j - 50) * (j - 50);     е) (i * i + j * j) - 2 * (i * i - j * j).
"""


import math

def get_m(i, j, choice):
    """Вычисляет значение m по выбранной формуле."""
    if choice == 'a':
        return i + j
    elif choice == 'b':
        return (i - 10)**2 + 25 * j**2
    elif choice == 'c':
        return (i - 50)**2 - j
    elif choice == 'd':
        return 25 * (i + 5) + (i - 5) * j**2
    elif choice == 'e':
        return (i - 50)**2 - (j - 50)**3
    elif choice == 'f':
        return (i**2 + j**2) - 2 * (i**2 - j**2)
    else:
        return 0

def main():
    print("Выберите формулу для вычисления цвета:")
    print("а) i + j")
    print("б) (i-10)^2 + 25j^2")
    print("в) (i-50)^2 - j")
    print("г) 25(i+5) + (i-5)j^2")
    print("д) (i-50)^2 - (j-50)^3")
    print("е) (i^2+j^2) - 2(i^2 - j^2)")
    choice = input("Введите букву (а-е): ").strip().lower()

    # Преобразование русских букв в латинские для удобства
    ru_to_en = {'а': 'a', 'б': 'b', 'в': 'c', 'г': 'd', 'д': 'e', 'е': 'f'}
    if choice in ru_to_en:
        choice = ru_to_en[choice]

    if choice not in ('a', 'b', 'c', 'd', 'e', 'f'):
        print("Неверный выбор.")
        return

    try:
        i_min = int(input("Введите минимальное i: "))
        i_max = int(input("Введите максимальное i: "))
        j_min = int(input("Введите минимальное j: "))
        j_max = int(input("Введите максимальное j: "))
        k = int(input("Введите k (максимальный номер цвета): "))
    except ValueError:
        print("Ошибка ввода. Введите целые числа.")
        return

    if i_max < i_min or j_max < j_min:
        print("Неверные границы области.")
        return

    print(f"\nЦвета точек (номера от 0 до {k}) для области i=[{i_min},{i_max}], j=[{j_min},{j_max}]:")
    for i in range(i_min, i_max + 1):
        row = []
        for j in range(j_min, j_max + 1):
            m = get_m(i, j, choice)
            color = int(abs(m)) % (k + 1)
            row.append(f"{color:3d}")
        print(" ".join(row))

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
