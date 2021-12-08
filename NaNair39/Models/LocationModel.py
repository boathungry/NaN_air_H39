class Location:
    def __init__(self, city, country, airport, phone, opening, manager):
        self.city = city
        self.country = country
        self.airport = airport
        self.phone = phone
        self.opening = opening
        self.manager = manager

    def __str__(self):
        return f"City: {self.city}, Country: {self.country}, Local airport: {self.airport}, Branch phone number: {self.phone}, Opening hours: {self.opening}, Local manager: {self.manager}"
