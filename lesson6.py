#1
import time
class TraffikLigth:
    __color = ["Красный", "Желтый", "Зеленый"]
    def running(self):
        print("Горит", self.__color[0], "сигнал светофора!")
        time.sleep(7)
        print("Горит", self.__color[1], "сигнал светофора!")
        time.sleep(2)
        print("Горит", self.__color[2], "сигнал светофора!")
        time.sleep(3)
traf_l = TraffikLigth()
traf_l.running()


#2
# class Road:
#     def __init__(self, l, w):
#         self._l = l
#         self._w = w
#     def calc(self):
#         return f"Масса полотна: {(self._l * self._w * 25 * 0.05) / 1000} т"
# l = int(input("Введите длину полотна: "))
# w = int(input("Введите ширину полотна: "))
# rd = Road(l, w)
# print(rd.calc())


#3
# class Worker:
#     def __init__(self, name, surname, position, wage, bonus):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = {"salary": wage, "bonus": bonus}
#
# class Position(Worker):
#     def get_full_name(self):
#         return f"{self.position} {self.name} {self.surname}"
#     def get_full_profit(self):
#         return f"{sum(self._income.values())}"
# worker_1 = Position("Li", "Chan", "director", 10000, 25000)
# print(worker_1.get_full_name())
# print(worker_1.get_full_profit())


#4
# class Car:
#     def __init__(self, name, color, speed, is_police = False):
#         self.name = name
#         self.color = color
#         self.speed = speed
#         self.is_police = is_police
#         print(f"Новая машина: {self.name}, цвет: {self.color}, полиция? {self.is_police}")
#     def go(self):
#         print(f"Машина {self.name} тронулась")
#     def stop(self):
#         print(f"Машина {self.name} остановилась")
#     def turn(self, dir):
#         print(f"Машина {self.name} повернула {'направо' if dir == 0 else 'налево'}")
#     def show_speed(self):
#         print(f"Машина {self.name} едет со скоростью {self.speed}")
# class TownCar(Car):
#     def show_speed(self):
#         print(f"Машина {self.name} едет со скоростью {self.speed} {'Скорость перевышена' if self.speed > 60 else 'Скорость допустимая'}")
# class WorkCar(Car):
#     def show_speed(self):
#         print(f"Машина {self.name} едет со скоростью {self.speed} {'Скорость перевышена' if self.speed > 40 else 'Скорость допустимая'}")
# class SportCar(Car):
#     pass
# class PoliceCar(Car):
#     def __init__(self, name, color, speed, is_police=True):
#         super().__init__(name, color, speed, is_police)
# town_car = TownCar("LIAZ", "red", 70)
# town_car.turn(1)
# town_car.show_speed()
# town_car.stop()
#
# work_car = WorkCar("TAXI", "yellow", 30)
# work_car.go()
# work_car.show_speed()
#
# police_car = PoliceCar("Granta", "black", 100)
# police_car.go()
# police_car.turn(0)
# police_car.show_speed()
# police_car.stop()
# print(police_car.is_police)


#5
# class Stacionary:
#     def __init__(self, title = "Отрисовывает"):
#         self.title = title
#     def draw(self):
#         print("Начинается отрисовка")
# class Pen(Stacionary):
#     def draw(self):
#         print(f"Начинается отрисовка ручкой {self.title}")
# class Pensil(Stacionary):
#     def draw(self):
#         print(f"Начинается отрисовка карандашом {self.title}")
# class Handler(Stacionary):
#     def draw(self):
#         print(f"Начинается отрисовка маркером {self.title}")
#
# stacionary = Stacionary()
# stacionary.draw()
#
# pen = Pen("шариковой")
# pen.draw()
#
# pensil = Pensil("графитным")
# pensil.draw()
#
# handler = Handler("перманентным")
# handler.draw()