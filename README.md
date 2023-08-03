# Random Password Generator

This repository contains a Python script that generates a random password based on user preferences. The password can be of any length, and can include uppercase and lowercase letters, digits, and special characters.

## How To Use

Follow the instructions below to use the password generator:

### Prerequisites

Ensure that Python 3.x is installed on your system. You can verify this by typing `python --version` or `python3 --version` into your terminal or command prompt. If you do not have Python installed, please install it from [here](https://www.python.org/downloads/).

### Download and Run the Script

1. Clone the repository to your local machine using the command: 

   ```bash
   git clone https://github.com/Artem-Ushenko/homework04.git
   ```
   
2. Navigate into the repository's directory using:

   ```bash
   cd homework04
   ```

3. Run the script using Python3 with the command:

   ```bash
   python3 password_generator_oop.py
   ```

### User Inputs

When you run the script, it will prompt you for the following inputs:

1. **Password Length**: Enter the desired length of your password. The default length is 8 if you simply press Enter without typing anything.

2. **Character Types**: For each of the following character types, type 'yes' if you want to include them in your password, and 'no' if you do not:

   - Uppercase letters
   - Lowercase letters
   - Digits
   - Special characters (e.g., punctuation)

### Output

After you have provided all the inputs, the script will generate a random password according to your preferences and print it to the console.

## Important Note

Please remember to save your password in a secure location. This script does not store or remember any passwords it generates.

## Contributing

Contributions are welcome! Please read the contributing guidelines before making any changes.

## License

This project is licensed under the terms of the MIT license. See the [LICENSE](LICENSE) file for details.

## Running Tests

This repository also includes a test suite that verifies the correct functionality of the password generator. Here's how you can run the tests:

### Prerequisites

Ensure that you have Python 3.x installed on your system as well as the unittest module (which is included in standard Python installations).

### Run the Tests

1. Navigate to the directory containing the test file. If it is in the main directory, you don't need to change your location from the previous steps.

2. Run the test file using Python's -m flag (which allows modules to be located using the Python import path), with the following command:

   ```bash
   python -m unittest password_generator_tests.py
   ```

The test suite includes the following test cases:

- `test_password_length`: Checks that the password generator creates a password of the correct length.
- `test_only_uppercase`: Verifies that the password generator correctly includes only uppercase letters when all other options are disabled.
- `test_only_lowercase`: Verifies that the password generator correctly includes only lowercase letters when all other options are disabled.
- `test_only_digits`: Verifies that the password generator correctly includes only digits when all other options are disabled.
- `test_no_char_set`: Tests that the password generator raises an exception when all character sets are set to False.

You will see the test results in the command line interface. For each test case, you will see either "ok" (the test passed) or "FAILED" (the test did not pass). At the end of the test run, you will see a summary of the tests that passed and failed. 

If you encounter any failures, you can use the detailed output to debug the issues. For any contributions or changes, ensure all tests are passing to maintain the integrity of the password generator.
