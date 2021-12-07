from Models.PropertyModel import Property

class WorkRequest():
    def __init__(self, id, work_request, location, properties, description, worker, priority, repeat, time, start, done):
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
        return_str = f"ID: {self.id}, Work request: {self.work_request}, Location: {self.location}, Properties: {self.properties}, Description: {self.description}, Worker: {self.worker}, Priority: {self.priority}, Reapeat: {self.repeat}, Time: {self.time}, Start: {self.start}, Done: {self.done}"

        if self.repeat == True:
            return_str = return_str + f", Reopens {self.repeat}"
        
        return return_str


