class LoginAccount:
    def __init__(self, ID, name, email, location, title):
        self.ID = ID
        self.name = name
        self.email = email
        self.location = location
        self.title = title

    def __str__(self):
        return f"{self.ID}, {self.name}, {self.email}, {self.location}, {self.title}"

    
