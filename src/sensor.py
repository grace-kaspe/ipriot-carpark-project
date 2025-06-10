class Sensor:
    def __init__(self,
                 id: str,
                 car_park: CarPark,
                 is_active: bool):
        self.id = id
        self.is_active = is_active
        self.car_parl = car_park

class EntrySensor:
    ...

class ExitSensor:
    ...