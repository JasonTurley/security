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
    print("-" * 50)
    print("Starting scan on ports {0} - {1} target: {2}".format(start, end, target))
    print("Time started: {}".format(datetime.now()))
    print("-" * 50)


def print_finish_banner(target : str, open_ports : list) -> None:
    """
    Prints a pretty banner for finishing up script
    """
    print("-" * 50)
    print("Finished scan on target: {}".format(target))
    print("Time finished: {}".format(datetime.now()))
    print("{} open port(s)".format(str(len(open_ports))))

    # print all open port numbers
    if len(open_ports) != 0:
        print("[", end="")

        for port in open_ports:
            print(port, end=" ")

        print("]")
    print("-" * 50)


if len(sys.argv) != 4:
    print("Usage: python3 {0} <ip> <start port> <end port>".format(sys.argv[0]))
    sys.exit()

try:
    # Translate hostname to IPv4
    target = socket.gethostbyname(sys.argv[1])
    start = sys.argv[2]
    end = sys.argv[3]

    print_start_banner(target, start, end)
    open_ports = []

    # Begin scanning ports
    for port in range(int(start), int(end)):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1.)
        err = s.connect_ex((target, port))

        if not err:
            open_ports.append(port)

        s.close()

    print_finish_banner(target, open_ports)

except KeyboardInterrupt:
    print("Exiting program.")
    sys.exit()

except socket.gaierror:
    print("Could not resolve hostname {}.".format(sys.argv[1]))
    sys.exit()
