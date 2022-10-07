import unittest
from database import Calculadora



class Test(unittest.TestCase):
    def test_suma(self):
        self.assertEquals(Calculadora.suma(1,2), 3)

if __name__ == '__main__':
    unittest.main()