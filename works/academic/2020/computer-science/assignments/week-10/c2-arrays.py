from array import array
import os

def clearterm():
	os.system("cls" if os.name == "nt" else "clear")

def add(arr):
	to_add = input("Enter a value to add: ")
	while True:
		try:
			idx = int(input("Enter the array position to insert at: "))
			if idx > 0 and idx <= len(arr):
				break
		except ValueError:
			pass
		print("Incorrect index. Please try again.")
	arr[idx - 1] = to_add
	return arr

def rem(arr):
	while True:
		try:
			idx = int(input("Enter the array position to delete: "))
			if idx > 0 and idx <= len(arr):
				break
		except ValueError:
			pass
		print("Incorrect index. Please try again.")
	del arr[idx - 1]
	return arr

def run_menu(arr):
	# req. 2 - user menu
	col = os.get_terminal_size().columns
	menu = {"1": add, "2": rem}
	clearterm()
	print("=" * col)
	print("1. Add to array".center(col))
	print("2. Remove array value".center(col))
	print("=" * col)
	print(f"CURRENT: {arr}")
	while True:
		opt = input("> ")
		if opt in menu.keys():
			break
		print("Invalid menu selection. Please try again.")
	clearterm()
	print(arr)
	return menu[opt](arr)

def main():
	# req. 1 - array of size 10
	arr = array(10, str, "")
	while True:
		try:
			arr = run_menu(arr)
		except KeyboardInterrupt:
			print("\nExiting...")
			break

if __name__ == "__main__":
	main()
