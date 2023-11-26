import unittest
import builtins
from payment import modif1
from unittest.mock import mock_open, patch, MagicMock, call
class TestPayment(unittest.TestCase):
    def test_function_name(self):

       result = modif1('employee_file.txt')  # Call the function being tested

       self.assertEqual(result, "BASIC SALARY UPDATED SUCCESSFULLY!")
if __name__ == '__main__':
    unittest.main()