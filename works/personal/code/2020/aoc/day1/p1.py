#!/usr/bin/python

def main():
	nums = []
	while True:
		toadd = input("> ")
		if toadd == "":
			break
		try:
			nums.append(int(toadd))
		except ValueError:
			print("Invalid number. Please try again.")
	for x in nums:
		complement = 2020 - x
		if complement in nums:
			pair = (x, complement)
			break
	print(f"Result: {pair[0] * pair[1]}")

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("Exiting...")
