class Employee:

    def __init__(self, name, location, address, phone, cellphone, title):
        self.name = name
        self.location = location
        self.address = address
        self.phone = phone
        self.cellphone = cellphone
        self.title = title

    def __str__(self):
        return f"{self.name} {self.title} {self.location} {self.address} {self.phone} {self.cellphone}"
