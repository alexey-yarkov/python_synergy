class Transport(object):
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
class Autobus(Transport):
    def seating_capacity(self, capacity):
        return f'Вместимость одного автобуса {self.name} {capacity} пассажиров'


a = Autobus('ПАЗ', 80, 1000)
print(a.seating_capacity(50))
