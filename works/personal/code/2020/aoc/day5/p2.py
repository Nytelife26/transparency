#!/usr/bin/python

def parse(partition):
	seats = [(x, list(range(8))) for x in range(128)]
	seat = [0, 0]
	for x in partition[:7]:
		slicer = len(seats) // 2
		seats = seats[:slicer] if x == "F" else seats[slicer:]
	row = seats[0][0]
	seats = seats[0][1]
	for x in partition[7:]:
		slicer = len(seats) // 2
		seats = seats[:slicer] if x == "L" else seats[slicer:]
	col = seats[0]
	return (row, col, row * 8 + col)

def main():
	partitions = []
	while True:
		toadd = input("> ").upper()
		if toadd == "":
			break
		if all(x in ["F", "B", "L", "R"] for x in toadd):
			partitions.append(toadd)
	possible = list(range(1027)) # 127 * 8 + 7 = 1023
	passes = [parse(x)[2] for x in partitions]
	seat = [x for x in possible if all([x not in passes,
	                                    x + 1 in passes,
	                                    x - 2 in passes])]
	print(f"Your seat is: {seat[0]}")

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("Exiting...")
