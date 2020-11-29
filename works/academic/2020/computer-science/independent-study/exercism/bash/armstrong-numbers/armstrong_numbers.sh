#!/usr/bin/env bash
test=0
for (( i=0; i<${#1}; i++ )); do
	(( test += ${1:$i:1}**${#1} ))
done
if [ $test -eq $1 ]; then
	echo "true"
	exit 0
fi
echo "false"
