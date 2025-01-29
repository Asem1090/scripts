import argparse
from string import ascii_lowercase
from unittest.util import _MAX_LENGTH
from openpyxl import load_workbook
from itertools import product

def attempt_password(file_path, password):
    """
    Attempts to open the Excel file with the given password.
    """
    try:
        # Try opening the file with the password
        load_workbook(filename=file_path, read_only=True, keep_links=False, password=password)
        return True  # If no error, password is correct
    except Exception as e:
        return False  # Password is incorrect

def brute_force(file_path, possible_passwords):
    """
    Iterates over possible passwords and tests them on the Excel file.
    """
    for password in possible_passwords:
        print(f"Trying password: {password}")
        if attempt_password(file_path, password):
            print(f"Password found: {password}")
            return password
    print("Password not found.")
    return None

def generate_possible_passwords():
    """
    Generates possible passwords based on remembered patterns.
    """
    # Example: Use combinations of prefixes, suffixes, and numbers
    SUFFIX = "@2001!A"
    MAX_LENGTH = 13 - len(SUFFIX)
    
    for length in range(6, MAX_LENGTH + 1):
        for combo in product(ascii_lowercase, repeat=length):
            yield ''.join(combo) + SUFFIX

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Brute force an Excel file's password.")
    parser.add_argument("file_path", help="Path to the Excel file")
    args = parser.parse_args()

    # Generate password possibilities
    possible_passwords = generate_possible_passwords()

    # Run the brute-force function
    # found_password = brute_force(args.file_path, possible_passwords)
    found_password = brute_force(r"C:\Users\asems\OneDrive - Qatar University\Documents\Other\Zak F.xls", possible_passwords)

    # Print the result
    if found_password:
        print(f"The correct password is: {found_password}")
    else:
        print("Could not determine the password.")

if __name__ == "__main__":
    main()
