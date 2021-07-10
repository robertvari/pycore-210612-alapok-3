import time


class CoffeeMachine:
    def __init__(self, model):
        self.model = model
        self.turned_on = False

        self.water = None
        self.beans = None

    def turn_on(self):
        self.turned_on = True

        print("Turning on...")
        time.sleep(2)

        print("Heating...")
        time.sleep(3)

        print(f"{self.model} Wellcome. Do you want a cup of coffee?")

    def fill_up_water(self):
        print("Filling up water tank...")
        time.sleep(2)
        self.water = True

    def fill_up_beans(self):
        print("Filling up beans...")
        time.sleep(2)
        self.beans = True

    def make_coffee(self):
        assert self.turned_on, "First turn it on!"
        assert self.water, "Please fill up water tank."
        assert self.beans, "Please fill up coffee beans"

        print("Making coffee....")

    def turn_off(self):
        assert self.turned_on, "Machine is turned off."

        self.turned_on = False
        print(f"{self.model} Turning off...")
        time.sleep(3)
        print("See you next time!")



my_coffee_machine = CoffeeMachine("DeLonghi")

my_coffee_machine.turn_on()

my_coffee_machine.fill_up_water()

my_coffee_machine.fill_up_beans()

my_coffee_machine.make_coffee()

my_coffee_machine.turn_off()
