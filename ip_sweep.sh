#!/bin/bash
# Given the first three octets of an ip address, pings all sequences of
# addresses

# Ensure user entered an valid ip
if [[ "$1" =~ ^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$ ]]; then
    # ping full range of ip addresses
    for ip in `seq 1 254`; do
        ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
    done
else
    echo "Please enter a valid ip address"
    echo "Example usage $0 127.0.0"
    exit 1;
fi
