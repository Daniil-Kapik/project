"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в
виде строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый,
с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип
к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Date:

    def __init__(self, date):
        self.date = date

    @classmethod
    def metod_one(cls, date):
        return [int(i) for i in date.split("-")]

    @staticmethod
    def metod_two(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 0 < year <= 2020:
                    return f"Дата валидна"
                else:
                    return f"Год не верный"
            else:
                return f"Месяц не верный"
        else:
            return f"День не верный"


print(Date.metod_one("10-11-2009"))
print(Date.metod_two(10, 11, 2009))
print(Date.metod_one("23-13-2040"))
print(Date.metod_two(13, 13, 2040))


