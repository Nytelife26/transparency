#!/usr/bin/env bash
score=0
l="${1,,}"
for (( i=0; i<${#1}; i++ )); do
	if [[ ${l:$i:1} =~ [aeioulnrst]$ ]]; then
		(( score += 1 ))
	elif [[ ${l:$i:1} =~ [dg]$ ]]; then
		(( score += 2 ))
	elif [[ ${l:$i:1} =~ [bcmp]$ ]]; then
		(( score += 3 ))
	elif [[ ${l:$i:1} =~ [fhvwy]$ ]]; then
		(( score += 4 ))
	elif [[ ${l:$i:1} =~ [k]$ ]]; then
		(( score += 5 ))
	elif [[ ${l:$i:1} =~ [jx]$ ]]; then
		(( score += 8 ))
	elif [[ ${l:$i:1} =~ [qz]$ ]]; then
		(( score += 10 ))
	fi
done
echo "$score"
