#!/usr/bin/env bash
if [ $# -ne 2 ] || ! [ $2 -eq $2 2>/dev/null ]; then
	echo "Usage: difference_of_squares.sh <command> <number>"
	echo
	echo "Valid commands are: sum_of_squares, square_of_sum, difference"
	exit 1
fi

sum_of_squares () {
	sq=0
	for (( i=1; i<=$1; i++ )); do
		sq=$(echo "$sq + ($i^2)" | bc -l)
	done
	echo "$sq"
}

square_of_sum () {
	sum=0
	for (( i=1; i<=$1; i++ )); do
		(( sum += $i ))
	done
	echo "$sum^2" | bc -l
}

difference () {
	sumsq=$(sum_of_squares "$1")
	sq=$(square_of_sum "$1")
	echo "$sq - $sumsq" | bc -l
}


if [[ $1 =~ square_of_sum|sum_of_square|difference$ ]]; then
	echo $($1 $2)
else
	exit 0
fi
