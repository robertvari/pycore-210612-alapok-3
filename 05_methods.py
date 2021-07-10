import time


class CoffeeMachine:
    def __init__(self, model):
        self.model = model
        self.turned_on = False

    def turn_on(self):
        self.turned_on = True

        print("Turning on...")
        time.sleep(2)

        print("Heating...")
        time.sleep(3)

        print(f"{self.model} Wellcome. Do you want a cup of coffee?")

    def make_coffee(self):
        assert self.turned_on, "First turn it on!"
        print("Making coffee....")


my_coffee_machine = CoffeeMachine("DeLonghi")
my_coffee_machine.turn_on()
my_coffee_machine.make_coffee()
