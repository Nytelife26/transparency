#!/usr/bin/env bash
invalid() {
	echo "Invalid number.  [1]NXX-NXX-XXXX N=2-9, X=0-9"
	exit 1
}

number=$(echo "$1" | sed -e 's/[^0-9]//g')
if [[ "$number" =~ ^1?[2-9][0-9]{2}[2-9][0-9]{6}$ ]]; then
	echo $(echo "$number" | sed -e 's/^1//')
else
	invalid
fi
