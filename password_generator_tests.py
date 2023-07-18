import unittest
from password_generator_oop import PasswordGenerator


class TestPasswordGenerator(unittest.TestCase):

    def test_password_length(self):
        """Test that the generated password has the correct length"""
        password_gen = PasswordGenerator(length=10)
        password = password_gen.generator()
        self.assertEqual(len(password), 10)

    def test_only_uppercase(self):
        """Test that password contains only uppercase if other flags are set to False"""
        password_gen = PasswordGenerator(length=10, include_uppercase=True, include_lowercase=False,
                                         include_digits=False, include_special_chars=False)
        password = password_gen.generator()
        self.assertTrue(password.isupper())

    def test_only_lowercase(self):
        """Test that password contains only lowercase if other flags are set to False"""
        password_gen = PasswordGenerator(length=10, include_uppercase=False, include_lowercase=True,
                                         include_digits=False, include_special_chars=False)
        password = password_gen.generator()
        self.assertTrue(password.islower())

    def test_only_digits(self):
        """Test that password contains only digits if other flags are set to False"""
        password_gen = PasswordGenerator(length=10, include_uppercase=False, include_lowercase=False,
                                         include_digits=True, include_special_chars=False)
        password = password_gen.generator()
        self.assertTrue(password.isdigit())

    def test_no_char_set(self):
        """Test that exception is raised when all char sets are set to False"""
        password_gen = PasswordGenerator(length=10, include_uppercase=False, include_lowercase=False,
                                         include_digits=False, include_special_chars=False)
        with self.assertRaises(ValueError):
            password_gen.generator()


if __name__ == "__main__":
    unittest.main()
