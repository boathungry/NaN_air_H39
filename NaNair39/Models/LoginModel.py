class LoginAccount:
    def __init__(self, name, email, location, title):
        self.name = name
        self.email = email
        self.location = location
        self.title = title

    def __str__(self):
        return f"{self.name}, {self.email}, {self.location}, {self.title}"

    
