"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
13. Файлы

502. Дан символьный файл f, содержащий произвольный текст длиной более 5000 слов. Слова в тексте разделены пробелами и знаками препинания. Получить 100 наиболее часто встречающихся слов и число их появлений. Решить задачу: 
а) без ограничения на длины слов;
б) предполагая, что любое слово текста состоит не более чем из 16 букв.
"""


import os
import random
import re
import string
from collections import Counter

# ==========================================================
# 1. ВСПОМОГАТЕЛЬНАЯ ФУНКЦИЯ: Создание тестового файла f (> 5000 слов)
# ==========================================================
def create_test_file(filename, word_count=6000):
    """Создаёт текстовый файл с заданным количеством случайных слов."""
    print(f"Генерация тестового файла '{filename}' с {word_count} словами...")
    # Словарь русских и английских букв для разнообразия
    chars = 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    words = []
    
    for _ in range(word_count):
        # Случайная длина слова от 1 до 16 символов (для проверки пункта б)
        length = random.randint(1, 16)
        word = ''.join(random.choices(chars, k=length))
        words.append(word)
    
    # Смешиваем слова со знаками препинания и пробелами
    # Используем .join, вставляя случайные пунктуационные знаки между словами.
    # Создаем строку, похожую на настоящий текст с произвольными разделителями.
    text_parts = []
    for i, w in enumerate(words):
        text_parts.append(w)
        # Добавляем случайный разделитель (пробел, запятая, точка, восклицательный знак и т.д.)
        if i < len(words) - 1:
            sep = random.choice([' ', ', ', '. ', '! ', '? ', '; '])
            text_parts.append(sep)
            
    text = ''.join(text_parts)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Тестовый файл готов.\n")

def ensure_file_exists(filename):
    """Проверяет существование файла и создаёт его при необходимости."""
    if not os.path.exists(filename):
        create_test_file(filename)

# ==========================================================
# 2. ЛОГИКА ПОДСЧЕТА ЧАСТОТЫ
# ==========================================================
def get_most_common_words(filename, limit=None, top_n=100):
    """
    Считывает файл, разбивает на слова (удаляя пунктуацию),
    считает частоту и возвращает top_n наиболее частых слов.
    
    limit: Если задано, учитывает только слова с длиной <= limit (для пункта б).
    top_n: Количество самых частых слов для вывода.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
            
        # 1. Очистка от знаков препинания и приведение к нижнему регистру
        # Используем регулярное выражение для поиска всех последовательностей букв.
        # [a-zA-Zа-яА-Я]+ находит слова, состоящие минимум из одной буквы.
        words = re.findall(r'[a-zA-Zа-яА-Я]+', text)
        words = [w.lower() for w in words]
        
        # 2. Фильтрация по длине (для пункта б)
        if limit is not None:
            words = [w for w in words if len(w) <= limit]
            
        # 3. Подсчет частот
        word_counts = Counter(words)
        
        # 4. Получение топ-N
        return word_counts.most_common(top_n)
        
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден.")
        return []
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return []

# ==========================================================
# 3. ОСНОВНАЯ ПРОГРАММА
# ==========================================================
def main():
    print("=== ЗАДАЧА 502: 100 наиболее частых слов в тексте ===\n")
    
    src_file = "f.txt"
    
    # 1. Убеждаемся, что файл существует
    ensure_file_exists(src_file)
    
    # 2. Решение пункта а) без ограничений на длину
    print("--- а) Без ограничения длины слов ---")
    top_100_a = get_most_common_words(src_file, limit=None, top_n=100)
    
    # Выводим результаты в консоль
    if top_100_a:
        print(f"Найдено {len(top_100_a)} уникальных слов (Топ-20 для просмотра):")
        for word, count in top_100_a[:20]: # Покажем топ-20 в консоли, чтобы не засорять вывод
            print(f"  {word}: {count}")
        print(f"  ... (остальные записаны в файл 'result_a.txt')")
        
        # Записываем полный топ-100 в файл
        with open("result_a.txt", 'w', encoding='utf-8') as f:
            f.write("Топ-100 слов (без ограничения длины):\n")
            for idx, (word, count) in enumerate(top_100_a, 1):
                f.write(f"{idx:3}. {word}: {count}\n")
    else:
        print("Не удалось получить список слов.")

    print("\n" + "-" * 40 + "\n")

    # 3. Решение пункта б) с ограничением в 16 символов
    print("--- б) С ограничением длины слов (<= 16 букв) ---")
    top_100_b = get_most_common_words(src_file, limit=16, top_n=100)
    
    if top_100_b:
        print(f"Найдено {len(top_100_b)} уникальных слов (Топ-20 для просмотра):")
        for word, count in top_100_b[:20]:
            print(f"  {word}: {count}")
        print(f"  ... (остальные записаны в файл 'result_b.txt')")
        
        # Записываем полный топ-100 в файл
        with open("result_b.txt", 'w', encoding='utf-8') as f:
            f.write("Топ-100 слов (длина <= 16 букв):\n")
            for idx, (word, count) in enumerate(top_100_b, 1):
                f.write(f"{idx:3}. {word}: {count}\n")
    else:
        print("Не удалось получить список слов.")

    print("\nОбработка завершена. Результаты сохранены в 'result_a.txt' и 'result_b.txt'.")

if __name__ == "__main__":
    main()
    input("\nНажмите Enter, чтобы завершить программу.")