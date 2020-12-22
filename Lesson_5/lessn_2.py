"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

# За текстовый файл я взял Ваш файл с методички

try:
    with open("intro-short.txt", "r", encoding="UTF-8") as my_file:
        print(f"Number of lines: {len([i for i in my_file])}")

    with open("intro-short.txt", "r", encoding="UTF-8") as my_file:
        print(f"Number of letters: {len(','.join(my_file.readlines()).split())}")
except IOError as er:
    print(er)
