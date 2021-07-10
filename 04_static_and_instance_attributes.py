class Employee:
    # static attribute
    name = "Robert"
    counter = 0

    def __init__(self, name):
        # instance attribute
        self.name = name
        Employee.counter += 1


tom = Employee("Tom")
john = Employee("John")
christina = Employee("Christina")
Robert = Employee("Robert")
Csaba = Employee("Csaba")

print(Csaba.counter)

