from Models.WorkRequestModel import WorkRequest
from Data_layer.DLAPI import DLAPI
from Logic_layer.RegistrationHandler import RegistrationHandler
from Logic_layer.ChangeHandler import ChangeHandler
from datetime import date
from dateutil.relativedelta import relativedelta


from Models.EmployeeModel import Employee

ID = "id"
REQUEST = "work request"
LOCATION = "location"
PROPERTIES = "properties"
DESCRIPTION = "description"
WORKER = "worker"
PRIORITY = "priority"
REPEAT = "repeat"
TIME = "time"
START = "start"
DONE = "done"



class WorkRequest(RegistrationHandler, ChangeHandler):
    def __init__(self, dl_api:DLAPI = DLAPI()) -> None:
        self.dl_api = dl_api

    def repeat_work_request(self, id, work_request, location, properties, description, worker, priority, repeat, time, start, done):
        date_today = date.today()
        if REPEAT == "y":
            if TIME == "daily":
                date_next = date_today + relativedelta(days=1)
            elif TIME == "weekly":
                date_next = date_today + relativedelta(days=8)
            elif TIME == "monthly":
                date_next = date_today + relativedelta(months=1)
            elif TIME == "yearly":
                date_next = date_today + relativedelta(years=1)

            RegistrationHandler.register_work_request(self, id, work_request, location, properties, description, worker, priority, repeat, date_next, start, done)
            
        
    def mark_as_done(self, work_request:WorkRequest):
        ChangeHandler.change_work_request(self, work_request, "done", date.today())

            

