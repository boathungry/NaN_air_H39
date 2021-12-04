from Data_layer.DLAPI import DLAPI
from Logic_layer.ChangeHandler import ChangeHandler
from Logic_layer.RegistrationHandler import RegistrationHandler

class LLAPI():
    def __init__(self, data_API = DLAPI()) -> None:
        self.dl_API = data_API
        self.change_handler = ChangeHandler()
        self.registration_handler = RegistrationHandler(data_API)
    