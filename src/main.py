from display import Display
from car_park import CarPark
from sensor import EntrySensor, ExitSensor

car_park =CarPark('111 Friend St', 399)


entry_sensor = EntrySensor('111', car_park, is_active=True)
exit_sensor = ExitSensor('222', car_park, is_active=True)
car_park.register(Display('abc'))
entry_sensor.detect_vehicle()
exit_sensor.detect_vehicle()

