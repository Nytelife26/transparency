def main():
    print("Enter 5 numbers to accumulate the total.")
    acc = 0
    for x in range(5):
        acc += int(input("> ")
    print("The total was {}".format(acc))