#!/usr/bin/python
import re

def main():
	passports = []
	parse = []
	while True:
		parse.append(input("> "))
		if parse[-2:] == ["", ""]:
			break
	parse = " ".join([x if x != "" else "\n" for x in parse]).split("\n")
	for x in parse:
		passports.append(
			{key: value for key, value in [
				y.split(":") for y in x.split()
			] if key != "cid"}
		)
	valid = 0
	for x in passports:
		if len(x.keys()) == 7:
			if height := re.search("([0-9]+)cm", x["hgt"]):
				height = int(height.group(1))
				valid_height = height >= 150 and height <= 193
			elif height := re.search("([0-9]+)in", x["hgt"]):
				height = int(height.group(1))
				valid_height = height >= 59 and height <= 76
			else:
				continue

			if all([
				int(x["byr"]) >= 1920 and int(x["byr"]) <= 2002,
				int(x["iyr"]) >= 2010 and int(x["iyr"]) <= 2020,
				int(x["eyr"]) >= 2020 and int(x["eyr"]) <= 2030,
				valid_height,
				re.match("#[0-9A-Fa-f]{6}$", x["hcl"]),
				x["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
				re.match("[0-9]{9}$", x["pid"])
			]):
				valid += 1
	print(f"There were {valid} valid passports.")

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("Exiting...")
