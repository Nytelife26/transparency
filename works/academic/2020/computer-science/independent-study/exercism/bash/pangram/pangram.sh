#!/usr/bin/env bash
unique=$(echo "${1,,}" | grep -Eo '[a-z]{1}' | sort -u)
if [ ${#unique} == 51 ]; then
	echo "true"
	exit 0
fi
echo "false"
