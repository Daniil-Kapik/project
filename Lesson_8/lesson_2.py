"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать
эту ситуацию и не завершиться с ошибкой.
"""


class MyZeroDivisionError(Exception):
    pass


while True:
    try:
        dividend = int(input("Введите делимое: "))
        divider = int(input("Введите делитель: "))
        if divider == 0:
            raise MyZeroDivisionError("Нельзя делить на 0")
        print(dividend / divider)
    except MyZeroDivisionError as e:
        print(e)
        continue
