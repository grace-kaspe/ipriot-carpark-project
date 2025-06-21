from display import Display
from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from pathlib import Path
import json

# create a car park object with the location moondalup, capacity 100, and log_file "moondalup.txt"
car_park =CarPark('Moondalup', 100, None, None)
car_park.log_file = Path("moondalup.txt")
car_park.config_file = Path("moondalup_config.json")

# Write the car park configuration to a file called "moondalup_config.json"
car_park.write_config()

# Reinitialize the car park object from the "moondalup_config.json" file
car_park.from_config("moondalup_config.json")

# create an entry sensor object with id 1, is_active True, and car_park car_park
entry_sensor = EntrySensor('1', car_park, is_active=True)

# create an exit sensor object with id 2, is_active True, and car_park car_park
exit_sensor = ExitSensor('2', car_park, is_active=True)

# create a display object with id 1, message "Welcome to Moondalup", is_on True, and car_park car_park
display = Display('1', message= "Welcome to Moondalup", is_on= True)


# drive 10 cars into the car park (must be triggered via the sensor - NOT by calling car_park.add_car directly)
for car in range(10):
    entry_sensor.detect_vehicle()

# drive 2 cars out of the car park (must be triggered via the sensor - NOT by calling car_park.remove_car directly)
for car in range(2):
    exit_sensor.detect_vehicle()


