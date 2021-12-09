class Location:
    def __init__(self, city = "", country = "", airport = "", phone_number = "", opening_hours = "", local_manager = ""):
        self.city = city
        self.country = country
        self.airport = airport
        self.phone_number = phone_number
        self.opening_hours = opening_hours
        self.local_manager = local_manager

    def __str__(self):
        return f"{self.city} {self.country} {self.airport} {self.phone_number} {self.opening_hours} {self.local_manager}"
    
    def __repr__(self) -> str:
        return f"{self.city} {self.country} {self.airport} {self.phone_number} {self.opening_hours} {self.local_manager}"
