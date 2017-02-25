import unittest
from semantic_comparator import *


class TestInputArguments(unittest.TestCase):

    def test_capture_arguments(self):
        self.assertEqual(capture_arguments(), False)
        self.assertEqual(capture_arguments(["1","1"]), False)
        self.assertEqual(capture_arguments(["a", "1"]), False)
        self.assertEqual(capture_arguments(["a", "1"]), False)

    def test_return_weighted_arguments(self):
        self.assertIsInstance(return_weighted_arguments(["1.0.0", "1.0.0"]), list)
        # self.assertTrue('FOO'.isupper())
        # self.assertFalse('Foo'.isupper())
        # self.assertEqual(s.split(), ['hello', 'world'])

    def test_is_valid_version_string(self):
        self.assertTrue(is_valid_version_string("1.0.0"))
        self.assertFalse(is_valid_version_string("1.0"))

    def test_calculate_weights(self):
        self.assertEqual(calculate_weights(["1.0.0", "1.0.0"]), [100, 100])

    # def test_test_versions(self):
    #     self.assertEqual(None, False)
    #
    # def test_main(self):
    #     self.assertEqual(None, False)


def run_tests():
    unittest.main()

if __name__ == '__main__':
    unittest.main()
