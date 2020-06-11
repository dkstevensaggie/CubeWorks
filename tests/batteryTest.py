import unittest
import Drivers.battery.battery_driver as bat

class TestBattery(unittest.TestCase):
    """
    Initializes a test case for the battery
    Defines methods that test the following:
    1. The battery reads the corect voltage.
    """
    testBat = bat.Battery() # initalize battery

    def testRead(self):
        """Asserts that the voltage read from the battery is valid."""
        maxVoltage = 3.5 # volts
        minVoltage = 4.12 # volts
        self.assertTrue(minVoltage <= self.testBat.read() <= maxVoltage)

