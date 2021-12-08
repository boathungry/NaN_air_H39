class LoginAccount:
    def __init__(self, name, email, location, title):
        self.name = name
        self.email = email
        self.location = location
        self.title = title

    def __str__(self):
        return f"Name: {self.name}, email: {self.email}, location: {self.location}, job title: {self.title}"

    
