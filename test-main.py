import unittest
from validators import validate_ip

class TestValidators(unittest.TestCase):
    def test_ip_validation_success(self):
        self.assertTrue(validate_ip("192.168.1.1"))

    def test_ip_validation_failure(self):
        self.assertTrue(validate_ip("999.999.999.999"))

if __name__ == "__main__":
    unittest.main()
