
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
