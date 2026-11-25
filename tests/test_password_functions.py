import os
import sys
import unittest

# Add the src folder to Python's import path
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "src")
    )
)

from analyzer import analyze_password
from hasher import hash_password, verify_password


class TestPasswordFunctions(unittest.TestCase):

    def test_password_analysis(self):
        password = "correct-horse-dummy-123"

        result = analyze_password(password)

        self.assertIn("score", result)
        self.assertIn("guesses", result)
        self.assertIn("warning", result)
        self.assertIn("suggestions", result)

        self.assertGreaterEqual(result["score"], 0)
        self.assertLessEqual(result["score"], 4)

    def test_password_hashing(self):
        password = "DummyPassword123!"

        hashed_password = hash_password(password)

        self.assertNotEqual(password, hashed_password)
        self.assertTrue(hashed_password.startswith("$argon2id$"))

    def test_correct_password_verification(self):
        password = "DummyPassword123!"

        hashed_password = hash_password(password)

        self.assertTrue(
            verify_password(password, hashed_password)
        )

    def test_incorrect_password_verification(self):
        password = "DummyPassword123!"

        hashed_password = hash_password(password)

        self.assertFalse(
            verify_password("WrongDummyPassword", hashed_password)
        )
    def test_invalid_hash_verification(self):
        password = "DummyPassword123!"
        invalid_hash = "this-is-not-a-valid-hash"
        self.assertFalse(
            verify_password(password,invalid_hash)
        )
if __name__ == "__main__":
    unittest.main()