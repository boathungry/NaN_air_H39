class Contractor:

    def __init__(self, name, phone, email, opening_hours, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.opening_hours = opening_hours
        self.address = address
    
    def __str__(self):
        return f"Name: {self.name}, email: {self.email}, phone: {self.phone}, address: {self.address}, opening hours: {self.opening_hours}"
