#!/usr/bin/env bash

# bash runs calculations with 64-bit signed integers.
# therefore, 2^63 will return a negative value.
# this behaviour is not what we want, so we use sed to remove the negative.
if [ $# -ne 1 ]; then
	echo "Usage: grains.sh <command|number>"
	echo
	echo "Valid commands: total"
	exit 1
fi
if [ $1 == "total" ]; then
	total=0
	for (( i=0; i<64; i++ )); do
		total=$(echo "$total + (2^$i)" | bc -l)
	done
	echo "$total"
	exit 0
fi
if [ $1 -lt 1 ] || [ $1 -gt 64 ]; then
	echo "Error: invalid input"
	exit 1
fi
echo "$(( 2 ** ($1 - 1) ))" | sed -e "s/-//"
