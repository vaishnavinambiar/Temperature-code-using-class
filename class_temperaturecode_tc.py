import unittest
from Temperature_using_class import *

class TemperatureTestCase(unittest.TestCase):

    def test_one(self):
        self.year = 2015
        self.month = 4
        self.day = 5
        self.assertEqual(self.year, 2015)
        self.assertEqual(self.month, 4)
        self.assertEqual(self.day, 5)

    def test_two(self):
        year = 2016
        month = 4
        day = 5
        self.assertEqual(my_date, [])

    def test_three(self):
        temp = 55
        convert_to_fahren= (9*temp+32*5)/5
        self.assertEqual(convert_to_fahren, 131.0)

    def test_four(self):
        temp = 66
        convert_to_celcius = (5*temp-32*5)/9
        self.assertEqual(convert_to_celcius, 131.0)

    def test_five(self):
        temperatures = [1.0, 2.0, 3.0]
        self.assertEqual(max(temperatures), 3.0)

    def test_six(self):
        temperatures = [1.0, 2.0, 3.0]
        self.assertEqual(min(temperatures), 1.0)

    def test_seven(self):
        average = (1.0 + 2.0 + 3.0)/3
        self.assertEqual(average, 2.0)
        
        
        

if __name__== '__main__':
    unittest.main()
