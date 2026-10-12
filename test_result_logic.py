
import unittest
from result_logic import predict_result


class TestPredictResult(unittest.TestCase):

    def test_pass_result(self):
        self.assertEqual(predict_result(70, 85), "FAIL")

    def test_fail_low_internal_marks(self):
        self.assertEqual(predict_result(30, 85), "FAIL")

    def test_fail_low_attendance(self):
        self.assertEqual(predict_result(70, 60), "FAIL")

    def test_fail_both_conditions(self):
        self.assertEqual(predict_result(30, 60), "FAIL")

    def test_minimum_pass_conditions(self):
        self.assertEqual(predict_result(40, 75), "PASS")


if __name__ == "__main__":
    unittest.main()
