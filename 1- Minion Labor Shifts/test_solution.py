import unittest
import solution

class MyTestCase(unittest.TestCase):
    def test_something(self):
        data = [1, 2, 3]
        result = solution.solution(data, 0)
        self.assertEqual(len(result), 0)

    def test_something_else(self):
        data = [1, 2, 2, 3, 3, 3, 4, 5, 5]
        result = solution.solution(data, 1)
        self.assertEqual(len(result), 2)
        self.assertEqual(result, [1,4])

    def test_something_else2(self):
        data = [1, 2, 2, 3, 3, 3, 4, 5, 5]
        result = solution.solution(data, 2)
        self.assertEqual(len(result), 6)
        self.assertEqual(result, [1,2,2,4,5,5])

    def test_something_else3(self):
        data = [5, 2, 2, 3, 3, 3, 4, 5, 1]
        result = solution.solution(data, 2)
        self.assertEqual(len(result), 6)
        self.assertEqual(result, [5,2,2,4,5,1])

if __name__ == '__main__':
    unittest.main()
