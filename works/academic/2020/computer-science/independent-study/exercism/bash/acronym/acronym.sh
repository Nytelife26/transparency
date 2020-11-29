#!/usr/bin/env bash
acronym=""
parsed=$(echo "$1" | sed -r -e 's/(\s|-|_)/\n/g' | sed -e 's/[^A-Za-z]//g')
for word in ${parsed}; do
	acronym="${acronym}${word:0:1}"
done
echo "${acronym^^}"
