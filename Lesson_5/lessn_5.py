"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить
ее на экран.
"""

try:
    with open("text_lesson_5.txt", "wt", encoding="UTF-8") as my_file:
        my_file.write("2 3 4 5 6 7 8")
    with open("text_lesson_5.txt", "rt", encoding="UTF-8") as my_file:
        print(sum([int(i) for i in my_file.read().split()]))
except IOError as er:
    print(er)