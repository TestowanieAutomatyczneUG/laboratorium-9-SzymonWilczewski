import unittest
from unittest.mock import *

from src.zad02.main import Car


class CarTest(unittest.TestCase):
    def test_needs_fuel(self):
        test_object = Car()
        test_object.needsFuel = Mock(name='needsFuel')
        test_object.needsFuel.return_value = False

        self.assertFalse(test_object.needsFuel())

    def test_get_engine_temperature(self):
        test_object = Car()
        test_object.getEngineTemperature = Mock(name='getEngineTemperature')
        test_object.getEngineTemperature.return_value = 100

        self.assertEqual(100, test_object.getEngineTemperature())

    def test_drive_to(self):
        test_object = Car()
        test_object.driveTo = Mock(name='driveTo')
        destination = 'Warsaw'
        test_object.driveTo.return_value = f'Driving to {destination}'

        self.assertEqual('Driving to Warsaw', test_object.driveTo('Warsaw'))


if __name__ == '__main__':
    unittest.main()
