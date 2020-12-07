#!/usr/bin/python

def main():
	rows = []
	while True:
		toadd = input("> ")
		if toadd == "":
			break
		rows.append(toadd)
	total = 1
	slopes = [(1, 1),
	          (3, 1),
	          (5, 1),
	          (7, 1),
	          (1, 2)]
	for x in slopes:
		idx = 0
		trees = 0
		for row in [rows[i] for i in range(0, len(rows), x[1])]:
			if row[idx % len(row)] == "#":
				trees += 1
			idx += x[0]
		print(trees)
		total *= trees
	print(f"You encountered {total} trees.")


if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("Exiting...")
