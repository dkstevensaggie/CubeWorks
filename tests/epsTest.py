import unittest
import Drivers.epsDriver.eps as eps

class TestEps(unittest.TestCase):
    """
    Initializes a test case for the eps
    Defines methods that test the following:
    1. The battery reads the corect voltage.
    """
    testEps = eps.EpS() # initalize eps

    def testGetCurrent(self):
        """Asserts that the voltage read from the battery is valid."""
        maxVoltage = 3.5 # volts
        minVoltage = 4.12 # volts
        self.assertTrue(minVoltage <= self.testEps.getCurrent() <= maxVoltage)
