class Display:
    def __init__(self,
                 id,
                 message = '',
                 is_on = False):
        self.id = id
        self.message = message
        self.is_on = is_on

    def __str__(self):
        return f"Display {self.id}: {self.message}"

    def update(self, data):
        """
            Accept data and print the data into any display
        """
        for key, value in data.items():
            print(f"{key}: {value}")

            # This is to update self message and is_on to pass unit test
            if "message" in data:
                self.message = data["message"]
            if "is_on" in data:
                self.is_on = data["is_on"]