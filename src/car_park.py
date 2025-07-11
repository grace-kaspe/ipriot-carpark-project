from display import Display
from pathlib import Path
from datetime import datetime # we'll use this to timestamp entries
import json


class CarPark:
    def __init__(self,
                 location,
                 capacity,
                 _plates = None,
                 _displays = None,
                 log_file=Path("log.txt"),
                 config_file = Path("config.json")
                 ):
        self.location = location
        self.capacity = capacity
        self.config_file = config_file
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

    def register(self, component):
        """
            Register Display into the carpark
        """
        # The isinstance function checks if an object is an instance of a class.
        if not isinstance(component, Display):
            raise TypeError("Object must be a Sensor or Display")

        elif isinstance(component,Display):
            self.displays.append(component)

    def add_car(self, plate):
        """
           Wwhen a car enters the car park, we record the number plate and update the displays
        """
        # if plate is already in plates list
        if plate in self.plates :
            raise f" This plate - {plate} is already in the car park"
        else:
            self.plates.append(plate)
            self.update_displays()
            self._log_car_activity(plate, "entered")

    def remove_car(self, plate):
        """
            When a car leaves the car park, we remove the number plate and update the displays
        """
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

    def update_displays(self):
        """
           Update display methods
        """
        # build dictionary containing data
        data = {"available_bays":  self.available_bays, "temperature": 27}

        #iterate the data and call update method
        for display in self.displays:
            display.update(data)

    """
       Safe config file in json format
    """
    def write_config(self):
        with open(self.config_file, "w") as f:
            json.dump({"location": self.location,
                       "capacity": self.capacity,
                       "log_file": str(self.log_file)}, f)

    @classmethod
    def from_config(cls, config_file=Path("config.json")):
        config_file = config_file if isinstance(config_file, Path) else Path(config_file)
        with config_file.open() as f:
            config = json.load(f)
        return cls(config["location"], config["capacity"], log_file=config["log_file"])