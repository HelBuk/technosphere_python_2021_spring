import unittest
from main import CustomList


class TestList(unittest.TestCase):

    def test_sum(self):
        """
        Test of checking summation
        """
        a = CustomList([1, 3, 5]) + [1, 2]
        b = [2, 5, 5]
        self.assertEqual(str(a), str(b))

    def test_rsum(self):
        """
        Test of checking right summation
        """
        a = [1, 2] + CustomList([1, 3, 5])
        b = CustomList([1, 2]) + CustomList([1, 3, 5])
        self.assertEqual(str(a), str(b))

    def test_sub(self):
        """
        Test of checking subtraction
        """
        a = CustomList([1, 2]) - [1, 3, 5]
        b = [0, -1, -5]
        self.assertEqual(str(a), str(b))

    def test_rsub(self):
        """
        Test of checking right subtraction
        """
        a = [1, 3, 5] - CustomList([1, 2])
        b = CustomList([1, 3, 5]) - CustomList([1, 2])
        self.assertEqual(str(a), str(b))

    def test_mid(self):
        """
              Test of checking the work of mid function
        """
        a = [1, 2]
        b = CustomList([1, 2])
        c = CustomList.mid(b,a)
        d = list
        self.assertEqual(type(c[2]), d)


if __name__ == '__main__':
    unittest.main()