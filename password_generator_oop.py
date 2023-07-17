import random
import string


class PasswordGenerator:
    """Was created class for object Password Generator"""

    def __init__(self, length=8, include_uppercase=True, include_lowercase=True, include_digits=True,
                 include_special_chars=True):
        """Method init with some conditions for object Password Generator"""

        self.length = length
        self.include_uppercase = include_uppercase
        self.include_lowercase = include_lowercase
        self.include_digits = include_digits
        self.include_special_chars = include_special_chars

    def generator(self):
        """The different character sets from which to generate the password"""

        uppercase_letters = string.ascii_uppercase if self.include_uppercase else ''
        lowercase_letters = string.ascii_lowercase if self.include_lowercase else ''
        digits = string.digits if self.include_digits else ''
        special_chars = string.punctuation if self.include_special_chars else ''

        # The combined character set
        all_chars = uppercase_letters + lowercase_letters + digits + special_chars

        # Generate a random password of the specified length
        password = ''.join(random.choice(all_chars) for _ in range(self.length))

        return password


def get_input_parameter(prompt):
    """Check function for input parameter which must be only yes or no"""

    response = input(prompt)
    if response.lower() in ['yes', 'no']:
        return response.lower() == 'yes'
    else:
        print("Please enter 'yes' or 'no' !!!")
        return get_input_parameter(prompt)


# Get the password length from the user, using a default value if no input is given
while True:
    try:
        length_input = input("Enter the desired password length (default: 8): ")
        length = int(length_input) if length_input else 8
        break
    except ValueError:
        print("Invalid input. Please enter an integer number.")

include_uppercase = get_input_parameter("Include uppercase letters (yes/no): ")
include_lowercase = get_input_parameter("Include lowercase letters (yes/no): ")
include_digits = get_input_parameter("Include digits (yes/no): ")
include_special_chars = get_input_parameter("Include special symbols (yes/no): ")

your_password = PasswordGenerator(length, include_uppercase, include_lowercase, include_digits, include_special_chars)
print(f"Your password: {your_password.generator()}")
