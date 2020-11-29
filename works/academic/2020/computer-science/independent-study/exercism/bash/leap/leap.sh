#!/usr/bin/env bash
if (( $# != 1 )) || ! [ $1 -eq $1 2>/dev/null ]; then
	echo "Usage: leap.sh <year>"
	exit 1
fi

if (( $1 % 4 == 0 )); then
	if (( $1 % 100 == 0 )) && (( $1 % 400 != 0 )); then
		echo "false"
	else
		echo "true"
	fi
else
	echo "false"
fi
