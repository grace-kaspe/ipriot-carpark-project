import unittest
from sensor import EntrySensor
from sensor import ExitSensor
from car_park import CarPark

class TestSensor(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark(location="123 Example Street", capacity=100)
        self.entry_sensor =  EntrySensor('111', self.car_park, is_active=True)
        self.exit_sensor = ExitSensor('123', self.car_park, is_active=True)

    def test_entry_sensor_initialised(self):
        self.assertEqual(self.entry_sensor.id, '111')

    def test_exit_sensor_initialised(self):
        self.assertEqual(self.exit_sensor.id, '123')

    def test_detect_vehicle_on_entry(self):
        self.plateEntry = self.entry_sensor.detect_vehicle()
        self.available_bays= self.car_park.available_bays
        self.assertEqual(self.available_bays, 99)

        self.plateExit = self.exit_sensor.detect_vehicle()
        self.available_bays = self.car_park.available_bays
        self.assertEqual(self.available_bays, 100)








