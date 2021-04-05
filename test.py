import unittest
from main import TicTacGame
import random


class TestGame(unittest.TestCase):
    def setUp(self):
        self.class_test = TicTacGame()
        self.table_attr = TicTacGame.table
        self.cnt_attr = TicTacGame.cnt
        self.res = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    def test_checking_winner(self):
        """
        Test of checking winner
        """
        for each in self.res:
            for i in each:
                self.table_attr[i - 1] = 'x'
            a = f"{self.class_test.check_winner()} is winning"
            b = "x is winning"
            self.assertEqual(a, b)
            self.table_attr = list(range(1, 10))

    def test_checking_draw(self):
        """
        Test of checking a draw
        """
        xy = ('x', 'o')
        for i in range(1, 10):
            self.table_attr[i - 1] = random.choice(xy)
        count = 0
        for each in self.res:
            if self.table_attr[each[0] - 1] != self.table_attr[each[1] - 1] != self.table_attr[each[2] - 1]:
                count += 1
                if count == len(self.res):
                    c = 'Ничья'
                    d = self.class_test.check_winner()
                    self.assertEqual(c, d)


if __name__ == '__main__':
    unittest.main()
