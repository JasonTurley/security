#!/bin/bash
# Pings a full range of ip addresses

function print_usage()
{
    echo "Please enter a valid ip address"
    echo "Example usage $0 127.0.0"
}

# validate the entered ip
if [[ "$1" =~ ^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$ ]]; then
    # ping full range of ip addresses
    for ip in `seq 1 254`; do
        ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
    done
else
    print_usage
    exit 1;
fi
