class Cup:
    color = None
    empty = True

    def __init__(self, color, empty):
        self.color = color
        self.empty = empty


class Employee:
    # constructor
    def __init__(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address


john = Employee(
    "John",
    "john@gmail.com",
    "0620 123 4567",
    "Budapest"
)

tom = Employee(
    "Tom",
    "tom@gmail.com",
    "0620 997 3344",
    "Debrecen"
)

print(john.name, john.email, john.phone, john.address)
print(tom.name, tom.email, tom.phone, tom.address)