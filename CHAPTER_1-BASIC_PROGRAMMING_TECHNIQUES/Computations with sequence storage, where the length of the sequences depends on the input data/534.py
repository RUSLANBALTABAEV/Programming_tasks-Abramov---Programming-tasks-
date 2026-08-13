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

534. Даны натуральное число n, действительные числа a1, ..., a2n.
Получить:
а) (a1 - a2n) * (a3 - a2n - 2) * (a5 - a2n - 4) ... (a2n - 1 - a2);
б) a1 * a2n + a2 * a2n - 1 + ... + an * an + 1;
в) min(a1 + an + 1, a2 + an + 2, an + a2n);
г) max(min(a1, a2n), min(a2, a2n - 1), ..., min(an, an + 1)).
"""


# ==========================================================
# ЧАСТЬ 1: Структура для двусвязного списка (для Варианта Б)
# ==========================================================

class Node:
    """Узел двусвязного списка."""
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


# ==========================================================
# ЧАСТЬ 2: Решение с использованием стандартного списка
# ==========================================================

def solve_list(data):
    """Решает задачу с использованием стандартного списка Python."""
    n = len(data) // 2  # Всего 2n элементов
    
    # а) Произведение: (a1 - a2n)(a3 - a2n-2) ... (a2n-1 - a2)
    res_a = 1.0
    for i in range(n):
        left_idx = 2 * i            # Индексы a1, a3, a5...
        right_idx = 2 * n - 2 * i - 1 # Индексы a2n, a2n-2...
        res_a *= (data[left_idx] - data[right_idx])

    # б) Сумма: a1*a2n + a2*a2n-1 + ... + an*an+1
    res_b = 0.0
    for i in range(n):
        left_idx = i
        right_idx = 2 * n - 1 - i
        res_b += (data[left_idx] * data[right_idx])

    # в) Минимум: min(a1 + an+1, a2 + an+2, ..., an + a2n)
    res_c = float('inf')
    for i in range(n):
        left_idx = i
        right_idx = n + i
        current_sum = data[left_idx] + data[right_idx]
        if current_sum < res_c:
            res_c = current_sum

    # г) Максимум из минимальных: max(min(a1, a2n), min(a2, a2n-1), ..., min(an, an+1))
    res_d = float('-inf')
    for i in range(n):
        left_idx = i
        right_idx = 2 * n - 1 - i
        min_val = min(data[left_idx], data[right_idx])
        if min_val > res_d:
            res_d = min_val

    return res_a, res_b, res_c, res_d


# ==========================================================
# ЧАСТЬ 3: Решение с использованием двусвязного списка
# ==========================================================

def solve_linked_list(data):
    """Решает задачу с использованием двусвязного списка (обход с двух концов)."""
    n = len(data) // 2
    head, tail = build_doubly_linked_list(data)
    
    # а) Произведение: (a1 - a2n)(a3 - a2n-2) ... 
    left = head
    right = tail
    res_a = 1.0
    for _ in range(n):
        res_a *= (left.val - right.val)
        left = left.next.next   # Переходим через один узел вправо (к a3, a5...)
        right = right.prev.prev # Переходим через один узел влево (к a2n-2, a2n-4...)

    # б) Сумма: a1*a2n + a2*a2n-1 + ...
    left = head
    right = tail
    res_b = 0.0
    for _ in range(n):
        res_b += (left.val * right.val)
        left = left.next
        right = right.prev

    # в) Минимум: min(a1 + an+1, a2 + an+2, ...)
    left = head
    right = tail
    # Сдвигаем правый указатель на n-1 шагов назад, чтобы он указывал на an+1
    for _ in range(n - 1):
        right = right.prev

    res_c = float('inf')
    for _ in range(n):
        current_sum = left.val + right.val
        if current_sum < res_c:
            res_c = current_sum
        left = left.next
        right = right.next  # Двигаемся к a_{n+2}, a_{n+3}...

    # г) Максимум из минимальных: max(min(a1, a2n), min(a2, a2n-1), ...)
    left = head
    right = tail
    res_d = float('-inf')
    for _ in range(n):
        min_val = min(left.val, right.val)
        if min_val > res_d:
            res_d = min_val
        left = left.next
        right = right.prev

    return res_a, res_b, res_c, res_d


# ==========================================================
# ЧАСТЬ 4: Основная программа
# ==========================================================

def main():
    print("=== ЗАДАЧА 534: Вычисления с симметричными элементами ===\n")
    
    try:
        n = int(input("Введите число n (количество пар): "))
        if n < 1:
            print("Ошибка: n должно быть больше 0.")
            return
            
        total_nums = 2 * n
        print(f"Введите {total_nums} действительных чисел через пробел:")
        data = list(map(float, input().split()))
        
        if len(data) != total_nums:
            print(f"Ошибка: введено {len(data)} чисел, а ожидается {total_nums}.")
            return

        print("\nВыберите способ решения:")
        print("1. Стандартный список (массив Python)")
        print("2. Двусвязный список (обход с двух концов)")
        choice = input("Ваш выбор (1/2): ").strip()

        if choice == '1':
            res_a, res_b, res_c, res_d = solve_list(data)
        elif choice == '2':
            res_a, res_b, res_c, res_d = solve_linked_list(data)
        else:
            print("Неверный выбор. Используется стандартный список.")
            res_a, res_b, res_c, res_d = solve_list(data)

        # Вывод результатов
        print(f"\nИсходные данные: {data}")
        print("-" * 40)
        print(f"а) Произведение (a1 - a2n)...(a2n-1 - a2) = {res_a:.6f}")
        print(f"б) Сумма a1*a2n + ... + an*an+1 = {res_b:.6f}")
        print(f"в) min(a1 + an+1, ..., an + a2n) = {res_c:.6f}")
        print(f"г) max(min(a1, a2n), ..., min(an, an+1)) = {res_d:.6f}")
        
    except ValueError:
        print("Ошибка: введите корректные числа.")

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")