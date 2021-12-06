from Models.WorkorderModel import Workorder
from Logic_layer.LLAPI import LLAPI
from RegistrationHandler import RegistrationHandler
from ChangeHandler import ChangeHandler
from datetime import date
import pandas

from NaNair39.Models.EmployeeModel import Employee


REQUEST = "work request"
LOCATION = "location"
PROPERTIES = "properties"
DESCRIPTION = "description"
REPEAT = "repeat"
TIME = "time"



class Workorder(RegistrationHandler, ChangeHandler):
    def __init__(self) -> None:
        pass

    def repeat_work_order(self, work_request, location, repeat, time, properties, description):
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

            RegistrationHandler.register_work_order(self, work_request, location, repeat, date_next, properties, description)
            
        
   # def mark_as_done():
     #   ChangeHandler.change_work_order(work_order:Workorder, attribute:str, new_value)
            

    def approve_report():

