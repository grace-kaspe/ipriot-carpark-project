from display import Display
from pathlib import Path
from datetime import datetime # we'll use this to timestamp entries

class CarPark:
    def __init__(self,
                 location,
                 capacity,
                 _plates = None,
                 _displays = None,
                 log_file=Path("log.txt")
                 ):
        self.location = location
        self.capacity = capacity

        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        # create the file if it doesn't exist:
        self.log_file.touch(exist_ok=True)

        # We must never set mutable defaults for parameters, thus it has to be none
        self.plates = _plates or []
        self.displays = _displays or []

    def __str__(self):
        return f"Car park at {self.location}, with {self.capacity}"

    def _log_car_activity(self, plate, action):
        with self.log_file.open("a") as f:
            f.write(f"{plate} {action} at {datetime.now():%Y-%m-%d %H:%M:%S}\n")

    # register sensors and displays
    def register(self, component):
        # The isinstance function checks if an object is an instance of a class.
        if not isinstance(component, Display):
            raise TypeError("Object must be a Sensor or Display")

        elif isinstance(component,Display):
            self.displays.append(component)

    #when a car enters the car park, we record the number plate and update the displays
    def add_car(self, plate):
        # if plate is already in plates list
        if plate in self.plates :
            raise f" This plate - {plate} is already in the car park"
        else:
            self.plates.append(plate)
            self.update_displays()
            self._log_car_activity(plate, "entered")

    # when a car leaves the car park, we remove the number plate and update the displays
    def remove_car(self, plate):
        # if plate is not in the plates list
        if plate in self.plates :
            self.plates.remove(plate)
            self.update_displays()
            self._log_car_activity(plate, "exited")
        else:
            raise ValueError(f" This plate - {plate} has never entered the car park :/ SYSTEM ERROR")

    # Calculating available bays
    @property
    def available_bays(self):
        return max((self.capacity - len(self.plates)), 0)

    # Update display methods
    def update_displays(self):
        # build dictionary containing data
        data = {"available_bays":  self.available_bays, "temperature": 27}

        #iterate the data and call update method
        for display in self.displays:
            display.update(data)