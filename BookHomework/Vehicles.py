class vehicle:
    def __init__(self):
        raise NotImplementedError('Don\'t just make a vehicle, make a specific type of vehicle.')
    
    def __str__(self):
        return "{}".format(self.name)

class motorcycle(vehicle):
    def __init__(self):
        self.name = 'Motorcycle'
        self.wheels = 4

class car(vehicle):
    def __init__(self):
        self.name = 'Car'
        self.wheels = 4