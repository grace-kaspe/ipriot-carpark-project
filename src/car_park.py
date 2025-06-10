from display import Display
from sensor import  Sensor

class CarPark:
    def __init__(self,
                 location,
                 capacity,
                 _plates = None,
                 _displays = None):
        self.location = location
        self.capacity = capacity

        # We must never set mutable defaults for parameters, thus it has to be none
        self.plates = _plates or []
        self.displays = _displays or []


    def __str__(self):
        return f"Car park at {self.location}, with {self.capacity}"

    # register sensors and displays
    def register(self, component):
        # The isinstance function checks if an object is an instance of a class.
        if not isinstance(component, (Sensor,Display)):
            raise TypeError("Object must be a Sensor or Display")

        if isinstance(component, Sensor):
            self.displays.append(component)
        elif isinstance(component,Display):
            self.displays.append(component)
        # TODO: add an elif to check if the component is a Display - MUST