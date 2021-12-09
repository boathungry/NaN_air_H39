class Property:

    def __init__(self, idnumber, name, location, address, size, rooms):
        self.idnumber = idnumber
        self.name = name
        self.location = location
        self.address = address
        self.size = size
        self.rooms = rooms

    def __str__(self):
        return f"{self.idnumber} {self.name} {self.location} {self.address} {self.size} {self.rooms}"
