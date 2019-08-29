#!/usr/bin/python3
"""
Scans a range of ports to see which are open.

Todo:
    * Add threading to port scan
    * Verify user entered ip address

"""

import sys
import socket
from datetime import datetime

def print_banner(target : str) -> None:
    """
    Prints a pretty banner specifying the target ip address and cureent time.
    """
    print("-" * 50)
    print("Scanning target: {}".format(target))
    print("Time started: {}".format(datetime.now()))
    print("-" * 50)


if len(sys.argv) != 2:
    print("Usage: python3 {} <ip>".format(sys.argv[0]))
    sys.exit()


# begin scanning ports
try:
    # Translate hostname to IPv4
    target = socket.gethostbyname(sys.argv[1])
    print_banner(target)

    for port in range(50, 85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1.)
        err = s.connect_ex((target, port))

        if not err:
            print("Port {} is open".format(port))

        s.close()

except KeyboardInterrupt:
    print("Exiting program.")
    sys.exit()

except socket.gaierror:
    print("Could not resolve hostname {}.".format(sys.argv[1]))
    sys.exit()
