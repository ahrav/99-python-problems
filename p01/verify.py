import unittest
from collections import namedtuple

from solution import answer

TestParameter = namedtuple('TestParameters', ['list_', 'last'], verbose=False)
TestParameters = [
            TestParameter(list_=[1], last=1),
            TestParameter(list_=[1,2], last=2),
            TestParameter(list_=[1,2,3], last=3),
        ]

class TestP01(unittest.TestCase):

    def test_answer(self):
        for test_parameter in TestParameters:
            actual = answer(test_parameter.list_)
            self.assertEqual(actual, test_parameter.last)

    def test_answer_empty_list(self):
        with self.assertRaises(IndexError) as context:
            list_ = []
            answer(list_)

    def test_big_list(self):
        list_ = range(100000000000000000000000000000)
        last = 99999999999999999999999999999
        actual = answer(list_)
        self.assertEqual(actual, last)

    def test_reference(self):
        a, b, c = ([1], [1, 1], [[1], 1, 1])
        list_ = [a, b, c]
        actual = answer(list_)
        import pdb; pdb.set_trace()
        self.assertEqual(actual, c)
        self.assertFalse(actual is c)

        deep = c[0]
        self.assertEqual(actual[0], deep)
        self.assertFalse(actual[0] is deep)

if __name__ == "__main__":
    unittest.main()
