import unittest
from fixedIncomeModels import macaulayDuration, modifiedDuration


class fixedIncomeItem:

    def __init__(self, face_value, num_years, coupon_payment_percent, curr_interest_rate):
        self.face_value = face_value
        self.num_years = num_years
        self.coupon_payment_percent = coupon_payment_percent
        self.curr_interest_rate = curr_interest_rate

    def getItemParams(self):
        return self.face_value, self.num_years, self.coupon_payment_percent, self.curr_interest_rate


class FixedIncomeModelTest(unittest.TestCase):

    def setUp(self):
        # Write code here if I need multiple values across the test
        self.fixedIncomeTestEx1 = fixedIncomeItem(1000, 5, 0.04, 0.045)
        self.fixedIncomeTestEx2 = fixedIncomeItem(1000, 5, 0.05, 0.05)
        # TODO: WRITE MORE INCOME EXAMPLES FOR MORE ADVANCED TESTING

    def test_maucaulay_duration(self):
        values1 = self.fixedIncomeTestEx1.getItemParams()
        self.assertEqual(macaulayDuration(values1[0], values1[1], values1[2], values1[3]), 4.63)

        values2 = self.fixedIncomeTestEx2.getItemParams()
        self.assertEqual(macaulayDuration(values2[0], values2[1], values2[2], values2[3]), 4.55)

    def test_modifided_duration(self):
        values = self.fixedIncomeTestEx1.getItemParams()
        self.assertEqual(modifiedDuration(values[0], values[1], values[2], values[3], 1), 4.43)
