#!/usr/bin/env bash
work=""
if (( $1 % 3 == 0 )); then
	work="${work}Pling"
fi
if (( $1 % 5 == 0 )); then
	work="${work}Plang"
fi
if (( $1 % 7 == 0 )); then
	work="${work}Plong"
fi
echo "${work:-$1}"
