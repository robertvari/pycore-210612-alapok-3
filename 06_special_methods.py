class Employee:
    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address

    def __str__(self):
        return f"Name: {self.name}  Phone: {self.phone}  Address: {self.address}"

    def __repr__(self):
        return self.name


robert = Employee("Robert", "06 20 123 4567", "Budapest")
tamas = Employee("Tamás", "06 20 987 5544", "Debrecen")
csilla = Employee("Csilla", "06 20 111 2233", "Pécs")
csaba = Employee("Csaba", "06 20 222 3344", "Szeged")

employee_list = [robert, tamas, csilla, csaba]
print(employee_list)