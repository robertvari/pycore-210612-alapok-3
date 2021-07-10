class VehicleBase:
    def __init__(self, model, speed, color="White"):
        self.speed = speed
        self.color = color
        self.model = model

    def __str__(self):
        return f"Model: {self.model} Speed: {self.speed}, Color: {self.color}"


class Car(VehicleBase):
    pass


class Bike(VehicleBase):
    pass


class Boat(VehicleBase):
    pass


class Train(VehicleBase):
    pass


my_car = Car("Peugeot", 150)
my_bike = Bike("Csepel", 40)

print(my_car)
print(my_bike)