class VehicleBase:
    def __init__(self, model, speed, color="White"):
        self.speed = speed
        self.color = color
        self.model = model

    def use(self):
        print(f"{self.model} starts...")

    def __str__(self):
        return f"Model: {self.model} Speed: {self.speed}, Color: {self.color}"


class Car(VehicleBase):
    pass


class Bike(VehicleBase):
    # override
    def use(self):
        print(f"{self.model} ring!!!")


class Boat(VehicleBase):
    pass


class Train(VehicleBase):
    pass


my_car = Car("Peugeot", 150)
my_bike = Bike("Csepel", 40)
my_boat = Boat("Titanic", 120)


# polymorphism
my_car.use()
my_bike.use()
my_boat.use()