#!/usr/bin/python

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
			valid += 1
	print(f"There were {valid} valid passports.")

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("Exiting...")
