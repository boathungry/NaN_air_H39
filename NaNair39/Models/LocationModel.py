class Location:
    def __init__(self, city, country):
        self.city = city
        self.country = country


    def __str__(self):
        return f"City: {self.city}, Country: {self.country}"
