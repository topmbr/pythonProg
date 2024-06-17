import unittest
from rectangle import calculate_area, calculate_perimeter

class TestRectangleFunctions(unittest.TestCase):

    def test_calculate_area(self):
        # Стандартные значения
        self.assertEqual(calculate_area(5, 3), 15)
        self.assertEqual(calculate_area(10, 10), 100)
        # Крайние случаи
        self.assertEqual(calculate_area(0, 5), 0)
        self.assertEqual(calculate_area(5, 0), 0)
        self.assertEqual(calculate_area(0, 0), 0)

    def test_calculate_perimeter(self):
        # Стандартные значения
        self.assertEqual(calculate_perimeter(5, 3), 16)
        self.assertEqual(calculate_perimeter(10, 10), 40)
        # Крайние случаи
        self.assertEqual(calculate_perimeter(0, 5), 10)
        self.assertEqual(calculate_perimeter(5, 0), 10)
        self.assertEqual(calculate_perimeter(0, 0), 0)

if __name__ == "__main__":
    unittest.main()
