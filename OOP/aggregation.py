class Car:
    def __init__(self, brand):
        self.brand = brand


class ShowRoom:
    def __init__(self, car):
        self.car = car

    def display_car(self):
        return f"Showroom has {self.car.brand} car"

    def display_car(self):
        return f"Showroom has {self.car.brand} car"
    

car_1 = Car("Toyota")
car_2 = Car("Honda")
showroom = ShowRoom(car_1)

print(showroom.display_car())

showroom = ShowRoom(car_2)

print(showroom.display_car())