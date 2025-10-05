import unittest
from simple_calculator import SimpleCalculator


class Testcal(unittest.TestCase):

    def setUp(self):
        # This creates a calculator instance before each test
        self.calc = SimpleCalculator()
    
    def test_addition(self):
        result = self.calc.add(4,3)
        self.assertEqual(result,7)
    def test_Subtract(self):
        result = self.calc.subtract(4,3)
        self.assertEqual(result,1)
    def test_multiply(self):
        result = self.calc.multiply(4,3)
        self.assertEqual(result,12)    
    def test_divide(self):
        self.assertEqual(self.calc.divide(4,2),2)
        self.assertIsNone(self.calc.divide(4,0))
        


if __name__ == "__main__":
  unittest.main()        