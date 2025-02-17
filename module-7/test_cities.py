# test_cities.py
import unittest
from city_functions import city_country

class CityCountryTestCase(unittest.TestCase):
    """Tests for the 'city_country' function."""

    def test_city_country(self):
        """Does 'Santiago, Chile - population 5000000' work?"""
        result = city_country("santiago", "chile", 5000000)
        self.assertEqual(result, "Santiago, Chile - population 5000000")

if __name__ == '__main__':
    unittest.main()
