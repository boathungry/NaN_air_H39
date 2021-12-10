from Models.PropertyModel import Property

class WorkRequest:
    def __init__(self, id = "", work_request = "", location = "", properties = "", description = "", worker  ="", priority = "", repeat = "", time = "", start = "", done = ""):
        self.id = id
        self.work_request = work_request
        self.location = location
        self.properties = properties
        self.description = description
        self.worker = worker
        self.priority = priority
        self.repeat = repeat
        self.time = time
        self.start = start
        self.done = done

    def __str__(self):
        """return_str = """

        """if self.repeat == True:
            return_str = return_str + f", Reopens {self.repeat}"""
        
        return f"{self.id} {self.work_request} {self.location} {self.properties} {self.description} {self.worker} {self.priority} {self.repeat} {self.time} {self.start} {self.done}"

    def __repr__(self) -> str:
        return f"{self.id} {self.work_request} {self.location} {self.properties} {self.description} {self.worker} {self.priority} {self.repeat} {self.time} {self.start} {self.done}"