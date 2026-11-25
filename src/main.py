from getpass import getpass
from analyzer import analyze_password
from hasher import hash_password, verify_password


def show_menu():
    print("\n===== Secure Password Analyzer & Hasher =====")
    print("1. Analyze Password Strength")
    print("2. Hash a Password")
    print("3. Verify a Password")
    print("4. Exit")


def analyze_option():
    password = getpass("\nEnter a dummy password to analyze: ")

    result = analyze_password(password)

    print("\n--- Password Strength Analysis ---")
    print("Strength Score:", result["score"])
    print("Estimated Guesses:", result["guesses"])

    print("\nWarning:")

    if result["warning"]:
        print(result["warning"])
    else:
        print("No specific weaknesses detected.")

    print("\nSuggestions:")

    if result["suggestions"]:
        for suggestion in result["suggestions"]:
            print("-", suggestion)
    else:
        print("No improvement suggestions.")


def hash_option():
    password = getpass("\nEnter a dummy password to hash: ")

    hashed_password = hash_password(password)

    print("\nPassword hashed successfully.")
    print("Generated Argon2id hash:")
    print(hashed_password)


def verify_option():
    stored_hash = input("\nEnter the stored Argon2id hash: ")
    password = getpass("Enter the password to verify: ")

    if verify_password(password, stored_hash):
        print("\nPassword verification successful!")
    else:
        print("\nPassword verification failed!")


def main():
    while True:
        show_menu()

        choice = input("\nChoose an option (1-4): ")

        if choice == "1":
            analyze_option()

        elif choice == "2":
            hash_option()

        elif choice == "3":
            verify_option()

        elif choice == "4":
            print("\nThank you for using the application!")
            break

        else:
            print("\nInvalid choice. Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()