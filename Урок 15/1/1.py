class Transport(object):
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def write(self):
        print(f'Название автомобиля: {self.name} Скорость: {self.max_speed} Пробег: {self.mileage}')
Autobus = Transport('ПАЗ', 80, 1000)
Autobus.write()
