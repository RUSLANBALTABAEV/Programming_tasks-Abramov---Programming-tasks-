"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
4. Простейшие циклы

94. Пусть
       u1 = u2 = 0; v1 = v2 = 0;
ui = (ui-1 - ui - 2 * ui - 1 - ui - 2) / (1 + u ^ 2 i - 1 + v ^ 2 i - 1); vi = (ui - 1 - vi - 1) / (abs(ui - 2 + vi - 1) + 2), i = 3,4,...

Дано натуральное n (n ≥ 3). Получить vn.
"""


def main():
    # Ввод натурального числа n (n >= 3)
    n = int(input("Введите натуральное число n (n >= 3): "))
    
    if n < 3:
        print("n должно быть не меньше 3")
        return
    
    # Инициализация начальных значений
    u_prev2 = 0  # u_{i-2}
    u_prev1 = 0  # u_{i-1}
    v_prev2 = 0  # v_{i-2}
    v_prev1 = 0  # v_{i-1}
    
    # Вычисление значений для i от 3 до n
    for i in range(3, n + 1):
        # Вычисление u_i
        u_current = (u_prev1 - u_prev2 * v_prev1 - v_prev2) / (1 + u_prev1**2 + v_prev1**2)
        
        # Вычисление v_i
        v_current = (u_prev1 - v_prev1) / (abs(u_prev2 + v_prev1) + 2)
        
        # Обновление значений для следующей итерации
        u_prev2, u_prev1 = u_prev1, u_current
        v_prev2, v_prev1 = v_prev1, v_current
    
    # Вывод результата v_n
    print(f"v_{n} = {v_current}")


if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")
