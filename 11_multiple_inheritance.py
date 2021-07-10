class HumanBase:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello. My name is {self.name}")

    def __str__(self):
        return self.name


class CommonPeople(HumanBase):
    pass


class Student(HumanBase):
    def my_school(self):
        print("I'm studying at BMI")


class Employee(Student):
    pass


Tom = Employee("Tom")
Chris = Student("Chris")
John = CommonPeople("John")


Tom.say_hello()
Tom.my_school()

John.say_hello()