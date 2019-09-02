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


if len(sys.argv) != 3:
    print_usage()
    sys.exit()

with open(sys.argv[1], "r") as dictionary:
    with open(sys.argv[2], "r") as credentials:
        total_cracked = 0

        for creds in credentials:
            user, actual_password = creds.split(":")  # ["user", "password"]

            # run full dictionary against each user password
            for password in dictionary:
                if password == actual_password:
                    total_cracked += 1

                    print("{user}'s password is {password}".format(
                        user=user, password=password), end="")
                    break

            # reset offset to beginning of password file
            dictionary.seek(0, 0)

        print()
        print("-" * 50)
        print("Cracked {} passwords".format(total_cracked))
