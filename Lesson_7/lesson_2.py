"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы
для основных классов проекта, проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


@abstractmethod
class Clothes(ABC):

    def __init__(self, v, h):
        self.v = v
        self.h = h

    def consumption(self):
        pass

    def summa(self):
        return f"Общий расход = {(self.v / 6.5 + 0.5) + (2 * self.h + 0.3):.2f} кв/м"


class Coat(Clothes):

    def __init__(self, v):
        self.v = v

    @property
    def consumption(self):
        return f"Расход на 1 пальто = {self.v / 6.5 + 0.5:.2f} м/кв"


class Costume(Clothes):

    def __init__(self, h):
        self.h = h

    @property
    def consumption(self):
        return f"Расход на 1 костюм = {2 * self.h + 0.3:.2f} м/кв"


coat1 = Coat(29)
costume1 = Costume(6)
a = Clothes(29, 6)
print(a.summa())
print(coat1.consumption)
print(costume1.consumption)
