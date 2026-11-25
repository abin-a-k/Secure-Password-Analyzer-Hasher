# Secure Password Analyzer & Hasher
## Project Overview

Secure Password Analyzer & Hasher is a Python-based command-line
cybersecurity application designed to analyze password strength,
generate secure password hashes using Argon2id, and verify passwords
against their generated hashes.

The application uses the zxcvbn library to estimate password strength
and the Argon2id algorithm for password hashing.
## Project Objectives

- Analyze password strength.
- Identify common and weak password patterns.
- Generate secure password hashes using Argon2id.
- Verify passwords against their hashes.
- Handle incorrect passwords and invalid hashes safely.
- Demonstrate basic password security concepts through a Python application.
## Technologies Used

- Python
- Argon2id
- argon2-cffi
- zxcvbn
- Visual Studio Code
- Python unittest
## Features

- Password strength analysis using zxcvbn.
- Password strength score from 0 to 4.
- Identification of common password weaknesses.
- Secure password hashing using Argon2id.
- Password verification using the generated hash.
- Hidden password input using Python's getpass module.
- Safe handling of incorrect passwords and invalid hashes.
- Automated testing using Python unittest.

## Application Workflow

1. The user launches the application.
2. The application displays a command-line menu.
3. The user selects a password analysis, hashing, or verification option.
4. For password analysis, the application evaluates the password strength.
5. For hashing, the application generates an Argon2id hash.
6. For verification, the application checks whether the entered password matches the hash.
7. The application displays the result.

## Security Considerations

- Passwords are not stored in plaintext by this application.
- Argon2id is used for password hashing.
- Password verification does not decrypt the hash.
- Password input is hidden during sensitive operations.
- The application is designed for educational and portfolio purposes.
## Installation

### Requirements

- Python 3.10 or later
- pip

### Setup

1. Clone the repository:

   git clone https://github.com/abin-a-k/Secure-Password-Analyzer-Hasher.git

2. Navigate to the project directory:

   cd Secure-Password-Analyzer-Hasher

3. Create a virtual environment:

   python -m venv .venv

4. Activate the virtual environment on Windows:

   .venv\Scripts\activate

5. Install the required dependencies:

   pip install -r requirements.txt

## Usage

Run the application using:

python src/main.py

The application displays a menu with the following options:

1. Analyze Password Strength
2. Hash a Password
3. Verify a Password
4. Exit

Select an option and follow the instructions displayed in the terminal.
## Testing

The application was tested using manual testing and automated unit tests.

### Manual Testing

The following features were tested manually:

- Password strength analysis.
- Password hashing using Argon2id.
- Verification of a correct password.
- Verification of an incorrect password.
- Handling of invalid password hashes.
- Command-line menu functionality.

### Automated Testing

Automated tests were written using Python's unittest framework.

The following test cases were executed:

1. Password analysis test.
2. Password hashing test.
3. Correct password verification test.
4. Incorrect password verification test.
5. Invalid hash verification test.

All 5 automated tests passed successfully.

### Test Command

Run the automated tests using:

```cmd
python -m unittest discover -s tests -v
```

### Test Result

The application successfully completed all 5 automated tests. The tests confirmed that the main password analysis, hashing, and verification functions behaved as expected.
