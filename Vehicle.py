class Vehicle(object):
    def __init__(self, brand, model, odometer, last_service):
        self.brand = brand.capitalize()
        self.model = model.capitalize()
        self.odometer = odometer
        self.last_service = last_service

