from NaNair39.Ui_layer.main_login import LogIn


class EmployeeUI(LogIn):
    def __init__(self, name):
        super().__init__(name, staff_class="s")