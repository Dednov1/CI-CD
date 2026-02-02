import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.car import Car
import unittest

class TestCase(unittest.TestCase):
    def setUp(self):
        self.car = Car(model="BMW X5", fuel_capacity=80)

    def tearDown(self):
        pass

    def test_drive(self):
        self.car.drive(20)
        self.assertRaises(Exception, lambda: self.car.drive(80000))

    def test_refuel(self):
        # Заправим 20 литров
        self.car.refuel_car(20)
        assert self.car.get_current_fuel_level() == 20
        # Проверим, что будет исключение, если перельем
        self.assertRaises(Exception, lambda: self.car.refuel_car(80))
EOF
