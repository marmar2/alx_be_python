import unittest
from simple_calculator import SimpleCalculator


class Testcal(unittest.TestCase):

    def setUp(self):
        # This creates a calculator instance before each test
        self.calc = SimpleCalculator()
    
    def test_addition(self):
        self.assertEqual(self.calc.add(4,3),7)
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(4,3),1)
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(4,3),12)    
    def test_division(self):
        self.assertEqual(self.calc.divide(4,2),2)
        self.assertIsNone(self.calc.divide(4,0))
        


if __name__ == "__main__":
  unittest.main()        