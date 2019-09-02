"""
cracker.py - a simple dictionary attack to crack user passwords.
"""
import sys

def print_usage() -> None:
    """Prints the correct way to execute the program
    """
    print("{} - executes a dictionary attack on a set of user passwords."
        .format(sys.argv[0]))
    print()
    print("Usage: python3 {} <passwords> <users>".format(sys.argv[0]))


def trim_newline(s : str) -> str:
    """Removes the newline from the end of a string
    """
    return s[:len(s)-1]

if len(sys.argv) != 3:
    print_usage()
    sys.exit()

with open(sys.argv[1], "r") as password_file:
    with open(sys.argv[2], "r") as user_file:
        total_cracked = 0

        for creds in user_file:
            user, actual_password = creds.split(":")  # ["user", "password"]

            # remove "\n" from actual_password
            actual_password = trim_newline(actual_password)

            # run full dictionary against user password
            for password in password_file:
                password = trim_newline(password)

                if password == actual_password:
                    total_cracked += 1
                    print("{user}'s password is {password}!".format(
                        user=user, password=password))
                    break

        print("Cracked a total of {} passwords".format(total_cracked))
