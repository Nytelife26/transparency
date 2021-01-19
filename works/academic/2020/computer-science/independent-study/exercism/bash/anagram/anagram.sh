#!/usr/bin/env bash

if [[ $# -lt 2 ]]; then
	echo "Usage: anagram.sh <word> [anagrams...]"
	exit 1
fi

lower() {
	printf '%s\n' "${1,,}"
}

initial=$(echo "$(lower $1)" | grep -o . | sort | tr -d "\n[:blank:]")
anagrams=""
for arg in $2; do
	if [[ "$(lower $arg)" = "$(lower $1)" ]]; then
		continue
	fi
	comparator=$(echo "$(lower $arg)" | grep -o . | sort | tr -d "\n[:blank:]")
	if [[ "$initial" = "$comparator" ]]; then
		anagrams="${anagrams} ${arg}"
	fi
done
echo $anagrams
