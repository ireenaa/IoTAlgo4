import unittest
from src.lab4 import floodfill


class TestFloodFill(unittest.TestCase):

    def test_floodfill_single_color(self):
        mat1 = [['A', 'A', 'A'], ['A', 'B', 'A'], ['A', 'A', 'A']]
        floodfill(mat1, 1, 1, 'C')
        self.assertEqual(mat1, [['A', 'A', 'A'], ['A', 'C', 'A'], ['A', 'A', 'A']])

    def test_floodfill_different_color(self):
        mat2 = [['X', 'X', 'X'], ['X', 'Y', 'X'], ['X', 'X', 'X']]
        floodfill(mat2, 1, 1, 'U')
        self.assertEqual(mat2, [['X', 'X', 'X'], ['X', 'U', 'X'], ['X', 'X', 'X']])

    def test_floodfill_complex(self):
        mat3 = [['R', 'R', 'G', 'G', 'G'], ['R', 'R', 'G', 'B', 'B'], ['R', 'R', 'B', 'B', 'B'],
                ['R', 'R', 'B', 'B', 'B']]
        floodfill(mat3, 0, 2, 'Y')
        self.assertEqual(mat3, [['R', 'R', 'Y', 'Y', 'Y'], ['R', 'R', 'Y', 'B', 'B'], ['R', 'R', 'B', 'B', 'B'],
                                ['R', 'R', 'B', 'B', 'B']])

    def test_floodfill_edge_case_1x1(self):
        mat4 = [['X']]
        floodfill(mat4, 0, 0, 'Y')
        self.assertEqual(mat4, [['Y']])

    def test_floodfill_edge_case_empty(self):
        mat5 = []
        floodfill(mat5, 0, 0, 'Y')
        self.assertEqual(mat5, [])


if __name__ == '__main__':
    unittest.main()
