#!/usr/bin/python

def main():
	groups = []
	group  = 0
	while True:
		toadd = input("> ")
		above = group >= len(groups)
		if toadd == "":
			if above:
				break
			group += 1
			continue
		if above:
			groups.append([])
		groups[group] += list(toadd)
	questions = sum(len(set(x)) for x in groups)
	print(f"The sum of yes questions is {questions}.")

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("Exiting...")
