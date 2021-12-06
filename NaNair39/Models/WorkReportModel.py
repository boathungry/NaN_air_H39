class WorkReport:

    def __init__(self, work_request, location, properties, description):
        self.work_request = work_request
        self.location = location
        self.properties = properties
        self.description = description
    
    def __str__(self):
        return f"{self.work_request}   {self.location}   {self.properties}   {self.description}"
