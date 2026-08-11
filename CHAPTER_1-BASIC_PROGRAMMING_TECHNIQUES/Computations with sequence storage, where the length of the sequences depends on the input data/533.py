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

533. Даны натуральное число n, действительный числа x1, ..., xn. 
Вычислить:
а) x1 * xn + x2 * xn - 1 + ... + xn * x1;
б) (x1 + xn) * (x2 + xn - 1) ... (xn + x1);
в) (x1 + x2 + 2 * xn) * (x2 + x3 + 2 * xn - 1) ... (xn - 1 + xn + 2 * x2).
Для решения этой задачи полезен список, изображенный на рис. 27.
"""


# ==========================================================
# ЧАСТЬ 1: Структура для двусвязного списка (Рис. 27)
# ==========================================================

class Node:
    """Узел двусвязного списка (как на рис. 27)."""
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

def build_doubly_linked_list(data):
    """Строит двусвязный список и возвращает голову и хвост."""
    if not data:
        return None, None
    head = Node(data[0])
    current = head
    for val in data[1:]:
        new_node = Node(val)
        current.next = new_node
        new_node.prev = current
        current = new_node
    return head, current  # current здесь — это хвост (tail)

def solve_linked_list(data):
    """Решает задачу с использованием двусвязного списка (Рис. 27)."""
    if not data:
        return None, None, None
    
    head, tail = build_doubly_linked_list(data)
    
    # --- а) Сумма x1*xn + x2*xn-1 + ... + xn*x1 ---
    left = head
    right = tail
    result_a = 0.0
    # Проходимся одновременно с обоих концов
    while left is not None and right is not None and left != right:
        result_a += left.val * right.val
        left = left.next
        right = right.prev
    # Если количество элементов нечётное, центральный умножается сам на себя
    if left == right:
        result_a += left.val * left.val

    # --- б) Произведение (x1+xn)(x2+xn-1)...(xn+x1) ---
    left = head
    right = tail
    result_b = 1.0
    while left is not None and right is not None and left != right:
        result_b *= (left.val + right.val)
        left = left.next
        right = right.prev
    if left == right:
        result_b *= (left.val + left.val)

    # --- в) Произведение (x1+x2+2xn)(x2+x3+2xn-1)...(xn-1+xn+2x2) ---
    left = head
    right = tail
    result_c = 1.0
    # Итераций должно быть ровно n-1
    while left.next is not None:
        term = left.val + left.next.val + 2 * right.val
        result_c *= term
        left = left.next
        right = right.prev
        
    return result_a, result_b, result_c


# ==========================================================
# ЧАСТЬ 2: Решение с использованием стандартного списка
# ==========================================================

def solve_list(data):
    """Решает задачу с использованием стандартного списка Python."""
    n = len(data)
    
    # а) Сумма симметричных произведений
    result_a = 0.0
    for i in range(n):
        result_a += data[i] * data[n - 1 - i]
        
    # б) Произведение симметричных сумм
    result_b = 1.0
    for i in range(n):
        result_b *= (data[i] + data[n - 1 - i])
        
    # в) Произведение скользящих сумм с удвоенным симметричным элементом
    result_c = 1.0
    for i in range(n - 1):
        # Элемент с конца, который нужно удвоить: x_{n-i}
        # В Python индексе: n-1-i
        result_c *= (data[i] + data[i + 1] + 2 * data[n - 1 - i])
        
    return result_a, result_b, result_c


# ==========================================================
# ЧАСТЬ 3: Основная программа
# ==========================================================

def main():
    print("=== ЗАДАЧА 533: Вычисление выражений с симметричными элементами ===\n")
    
    try:
        n = int(input("Введите количество чисел n (n >= 2): "))
        if n < 2:
            print("Ошибка: n должно быть больше или равно 2.")
            return
            
        print(f"Введите {n} действительных чисел через пробел:")
        data = list(map(float, input().split()))
        
        if len(data) != n:
            print(f"Ошибка: введено {len(data)} чисел, а ожидается {n}.")
            return

        print("\nВыберите способ решения:")
        print("1. Стандартный список (массив Python)")
        print("2. Двусвязный список (как на Рис. 27)")
        choice = input("Ваш выбор (1/2): ").strip()

        if choice == '1':
            res_a, res_b, res_c = solve_list(data)
        elif choice == '2':
            res_a, res_b, res_c = solve_linked_list(data)
        else:
            print("Неверный выбор. Используется стандартный список.")
            res_a, res_b, res_c = solve_list(data)

        # Вывод результатов
        print(f"\nИсходные данные: {data}")
        print("-" * 40)
        print(f"а) Сумма x1*xn + ... + xn*x1 = {res_a:.6f}")
        print(f"б) Произведение (x1+xn)...(xn+x1) = {res_b:.6f}")
        print(f"в) Произведение (x1+x2+2xn)...(x{{n-1}}+xn+2x2) = {res_c:.6f}")
        
    except ValueError:
        print("Ошибка: введите корректные числа.")

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")