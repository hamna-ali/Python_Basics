class LivingThing:
    def breathe(self):
        raise NotImplementedError


class Animal(LivingThing):
    def breathe(self):
        return "Animal breathes through lungs"


class Plant(LivingThing):
    def breathe(self):
        return "Plant breathes through stomata"


animal = Animal()
plant = Plant()

print(animal.breathe())
print(plant.breathe())
