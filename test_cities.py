import unittest
from city_functions import city_function
class City_test(unittest.TestCase):
    def test_city_country(self):
        city_funtcion = city_function("santiago","chile")
        self.assertEqual(city_funtcion,"santiago, chile")
    def test_city_country_population(self):
        city_funtcion = city_function("santiago","chile",population = "5000000")
        self.assertEqual(city_funtcion, "santiago, chile - population 5000000")
unittest.main()