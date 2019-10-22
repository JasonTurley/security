""" cracker.py - a simple password_list attack to crack user passwords.
"""
import sys

def print_usage() -> None:
    """Prints the correct way to execute the program
    """
    print("Password Cracker - executes a dictionary attack on a set of user credentials.")
    print("Created 2019 by Jason Turley")
    print("Github: https://github.com/JasonTurley/password-cracker")
    print()
    print("Usage: python3 {} <PASSWORD-LIST> <USER-LIST>".format(sys.argv[0]))


# Check user entered correct number of arguments
if len(sys.argv) != 3:
    print_usage()
    sys.exit()


with open(sys.argv[1], "r") as password_list:
    with open(sys.argv[2], "r") as credentials:
        total_cracked = 0

        for creds in credentials:
            user, actual_password = creds.split(":")  # ["user", "password"]

            # Execute attack
            for password in password_list:
                if password == actual_password:
                    total_cracked += 1
                    print("{}'s password is {}".format(user, password), end="")
                    break

            # Reset to the beginning of password list
            password_list.seek(0, 0)

        # Print results
        print()
        print("-" * 30)
        print("Cracked a total of {} passwords".format(total_cracked))
