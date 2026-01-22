"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
7. Сочетания цикла и разветвления

204. В некоторых видах спортивных состязаний выступление
каждого спортсмена независимо оценивается несколькими судьями,
затем из всей совокупности оценок удаляются наиболее высокая и
наиболее низкая, а для оставшихся оценок вычисляется среднее
арифметическое, которое и идет в зачет спортсмену. Если наиболее
высокую оценку выставило несколько судей, то из совокупности
оценок удаляется только одна такая оценка; аналогично поступают с
наиболее низкими оценками.
Даны натуральное число n, действительные положительные
числа a1, … , an(n ≥ 3). Считая, что числа a1, … , an – это оценки,
выставленные судьями одному из участников соревнований,
определить оценку, которая пойдет в зачет этому спортсмену.
"""

def calculate_final_score(n, scores):
    """
    Вычисляет итоговую оценку спортсмена после удаления одной минимальной
    и одной максимальной оценки.
    n: натуральное число (количество оценок, n >= 3)
    scores: список положительных действительных чисел [a₁, a₂, ..., aₙ]
    Возвращает итоговую оценку.
    """
    if n < 3:
        return None, "Ошибка: должно быть не менее 3 оценок"
    
    # Создаем копию, чтобы не изменять оригинальный список
    scores_copy = scores.copy()
    
    # Находим и удаляем одну минимальную оценку
    min_score = min(scores_copy)
    scores_copy.remove(min_score)
    
    # Находим и удаляем одну максимальную оценку
    max_score = max(scores_copy)
    scores_copy.remove(max_score)
    
    # Вычисляем среднее арифметическое оставшихся оценок
    final_score = sum(scores_copy) / len(scores_copy)
    
    return final_score, None


def calculate_final_score_detailed(n, scores):
    """
    Подробная версия с пошаговыми пояснениями.
    Возвращает итоговую оценку и строку с подробным описанием.
    """
    if n < 3:
        return None, "Ошибка: должно быть не менее 3 оценок"
    
    steps = []
    steps.append(f"1. Исходные оценки: {scores}")
    
    # Находим минимальную оценку
    min_score = min(scores)
    steps.append(f"2. Находим минимальную оценку: {min_score}")
    
    # Находим максимальную оценку
    max_score = max(scores)
    steps.append(f"3. Находим максимальную оценку: {max_score}")
    
    # Удаляем одну минимальную оценку
    scores_without_min = scores.copy()
    scores_without_min.remove(min_score)
    steps.append(f"4. Удаляем одну минимальную оценку: {scores_without_min}")
    
    # Удаляем одну максимальную оценку
    scores_final = scores_without_min.copy()
    scores_final.remove(max_score)
    steps.append(f"5. Удаляем одну максимальную оценку: {scores_final}")
    
    # Вычисляем среднее арифметическое
    average_score = sum(scores_final) / len(scores_final)
    steps.append(f"6. Вычисляем среднее арифметическое: {sum(scores_final)} / {len(scores_final)} = {average_score:.2f}")
    
    detailed_explanation = "\n".join(steps)
    return average_score, detailed_explanation


def main():
    """
    Основная функция программы с выбором режима работы:
    1. Использовать примеры из кода
    2. Ввести свои данные
    """
    print("Программа расчета итоговой оценки спортсмена")
    print("=" * 60)
    
    choice = input("Выберите режим:\n1 - Использовать примеры из кода\n2 - Ввести свои данные\nВведите 1 или 2: ")
    
    if choice == '1':
        # Используем примеры из кода
        examples = [
            ("Пример 1: Разные оценки", 6, [9.5, 8.0, 9.0, 9.5, 8.5, 9.0]),
            ("Пример 2: Все оценки одинаковые", 4, [8.0, 8.0, 8.0, 8.0]),
            ("Пример 3: Несколько одинаковых минимальных и максимальных", 6, [5.0, 9.5, 8.0, 9.5, 5.0, 8.5]),
        ]
        
        for title, n, scores in examples:
            print(f"\n{title}")
            print(f"Количество оценок: n = {n}")
            print(f"Оценки судей: {scores}")
            
            final_score, error = calculate_final_score(n, scores)
            if error:
                print(f"Ошибка: {error}")
            else:
                print(f"Итоговая оценка: {final_score:.2f}")
                
                # Подробный расчет для первого примера
                if title == "Пример 1: Разные оценки":
                    detailed_choice = input("\nПоказать подробный расчет для этого примера? (да/нет): ")
                    if detailed_choice.lower() in ['да', 'д', 'yes', 'y']:
                        final_score_detailed, explanation = calculate_final_score_detailed(n, scores)
                        print("\nПодробный расчет:")
                        print(explanation)
                        print(f"\nИтоговая оценка: {final_score_detailed:.2f}")
            
            print("-" * 40)
    
    elif choice == '2':
        # Ввод данных от пользователя
        try:
            n = int(input("\nВведите количество оценок (n ≥ 3): "))
            if n < 3:
                print("Ошибка: должно быть не менее 3 оценок!")
                return
            
            scores = []
            print("\nВведите оценки судей:")
            for i in range(n):
                while True:
                    try:
                        value = float(input(f"Оценка судьи {i+1}: "))
                        if value <= 0:
                            print("Оценка должна быть положительным числом!")
                            continue
                        scores.append(value)
                        break
                    except ValueError:
                        print("Ошибка! Введите число в правильном формате (например: 8.5)")
            
            print(f"\nВведены оценки: {scores}")
            
            # Вычисление итоговой оценки
            final_score, error = calculate_final_score(n, scores)
            if error:
                print(f"Ошибка: {error}")
            else:
                print(f"Итоговая оценка спортсмена: {final_score:.2f}")
                
                # Предложение показать подробный расчет
                detailed_choice = input("\nПоказать подробный расчет? (да/нет): ")
                if detailed_choice.lower() in ['да', 'д', 'yes', 'y']:
                    final_score_detailed, explanation = calculate_final_score_detailed(n, scores)
                    print("\nПодробный расчет:")
                    print(explanation)
                    print(f"\nИтоговая оценка: {final_score_detailed:.2f}")
        
        except ValueError:
            print("Ошибка ввода! Убедитесь, что вводите числа в правильном формате.")
            return
    
    else:
        print("Неверный выбор. Программа завершена.")
        return
    
    print("\n" + "=" * 60)
    print("Пояснение:")
    print("В спортивных состязаниях часто используется система оценки,")
    print("когда удаляются одна наивысшая и одна наинизшая оценка,")
    print("а из оставшихся вычисляется среднее арифметическое.")
    print("Это позволяет исключить влияние предвзятости отдельных судей.")
    print("=" * 60)


if __name__ == "__main__":
    main()
    input("\n\nНажмите Enter, чтобы завершить программу.")
