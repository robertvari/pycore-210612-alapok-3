class Employee:
    def __init__(self, name):
        # protected member
        self._name = name

        # private member
        self.__age = 42

    # getter method
    def get_name(self):
        return self._name

    # setter method
    def set_name(self, new_name):
        self._name = new_name


robert = Employee("Robert")
robert.set_name("Tamás")
print(robert.get_name())