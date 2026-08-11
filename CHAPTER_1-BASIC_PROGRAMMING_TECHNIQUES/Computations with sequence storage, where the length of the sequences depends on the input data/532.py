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

532. Даны натуральное число n, действительны числа a1, ..., an. Если последовательность a1, ..., an упорядочена по неубыванию (т.е. если a1 <= a2 <= ... <= an), то оставить ее без изменения. Иначе получить последовательность an, ..., a1.
Для решения этой задачи полезен список, изображенный на рис. 26.
"""


# ==========================================================
# ЧАСТЬ 1: Решение с использованием двусвязного списка (Рис. 26)
# ==========================================================

class Node:
    """Узел двусвязного списка (как на рис. 26)."""
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

def is_sorted_dll(head):
    """Проверяет, упорядочен ли двусвязный список по неубыванию."""
    current = head
    while current and current.next:
        if current.val > current.next.val:
            return False
        current = current.next
    return True

def get_sequence_from_dll(head, tail, reverse=False):
    """Извлекает значения из списка (прямо или обратно)."""
    result = []
    if reverse:
        current = tail
        while current:
            result.append(current.val)
            current = current.prev
    else:
        current = head
        while current:
            result.append(current.val)
            current = current.next
    return result

def solve_linked_list(data):
    """Решает задачу с использованием двусвязного списка."""
    head, tail = build_doubly_linked_list(data)
    if is_sorted_dll(head):
        return get_sequence_from_dll(head, tail, reverse=False)
    else:
        return get_sequence_from_dll(head, tail, reverse=True)


# ==========================================================
# ЧАСТЬ 2: Решение с использованием стандартного списка
# ==========================================================

def solve_list(data):
    """Решает задачу с использованием стандартного списка Python."""
    # Проверяем условие a1 <= a2 <= ... <= an
    # zip(data, data[1:]) создаёт пары соседних элементов для сравнения
    is_sorted = all(x <= y for x, y in zip(data, data[1:]))
    
    if is_sorted:
        return data
    else:
        return data[::-1]  # Переворачиваем список


# ==========================================================
# ЧАСТЬ 3: Основная программа
# ==========================================================

def main():
    print("=== ЗАДАЧА 532: Проверка упорядоченности и разворот списка ===\n")
    
    try:
        n = int(input("Введите количество чисел n (n >= 1): "))
        if n < 1:
            print("Ошибка: n должно быть больше 0.")
            return
            
        print(f"Введите {n} действительных чисел через пробел:")
        data = list(map(float, input().split()))
        
        if len(data) != n:
            print(f"Ошибка: введено {len(data)} чисел, а ожидается {n}.")
            return

        print("\nВыберите способ решения:")
        print("1. Стандартный список (массив Python)")
        print("2. Двусвязный список (как на Рис. 26)")
        choice = input("Ваш выбор (1/2): ").strip()

        if choice == '1':
            result = solve_list(data)
        elif choice == '2':
            result = solve_linked_list(data)
        else:
            print("Неверный выбор. Используется стандартный список.")
            result = solve_list(data)

        # Вывод результата
        print(f"\nИсходная последовательность: {data}")
        print(f"Результат: {result}")
        
    except ValueError:
        print("Ошибка: введите корректные числа.")

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")