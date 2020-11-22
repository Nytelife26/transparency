import os
import time
import json

term = os.get_terminal_size().columns
try:
	with open("stats.json", "x") as outfile:
		json.dump(
			{
				"bestmove": 0,
				"besttime": 0,
				"gamewins": 0,
				"gameplay": 0
			},
			outfile
		)
except:
	pass

def getstats():
	with open("stats.json", "r") as infile:
		return json.load(infile)

def recstats(stats):
	with open("stats.json", "w") as outfile:
		return json.dump(stats, outfile)

def clearterm():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")

def display(left, right):
	side = (term - 3) // 2
	clearterm()
	left  = ["~ WRONG SIDE ~"] + left
	right = ["~ RIGHT SIDE ~"] + right

	for x in range(0, 5):
		global l
		global r
		for y in ["left", "right"]:
			exec(f"""
global l
global r
try:
	{y[0]} = {y}[x].center(side)
except IndexError:	  
	{y[0]} = ''.center(side)
			""")
		print(f"{l} | {r}")

def swap(left, right, entity):
	if "You" in left:
		right.append(left.pop(left.index("You")))
		if entity in left:
			right.append(left.pop(left.index(entity)))
	elif "You" in right:
		left.append(right.pop(right.index("You")))
		if entity in right:
			left.append(right.pop(right.index(entity)))
	return (left, right)

def play(lside, rside):
	display(lside, rside)
	choices = {"f": "Fox", "h": "Hen", "c": "Corn", "n": None}
	while True:
		choice = input("Which do you wish to move? (F, H, C, or N for none)\n> ").lower()
		if choice in choices.keys():
			lside, rside = swap(lside, rside, choices[choice])
			break
		print("That was not one of the required choices. Please try again.")

	fox = ["Fox" in lside, "Fox" in rside]
	hen = ["Hen" in lside, "Hen" in rside]
	corn = ["Corn" in lside, "Corn" in rside]
	you = ["You" in lside, "You" in rside]

	display(lside, rside)
	if all([x == [False, True] for x in [fox, hen, corn]]):
		return (True, True, lside, rside)
	if fox == hen and fox != you:
		print("You let the fox eat the hen... Better luck next time! :(")
		return (True, False, lside, rside)
	if hen == corn and hen != you:
		print("You let the hen eat the corn... Better luck next time! :(")
		return (True, False, lside, rside)
	return (False, False, lside, rside)

def game():
	lside = ["You", "Fox", "Hen", "Corn"]
	rside = []
	moves = 0
	orig = time.time()
	stats = getstats()
	stats["gameplay"] += 1
	while True:
		moves += 1
		turn = play(lside, rside)
		if turn[0]:
			elapsed = round(time.time() - orig, 2)
			break

	if turn[1]:
		stats["gamewins"] += 1
		print(f"You won in {moves} moves, and {elapsed} seconds! Well done!")
		if moves < stats["bestmove"] or not stats["bestmove"]:
			print("That's a new personal best!")
			stats["bestmove"] = moves
		if elapsed < stats["besttime"] or not stats["besttime"]:
			print("Wow, a new best time! Congrats!")
			stats["besttime"] = elapsed
	recstats(stats)
	input("Press enter to return to main menu...")

def info():
	stats = getstats()
	print(f"""
You have played {stats["gameplay"]} games, \
of which you have won {stats["gamewins"]}.

Your best scores were {stats["bestmove"]} moves \
and {stats["besttime"]} seconds.

You may press return to exit this page at any time.
	""")
	input(">  ")

def help():
	print("""
This is a Python implementation of the Fox and Hen game, by Tyler J. Russell.

The gist of the game is that you, the player, must move all the other entities \
(the fox, hen, and corn) to the other side of the river. However, the \
challenge is that you may not leave the fox and hen or hen and corn on either \
side together unattended at any time. Otherwise, the fox will eat the hen, or \
the hen will eat the corn.

Each turn, you can choose to take ONE of the entities with you, or nothing at \
all. Note that choosing to take nothing will move you to the other side, just \
without anything else to accompany you.

Mathematically speaking, the best solution to this challenge requires only 7 \
steps. See if you can achieve that, or do your best!

Have fun :)
You may press return to exit this page at any time.
	""")
	input("> ")

def mainmenu():
	while True:
		clearterm()

		print("=" * term)
		print("WELCOME TO THE FOX AND HEN GAME!".center(term))
		print("=" * term)
		print("1. PLAY GAME".center(term))
		print("2. YOUR INFO".center(term))
		print("3. SHOW HELP".center(term))
		print("4. EXIT GAME".center(term))
		print("=" * term)

		choices = {"1": game, "2": info, "3": help, "4": None}
		choice = input("> ")
		if choice in choices.keys():
			if choice is "4":
				raise KeyboardInterrupt
			clearterm()
			choices[choice]()

if __name__ == "__main__":
	try:
		mainmenu()
	except KeyboardInterrupt:
		clearterm()
		print("\nExiting... See you next time!")
