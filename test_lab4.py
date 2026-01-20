import unittest

from lab4_pattern import Logger

class TestMath(unittest.TestCase):

    def test_add(self):
        self.assertEqual(2 + 3, 5)

    def test_subtract(self):
        self.assertEqual(10 - 4, 6)

    def test_multiply(self):
        self.assertEqual(3 * 4, 12)

    def test_divide(self):
        self.assertEqual(12 / 3, 4)

class TestLoggerSingleton(unittest.TestCase):

    def test_singleton_instance(self):
        logger1 = Logger()
        logger2 = Logger()
        self.assertIs(logger1, logger2)

if __name__ == "__main__":
    unittest.main()

