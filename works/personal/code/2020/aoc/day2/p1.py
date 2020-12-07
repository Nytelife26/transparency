#!/usr/bin/python
import re

def main():
	passes = []
	while True:
		check = input("> ")
		if check == "":
			break
		if toadd := re.search("([0-9]+)-([0-9]+) ([a-zA-Z]): (.+)", check):
			if len(toadd.groups()) == 4:
				passes.append(toadd.groups())
				continue
		print("Invalid password policy. Please try again.")
	valid = 0
	for x in passes:
		count = x[3].count(x[2])
		if count >= int(x[0]) and count <= int(x[1]):
			valid += 1
	print(f"There were {valid} valid passwords.")


if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("Exiting...")
