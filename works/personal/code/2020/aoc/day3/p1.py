#!/usr/bin/python

def main():
	rows = []
	while True:
		toadd = input("> ")
		if toadd == "":
			break
		rows.append(toadd)
	idx = 0
	trees = 0
	for x in rows:
		if x[idx % len(x)] == "#":
			trees += 1
		idx += 3
	print(f"You encountered {trees} trees.")


if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("Exiting...")
