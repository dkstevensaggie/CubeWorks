import unittest
import Drivers.cpuTemp.cpuTempDriver as cpuTemp

## this is a test function that return a possible temp ##
#def func(num):
#    return num

class TestCpu(unittest.TestCase): # in this case with only one function to be tested, do I really need a class?
    """
    Initializes a test case for the cpu temperature sensor
    Defines methods that test the following:
    1. Asserts that it returns a valid temperature.
    """
    testCpu = cpuTemp.measureCpuTemp() # initialize
    ## this is the test of the test ##
#    testCpu = func(50)

    def testCpuTemp(self):
        """
        Asserts that the cpuTemp returns a valid temperature between a low and a high and a low temp.
        """
        lowtemp = 0
        hightemp = 100
        self.assertTrue(lowtemp <= self.testCpu <= hightemp)


if __name__ == '__main__':
    unittest.main()
