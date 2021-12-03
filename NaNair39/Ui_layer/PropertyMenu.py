from NaNair39.Ui_layer.main_login import LogIn


class PropertyMenu(LogIn):
    def __init__(self):
        super().__init__()
    def location_options(self):
        location_deets = get_location_details(self.location)
        on = True
        while on:
            if self.staff_class == "m":
                pass
            elif self.staff_class == "e":
                pass