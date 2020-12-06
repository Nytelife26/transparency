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
	trio = False
	for x in nums:
		complement_one = 2020 - x
		for y in nums:
			complement_two = complement_one - y
			if complement_two in nums:
				trio = (x, y, complement_two)
				break
		if trio:
			break
	print(f"Result: {trio[0] * trio[1] * trio[2]}")

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("Exiting...")
