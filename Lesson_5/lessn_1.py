"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.

"""

while True:
    user_input = input('Введите произвольную строку: ')
    if not user_input:
        break

    try:
        with open("text_lesson_1.txt", 'a', encoding='utf-8') as fn:
            fn.write(f'{user_input}\n')
    except IOError as er:
        print(er)
        break
