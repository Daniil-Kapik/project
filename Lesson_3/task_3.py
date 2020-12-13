"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(arg1, arg2, arg3):
    return sorted([arg1, arg2, arg3])[-1] + sorted([arg1, arg2, arg3])[-2]


print(my_func(12, 5, 8))