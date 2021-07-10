class HumanBase:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello. My name is {self.name}")

    def __str__(self):
        return self.name


class FatherBase(HumanBase):
    def say_hello(self):
        print("Luke. I'm you father.")


class MotherBase(HumanBase):
    def say_hello(self):
        print("I'm your mother")


# multiple inheritance
class Child(MotherBase, FatherBase):
    # testing Method Resolution Order
    pass


class CommonPeople(HumanBase):
    pass


class Student(HumanBase):
    def my_school(self):
        print("I'm studying at BMI")


# grandchild
class Employee(Student):
    pass


Luke = Child("Luke Skywalker")
Luke.say_hello()