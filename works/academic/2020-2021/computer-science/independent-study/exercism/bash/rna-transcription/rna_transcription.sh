#!/usr/bin/env bash
input="${1,,}"
RNA=""
for (( i=0; i<${#1}; i++ )); do
	chr=${input:$i:1}
	if [[ $chr =~ [^gcta]$ ]]; then
		echo "Invalid nucleotide detected."
		exit 1
	fi
	RNA="${RNA}$(echo ${chr} | sed -e 's/g/x/;s/c/g/;s/x/c/;s/a/u/;s/t/a/')"
done
echo "${RNA^^}"
