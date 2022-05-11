from unit import Car, random_financing_model
import unittest

class TestFinancing(unittest.TestCase):

    def test_random_financing_model(self):
        car = Car("Honda", "Civic", "2009", "Green", 100000)
        self.assertEqual(random_financing_model(car.value), car.value // 3)

if __name__ == '__main__':
    unittest.main()