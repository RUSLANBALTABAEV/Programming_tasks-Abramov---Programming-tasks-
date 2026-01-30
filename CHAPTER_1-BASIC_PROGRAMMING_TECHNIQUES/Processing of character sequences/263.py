"""
ГЛАВА 1
ОСНОВНЫЕ ПРИЁМЫ ПРОГРАММИРОВАНИЯ
7. Сочетания цикла и разветвления

263. Даны натуральное число n, символы s1, …, sn. Заменить в последовательности s1, …, sn каждую группу букв child группой букв children.
"""


def replace_child(s):
    result = ""
    i = 0
    while i < len(s):
        if s[i:i+5] == "child":
            result += "children"
            i += 5
        else:
            result += s[i]
            i += 1
    return result

def main():
    n = int(input())
    s = input()
    print(replace_child(s))

if __name__ == "__main__":
    main()
