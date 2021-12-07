from Models.WorkRequestModel import WorkRequest
from Logic_layer.LLAPI import LLAPI
from RegistrationHandler import RegistrationHandler
from ChangeHandler import ChangeHandler
from datetime import date
import pandas

from NaNair39.Models.EmployeeModel import Employee

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
    def __init__(self) -> None:
        pass

    def repeat_work_request(self, id, work_request, location, properties, description, worker, priority, repeat, time, start, done):
        date_today = date.today()
        if REPEAT == "y":
            if TIME == "daily":
                date_next = date_today + pandas.DateOffset(days=1)
            elif TIME == "weekly":
                date_next = date_today + pandas.DateOffset(days=8)
            elif TIME == "monthly":
                date_next = date_today + pandas.DateOffset(months=1)
            elif TIME == "yearly":
                date_next = date_today + pandas.DateOffset(years=1)

            RegistrationHandler.register_work_request(self, work_request, location, properties, description, worker, priority, repeat, time, start, done)
            
        
   # def mark_as_done():
     #   ChangeHandler.change_work_request(work_request:Workrequest, attribute:str, new_value)
            
