import unittest
from my_code import add


class Test(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(add(""), 0)

    def test_single_number(self):
        self.assertEqual(add("3"), 3)

    def test_two_numbers(self):
        self.assertEqual(add("1,2"), 3)

    def test_multiple_numbers(self):
        self.assertEqual(add("1,2,3"), 6)

    def test_multiple_numbers2(self):
        self.assertEqual(add("10,20,30,40"), 100)

    def test_newline(self):
        with self.assertRaises(ValueError):
            add("\n")

    def test_newline2(self):
        self.assertEqual(add("1\n2\n3"), 6)

    def test_newline3(self):
        self.assertEqual(add("1\n2,3"), 6)

    def test_invalid_newline(self):
        with self.assertRaises(ValueError):
            add(",\n1")

    def test_invalid_newline2(self):
        with self.assertRaises(ValueError):
            add("1\n,2")

    def test_invalid_newline3(self):
        with self.assertRaises(ValueError):
            add("1,2\n,")

    def test_invalid_newline4(self):
        with self.assertRaises(ValueError):
            add("1,\n,3")

    def test_invalid_newline5(self):
        with self.assertRaises(ValueError):
            add("1,,3")


if __name__ == "__main__":
    unittest.main()
