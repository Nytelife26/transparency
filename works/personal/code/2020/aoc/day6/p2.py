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
		groups[group].append(list(toadd))
	# a list of all answers for every person in a group if the answer was
	# selected by all other people in the group, for every group in all the
	# groups. clarified because you are not expected to be able to comprehend
	# this comprehension without that explanation. i certainly couldn't.
	q = [[a for p in g for a in p if all([a in x for x in g])] for g in groups]
	questions = sum([len(set(x)) for x in q])

	print(f"The sum of yes questions is {questions}.")

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("Exiting...")
