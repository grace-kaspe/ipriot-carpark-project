from abc import ABC, abstractmethod

from car_park import CarPark

import random

class Sensor(ABC):
    def __init__(self,
                 id: str,
                 car_park: CarPark,
                 is_active: bool):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    @abstractmethod
    def update_car_park(self, plate):
        pass

    def _scan_plate(self):
        return f"FAKE-{random.randint(0, 999) : 03d}"

    def detect_vehicle(self):
        plate = self._scan_plate()
        self.update_car_park(plate)

class EntrySensor(Sensor):
    """
        Entry sensor is the Concrete class of Sensor, which is an abstract class.
        The exit handles the removal of a license plate
    """
    def update_car_park(self, plate):
        self.car_park.add_car(plate)
        print(f"Incoming 🚘 vehicle detected. Plate: {plate}")

class ExitSensor(Sensor):
    """
        Exit sensor is the Concrete class of Sensor, which is an abstract class
        The exit handles the removal of a license plate
    """
    def update_car_park(self, plate):
        self.car_park.remove_car(plate)
        print(f"Outgoing 🚗 vehicle detected. Plate: {plate}")

    def _scan_plate(self):
        return random.choice(self.car_park.plates)