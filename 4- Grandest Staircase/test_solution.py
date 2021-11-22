import unittest
import solution

class MyTestCase(unittest.TestCase):

    def test_something(self):
        result = solution.solution(200)
        self.assertEqual(result, 487067745)

    def test_something2(self):
        result = solution.solution(3)
        self.assertEqual(result, 1)

    def test_something3(self):
        result = solution.solution(1)
        self.assertEqual(result, 0)

        result = solution.solution(2)
        self.assertEqual(result, 0)

    def test_something4(self):
        result = solution.solution(6)
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()
