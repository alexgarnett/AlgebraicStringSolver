import unittest
from src.solver import *


class TestMathSolver(unittest.TestCase):

    def test_invalid_input(self):
        with self.assertRaises(Exception):
            solve('2 & 2')

    def test_proper_format(self):
        self.assertEqual(proper_format('2'), '2.00')
        self.assertEqual(proper_format('3.1'), '3.10')

    def test_multiplication(self):
        self.assertEqual(do_step(['2', '*', '3']), ['6.0'])

    def test_division(self):
        self.assertEqual(do_step(['6', '/', '3']), ['2.0'])

    def test_division_by_zero(self):
        with self.assertRaises(SystemExit):
            do_step(['6', '/', '0'])

    def test_full_solve(self):
        self.assertEqual(solve('2 + 3 * 4'), '14.00')
        self.assertEqual(solve('18 / 2 - 3'), '6.00')

    def test_adjacent_operators(self):
        with self.assertRaises(Exception):
            solve('1 + 5 -* 6')

    def test_format_beginning(self):
        with self.assertRaises(Exception):
            solve('/ 1 + 8')

    def test_format_end(self):
        with self.assertRaises(Exception):
            solve('7 * 3 -')

    def test_spacing_around_operators(self):
        with self.assertRaises(Exception):
            solve('10/ 2')

    def test_spacing_follow_operator(self):
        with self.assertRaises(Exception):
            solve('5 +  7')


if __name__ == '__main__':
    unittest.main()
