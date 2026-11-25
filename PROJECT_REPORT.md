# Secure Password Analyzer & Hasher

## 1. Introduction

Password security is an important part of cybersecurity. Weak passwords can make user accounts vulnerable to unauthorized access.

The Secure Password Analyzer & Hasher is a Python-based command-line application developed to demonstrate basic password security concepts, including password strength analysis, secure password hashing, and password verification.

The application uses the zxcvbn library to analyze password strength and Argon2id to securely hash passwords.

## 2. Objectives

The main objectives of this project are:

- To analyze password strength.
- To identify common password weaknesses.
- To generate secure password hashes using Argon2id.
- To verify passwords against generated hashes.
- To handle incorrect passwords and invalid hashes safely.
- To understand password security through practical implementation.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| Argon2id | Password hashing |
| argon2-cffi | Argon2 implementation in Python |
| zxcvbn | Password strength estimation |
| unittest | Automated testing |
| Visual Studio Code | Development environment |

## 4. System Requirements

- Windows operating system
- Python 3.10 or later
- Visual Studio Code
- Required Python libraries
- Git for version control

## 5. Project Structure

```text
Secure-Password-Analyzer-Hasher/
├── src/
│   ├── main.py
│   ├── analyzer.py
│   └── hasher.py
├── tests/
│   └── test_password_functions.py
├── screenshots/
├── README.md
├── PROJECT_REPORT.md
├── requirements.txt
└── .gitignore
```

The `.venv` folder contains the project's virtual environment and is excluded from version control.

## 6. Project Features

### Password Strength Analysis

The application uses zxcvbn to estimate password strength.

The strength score ranges from 0 to 4:

- 0 – Very weak
- 1 – Weak
- 2 – Fair
- 3 – Strong
- 4 – Very strong

The application can also display warnings and suggestions when available.

### Password Hashing

The application uses Argon2id to generate password hashes.

Argon2id is a memory-hard password hashing algorithm designed to make password guessing more expensive.

A unique random salt is used when generating each hash.

### Password Verification

The application verifies whether an entered password matches a previously generated hash.

Password hashes are not decrypted. Verification checks whether the entered password produces a valid match.

### Hidden Password Input

The application uses Python's `getpass` module to hide password input during sensitive operations.

## 7. Application Workflow

1. The user launches the application.
2. The application displays a command-line menu.
3. The user selects an operation.
4. The application analyzes password strength, generates a hash, or verifies a password.
5. The application displays the result.
6. The user can continue using the menu or exit.

## 8. Testing

The application was tested using manual testing and automated unit tests.

### Manual Testing

The following operations were tested:

- Password strength analysis
- Password hashing
- Correct password verification
- Incorrect password verification
- Invalid hash handling
- Command-line menu operation

### Automated Testing

Automated tests were developed using Python's unittest framework.

The following five test cases were executed:

1. Password analysis
2. Password hashing
3. Correct password verification
4. Incorrect password verification
5. Invalid hash verification

All five automated tests passed successfully.

### Test Command

```cmd
python -m unittest discover -s tests -v
```

## 9. Screenshots

The following screenshots provide evidence of the application's functionality:

1. Application Menu – `screenshots/application-menu.png`
2. Password Analysis – `screenshots/password-analysis.png`
3. Automated Test Results – `screenshots/test-results.png`
4. Password Hashing and Verification – `screenshots/hashing-verification.png`

## 10. Security Considerations

- Passwords should never be stored in plaintext.
- Argon2id is used for password hashing.
- Password hashes cannot be directly decrypted.
- Password input is hidden during sensitive operations.
- Real passwords should never be used in screenshots or demonstrations.
- The application does not currently store hashes in a database or file.
- The application is an educational cybersecurity project and is not intended to replace a production authentication system.

## 11. Conclusion

The Secure Password Analyzer & Hasher project demonstrates the practical implementation of password security concepts using Python.

Through this project, the developer gained practical experience with password strength estimation, Argon2id hashing, password verification, command-line application development, and automated testing.

The project provides a foundation for further learning in application security and secure software development.