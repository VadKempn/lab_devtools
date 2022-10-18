from main import fourth_angle
import unittest


class Test(unittest.TestCase):
    def test_1(self):
        """
        It tests the fourth_angle function.
        """
        self.assertEqual(fourth_angle(2, 5, 1), 10)
        self.assertEqual(fourth_angle(4, 1, 7), 28)
        self.assertEqual(fourth_angle(2, 8, 3), 48)
        self.assertEqual(fourth_angle(4, 5, 1), 10)


qu

