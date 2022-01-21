#!/usr/bin/env bash
if [[ $# -ne 1 ]] || ! [ "$1" -eq "$1" ] &>/dev/null; then
	echo "Usage: collatz_conjecture.sh <positive integer>"
	exit 1
fi
if [[ $1 -le 0 ]]; then
	echo "Error: Only positive numbers are allowed"
	exit 1
fi

rn=$1
pc=0
while [[ $rn -ne 1 ]]; do
	(( pc += 1 ))
	if [[ $(( $rn % 2 )) -eq 0 ]]; then
		(( rn /= 2 ))
	else
		(( rn = $rn * 3 + 1 ))
	fi
done

echo $pc
