import unittest

from karatsuba import karatsuba


class KaratsubaTestCase(unittest.TestCase):
    def test_karatsuba(self):
        self.assertEqual(25, karatsuba(5, 5))
        self.assertEqual(408, karatsuba(12, 34))
        self.assertEqual(7006652, karatsuba(1234, 5678))


if __name__ == '__main__':
    unittest.main()
