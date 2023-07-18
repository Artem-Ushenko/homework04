import random
import string


class PasswordGenerator:
    """
    Was created class for object Password Generator based on task.

    This class can generate a random password of a specified length, including
    optional combinations of uppercase and lowercase letters, digits, and special characters.

   Attributes:
        length (int): Length of the password to be generated.
        include_uppercase (bool): Whether to include uppercase letters in the password.
        include_lowercase (bool): Whether to include lowercase letters in the password.
        include_digits (bool): Whether to include digits in the password.
        include_special_chars (bool): Whether to include special characters in the password.
    """

    def __init__(self, length=8, include_uppercase=True, include_lowercase=True, include_digits=True,
                 include_special_chars=True):
        """
        Method initialization with conditions: length, include uppercase letters, include lowercase letters,
        include digits and include special symbols for object Password Generator

        Initialize PasswordGenerator with the user's preferences.

        Args:
        length (int, optional): Desired length of the password. Defaults to 8.
        include_uppercase (bool, optional): If True, includes uppercase letters in the password. Defaults to True.
        include_lowercase (bool, optional): If True, includes lowercase letters in the password. Defaults to True.
        include_digits (bool, optional): If True, includes digits in the password. Defaults to True.
        include_special_chars (bool, optional): If True, includes special characters in the password. Defaults to True.
        """

        self.length = length
        self.include_uppercase = include_uppercase
        self.include_lowercase = include_lowercase
        self.include_digits = include_digits
        self.include_special_chars = include_special_chars

    def generator(self):
        """
        Generate and return a random password based on the initialized attributes.

        The generated password can include a mix of uppercase and lowercase letters,
        digits, and special characters, based on the user's preferences set during initialization.

        Returns:
        The randomly generated password as a string.
        """
        character_sets = []

        if self.include_uppercase:
            character_sets.append(string.ascii_uppercase)

        if self.include_lowercase:
            character_sets.append(string.ascii_lowercase)

        if self.include_digits:
            character_sets.append(string.digits)

        if self.include_special_chars:
            character_sets.append(string.punctuation)

        if not character_sets:
            raise ValueError("At least one character set must be included.")

        password = ''
        for _ in range(self.length):
            character_set = random.choice(character_sets)
            password += random.choice(character_set)

        return password


def get_input_parameter(prompt):
    """
    Check function for input parameter which must be only yes or no.

    If the user enters an invalid input (not 'yes' or 'no'), the function will
    repeatedly ask until a valid input is given.

    Args:
    'prompt' (str): The question to ask the user.

    Returns:
    bool: Returns True if user's response is 'yes', False if 'no'.

    """

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

# Waiting for the input of responses from the user
include_uppercase = get_input_parameter("Include uppercase letters (yes/no): ")
include_lowercase = get_input_parameter("Include lowercase letters (yes/no): ")
include_digits = get_input_parameter("Include digits (yes/no): ")
include_special_chars = get_input_parameter("Include special symbols (yes/no): ")

# Declare a variable and assign our class PasswordGenerator to it
your_password = PasswordGenerator(length, include_uppercase, include_lowercase, include_digits, include_special_chars)

# Print the value to the CLI
print(f"Your password: {your_password.generator()}")
