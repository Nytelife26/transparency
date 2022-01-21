#!/usr/bin/env bash
c=$(echo "$1" | grep -Eo "[a-zA-Z0-9?!]" | sed -re "s/\n//g")
if [ "${c:$(( ${#c}-1 )):1}" == "?" ] && [ "$c" == "${c^^}" ] && [[ "$c" =~ [a-zA-Z] ]]; then
	echo "Calm down, I know what I'm doing!"
elif [ "$c" == "${c^^}" ] && [[ "$c" =~ [a-zA-Z] ]]; then
	echo "Whoa, chill out!"
elif [ "${c:$(( ${#c}-1 )):1}" == "?" ]; then
	echo "Sure."
elif [ -z "${c,,}" ]; then
	echo "Fine. Be that way!"
else
	echo "Whatever."
fi
