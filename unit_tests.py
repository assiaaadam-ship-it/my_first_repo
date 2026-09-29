import unittest

class TestMath(unittest.TestCase):
    def test_plus(self):
        self.asserEqual(4, 2+2)


if __name__ == '__main__':
    unittest.main()