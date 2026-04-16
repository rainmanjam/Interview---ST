import unittest
from typing import cast

from sort import sort


class TestSort(unittest.TestCase):
    # STANDARD
    def test_standard_normal_package(self):
        self.assertEqual(sort(10, 10, 10, 5), "STANDARD")

    def test_standard_just_below_dimension_and_mass_thresholds(self):
        self.assertEqual(sort(149, 1, 1, 19), "STANDARD")

    def test_standard_volume_below_threshold(self):
        self.assertEqual(sort(99, 100, 100, 10), "STANDARD")

    # SPECIAL (bulky only)
    def test_special_bulky_by_volume_at_threshold(self):
        self.assertEqual(sort(100, 100, 100, 10), "SPECIAL")

    def test_special_bulky_by_volume_above_threshold(self):
        self.assertEqual(sort(200, 200, 200, 5), "SPECIAL")

    def test_special_bulky_by_width_at_threshold(self):
        self.assertEqual(sort(150, 1, 1, 5), "SPECIAL")

    def test_special_bulky_by_height_at_threshold(self):
        self.assertEqual(sort(1, 150, 1, 5), "SPECIAL")

    def test_special_bulky_by_length_at_threshold(self):
        self.assertEqual(sort(1, 1, 150, 5), "SPECIAL")

    def test_special_bulky_by_dimension_above_threshold(self):
        self.assertEqual(sort(200, 10, 10, 5), "SPECIAL")

    # SPECIAL (heavy only)
    def test_special_heavy_at_threshold(self):
        self.assertEqual(sort(10, 10, 10, 20), "SPECIAL")

    def test_special_heavy_above_threshold(self):
        self.assertEqual(sort(10, 10, 10, 50), "SPECIAL")

    # REJECTED (bulky and heavy)
    def test_rejected_bulky_by_volume_and_heavy(self):
        self.assertEqual(sort(100, 100, 100, 20), "REJECTED")

    def test_rejected_bulky_by_dimension_and_heavy(self):
        self.assertEqual(sort(150, 10, 10, 20), "REJECTED")

    def test_rejected_massively_oversized_and_overweight(self):
        self.assertEqual(sort(500, 500, 500, 100), "REJECTED")

    # Boundary checks
    def test_boundary_standard_case(self):
        self.assertEqual(sort(149, 1, 1, 19), "STANDARD")

    def test_boundary_volume_below_million(self):
        self.assertEqual(sort(99, 100, 100, 1), "STANDARD")

    def test_boundary_volume_at_million(self):
        self.assertEqual(sort(100, 100, 100, 1), "SPECIAL")

    def test_boundary_mass_19_not_heavy(self):
        self.assertEqual(sort(10, 10, 10, 19), "STANDARD")

    def test_boundary_mass_20_heavy(self):
        self.assertEqual(sort(10, 10, 10, 20), "SPECIAL")

    # Input validation
    def test_invalid_negative_width_raises_value_error(self):
        with self.assertRaises(ValueError):
            sort(-1, 10, 10, 5)

    def test_invalid_negative_mass_raises_value_error(self):
        with self.assertRaises(ValueError):
            sort(10, 10, 10, -1)

    def test_invalid_nan_dimension_raises_type_error(self):
        with self.assertRaises(TypeError):
            sort(float("nan"), 10, 10, 5)

    def test_invalid_infinity_mass_raises_type_error(self):
        with self.assertRaises(TypeError):
            sort(10, 10, 10, float("inf"))

    def test_invalid_string_argument_raises_type_error(self):
        with self.assertRaises(TypeError):
            sort(cast(float, "10"), 10, 10, 5)

    # Edge cases
    def test_edge_zero_dimensions(self):
        self.assertEqual(sort(0, 0, 0, 0), "STANDARD")

    def test_edge_zero_mass_large_volume(self):
        self.assertEqual(sort(100, 100, 100, 0), "SPECIAL")


if __name__ == "__main__":
    unittest.main()
