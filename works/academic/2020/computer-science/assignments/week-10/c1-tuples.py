# req. 1 - names of months as a tuple
MONTHS = ("January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
          "October",
          "November",
          "December")

# req. 2 - function that returns name from number
def month(num):
	return MONTHS[int(num) - 1]

def ordinal(num):
	try:
		insertion = {"1": "st", "2": "nd", "3": "rd"}[str(num)[-1]]
	except KeyError:
		insertion = "th"
	return f"{num}{insertion}"

def main():
	# req. 3 - convert numerical dob to string
	strin = input("Enter a numerical date of birth (DD/MM/YYYY): ").split("/")
	if len(strin) != 3 or (strin[1] <= "0" or strin[1] > "12"):
		print("Invalid DoB. Please try again.")
		return
	print(f"{ordinal(strin[0])} {month(strin[1])} {strin[2]}")

if __name__ == "__main__":
	while True:
		try:
			main()
		except KeyboardInterrupt:
			print("Exiting...")
			break
