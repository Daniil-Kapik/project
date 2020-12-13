"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def division_numbers(a, b):
    return a / b


while True:
    dividend = input("Для выхода нажмиите q. Введите делимое: ")
    if dividend == "q":
        break
    divider = int(input("Введите делитель: "))
    dividend = int(dividend)
    try:
        print(division_numbers(dividend, divider))
    except ZeroDivisionError:
        print("На 0 делить нельзя, введите делитель еще раз: ")
        continue




