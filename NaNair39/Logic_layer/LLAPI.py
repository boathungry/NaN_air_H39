from Data_layer.DLAPI import DLAPI
from Logic_layer.ChangeHandler import ChangeHandler
from Logic_layer.RegistrationHandler import RegistrationHandler

class LLAPI():
    def __init__(self, data_API = DLAPI()) -> None:
        self.dl_API = data_API
        self.change_handler = ChangeHandler(data_API)
        self.registration_handler = RegistrationHandler(data_API)
    
    def change_employee(self, employee, attribute, new_value):
        """Passes the chosen employee, attribute and new value through the logic layer where the attribute is changed to the new value."""
        self.change_handler.change_employee(employee, attribute, new_value)

    def change_property(self, property, attribute, new_value):
        """Passes the chosen property, attribute and new value through the logic layer where the attribute is changed to the new value."""
        self.change_handler.change_property(property, attribute, new_value)

    def change_contractor(self, contractor, attribute, new_value):
        """Passes the chosen contractor, attribute and new value through the logic layer where the attribute is changed to the new value."""
        self.change_handler.change_contractor(contractor, attribute, new_value)

    def change_work_report(self, work_report, attribute, new_value):
        """Passes the chosen work report, attribute and new value through the logic layer where the attribute is changed to the new value."""
        self.change_handler.change_work_report(work_report, attribute, new_value)

    def change_work_request(self, work_request, attribute, new_value):
        """Passes the chosen work request, attribute and new value through the logic layer where the attribute is changed to the new value."""
        self.change_handler.change_work_request(work_request, attribute, new_value)

    def create_employee(self, name, location, address, phone, cellphone, title):
        self.registration_handler.register_employee(name, location, address, phone, cellphone, title)

    def create_property(self, name, location, size, rooms):
        self.registration_handler.register_property(name, location, size, rooms)
    
    def create_contractor(self, name, phone, email, opening_hours, address):
        self.registration_handler.register_contractor(name, phone, email, opening_hours, address)

    def create_work_report(self, work_request, location, properties, description):
        self.registration_handler.register_work_report(work_request, location, properties, description)

    def create_work_request(self, id, work_request, location, properties, description, worker, priority, repeat, time, start, done):
        self.registration_handler.register_work_request(self, id, work_request, location, properties, description, worker, priority, repeat, time, start, done)
