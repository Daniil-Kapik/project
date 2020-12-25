"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно
выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"{self.color} {self.name} начал движение"

    def stop(self):
        return f"{self.color} {self.name} начал останавливаться"

    def turn(self, direction):
        return f"{self.color} {self.name} повернул в{direction}"

    def show_speed(self):
        return f"{self.color} {self.name} скорость = {self.speed} км/ч"


class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f"Превышение скорости!"
        else:
            return f"Скорость = {self.speed} км/ч"


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f"Превышение скорости!"
        else:
            return f"Скорость = {self.speed} км/ч"


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


bmv = TownCar(60, "Красный", "bmv", False)
gazel = WorkCar(70, "Желтый", "gazel", False)
bugatti = SportCar(200, "Синий", "bugatti", False)
mercedes = PoliceCar(160, "Зеленый", "mercedes", True)

print(f"{bmv.go()}\n{bmv.turn('право')}\n{bmv.show_speed()}\n{bmv.stop()}\n"
      f"Полиция = {bmv.is_police}\n")
print(f"{gazel.go()}\n{gazel.turn('лево')}\n{gazel.show_speed()}\n{gazel.stop()}\n"
      f"Полиция = {gazel.is_police}\n")
print(f"{mercedes.go()}\n{mercedes.turn('право')}\n{mercedes.show_speed()}\n{mercedes.stop()}\n"
      f"Полиция = {mercedes.is_police}\n")
