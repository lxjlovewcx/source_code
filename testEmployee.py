import unittest
from employee import Employee
class Employeetest(unittest.TestCase):
    def setUp(self):
        self.myself = Employee("xuejian","li",salery=10000)
    def test_give_default_raise(self):
        self.myself.give_raise()
        self.assertEqual(15000,self.myself.salery)
    def test_give_custom_raise(self):
        self.myself.give_raise(increase = 7500)
        self.assertEqual(17500,self.myself.salery)
unittest.main()