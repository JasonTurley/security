#!/bin/bash
# Given the first three octets of an ip address, pings all sequences of
# addresses

if [ "$1" == "" ]
then
echo "You forgot an ip address!"
echo "usage: $0 10.2.0"

else
for ip in `seq 1 254`; do
ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
done
fi
