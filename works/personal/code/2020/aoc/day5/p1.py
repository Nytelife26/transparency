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
	print(f"Highest seat ID: {max([parse(x)[2] for x in partitions])}")

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("Exiting...")
