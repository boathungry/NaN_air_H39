class Location:
    def __init__(self, city = "", country = "", airport = "", phone_number = "", opening_hours = "", local_manager = ""):
        self.city = city
        self.country = country
        self.airport = airport
        self.phone_number = phone_number
        self.opening_hours = opening_hours
        self.local_manager = local_manager

    def __str__(self):
        return f"City: {self.city}, Country: {self.country}, Local airport: {self.airport}, Branch phone number: {self.phone_number}, Opening hours: {self.opening_hours}, Local manager: {self.local_manager}"
