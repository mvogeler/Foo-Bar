import unittest
import solution

class MyTestCase(unittest.TestCase):
    def test_something(self):
        data = [1, 2, 3]
        result = solution.solution(data, 0)
        self.assertEqual(result, [-1, -1])

    def test_something1(self):
        data = [1, 2, 3]
        result = solution.solution(data, 1)
        self.assertEqual(result, [0, 0])

    def test_something2(self):
        data = [1, 2, 3]
        result = solution.solution(data, 3)
        self.assertEqual(result, [0, 1])

    def test_something3(self):
        data = [1, 2, 3]
        result = solution.solution(data, 6)
        self.assertEqual(result, [0, 2])

    def test_something4(self):
        data = [1, 2, 3]
        result = solution.solution(data, 5)
        self.assertEqual(result, [1, 2])

    def test_something5(self):
        data = [1, 2, 3]
        result = solution.solution(data, 7)
        self.assertEqual(result, [-1, -1])

    def test_something6(self):
        data = [1, 2, 3, 4]
        result = solution.solution(data, 15)
        self.assertEqual(result, [-1, -1])

    def test_something7(self):
        data = [4, 3, 10, 2, 8]
        result = solution.solution(data, 12)
        self.assertEqual(result, [2, 3])

if __name__ == '__main__':
    unittest.main()
