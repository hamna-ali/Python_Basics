from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def fuel_type(self):
        pass


class Car(Vehicle):
    def fuel_type(self):
        return "Petrol"


class ElectricBike(Vehicle):
    def fuel_type(self):
        return "Electric"


car = Car()
bike = ElectricBike()

print("Car has fuel type: ",car.fuel_type())
print("Bike has fuel type: ",bike.fuel_type())
