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

def print_start_banner(target : str, start : str, end : str) -> None:
    """
    Prints a pretty banner for starting up script
    """
    print("-" * 60)
    print("Starting scan on ports {0} - {1} target: {2}".format(start, end, target))
    print("Time started: {}".format(datetime.now()))
    print("-" * 60)


def print_finish_banner(target : str, num : int) -> None:
    """
    Prints a pretty banner for finishing up script
    """
    print()
    print("-" * 60)
    print("Finished scan on target: {}".format(target))
    print("Time finished: {}".format(datetime.now()))
    print("{} open port(s)".format(num))
    print("-" * 60)


# Check command line args
if len(sys.argv) == 2:
    # Use default port range 0 to 1000
    start_port = 0
    end_port = 1000

elif len(sys.argv) == 4:
    # Use provided port ranges
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3])

else:
    # Error
    print("Usage: python3 {0} <ip> [[start port] [end port]]".format(sys.argv[0]))
    sys.exit()

try:
    # Translate hostname to IPv4
    target = socket.gethostbyname(sys.argv[1])

    print_start_banner(target, str(start_port), str(end_port))
    count = 0

    # Begin scanning ports
    for port in range(start_port, end_port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1.)
        err = s.connect_ex((target, port))

        # A return value of 0 indicates open port
        if not err:
            count += 1
            print("port {} is open".format(port))

        s.close()

    print_finish_banner(target, count)

except KeyboardInterrupt:
    print("Exiting program.")
    sys.exit()

except socket.gaierror:
    print("Could not resolve hostname {}.".format(sys.argv[1]))
    sys.exit()
