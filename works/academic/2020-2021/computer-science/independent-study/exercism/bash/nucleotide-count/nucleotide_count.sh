#!/usr/bin/env bash
A=0; C=0; G=0; T=0;

for (( i=0; i<${#1}; i++ )); do
	char=${1:$i:1}
	if [[ "ACGT" != *"$char"* ]]; then
		echo "Invalid nucleotide in strand"
		exit 1
	fi
	(( $char++ ))
done
echo "A: $A
C: $C
G: $G
T: $T"
