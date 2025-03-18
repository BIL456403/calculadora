import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora()

    def test_multiplicar(self):
        self.assertEqual(self.calc.multiplicar(2, 3), 6)
        self.assertEqual(self.calc.multiplicar(-1, 5), -5)
        self.assertEqual(self.calc.multiplicar(0, 100), 0)
        self.assertEqual(self.calc.multiplicar("2", "3"), 6)
        self.assertEqual(self.calc.multiplicar("a", "b"), "Por favor, ingresa dos números válidos.")

if __name__ == "__main__":
    unittest.main()
