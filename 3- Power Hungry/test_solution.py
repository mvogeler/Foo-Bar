import unittest
import solution

class MyTestCase(unittest.TestCase):
    def test_something(self):
        data = [2, 0, 2, 2, 0]
        result = solution.solution(data)
        self.assertEqual(result, "8")

    def test_something1(self):
        data = [-2, -3, 4, -5]
        result = solution.solution(data)
        self.assertEqual(result, "60")

    def test_something2(self):
        data = [2, -3, 1, 0, -5]
        result = solution.solution(data)
        self.assertEqual(result, "30")

    def test_something3(self):
        data = [0, 0]
        result = solution.solution(data)
        self.assertEqual(result, "0")

    def test_something4(self):
        data = [2]
        result = solution.solution(data)
        self.assertEqual(result, "2")

    def test_something5(self):
        data = [2, 3, 4]
        result = solution.solution(data)
        self.assertEqual(result, "24")

    def test_something6(self):
        data = [1, 3, 4]
        result = solution.solution(data)
        self.assertEqual(result, "12")

    def test_something7(self):
        data = [-1]
        result = solution.solution(data)
        self.assertEqual(result, "-1")

    def test_something8(self):
        data = [-2, 0, 0]
        result = solution.solution(data)
        self.assertEqual(result, "0")
        
if __name__ == '__main__':
    unittest.main()
