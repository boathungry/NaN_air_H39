class Contractor:

    def __init__(self, name, phone, email, opening_hours, address, location):
        self.name = name
        self.phone = phone
        self.email = email
        self.opening_hours = opening_hours
        self.address = address
        self.location = location
    
    def __str__(self):
        return f"Name: {self.name}, phone: {self.phone}, email: {self.email}, opening hours: {self.opening_hours}, address: {self.address}, location: {self.location}"
