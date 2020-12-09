#!/usr/bin/python

# I am aware this solution is inefficient. However, it is simply following
# the specification required by the class. It bears no reflection upon my
# personal choices as a developer. Thank you.

import os

def clearterm():
	os.system("cls" if os.name == "nt" else "clear")

def confirm(string):
	return input(string).lower() in ["", "y"]

def add(monsters):
	while True:
		try:
			new = [input("Enter the name of the monster: "),
			       int(input("Enter the strength of the monster: ")),
			       int(input("Enter the speed of the monster: ")),
			       int(input("Enter the skill of the monster: "))]
			if any([x <= 0 or x > 10 for x in new if type(x) == int]):
				raise ValueError
			if not new[0]:
				raise ValueError
			break
		except ValueError:
			print("Invalid monster information. Please try again.")
	show([new], True)
	if confirm("Is that correct? (Y/n): "):
		monsters.append(new)
	return monsters

def rem(monsters):
	show(monsters, True)
	print("NOTE: Numbers go from left to right, and then by row.")
	while True:
		selection = input("Enter the name or number to delete: ")
		try:
			monster = [monsters[int(selection)-1]]
		except ValueError:
			monster = [x for x in monsters if x[0].lower() == selection]
		except IndexError:
			monster = []
		if monster:
			break
		print("Invalid selection. Please try again.")
	show([monster[0]], True)
	if confirm("Is that the monster you wish to delete? (Y/n): "):
		del monsters[monsters.index(monster[0])]
	return monsters

def show(monsters, confirmation=False):
	per_row = os.get_terminal_size().columns // 21
	for i in range(0, len(monsters), per_row):
		header = ""
		titles = ""
		strng  = ""
		speed  = ""
		skill  = ""
		for x in monsters[i:i+per_row]:
			header += f"{'='*20} "
			titles += f"{x[0].upper().center(20)} "
			strng  += f"STRENGTH: {'*'*x[1]}{' '*(10-x[1])} "
			speed  += f"SPEED:    {'*'*x[2]}{' '*(10-x[2])} "
			skill  += f"SKILL:    {'*'*x[3]}{' '*(10-x[3])} "
		print("\n".join([header, titles, header, strng, speed, skill]))
	if not confirmation:
		input("\nPress ENTER to continue at any time.")
	return monsters

def play(monsters):
	return monsters

def help(monsters):
	return monsters

def main():
	monsters = [["Gorgatron", 2, 5, 6],
	            ["Mechanibot", 3, 9, 8],
	            ["Sharkadroid", 9, 4, 6]]
	choices = {"1": add,
	           "2": rem,
	           "3": show,
	           "4": play,
	           "5": help}
	col = os.get_terminal_size().columns
	while True:
		clearterm()
		print("=" * col)
		print("WELCOME TO GORGATRON".center(col))
		print("=" * col)
		print("\t1. Add a new monster")
		print("\t2. Remove a monster")
		print("\t3. Show all monsters")
		print("\t4. Play the game")
		print("\t5. Show help")
		print("\t6. Exit the game (or CTRL+C at any time)")
		print("=" * col)

		choice = input("\n> ")
		if choice == "6":
			raise KeyboardInterrupt
		if choice in choices.keys():
			clearterm()
			monsters = choices[choice](monsters)

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("\nExiting...")
