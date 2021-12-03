class Property:

    def __init__(self, name, location, size, rooms):
        self.name = name
        self.locationn = location
        self.size = size
        self.rooms = rooms

    def __str__(self):
        return f"{self.name} {self.location} {self.size} {self.rooms}"
