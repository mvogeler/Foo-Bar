import unittest
import solution

class MyTestCase(unittest.TestCase):

    def test_something(self):
        result = solution.solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]])
        self.assertEqual([7, 6, 8, 21], result)

    def test_something2(self):
        result = solution.solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
        self.assertEqual([0, 3, 2, 9, 14], result)

if __name__ == '__main__':
    unittest.main()
