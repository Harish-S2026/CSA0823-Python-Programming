
# Task 9: Calculator and automated tests

import unittest

BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30


def payout(litres, fat, snf):
    """Validate inputs and calculate payment."""
    if litres <= 0:
        raise ValueError("Litres must be positive")

    if not 2.0 <= fat <= 7.0:
        raise ValueError("Fat must be between 2.0 and 7.0")

    if snf <= 0:
        raise ValueError("SNF must be positive")

    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)

    rate = BASE_RATE + fat_steps * FAT_STEP_VALUE \
           + snf_steps * SNF_STEP_VALUE

    return round(litres * round(rate, 2), 2)


class TestMilkPayment(unittest.TestCase):

    def test_standard(self):
        self.assertEqual(payout(10, 3.5, 8.5), 300.00)

    def test_above_standard(self):
        self.assertEqual(payout(8.5, 4.2, 8.7), 283.90)

    def test_below_standard(self):
        self.assertEqual(payout(12, 3.1, 8.3), 333.60)

    def test_lowest_fat(self):
        self.assertEqual(payout(10, 2.0, 8.5), 240.00)

    def test_highest_fat(self):
        self.assertEqual(payout(10, 7.0, 8.5), 440.00)

    def test_negative_litres(self):
        with self.assertRaises(ValueError):
            payout(-5, 3.5, 8.5)

    def test_invalid_fat(self):
        with self.assertRaises(ValueError):
            payout(10, 8.0, 8.5)


if __name__ == "__main__":
    unittest.main()
