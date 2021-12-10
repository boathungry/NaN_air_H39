class WorkReport:

    def __init__(self, id, work_request_id, description, location, properties, worker, comment, regular_maintenance, expenses, start, done):
        self.id = id
        self.work_request_id = work_request_id
        self.description = description
        self.location = location
        self.properties = properties
        self.worker = worker
        self.comment = comment
        self.regular_maintenance = regular_maintenance
        self.expenses = expenses
        self.start = start
        self.done = done

        
    
    def __str__(self):
        return f"ID: {self.id}, Work request ID: {self.work_request_id}, Description: {self.description}, Location: {self.location}, Properties: {self.properties}, Worker: {self.worker}, Comment: {self.comment}, Regular maintenance: {self.regular_maintenance}, Expenses: {self.expenses}, Start: {self.start}, Done: {self.done}"

