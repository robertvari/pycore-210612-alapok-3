class Employee:
    def __init__(self, name):
        # protected member
        self._first_name = name

    @property
    def name(self):
        print("name property called")
        return self._first_name

    @name.setter
    def name(self, new_name):
        print("set name called")
        self._first_name = new_name


robert = Employee("Robert")
robert.name = "Tamás"
print(robert.name)