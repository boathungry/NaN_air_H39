class Employee:

    def __init__(self, idnumber = "", name = "", email= "", location = "", address = "", phone = "", cellphone = "", title = ""):
        self.idnumber = idnumber
        self.name = name
        self.email = email
        self.location = location
        self.address = address
        self.phone = phone
        self.cellphone = cellphone
        self.title = title

    def __str__(self):
        return f"{self.idnumber} {self.name} {self.email} {self.location} {self.address} {self.phone} {self.cellphone} {self.title}"

    def __repr__(self) -> str:
        return f"{self.idnumber} {self.name} {self.email} {self.location} {self.address} {self.phone} {self.cellphone} {self.title}"
