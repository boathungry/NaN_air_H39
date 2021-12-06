from Models.PropertyModel import Property

class WorkRequest():
    def __init__(self, request_id, open_date, due_date, priority:str, property:Property, repeat:bool = False, repeat_interval_days:int = 0):
        self.id = request_id
        self.open_date = open_date
        self.due_date = due_date
        self.priority = priority
        self.property = property
        self.repeat = repeat
        self.repeat_interval = repeat_interval_days

    def __str__(self):
        return_str = f"ID: {self.id}, Opens: {self.open_date}, Due: {self.due_date}, Priority: {self.priority}"

        if self.repeat == True:
            return_str = return_str + f", Reopens every {self.repeat_interval} days"
        
        return return_str